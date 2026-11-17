#!/usr/bin/env python3
"""helloao-fetch.py — public-domain commentaries and open Bible translations by verse.

Reads the Free Use Bible API (bible.helloao.org, no key). It serves seven
commentaries and about 1,500 translations as JSON.

Usage
  helloao-fetch.py commentary "Revelation 14:1-5"             # every commentary on the span
  helloao-fetch.py commentary "Rev 14:3" --only matthew-henry,tyndale
  helloao-fetch.py commentary "Wahyu 14:3" --full              # no 400-word cap per commentary
  helloao-fetch.py verse "Revelation 14:3"                     # eng_kjv, BSB, ind_tsi
  helloao-fetch.py verse "Mazmur 40:3-4" --t ind_tsi,ind_ayt
  helloao-fetch.py list commentaries
  helloao-fetch.py list translations indonesian                # filter by language or name

Commentary ids: adam-clarke, jamieson-fausset-brown, john-calvin, john-gill,
keil-delitzsch (Old Testament only), matthew-henry, tyndale.

A commentary entry is keyed to the verse it starts at and runs to the next
entry, so Matthew Henry's entry "from verse 1" on Revelation 14 covers verses
1-5. Each entry prints with the span it covers.

Exit codes: 0 text printed · 1 nothing found for that reference · 2 the API
could not be reached (a network failure: retry later) · 64 bad usage.

Honesty rules for anything you cite from this
  - None of these commentaries is Adventist. Read each against the state of the
    dead, the Sabbath and the sanctuary before using a sentence from it.
  - Terjemahan Baru is not served here. ind_tsi is the Terjemahan Sederhana
    Indonesia, a plain-language version, not a substitute for TB in citations.
"""
import json
import re
import sys
import time
import urllib.error
import urllib.request

API = "https://bible.helloao.org/api"
UA = "Mozilla/5.0 (helloao-fetch)"
CAP = 400
DEFAULT_TRANSLATIONS = ["eng_kjv", "BSB", "ind_tsi"]

# USFM code, English name, Indonesian name, extra abbreviations.
BOOKS = [
    ("GEN", "Genesis", "Kejadian", "gen kej"), ("EXO", "Exodus", "Keluaran", "ex exod kel"),
    ("LEV", "Leviticus", "Imamat", "lev im"), ("NUM", "Numbers", "Bilangan", "num bil"),
    ("DEU", "Deuteronomy", "Ulangan", "deut dt ul"), ("JOS", "Joshua", "Yosua", "josh yos"),
    ("JDG", "Judges", "Hakim-hakim", "judg hak hakim"), ("RUT", "Ruth", "Rut", ""),
    ("1SA", "1 Samuel", "1 Samuel", "1sam"), ("2SA", "2 Samuel", "2 Samuel", "2sam"),
    ("1KI", "1 Kings", "1 Raja-raja", "1kgs 1raj 1 raja"), ("2KI", "2 Kings", "2 Raja-raja", "2kgs 2raj 2 raja"),
    ("1CH", "1 Chronicles", "1 Tawarikh", "1chr 1chron 1taw"), ("2CH", "2 Chronicles", "2 Tawarikh", "2chr 2chron 2taw"),
    ("EZR", "Ezra", "Ezra", "ezr"), ("NEH", "Nehemiah", "Nehemia", "neh"),
    ("EST", "Esther", "Ester", "esth est"), ("JOB", "Job", "Ayub", "ayb"),
    ("PSA", "Psalms", "Mazmur", "psalm ps mzm"), ("PRO", "Proverbs", "Amsal", "prov ams"),
    ("ECC", "Ecclesiastes", "Pengkhotbah", "eccl pkh"), ("SNG", "Song of Solomon", "Kidung Agung", "song songs sos kid"),
    ("ISA", "Isaiah", "Yesaya", "isa yes"), ("JER", "Jeremiah", "Yeremia", "jer yer"),
    ("LAM", "Lamentations", "Ratapan", "lam rat"), ("EZK", "Ezekiel", "Yehezkiel", "ezek eze yeh"),
    ("DAN", "Daniel", "Daniel", "dan"), ("HOS", "Hosea", "Hosea", "hos"),
    ("JOL", "Joel", "Yoel", "joel yl"), ("AMO", "Amos", "Amos", "am"),
    ("OBA", "Obadiah", "Obaja", "obad ob"), ("JON", "Jonah", "Yunus", "jon yun"),
    ("MIC", "Micah", "Mikha", "mic mi"), ("NAM", "Nahum", "Nahum", "nah"),
    ("HAB", "Habakkuk", "Habakuk", "hab"), ("ZEP", "Zephaniah", "Zefanya", "zeph zef"),
    ("HAG", "Haggai", "Hagai", "hag"), ("ZEC", "Zechariah", "Zakharia", "zech za"),
    ("MAL", "Malachi", "Maleakhi", "mal"), ("MAT", "Matthew", "Matius", "matt mt mat"),
    ("MRK", "Mark", "Markus", "mk mrk"), ("LUK", "Luke", "Lukas", "lk luk"),
    ("JHN", "John", "Yohanes", "jn joh yoh"), ("ACT", "Acts", "Kisah Para Rasul", "kis kisah"),
    ("ROM", "Romans", "Roma", "rom rm"), ("1CO", "1 Corinthians", "1 Korintus", "1cor 1kor"),
    ("2CO", "2 Corinthians", "2 Korintus", "2cor 2kor"), ("GAL", "Galatians", "Galatia", "gal"),
    ("EPH", "Ephesians", "Efesus", "eph ef"), ("PHP", "Philippians", "Filipi", "phil flp"),
    ("COL", "Colossians", "Kolose", "col kol"), ("1TH", "1 Thessalonians", "1 Tesalonika", "1thess 1tes"),
    ("2TH", "2 Thessalonians", "2 Tesalonika", "2thess 2tes"), ("1TI", "1 Timothy", "1 Timotius", "1tim"),
    ("2TI", "2 Timothy", "2 Timotius", "2tim"), ("TIT", "Titus", "Titus", "tit"),
    ("PHM", "Philemon", "Filemon", "philem flm"), ("HEB", "Hebrews", "Ibrani", "heb ibr"),
    ("JAS", "James", "Yakobus", "jas yak"), ("1PE", "1 Peter", "1 Petrus", "1pet 1ptr"),
    ("2PE", "2 Peter", "2 Petrus", "2pet 2ptr"), ("1JN", "1 John", "1 Yohanes", "1jn 1yoh"),
    ("2JN", "2 John", "2 Yohanes", "2jn 2yoh"), ("3JN", "3 John", "3 Yohanes", "3jn 3yoh"),
    ("JUD", "Jude", "Yudas", "jud yud"), ("REV", "Revelation", "Wahyu", "rev why apocalypse"),
]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


LOOKUP = {}
for code, en, idn, extra in BOOKS:
    for name in [code, en, idn] + extra.split():
        LOOKUP.setdefault(norm(name), code)
NAMES = {code: en for code, en, _, _ in BOOKS}


class NotFound(Exception):
    pass


def parse_ref(ref):
    """'Revelation 14:1-5' -> (REV, 14, 1, 5). A bare chapter gives verses None."""
    m = re.match(r"^\s*(.+?)\s+(\d+)(?:\s*[:.]\s*(\d+)(?:\s*[-–]\s*(\d+))?)?\s*$", ref)
    if not m:
        raise NotFound(f'Cannot read "{ref}". Write it as "Revelation 14:1-5" or "Wahyu 14:3".')
    code = LOOKUP.get(norm(m.group(1)))
    if not code:
        raise NotFound(f'Unknown book "{m.group(1)}". English and Indonesian names and USFM codes are accepted.')
    v1 = int(m.group(3)) if m.group(3) else None
    v2 = int(m.group(4)) if m.group(4) else v1
    if v1 and v2 < v1:
        raise NotFound(f'"{ref}" ends before it starts.')
    return code, int(m.group(2)), v1, v2


def fetch(path):
    """About 70 seconds at worst, so a dead API reports itself instead of
    holding the caller past a two-minute command timeout."""
    last = None
    for i in range(3):
        try:
            req = urllib.request.Request(f"{API}/{path}", headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (403, 404):
                raise NotFound(f"The API has nothing at {path} (HTTP {e.code}).")
            last = e
        except Exception as e:                       # timeouts, DNS, bad JSON
            last = e
        if i < 2:
            time.sleep(2 * (i + 1))
    print(f"Could not reach {API}/{path} after 3 attempts ({last}). "
          "This is a network failure, not a missing text: retry later.", file=sys.stderr)
    raise SystemExit(2)


def flatten(content):
    """A verse or commentary entry is a list of strings and small objects."""
    out = []
    for part in content or []:
        if isinstance(part, str):
            out.append(part)
        elif isinstance(part, dict):
            if part.get("lineBreak"):
                out.append("\n")
            elif "text" in part:
                out.append(str(part["text"]))
            elif "heading" in part:
                out.append(str(part["heading"]))
    text = " ".join(out)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" ?\n ?", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def cap(text, limit):
    words = text.split(" ")
    if limit is None or len(text.split()) <= limit:
        return text, False
    kept, count = [], 0
    for w in words:
        count += len(w.split()) or 0
        if count > limit:
            break
        kept.append(w)
    return " ".join(kept).rstrip() + " …", True


def cmd_commentary(ref, only, full):
    code, chap, v1, v2 = parse_ref(ref)
    listing = fetch("available_commentaries.json")["commentaries"]
    known = {c["id"]: c for c in listing}
    ids = only or list(known)
    bad = [i for i in ids if i not in known]
    if bad:
        raise NotFound(f"Unknown commentary id: {', '.join(bad)}. Known: {', '.join(known)}.")
    printed = 0
    for cid in ids:
        try:
            data = fetch(f"c/{cid}/{code}/{chap}.json")
        except NotFound:
            print(f"## {known[cid].get('name', cid)} [{cid}]\n(no entry for {NAMES[code]} {chap})\n")
            continue
        entries = [e for e in data["chapter"]["content"] if e.get("type") == "verse"]
        entries.sort(key=lambda e: e["number"])
        last_verse = max([e["number"] for e in entries] + [v2 or 0])
        spans = []
        for i, e in enumerate(entries):
            end = entries[i + 1]["number"] - 1 if i + 1 < len(entries) else None
            spans.append((e["number"], end, e))
        if v1 is None:
            chosen = spans
        else:
            chosen = [s for s in spans if s[0] <= v2 and (s[1] is None or s[1] >= v1)]
        print(f"## {known[cid].get('name', cid)} [{cid}]")
        if not chosen:
            print(f"(no entry covering {NAMES[code]} {chap}:{v1}" + (f"-{v2}" if v2 != v1 else "") + ")\n")
            continue
        budget = None if full else CAP
        used, truncated = 0, False
        for start, end, e in chosen:
            span = f"{chap}:{start}" + (f"-{end}" if end and end != start else "" if end else " to the end of the entry")
            text = flatten(e.get("content"))
            if budget is not None:
                remaining = budget - used
                if remaining <= 0:
                    truncated = True
                    break
                text, cut = cap(text, remaining)
                truncated = truncated or cut
                used += len(text.split())
            print(f"\n[{NAMES[code]} {span}]\n{text}")
            printed += 1
        if truncated:
            print(f"\n(cut at {CAP} words; rerun with --full for the whole entry)")
        print()
    if not printed:
        raise NotFound(f"No commentary entry found for {ref}.")
    print("Not Adventist sources. Check any sentence against the state of the dead, "
          "the Sabbath and the sanctuary before using it.")


def cmd_verse(ref, translations):
    code, chap, v1, v2 = parse_ref(ref)
    printed = 0
    for tid in translations:
        try:
            data = fetch(f"{tid}/{code}/{chap}.json")
        except NotFound:
            print(f"## {tid}\n(no {NAMES[code]} {chap} in this translation)\n")
            continue
        name = data["translation"].get("englishName") or data["translation"].get("name") or tid
        print(f"## {name} [{tid}]")
        for e in data["chapter"]["content"]:
            if e.get("type") != "verse":
                continue
            if v1 is None or v1 <= e["number"] <= v2:
                print(f"{chap}:{e['number']} {flatten(e.get('content'))}")
                printed += 1
        print()
    if not printed:
        raise NotFound(f"No verse text found for {ref}.")


def cmd_list(what, needle):
    if what == "commentaries":
        for c in fetch("available_commentaries.json")["commentaries"]:
            print(f"{c['id']:26} {c.get('numberOfBooks', '?'):>3} books  {c.get('name', '')}  {c.get('licenseUrl', '')}")
    elif what == "translations":
        rows = fetch("available_translations.json")["translations"]
        n = (needle or "").lower()
        shown = 0
        for t in rows:
            hay = " ".join(str(t.get(k, "")) for k in ("id", "englishName", "name", "language", "languageEnglishName", "languageName")).lower()
            if n and n not in hay:
                continue
            print(f"{t['id']:14} {t.get('language', ''):5} {t.get('englishName', '')}")
            shown += 1
        if not shown:
            raise NotFound(f'No translation matches "{needle}".')
    else:
        raise SystemExit(64)


def main():
    a = sys.argv[1:]
    if len(a) < 2 or a[0] not in ("commentary", "verse", "list"):
        print(__doc__)
        raise SystemExit(64)
    try:
        if a[0] == "commentary":
            only = None
            if "--only" in a:
                only = [x.strip() for x in a[a.index("--only") + 1].split(",") if x.strip()]
            cmd_commentary(a[1], only, "--full" in a)
        elif a[0] == "verse":
            t = DEFAULT_TRANSLATIONS
            if "--t" in a:
                t = [x.strip() for x in a[a.index("--t") + 1].split(",") if x.strip()]
            cmd_verse(a[1], t)
        else:
            cmd_list(a[1], a[2] if len(a) > 2 else None)
    except NotFound as e:
        print(str(e), file=sys.stderr)
        raise SystemExit(1)
    except IndexError:
        print(__doc__)
        raise SystemExit(64)


if __name__ == "__main__":
    main()
