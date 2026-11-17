#!/usr/bin/env python3
"""render-study.py — turn bible-study.md into the reading copy, bible-study.html.

Fills bible-study-deep/references/html-template.html. The markdown is the
workshop and keeps the Verification Ledger; the HTML is the reading copy and
gets none of it.

Usage
  render-study.py <bible-study.md>                 # writes bible-study.html beside it
  render-study.py <bible-study.md> --out <file> --lang id --reference "..."

Read from the markdown header
  # Bible Study: <passage>        ## <title>
  *Prepared for: <audience>*      *Translation: <translation>*
Each can be overridden: --passage --title --audience --translation.

Exit 0 written · 1 the markdown lacks a header field or a section · 64 usage.
Warnings on stderr name any workshop apparatus that reached the page.
"""
import html
import re
import sys
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "bible-study-deep/references/html-template.html"
LEDGER = re.compile(r"^## (Verification Ledger|Buku Besar Verifikasi|Catatan Verifikasi)\b.*", re.M)


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", s).lower()).strip("-")


def opt(args, name):
    return args[args.index(name) + 1] if name in args else None


def body_html(md):
    """Markdown body -> (html, toc entries, number of numbered sections)."""
    lines, out, toc = md.split("\n"), [], []
    hue, is_open, secname, numbered, i = 1, False, "", 0, 0

    def close():
        nonlocal is_open
        if is_open:
            out.append("</section>\n")
            is_open = False

    while i < len(lines):
        l = lines[i]
        if not l.strip() or l.strip() == "---":
            i += 1
            continue
        m = re.match(r"## (?:(\d+)\. )?(.*)", l)
        if m:
            close()
            n, t = m.group(1), m.group(2)
            secname = t
            if n:
                numbered += 1
                hue, sid, num, label = min(int(n), 8), "s" + n, f'<span class="num">{n}</span> ', f"{n}. {t}"
            else:
                hue, sid, num, label = 1, slug(t)[:50], "", t
            out.append(f'<section class="sec" data-hue="{hue}">\n  <h2 id="{sid}">{num}{inline(t)}</h2>')
            toc.append(f'  <li data-hue="{hue}"><a href="#{sid}">{inline(label)}</a></li>')
            is_open = True
            i += 1
            continue
        if l.startswith("### "):
            t = re.sub(r"^\d+\.\d+\.\s*", "", l[4:])
            sid = slug(t)[:50]
            out.append(f'  <h3 id="{sid}">{inline(t)}</h3>')
            short = re.sub(r" \(.*?\)", "", t)
            toc.append(f'  <li class="l3" data-hue="{hue}"><a href="#{sid}">{inline(short)}</a></li>')
            i += 1
            continue
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head, rest = rows[0], rows[2:]
            if head[0] in ("Field", "Bidang"):
                out.append('  <div class="tablewrap"><table class="spec"><tbody>')
                out += [f"    <tr><td>{inline(r[0])}</td><td>{inline(r[1])}</td></tr>" for r in rest if len(r) > 1]
                out.append("  </tbody></table></div>")
            else:
                out.append('  <div class="tablewrap"><table class="grid">\n    <thead><tr>'
                           + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>\n    <tbody>")
                out += ["    <tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rest]
                out.append("    </tbody>\n  </table></div>")
            continue
        if l.startswith(">"):
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i][1:].strip())
                i += 1
            q = [x for x in q if x]
            if not q:
                continue
            note = q.pop()[2:] if len(q) > 1 and q[-1].startswith("— ") else ""
            cls = ("scripture" if re.match(r"Passage|Konteks", secname)
                   else "egw" if re.match(r"Ellen", secname) else "cited")
            out.append(f'  <blockquote class="{cls}"><p>{inline(" ".join(q))}</p></blockquote>')
            if note:
                out.append(f'  <p class="note">{inline(note)}</p>')
            continue
        if l.startswith("- "):
            out.append("  <ul>")
            while i < len(lines) and lines[i].startswith("- "):
                out.append(f"    <li>{inline(lines[i][2:])}</li>")
                i += 1
            out.append("  </ul>")
            continue
        if re.match(r"\d+\. ", l):
            # One <ol> for the whole run, so the count does not restart at every item.
            out.append("  <ol>")
            while i < len(lines) and re.match(r"\d+\. ", lines[i]):
                out.append("    <li>" + inline(re.sub(r"^\d+\. ", "", lines[i])) + "</li>")
                i += 1
            out.append("  </ol>")
            continue
        m = re.match(r"(.*?)\*\*(Flag|Catatan doktrin):\*\*\s*(.+)", l)
        if m:
            if m.group(1).strip():
                out.append(f"  <p>{inline(m.group(1).strip())}</p>")
            b = m.group(3)
            out.append(f'  <div class="flag"><p>{inline(b[0].upper() + b[1:])}</p></div>')
            i += 1
            continue
        cls = ' class="note"' if l.startswith("**Notes:**") else ""
        out.append(f"  <p{cls}>{inline(l)}</p>")
        i += 1
    close()
    return "\n".join(out), toc, numbered


def main():
    a = sys.argv[1:]
    if not a or a[0].startswith("-"):
        print(__doc__)
        raise SystemExit(64)
    src = Path(a[0]).expanduser()
    md = src.read_text()

    def header(pattern, flag, what):
        m = re.search(pattern, md, re.M)
        v = opt(a, flag) or (m.group(1).strip() if m else None)
        if not v:
            sys.exit(f"{src.name} has no {what}; pass {flag}.")
        return v

    passage = header(r"^# (?:Bible Study|Pendalaman Alkitab|Pelajaran Alkitab):\s*(.+)$", "--passage", "'# Bible Study: <passage>' line")
    first = re.search(r"^## (.+)$", md, re.M)
    if not first:
        sys.exit(f"{src.name} has no '## ' section.")
    titled = not re.match(r"\d+\. ", first.group(1))
    title = opt(a, "--title") or (first.group(1).strip() if titled else passage)
    audience = header(r"^\*(?:Prepared for|Disiapkan untuk):\s*(.+?)\*$", "--audience", "'*Prepared for: …*' line")
    translation = header(r"^\*(?:Translation|Terjemahan):\s*(.+?)\*$", "--translation", "'*Translation: …*' line")

    # The body is every '## ' section after the title heading, up to the ledger.
    body_md = LEDGER.split(md)[0]
    heads = list(re.finditer(r"^## ", body_md, re.M))
    start = heads[1] if titled and len(heads) > 1 else heads[0]
    body_md = body_md[start.start():]
    body_md = re.sub(r"\s*\(para_id [\d.]+\)", "", body_md)
    body_md = re.sub(r",? ?[Ll]ocal library #\d+,?", "", body_md)
    # Candidates the study weighed and set aside are workshop material.
    body_md = re.sub(r"(?ms)^### Set aside.*?(?=^#|^> Recommendation|\Z)", "", body_md)
    body_md = re.sub(r" ?\bTier [0-3], (?:verbatim|paraphrased?)\.?", "", body_md)
    body, toc, numbered = body_html(body_md)
    if not numbered:
        sys.exit(f"{src.name} has no numbered '## 1. …' sections.")

    tpl = TEMPLATE.read_text()
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    page = (tpl[:tpl.index('<nav class="toc"')]
            + '<nav class="toc" id="toc"><div class="th">Contents</div><ol>\n' + "\n".join(toc) + "\n</ol></nav>\n\n"
            + tpl[tpl.index("<article>"):tpl.index("<!-- One <section")]
            + body + "\n" + tpl[tpl.index('<footer class="doc">'):])
    page = page.replace("<b>8</b> sections", f"<b>{numbered}</b> sections")
    fields = {"LANG": opt(a, "--lang") or "en", "PASSAGE": passage, "TITLE": title, "AUDIENCE": audience,
              "TRANSLATION": translation, "REFERENCE": opt(a, "--reference") or "",
              "WORDS": f"{words:,}", "MINUTES": str(round(words / 200))}
    for k, v in fields.items():
        page = page.replace("{{" + k + "}}", html.escape(v, quote=False))
    out = Path(opt(a, "--out") or src.with_suffix(".html")).expanduser()
    out.write_text(page)
    print(f"{out}  ({numbered} sections, {words:,} words)")
    visible = re.sub(r"(?s)<(script|style)\b.*?</\1>", "", page)
    for pat, what in ((r"para_id", "a para_id"), (r"\bHTTP [45]\d\d\b", "an HTTP status code"),
                      (r"located-unread|\[unverified|\bTier [0-3]\b", "a provenance tag"), (r"\{\{[A-Z]+\}\}", "an unfilled placeholder"),
                      (r">https?://[^<]{12,}</a>", "a bare URL as link text")):
        if re.search(pat, visible):
            print(f"WARNING: the page contains {what}; the reading copy should not.", file=sys.stderr)


if __name__ == "__main__":
    main()
