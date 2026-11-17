#!/usr/bin/env python3
"""bible.py — original-language words, lexicon, cross-references and verse text.

Local first: reads a SQLite database built from open datasets. Where that
database is absent (another computer, a fresh checkout) every command falls
back to free APIs and says so on its first line, so the same skill
instructions work everywhere.

Usage
  bible.py pack "Revelation 14:1-5"      # one bundle for a study: text, words, variants, lexicon, cross-references
  bible.py pack "Revelation 14:1-5" --brief   # the same without the per-word table, and five cross-references
  bible.py words "Exodus 15:1"           # every Hebrew or Greek word with Strong's number, parsing and gloss
  bible.py strongs G5603                 # lexicon entry and where the word occurs
  bible.py xref "Revelation 14:3" -n 12  # cross-references, most-voted first
  bible.py verse "Wahyu 14:3" --t eng_kjv,BSB,ind_ayt
  bible.py commentary "Rev 14:3"         # classic commentaries (delegates to helloao-fetch.py)
  bible.py status                        # local or fallback, what is loaded, when it was synced
  bible.py sync [--refresh]              # download the datasets (about 135 MB) and build the database

Data lives in $BIBLE_DATA, default ~/DEV/bible-data. Book names may be English,
Indonesian or USFM codes.

Local sources (see `status` for dates):
  STEPBible TAGNT/TAHOT and TBESG/TBESH, CC BY 4.0 (www.STEPBible.org)
  OpenBible.info cross-references, CC BY
  KJV, Berean Standard Bible, Alkitab Yang Terbuka via the Free Use Bible API
Fallback sources: bible.helloao.org (text), bolls.life (Strong's-tagged KJV and
a brief lexicon), OpenBible.info (cross-references, fetched to a temp cache).
The fallback gives Strong's numbers without parsing, and no KJV-versus-NA28
word differences.

Exit codes: 0 printed · 1 nothing found · 2 network failure, retry · 64 usage.
Terjemahan Baru is not stored or served here; keep citing it from its own source.
"""
import html
import importlib.util
import io
import json
import os
import re
import sqlite3
import sys
import tempfile
import time
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("helloao", HERE / "helloao-fetch.py")
H = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(H)
NotFound = H.NotFound

DATA = Path(os.environ.get("BIBLE_DATA", "~/DEV/bible-data")).expanduser()
DB = DATA / "bible.db"
RAW = DATA / "raw"
USFM = [b[0] for b in H.BOOKS]
OSIS = ("Gen Exod Lev Num Deut Josh Judg Ruth 1Sam 2Sam 1Kgs 2Kgs 1Chr 2Chr Ezra Neh Esth Job Ps Prov "
        "Eccl Song Isa Jer Lam Ezek Dan Hos Joel Amos Obad Jonah Mic Nah Hab Zeph Hag Zech Mal Matt Mark "
        "Luke John Acts Rom 1Cor 2Cor Gal Eph Phil Col 1Thess 2Thess 1Tim 2Tim Titus Phlm Heb Jas 1Pet "
        "2Pet 1John 2John 3John Jude Rev").split()
OSIS2USFM = dict(zip(OSIS, USFM))
STEP = "https://raw.githubusercontent.com/STEPBible/STEPBible-Data/master"
TA = STEP + "/Translators%20Amalgamated%20OT%2BNT/"
SOURCES = [
    ("tagnt-1.txt", TA + "TAGNT%20Mat-Jhn%20-%20Translators%20Amalgamated%20Greek%20NT%20-%20STEPBible.org%20CC-BY.txt"),
    ("tagnt-2.txt", TA + "TAGNT%20Act-Rev%20-%20Translators%20Amalgamated%20Greek%20NT%20-%20STEPBible.org%20CC-BY.txt"),
    ("tahot-1.txt", TA + "TAHOT%20Gen-Deu%20-%20Translators%20Amalgamated%20Hebrew%20OT%20-%20STEPBible.org%20CC%20BY.txt"),
    ("tahot-2.txt", TA + "TAHOT%20Jos-Est%20-%20Translators%20Amalgamated%20Hebrew%20OT%20-%20STEPBible.org%20CC%20BY.txt"),
    ("tahot-3.txt", TA + "TAHOT%20Job-Sng%20-%20Translators%20Amalgamated%20Hebrew%20OT%20-%20STEPBible.org%20CC%20BY.txt"),
    ("tahot-4.txt", TA + "TAHOT%20Isa-Mal%20-%20Translators%20Amalgamated%20Hebrew%20OT%20-%20STEPBible.org%20CC%20BY.txt"),
    ("tbesg.txt", STEP + "/Lexicons/TBESG%20-%20Translators%20Brief%20lexicon%20of%20Extended%20Strongs%20for%20Greek%20-%20STEPBible.org%20CC%20BY.txt"),
    ("tbesh.txt", STEP + "/Lexicons/TBESH%20-%20Translators%20Brief%20lexicon%20of%20Extended%20Strongs%20for%20Hebrew%20-%20STEPBible.org%20CC%20BY.txt"),
    ("cross-references.zip", "https://a.openbible.info/data/cross-references.zip"),
    ("eng_kjv.json", "https://bible.helloao.org/api/eng_kjv/complete.json"),
    ("BSB.json", "https://bible.helloao.org/api/BSB/complete.json"),
    ("ind_ayt.json", "https://bible.helloao.org/api/ind_ayt/complete.json"),
]
LOCAL_TEXTS = ["eng_kjv", "BSB", "ind_ayt"]


def strong(s):
    """G103, G0103, H7892a -> G0103, G0103, H7892A."""
    m = re.match(r"^([GHgh])0*(\d+)([A-Za-z]?)$", s.strip())
    return f"{m.group(1).upper()}{int(m.group(2)):04d}{m.group(3).upper()}" if m else s.strip().upper()


def strip_tags(s):
    s = re.sub(r"(?i)<br\s*/?>", "; ", s)
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    return re.sub(r"\s+", " ", s).strip(" ;")


def http_bytes(url):
    last = None
    for i in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (bible.py)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            last = e
            if i < 2:
                time.sleep(2 * (i + 1))
    print(f"Could not reach {url} after 3 attempts ({last}). "
          "This is a network failure, not a missing text: retry later.", file=sys.stderr)
    raise SystemExit(2)


# ---------------------------------------------------------------- sync

def sync(refresh):
    RAW.mkdir(parents=True, exist_ok=True)
    for name, url in SOURCES:
        f = RAW / name
        if f.exists() and not refresh:
            continue
        print(f"downloading {name} …", flush=True)
        f.write_bytes(http_bytes(url))
    tmp = DATA / "bible.db.tmp"
    if tmp.exists():
        tmp.unlink()
    db = sqlite3.connect(tmp)
    db.executescript("""
      CREATE TABLE words(book TEXT, chap INT, verse INT, pos INT, lang TEXT, orig TEXT, translit TEXT,
                         english TEXT, strongs TEXT, morph TEXT, lemma TEXT, gloss TEXT, type TEXT, variant TEXT);
      CREATE TABLE lexicon(strongs TEXT PRIMARY KEY, lemma TEXT, translit TEXT, pos TEXT, gloss TEXT, definition TEXT);
      CREATE TABLE xrefs(book TEXT, chap INT, verse INT, target TEXT, votes INT);
      CREATE TABLE verses(tid TEXT, book TEXT, chap INT, verse INT, text TEXT);
      CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT);
    """)
    ref = re.compile(r"^([1-3A-Z][A-Za-z]{2})\.(\d+)\.(\d+)(?:\([^)]*\))?#(\d+)=(\S+)")
    rows = []
    for name in ("tagnt-1.txt", "tagnt-2.txt"):
        for line in (RAW / name).read_text(encoding="utf-8").splitlines():
            c = line.split("\t")
            m = ref.match(c[0])
            if not m or len(c) < 6 or m.group(1).upper() not in USFM:
                continue
            g = re.match(r"^(.*?)\s*\((.*)\)\s*$", c[1])
            orig, translit = (g.group(1), g.group(2)) if g else (c[1], "")
            sm = c[3].split("=", 1)
            lemma, _, gloss = c[4].partition("=")
            rows.append((m.group(1).upper(), int(m.group(2)), int(m.group(3)), int(m.group(4)), "G", orig, translit,
                         c[2], strong(sm[0].split("+")[0]), sm[1] if len(sm) > 1 else "", lemma, gloss, m.group(5),
                         c[6].strip() if len(c) > 6 else ""))
    for name in ("tahot-1.txt", "tahot-2.txt", "tahot-3.txt", "tahot-4.txt"):
        for line in (RAW / name).read_text(encoding="utf-8").splitlines():
            c = line.split("\t")
            m = ref.match(c[0])
            if not m or len(c) < 6 or m.group(1).upper() not in USFM:
                continue
            main = re.search(r"\{([^}]+)\}", c[4])
            sid = strong(main.group(1)) if main else strong(re.split(r"[\\/]", c[4])[0])
            lemma = gloss = ""
            if len(c) > 11:
                e = re.search(r"\{[^=}]+=([^=}]*)=([^}]*)\}", c[11])
                if e:
                    lemma, gloss = e.group(1), e.group(2).split("»")[0]
            rows.append((m.group(1).upper(), int(m.group(2)), int(m.group(3)), int(m.group(4)), "H",
                         c[1].replace("\\", ""), c[2], c[3], sid, c[5], lemma, gloss, m.group(5), ""))
    db.executemany("INSERT INTO words VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)
    lex = {}
    for name in ("tbesg.txt", "tbesh.txt"):
        for line in (RAW / name).read_text(encoding="utf-8").splitlines():
            c = line.split("\t")
            if len(c) < 8 or not re.match(r"^[GH]\d+[A-Za-z]?$", c[0]):
                continue
            sid = strong(c[1].replace("=", "").strip() or c[0])
            lex.setdefault(sid, (sid, c[3], c[4], c[5], c[6], strip_tags(c[7])))
    db.executemany("INSERT INTO lexicon VALUES(?,?,?,?,?,?)", list(lex.values()))
    xr, stamp = [], ""
    with zipfile.ZipFile(RAW / "cross-references.zip") as z:
        text = z.read(z.namelist()[0]).decode("utf-8")
    for i, line in enumerate(text.splitlines()):
        c = line.split("\t")
        if i == 0:
            stamp = c[-1].lstrip("#") if len(c) > 3 else ""
            continue
        a = c[0].split(".")
        if len(c) < 3 or a[0] not in OSIS2USFM:
            continue
        xr.append((OSIS2USFM[a[0]], int(a[1]), int(a[2]), c[1], int(c[2])))
    db.executemany("INSERT INTO xrefs VALUES(?,?,?,?,?)", xr)
    vs = []
    for tid in LOCAL_TEXTS:
        d = json.loads((RAW / f"{tid}.json").read_text(encoding="utf-8"))
        for b in d["books"]:
            for ch in b["chapters"]:
                for e in ch["chapter"]["content"]:
                    if e.get("type") == "verse":
                        vs.append((tid, b["id"], ch["chapter"]["number"], e["number"], H.flatten(e.get("content"))))
    db.executemany("INSERT INTO verses VALUES(?,?,?,?,?)", vs)
    db.executescript("""
      CREATE INDEX w_ref ON words(book, chap, verse, pos);
      CREATE INDEX w_str ON words(strongs);
      CREATE INDEX x_ref ON xrefs(book, chap, verse);
      CREATE INDEX v_ref ON verses(tid, book, chap, verse);
    """)
    db.executemany("INSERT INTO meta VALUES(?,?)", [
        ("synced", time.strftime("%Y-%m-%d")), ("openbible", stamp),
        ("words", str(len(rows))), ("lexicon", str(len(lex))), ("xrefs", str(len(xr))), ("verses", str(len(vs)))])
    db.commit()
    db.close()
    os.replace(tmp, DB)
    print(f"built {DB}: {len(rows):,} words, {len(lex):,} lexicon entries, {len(xr):,} cross-references, {len(vs):,} verses")


# ---------------------------------------------------------------- access

def local():
    return sqlite3.connect(DB) if DB.exists() else None


def banner(db):
    if db:
        row = db.execute("SELECT value FROM meta WHERE key='synced'").fetchone()
        return f"(local data, synced {row[0]})"
    return "(fallback: no local database here, reading free APIs; run `bible.py sync` for full data)"


def span(v1, v2):
    return "" if v1 is None else (f":{v1}" if v1 == v2 else f":{v1}-{v2}")


def verse_filter(v1, v2):
    return ("", []) if v1 is None else (" AND verse BETWEEN ? AND ?", [v1, v2])


def get_text(db, tid, code, chap, v1, v2):
    """[(verse, text)] from the local table, else the API."""
    if db and tid in LOCAL_TEXTS:
        w, p = verse_filter(v1, v2)
        return db.execute(f"SELECT verse, text FROM verses WHERE tid=? AND book=? AND chap=?{w} ORDER BY verse",
                          [tid, code, chap] + p).fetchall()
    data = H.fetch(f"{tid}/{code}/{chap}.json")
    return [(e["number"], H.flatten(e.get("content"))) for e in data["chapter"]["content"]
            if e.get("type") == "verse" and (v1 is None or v1 <= e["number"] <= v2)]


def get_words(db, code, chap, v1, v2):
    """[(verse, pos, orig, translit, english, strongs, morph, lemma, gloss, type, variant)]"""
    if db:
        w, p = verse_filter(v1, v2)
        return db.execute("SELECT verse,pos,orig,translit,english,strongs,morph,lemma,gloss,type,variant FROM words "
                          f"WHERE book=? AND chap=?{w} ORDER BY verse,pos", [code, chap] + p).fetchall()
    num = USFM.index(code) + 1
    letter = "G" if num >= 40 else "H"
    raw = json.loads(http_bytes(f"https://bolls.life/get-text/KJV/{num}/{chap}/"))
    out = []
    for v in raw:
        if v1 is not None and not (v1 <= v["verse"] <= v2):
            continue
        text = re.sub(r"<sup>.*?</sup>|<i>|</i>", "", v["text"])
        pos = 0
        for m in re.finditer(r"([^<]*?)((?:<S>\d+</S>)+)", text):
            for n in re.findall(r"<S>(\d+)</S>", m.group(2)):
                pos += 1
                out.append((v["verse"], pos, "", "", m.group(1).strip(" ,.;:"), strong(letter + n), "", "", "", "", ""))
    return out


def get_lexicon(db, sid):
    """(lemma, translit, pos, gloss, definition, count) or None."""
    if db:
        r = db.execute("SELECT lemma,translit,pos,gloss,definition FROM lexicon WHERE strongs=?", [sid]).fetchone()
        if not r:
            r = db.execute("SELECT lemma,translit,pos,gloss,definition FROM lexicon WHERE strongs LIKE ? ORDER BY strongs",
                           [sid + "%"]).fetchone()
        if not r:
            return None
        n = db.execute("SELECT COUNT(*) FROM words WHERE strongs=? OR strongs LIKE ?", [sid, sid + "_"]).fetchone()[0]
        return r + (n,)
    plain = re.sub(r"^([GH])0+", r"\1", sid)
    d = json.loads(http_bytes(f"https://bolls.life/dictionary-definition/BDBT/{plain}/"))
    if not d:
        return None
    e = d[0]
    return (strip_tags(e.get("lexeme", "")), e.get("transliteration", ""), "", e.get("short_definition", "") or "",
            strip_tags(e.get("definition", "")), None)


def get_xrefs(db, code, chap, v1, v2, n):
    if db:
        w, p = verse_filter(v1, v2)
        return db.execute(f"SELECT verse,target,votes FROM xrefs WHERE book=? AND chap=?{w} ORDER BY votes DESC LIMIT ?",
                          [code, chap] + p + [n]).fetchall()
    cache = Path(tempfile.gettempdir()) / "bible-py-cross-references.zip"
    if not cache.exists():
        cache.write_bytes(http_bytes("https://a.openbible.info/data/cross-references.zip"))
    with zipfile.ZipFile(cache) as z:
        text = z.read(z.namelist()[0]).decode("utf-8")
    key = f"{OSIS[USFM.index(code)]}.{chap}."
    hits = []
    for line in io.StringIO(text):
        if line.startswith(key):
            c = line.rstrip("\n").split("\t")
            v = int(c[0].split(".")[2])
            if v1 is None or v1 <= v <= v2:
                hits.append((v, c[1], int(c[2])))
    return sorted(hits, key=lambda h: -h[2])[:n]


def pretty_target(t):
    """Rev.14.1 or Ps.98.1-Ps.98.3 -> (label, code, chap, v1, v2)."""
    a, _, b = t.partition("-")
    x = a.split(".")
    code, chap, v1 = OSIS2USFM.get(x[0]), int(x[1]), int(x[2])
    v2 = v1
    if b:
        y = b.split(".")
        if y[0] == x[0] and int(y[1]) == chap:
            v2 = int(y[2])
    return f"{H.NAMES.get(code, x[0])} {chap}{span(v1, v2)}", code, chap, v1, v2


def variant_note(t):
    if not t:
        return None
    if "K" in t and "N" not in t.upper().replace("(N)", ""):
        return "in the KJV's Greek (Textus Receptus), not in NA28"
    if t.replace("(k)", "").replace("(K)", "").find("K") < 0 and "k" not in t.replace("(k)", "") and "N" in t:
        return None if "(" in t else "in NA28, not in the KJV's Greek"
    if t in ("k", "ko"):
        return "a different reading in the KJV's Greek, not in NA28"
    if t in ("no", "n"):
        return "a different reading in NA28, not in the KJV's Greek"
    return None


# ---------------------------------------------------------------- commands

def print_words(rows, lang):
    cur = None
    for v, pos, orig, tr, eng, sid, morph, lemma, gloss, typ, _var in rows:
        if v != cur:
            print(f"\nverse {v}")
            cur = v
        bits = [f"{pos:>3}", orig, f"({tr})" if tr else "", sid, morph, f"{lemma} = {gloss}" if lemma else "", f"→ {eng}"]
        print("  " + "  ".join(b for b in bits if b))


def cmd_words(ref):
    code, chap, v1, v2 = H.parse_ref(ref)
    db = local()
    rows = get_words(db, code, chap, v1, v2)
    if not rows:
        raise NotFound(f"No word data for {ref}.")
    print(f"# Words: {H.NAMES[code]} {chap}{span(v1, v2)} {banner(db)}")
    print_words(rows, "")


def cmd_strongs(sid):
    sid = strong(sid)
    db = local()
    e = get_lexicon(db, sid)
    if not e:
        raise NotFound(f"No lexicon entry for {sid}.")
    lemma, tr, pos, gloss, definition, n = e
    print(f"# {sid} {banner(db)}\n{lemma} ({tr}) {pos}  {gloss}\n{definition}")
    if db:
        refs = db.execute("SELECT DISTINCT book,chap,verse FROM words WHERE strongs=? OR strongs LIKE ? "
                          "ORDER BY rowid LIMIT 40", [sid, sid + "_"]).fetchall()
        print(f"\nOccurs {n} time(s). " + ("First 40: " if n > 40 else "") +
              "; ".join(f"{b} {c}:{v}" for b, c, v in refs))


def cmd_xref(ref, n):
    code, chap, v1, v2 = H.parse_ref(ref)
    db = local()
    rows = get_xrefs(db, code, chap, v1, v2, n)
    if not rows:
        raise NotFound(f"No cross-references for {ref}.")
    print(f"# Cross-references: {H.NAMES[code]} {chap}{span(v1, v2)} {banner(db)}")
    xref_lines(db, rows, chap)
    print("\nSource: OpenBible.info, CC BY. Votes are reader votes, a rough measure of relevance.")


def xref_lines(db, rows, chap):
    for v, target, votes in rows:
        label, tcode, tchap, t1, t2 = pretty_target(target)
        text = ""
        if db and tcode:
            got = get_text(db, "eng_kjv", tcode, tchap, t1, t2)
            text = " ".join(t for _, t in got)
            if len(text) > 220:
                text = text[:217].rsplit(" ", 1)[0] + " …"
        print(f"  {chap}:{v} → {label} ({votes})" + (f"  {text}" if text else ""))


def cmd_verse(ref, tids):
    code, chap, v1, v2 = H.parse_ref(ref)
    db = local()
    print(f"# {H.NAMES[code]} {chap}{span(v1, v2)} {banner(db)}")
    shown = 0
    for tid in tids:
        try:
            rows = get_text(db, tid, code, chap, v1, v2)
        except NotFound:
            rows = []
        print(f"\n## {tid}")
        if not rows:
            print("(not in this translation)")
        for v, t in rows:
            print(f"{chap}:{v} {t}")
            shown += 1
    if not shown:
        raise NotFound(f"No verse text found for {ref}.")


def cmd_pack(ref, brief=False):
    code, chap, v1, v2 = H.parse_ref(ref)
    db = local()
    lang = "Greek" if USFM.index(code) >= 39 else "Hebrew"
    print(f"# Study pack: {H.NAMES[code]} {chap}{span(v1, v2)} {banner(db)}")
    print("\n## Text")
    for tid in LOCAL_TEXTS:
        try:
            rows = get_text(db, tid, code, chap, v1, v2)
        except NotFound:
            rows = []
        print(f"\n[{tid}]")
        for v, t in rows:
            print(f"{chap}:{v} {t}")
    words = get_words(db, code, chap, v1, v2)
    if brief:
        print(f"\n## Words ({lang}): {len(words)} in the span; left out of the brief pack, see `bible.py words \"{ref}\"`")
    else:
        print(f"\n## Words ({lang})")
        print_words(words, lang)
    if db and lang == "Greek":
        notes = []
        for v, _, orig, tr, eng, _, _, _, _, typ, var in words:
            if var:
                notes.append((v, orig, tr, eng, "other editions read " + re.sub(r"\s+", " ", var)))
            elif variant_note(typ):
                notes.append((v, orig, tr, eng, variant_note(typ)))
        print("\n## Where the KJV's Greek and NA28 differ")
        if notes:
            for v, orig, tr, eng, note in notes:
                print(f"  {chap}:{v}  {orig} ({tr}) \"{eng}\": {note}")
        else:
            print("  None recorded in this span.")
    print("\n## Lexicon: the less common words")
    seen, shown = set(), 0
    for row in words:
        sid = row[5]
        if sid in seen:
            continue
        seen.add(sid)
        e = get_lexicon(db, sid) if db else None
        if not e or e[5] is None or e[5] > 150 or shown >= 14:
            continue
        lemma, tr, pos, gloss, definition, n = e
        d = definition if len(definition) <= 260 else definition[:257].rsplit(" ", 1)[0] + " …"
        print(f"  {sid}  {lemma} ({tr})  {gloss}  [{n}×]  {d}")
        shown += 1
    if not db:
        print("  (needs the local database; in fallback use `bible.py strongs <number>` for one word at a time)")
    elif not shown:
        print("  (every word here occurs more than 150 times)")
    xr = get_xrefs(db, code, chap, v1, v2, 5 if brief else 10)
    print("\n## Cross-references (most-voted first)")
    xref_lines(db, xr, chap)
    print(f"\n## Next\n  bible.py commentary \"{ref}\"   # classic commentaries on this span"
          "\n  Terjemahan Baru, SDABC, Ellen White and BRI come from their own tools.")


def cmd_status():
    db = local()
    print(f"data folder: {DATA}")
    if not db:
        print("mode: fallback (no bible.db). Text from bible.helloao.org, Strong's from bolls.life, "
              "cross-references from OpenBible.info. Run `bible.py sync` to build the local database.")
        return
    meta = dict(db.execute("SELECT key,value FROM meta").fetchall())
    size = DB.stat().st_size / 1048576
    print(f"mode: local · synced {meta.get('synced')} · bible.db {size:.0f} MB")
    try:
        age = (time.time() - time.mktime(time.strptime(meta.get("synced", ""), "%Y-%m-%d"))) / 86400
        if age > 180:
            print(f"WARNING: the data is {age:.0f} days old. Run `bible.py sync --refresh` to download it again.")
    except ValueError:
        pass
    print(f"words {int(meta['words']):,} · lexicon {int(meta['lexicon']):,} · cross-references {int(meta['xrefs']):,} "
          f"(OpenBible {meta.get('openbible', '')}) · verses {int(meta['verses']):,} in {', '.join(LOCAL_TEXTS)}")


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        raise SystemExit(64)
    try:
        cmd = a[0]
        if cmd == "status":
            cmd_status()
        elif cmd == "sync":
            sync("--refresh" in a)
        elif cmd == "pack":
            cmd_pack(a[1], "--brief" in a)
        elif cmd == "words":
            cmd_words(a[1])
        elif cmd == "strongs":
            cmd_strongs(a[1])
        elif cmd == "xref":
            cmd_xref(a[1], int(a[a.index("-n") + 1]) if "-n" in a else 8)
        elif cmd == "verse":
            cmd_verse(a[1], [x.strip() for x in a[a.index("--t") + 1].split(",")] if "--t" in a else LOCAL_TEXTS)
        elif cmd == "commentary":
            H.cmd_commentary(a[1], [x.strip() for x in a[a.index("--only") + 1].split(",")] if "--only" in a else None,
                             "--full" in a)
        else:
            print(__doc__)
            raise SystemExit(64)
    except NotFound as e:
        print(str(e), file=sys.stderr)
        raise SystemExit(1)
    except (IndexError, ValueError):
        print(__doc__)
        raise SystemExit(64)


if __name__ == "__main__":
    main()
