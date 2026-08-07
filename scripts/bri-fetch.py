#!/usr/bin/env python3
"""
bri-fetch.py — read Biblical Research Institute articles that the live site blocks.

adventistbiblicalresearch.org sits behind a Vercel bot-detection checkpoint that
returns 403 to every automated request, whatever headers you send. A browser is
fine; a script is not. This goes around it through the Wayback Machine, which
holds clean 200 snapshots, and pulls the article out of the Next.js
__NEXT_DATA__ payload (the archived HTML shell contains only the page title).

Usage
  bri-fetch.py search "tongues"            # archived BRI URLs matching a keyword
  bri-fetch.py get <bri-url>               # print the article as text
  bri-fetch.py get <bri-url> --json        # title/author/date/body as JSON
  bri-fetch.py get <wayback-url>           # pin a specific snapshot

Honesty rules for anything you cite from this
  - Snapshots are dated. Report the snapshot date alongside the citation.
  - The live page is authoritative. If it matters, open the URL in a browser.
  - This retrieves the real article text, so quoting it is legitimate — but say
    where the text came from.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0 Safari/537.36")
CDX = "https://web.archive.org/cdx/search/cdx"


def http(url, tries=4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception as e:                      # archive.org rate-limits; back off
            last = e
            time.sleep(3 * (i + 1))
    raise SystemExit(f"Could not fetch {url}: {last}")


def search(term):
    q = (f"{CDX}?url=adventistbiblicalresearch.org&matchType=domain"
         f"&filter=original:.*{urllib.parse.quote(term)}.*&filter=statuscode:200"
         f"&fl=original,timestamp&collapse=urlkey&limit=60")
    return [l.split() for l in http(q).strip().splitlines() if l.strip()]


def snapshots(url, n=6):
    """Timestamps of the last n good snapshots, newest first."""
    seen = []
    for u in (url, url.rstrip("/"), url.replace("https://www.", "https://"),
              url.replace("https://", "https://www.")):
        q = (f"{CDX}?url={urllib.parse.quote(u, safe='')}"
             f"&filter=statuscode:200&fl=timestamp&limit=-{n}")
        for l in http(q).strip().splitlines():
            t = l.strip()
            if t and t not in seen:
                seen.append(t)
    return sorted(seen, reverse=True)[:n]


def render(node, depth=0):
    """ProseMirror body doc -> markdown-ish text, in document order."""
    if node is None:
        return ""
    if isinstance(node, list):
        return "".join(render(n, depth) for n in node)
    if not isinstance(node, dict):
        return ""
    t, kids = node.get("type"), node.get("content")
    if t == "text":
        txt = node.get("text", "")
        marks = {m.get("type") for m in (node.get("marks") or [])}
        if marks & {"italic", "em"}:
            txt = f"*{txt}*"
        if marks & {"bold", "strong"}:
            txt = f"**{txt}**"
        return txt
    if t in ("hardBreak", "br"):
        return "\n"
    if t == "paragraph":
        return render(kids, depth).strip() + "\n\n"
    if t == "heading":
        lvl = int((node.get("attrs") or {}).get("level", 2))
        return "#" * lvl + " " + render(kids, depth).strip() + "\n\n"
    if t == "blockquote":
        return "> " + render(kids, depth).strip().replace("\n", "\n> ") + "\n\n"
    if t in ("bulletList", "orderedList"):
        out = []
        for i, li in enumerate(kids or [], 1):
            mark = "- " if t == "bulletList" else f"{i}. "
            out.append("  " * depth + mark + render(li.get("content"), depth + 1).strip())
        return "\n".join(out) + "\n\n"
    if t == "listItem":
        return render(kids, depth)
    if t == "footnotes":
        body = render(kids, depth).strip()
        return "\n---\nNOTES\n\n" + body + "\n" if body else ""
    if t == "footnote":
        return render(kids, depth).strip() + "\n\n"
    return render(kids, depth)


def find_article(data):
    """Canonical article node, with a shape-matched fallback."""
    pg = data.get("props", {}).get("pageProps", {}).get("page", {}) or {}
    a = (pg.get("resources") or {}).get("Article")
    if isinstance(a, dict) and isinstance(a.get("body"), dict):
        return a
    found = []

    def walk(n):
        if isinstance(n, dict):
            if n.get("title") and isinstance(n.get("body"), dict) and "content" in n["body"]:
                found.append(n)
            for v in n.values():
                walk(v)
        elif isinstance(n, list):
            for v in n:
                walk(v)
    walk(data)
    return found[0] if found else None


def people(data):
    """_id -> display name, so the article's author ids resolve to names."""
    names = {}

    def walk(n):
        if isinstance(n, dict):
            if n.get("_id"):
                nm = n.get("name") or " ".join(
                    x for x in (n.get("firstName"), n.get("lastName")) if x)
                if nm and isinstance(nm, str) and len(nm) < 80:
                    names.setdefault(n["_id"], nm.strip())
            for v in n.values():
                walk(v)
        elif isinstance(n, list):
            for v in n:
                walk(v)
    walk(data)
    return names


def strip_html(s):
    s = re.sub(r"(?is)<(script|style|nav|footer|header|form|svg|noscript)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)</(p|div|h[1-6]|li|tr|blockquote)>", "\n\n", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    for a, b in (("&nbsp;", " "), ("&amp;", "&"), ("&rsquo;", "'"), ("&#8217;", "'"),
                 ("&lsquo;", "'"), ("&ldquo;", '"'), ("&rdquo;", '"'), ("&#8220;", '"'),
                 ("&#8221;", '"'), ("&mdash;", "—"), ("&ndash;", "–"), ("&quot;", '"'),
                 ("&lt;", "<"), ("&gt;", ">"), ("&#39;", "'")):
        s = s.replace(a, b)
    s = "\n".join(l.strip() for l in s.splitlines())
    return re.sub(r"\n{3,}", "\n\n", s).strip()


def from_plain_html(html, url, ts):
    """Pre-Next.js snapshots: server-rendered Drupal markup."""
    title = ""
    mt = re.search(r"<title>(.*?)</title>", html, re.S)
    if mt:
        title = re.sub(r"\s+", " ", strip_html(mt.group(1))).split("|")[0].strip()
    body = ""
    for pat in (r'(?is)<div[^>]*class="[^"]*field-item[^"]*".*?>(.*?)</div>\s*</div>',
                r"(?is)<article[^>]*>(.*?)</article>",
                r'(?is)<div[^>]*id="content"[^>]*>(.*?)</div>\s*</div>'):
        cands = [strip_html(c) for c in re.findall(pat, html)]
        cands = [c for c in cands if len(c.split()) > 120]
        if cands:
            body = max(cands, key=len)
            break
    if not body:
        body = strip_html(html)
    return {"url": url, "snapshot": f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}", "title": title,
            "subtitle": "", "author": "", "date": "", "body": body}


def get(url):
    if "web.archive.org" in url:
        m = re.search(r"/web/(\d{14})", url)
        stamps, direct = [m.group(1) if m else "00000000000000"], url
    else:
        stamps, direct = snapshots(url), None
        if not stamps:
            raise SystemExit(f"No archived snapshot found for {url}")

    # Captures of a client-rendered page can be empty shells. Walk back until one
    # actually carries the article.
    best, ts = None, stamps[0]
    for stamp in stamps:
        snap_url = direct or f"https://web.archive.org/web/{stamp}id_/{url}"
        try:
            html = http(snap_url)
        except SystemExit:
            continue
        m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
        if m:
            data = json.loads(m.group(1))
            art = find_article(data)
            if art:
                ts = stamp
                break
        else:
            plain = from_plain_html(html, url, stamp)
            if len(plain["body"].split()) > 150:
                return plain
            best = best or plain
        art = None
        time.sleep(1)
    if not art:
        if best:
            return best
        raise SystemExit("No snapshot of that URL carries article text. "
                         "Try `bri-fetch.py search <keyword>` for an older path.")

    names = people(data)
    authors = ", ".join(filter(None, (names.get(a.get("person"), "")
                                      for a in (art.get("authors") or []))))
    return {
        "url": url,
        "snapshot": f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}",
        "title": art.get("title") or "",
        "subtitle": art.get("subtitle") or "",
        "author": authors,
        "date": (art.get("publishedAt") or "")[:10],
        "body": re.sub(r"\n{3,}", "\n\n", render(art.get("body"))).strip(),
    }


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        raise SystemExit(1)
    cmd, arg = sys.argv[1], sys.argv[2]
    if cmd == "search":
        for u, t in search(arg):
            print(f"{t[:4]}-{t[4:6]}-{t[6:8]}  {u}")
    elif cmd == "get":
        art = get(arg)
        if "--json" in sys.argv:
            print(json.dumps(art, indent=2, ensure_ascii=False))
        else:
            print(art["title"])
            if art["subtitle"]:
                print(art["subtitle"])
            if art["author"]:
                print(f"Author: {art['author']}")
            if art["date"]:
                print(f"Published: {art['date']}")
            print(f"Source: {art['url']}")
            print(f"Wayback snapshot: {art['snapshot']}")
            print(f"Words: {len(art['body'].split())}")
            print("-" * 70)
            print(art["body"])
    else:
        print(__doc__)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
