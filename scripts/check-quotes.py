#!/usr/bin/env python3
"""check-quotes.py — compare every quoted Bible verse in a file with the Bible.

Usage
  check-quotes.py <file-or-folder> [...]     # .md files and deck.json; a folder is searched

What is checked
  A markdown blockquote whose citation names one passage and KJV or TB:
      > "quoted words"
      > — Wahyu 14:3 (TB)            also "— Revelation 14:1-5, KJV", the citation
                                     on the next line after the quote, or in
                                     brackets closing it: (Romans 3:23, KJV)
  A deck.json verse slide: "text" against "ref".
  The quotation passes when its words appear, in order and unchanged, in the
  cited verses. An ellipsis (… or ...) may skip words. Case, punctuation and
  verse numbers are ignored.

What is not checked, and is counted so the gap is visible
  Ellen White and other quotations; citations naming several passages;
  quotations inside running prose or tables.

Sources
  KJV: the local database through bible.py (falls back to bible.helloao.org).
  TB:  bolls.life, one request per chapter.

Exit 0 every checked quotation matches · 1 at least one does not ·
     2 a source could not be reached, so some were not checked · 64 usage.
"""
import difflib
import importlib.util
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("bible", HERE / "bible.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)
H = B.H

CITE = re.compile(r"^\W*(?P<ref>.+?\d+\s*[:.]\s*\d+(?:\s*[-–]\s*\d+)?)\s*(?:\((?P<a>KJV|TB)\b[^)]*\)|,\s*(?P<b>KJV|TB)\b)(?P<rest>.*)$")
_tb_cache, _unreachable = {}, []


def norm(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[\d¶*_]+", " ", s.lower())
    return " ".join(re.sub(r"[^\w\s]", " ", s).split())


def tb_chapter(code, chap):
    key = (code, chap)
    if key not in _tb_cache:
        url = f"https://bolls.life/get-text/TB/{B.USFM.index(code) + 1}/{chap}/"
        rows = None
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                rows = json.loads(urllib.request.urlopen(req, timeout=20).read())
                break
            except Exception:
                time.sleep(1 + attempt)
        _tb_cache[key] = None if rows is None else {r["verse"]: r["text"] for r in rows}
    return _tb_cache[key]


def passage(version, ref):
    """Text of the cited span, or None when its source cannot be reached."""
    code, chap, v1, v2 = H.parse_ref(ref)
    if v1 is None:
        raise H.NotFound(f'"{ref}" names no verse.')
    if version == "TB":
        verses = tb_chapter(code, chap)
        if verses is None:
            return None
        rows = [(v, verses[v]) for v in range(v1, v2 + 1) if v in verses]
    else:
        rows = B.get_text(B.local(), "eng_kjv", code, chap, v1, v2)
    if not rows:
        raise H.NotFound(f"no verse text found for {ref}")
    return " ".join(t for _, t in rows)


def compare(quote, source):
    """None when the quotation is in the source; otherwise a short account of where it leaves it."""
    src, pos = norm(source), 0
    for piece in re.split(r"…|\.\.\.|\[\.\.\.\]", quote):
        p = norm(piece)
        if not p:
            continue
        at = src.find(p, pos)
        if at < 0:
            m = difflib.SequenceMatcher(None, p, src, autojunk=False)
            blocks = [b for b in m.get_matching_blocks() if b.size]
            # The first place the quotation's words stop following the verse.
            i = j = 0
            for b in blocks:
                if b.a != i:
                    break
                i, j = b.a + b.size, b.b + b.size
            return (f'quoted "…{p[max(0, i - 30):i + 45]}…"\n'
                    f'      Bible  "…{src[max(0, j - 30):j + 45]}…"')
        pos = at + len(p)
    return None


def quotes_in_markdown(text):
    """(line number, quotation, citation line) for every blockquote."""
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        if not lines[i].startswith(">"):
            i += 1
            continue
        start, block = i, []
        while i < len(lines) and lines[i].startswith(">"):
            block.append(lines[i][1:].strip())
            i += 1
        block = [b for b in block if b]
        if not block:
            continue
        cite = ""
        if len(block) > 1 and (CITE.match(block[-1]) or block[-1].startswith(("—", "–"))):
            cite = block.pop()
        else:
            j = i
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and len(lines[j]) < 120 and (CITE.match(lines[j]) or lines[j].startswith(("—", "–"))):
                cite = lines[j].strip()
        quote = " ".join(block)
        if not cite:
            # The foundation's one-line form: > "words" (Romans 3:23, KJV)
            m = re.search(r"\(([^()]+?\d+\s*[:.]\s*\d+(?:\s*[-–]\s*\d+)?),?\s*(KJV|TB)\b[^)]*\)\s*$", quote)
            if m:
                quote, cite = quote[:m.start()], f"{m.group(1)} ({m.group(2)})"
        yield start + 1, quote, cite


def items(path):
    if path.name.endswith(".json"):
        deck = json.loads(path.read_text())
        for n, sl in enumerate(deck.get("slides", []), 1):
            if sl.get("type") == "verse":
                yield f"slide {n}", sl.get("text", ""), sl.get("ref", "")
    else:
        for line, quote, cite in quotes_in_markdown(path.read_text(errors="replace")):
            yield f"line {line}", quote, cite


def check(path):
    ok = bad = other = skipped = 0
    for where, quote, cite in items(path):
        m = CITE.match(cite)
        if not m:
            other += 1
            continue
        version, ref = m.group("a") or m.group("b"), m.group("ref").strip(" *—–-")
        if ";" in ref or re.search(r"\d\s*[;,]\s*\d+\s*:", cite):
            skipped += 1
            print(f"  SKIPPED  {path.name} {where}: {cite.strip()} names several passages")
            continue
        try:
            source = passage(version, ref)
        except H.NotFound as e:
            bad += 1
            print(f"  FAIL     {path.name} {where}: {ref} ({version}): {e}")
            continue
        if source is None:
            if version not in _unreachable:
                _unreachable.append(version)
            skipped += 1
            continue
        diff = compare(quote, source)
        if diff:
            bad += 1
            print(f"  FAIL     {path.name} {where}: {ref} ({version})\n      {diff}")
        else:
            ok += 1
    return ok, bad, other, skipped


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not args:
        print(__doc__)
        raise SystemExit(64)
    files = []
    for a in args:
        p = Path(a).expanduser()
        if p.is_dir():
            files += sorted(f for f in p.rglob("*") if f.suffix == ".md" and f.name != "README.md" or f.name == "deck.json")
        elif p.is_file():
            files.append(p)
        else:
            sys.exit(f"No such file or folder: {a}")
    total = [0, 0, 0, 0]
    for f in files:
        r = check(f)
        total = [x + y for x, y in zip(total, r)]
        if any(r):
            print(f"{f.name}: {r[0]} match, {r[1]} differ, {r[3]} skipped, {r[2]} not Scripture (unchecked)")
    ok, bad, other, skipped = total
    print(f"\nScripture quotations: {ok} match, {bad} differ, {skipped} not checked. "
          f"Other quotations (Ellen White, commentaries): {other}, not checked by this tool.")
    if _unreachable:
        print(f"Could not reach the source for {', '.join(_unreachable)}; those quotations were not checked. Retry later.",
              file=sys.stderr)
    raise SystemExit(1 if bad else 2 if _unreachable else 0)


if __name__ == "__main__":
    main()
