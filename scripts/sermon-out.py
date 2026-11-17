#!/usr/bin/env python3
"""sermon-out.py — where a sermon or Bible study is saved, and how its folder is laid out.

The one place that knows the output location, so no skill carries a path.

Usage
  sermon-out.py root                           # print the output root and why it was chosen
  sermon-out.py dir 2026-11-21 "Sermon Title"  # create the title folder, print its path
  sermon-out.py dir - "Study Title"            # no date known: the title alone
  sermon-out.py dir 2026-11-28 "ss Lesson Title"   # a Sabbath School guide: the title starts with "ss"
  sermon-out.py tidy <folder>                  # file loose items into the layout, rewrite README.md
  sermon-out.py tidy <folder> --index-only     # move nothing, only rewrite README.md
  sermon-out.py layout                         # print the layout

Root, first match wins
  1. $SERMON_OUTPUT
  2. the sermon library's inbox in OneDrive (when the library exists on this computer)
  3. <repo>/output                             (any other computer)

Layout of one title folder
  README.md       what this is and what is in it (written by `tidy`)
  study/          bible-study.md, bible-study.html
  sermon/         research-notes.md, sermon-outline.md, sermon-manuscript.md
  slides/         slides.md, deck.json, the .pptx and its .pdf
  _resources/     source texts fetched for the work (commentary, articles, verse dumps)
  _assets/        images and other media

A Sabbath School folder ([date]-ss-[title]) stays flat, because the publisher
names the lesson after the folder that holds the page:
  teachers-guide.md, teachers-guide.html, slides/
`tidy` never moves teachers-guide files, and never moves anything in a folder
that already has subfolders of its own beyond the layout (old work whose
scripts and pages point at those subfolders).

The inbox is a landing place: the preacher moves a finished folder into the
library's numbered categories by hand. Only finished files belong in it. Build
folders (node_modules, a Python venv) stay out of OneDrive.
"""
import os
import re
import shutil
import sys
import time
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LIBRARY = Path.home() / "Library/CloudStorage/OneDrive-Personal/_HOME/_sermon"

STUDY = {"bible-study.md", "bible-study.html"}
SERMON = {"research-notes.md", "sermon-outline.md", "sermon-manuscript.md"}
SLIDE_NAMES = {"slides.md", "deck.json"}
SLIDE_EXT = {".pptx", ".ppt", ".key", ".pdf"}
ASSET_EXT = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".mp3", ".mp4", ".mov", ".m4a", ".wav"}
JUNK = {".DS_Store"}
LAYOUT = {"study", "sermon", "slides", "_resources", "_assets"}
LABELS = [
    ("study", "Bible study"), ("sermon", "Sermon"), ("slides", "Slides"),
    ("_resources", "Source texts"), ("_assets", "Media"),
]


def root():
    env = os.environ.get("SERMON_OUTPUT")
    if env:
        return Path(env).expanduser(), "$SERMON_OUTPUT"
    if LIBRARY.is_dir():
        return LIBRARY / "inbox", "the sermon library's inbox in OneDrive"
    return REPO / "output", "the repo's output folder (no sermon library on this computer)"


def slug(title):
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def place(name):
    """Which subfolder a loose file belongs in; None when it stays where it is."""
    if name.startswith("teachers-guide"):
        return None
    ext = Path(name).suffix.lower()
    if name in STUDY:
        return "study"
    if name in SERMON:
        return "sermon"
    if name in SLIDE_NAMES or ext in SLIDE_EXT:
        return "slides"
    if ext in ASSET_EXT:
        return "_assets"
    return "_resources"


def header_field(folder, labels):
    """A '**Label:** value' line from the outline or the study, if either has one."""
    label = "(?:" + "|".join(labels.split("|")) + ")"
    for rel in ("sermon/sermon-outline.md", "study/bible-study.md", "sermon/research-notes.md",
                "sermon-outline.md", "sermon-manuscript.md", "bible-study.md", "teachers-guide.md"):
        f = folder / rel
        if f.is_file():
            m = re.search(rf"^\*\*{label}[^:*]*:\*\*\s*(.+)$", f.read_text(errors="replace"), re.M)
            if m:
                return m.group(1).strip()
    return ""


def write_readme(folder):
    title = header_field(folder, "Sermon Title|Judul Khotbah")
    if not title:
        # Otherwise the first heading of the main document.
        for rel in ("teachers-guide.md", "sermon/sermon-manuscript.md", "sermon-manuscript.md",
                    "study/bible-study.md", "bible-study.md"):
            f = folder / rel
            m = re.search(r"^# (.+)$", f.read_text(errors="replace"), re.M) if f.is_file() else None
            if m:
                title = m.group(1).strip()
                break
    title = title or folder.name
    lines = [f"# {title}", ""]
    for name, labels in (("Date", "Date|Tanggal"), ("Location", "Location|Tempat"),
                         ("Main verse", "Main Verse|Ayat Inti"), ("Passage", "Passage|Perikop")):
        v = header_field(folder, labels)
        if v:
            lines.append(f"- **{name}:** {v}")
    if len(lines) > 2:
        lines.append("")
    skip = lambda n: n in JUNK or n.startswith("~$") or n == "README.md"
    top = sorted(p.name for p in folder.iterdir() if p.is_file() and not skip(p.name))
    if top:
        lines += ["## Files", ""] + [f"- [{n}]({n.replace(' ', '%20')})" for n in top] + [""]
    names = dict(LABELS)
    subs = [s for s, _ in LABELS] + sorted(p.name for p in folder.iterdir() if p.is_dir() and p.name not in names)
    for sub in subs:
        d = folder / sub
        files = sorted(p.name for p in d.iterdir() if not skip(p.name)) if d.is_dir() else []
        if files:
            shown = files[:12] + ([f"… and {len(files) - 12} more"] if len(files) > 12 else [])
            lines += [f"## {names.get(sub, sub)} (`{sub}/`)", ""]
            lines += [f"- [{n}]({sub}/{n.replace(' ', '%20')})" if not n.startswith("…") else f"- {n}" for n in shown] + [""]
    lines.append(f"_Index written {time.strftime('%Y-%m-%d')} by sermon-out.py tidy._")
    (folder / "README.md").write_text("\n".join(lines) + "\n")


def tidy(folder, index_only=False):
    folder = Path(folder).expanduser()
    if not folder.is_dir():
        sys.exit(f"No such folder: {folder}")
    moved = []
    foreign = [p.name for p in folder.iterdir() if p.is_dir() and p.name not in LAYOUT]
    if foreign and not index_only:
        index_only = True
        print(f"  (nothing moved: {', '.join(sorted(foreign))}/ may be pointed at by files here)")
    for p in sorted(folder.iterdir()):
        if index_only or p.name in JUNK or p.name.startswith("~$") or p.name == "README.md" or p.is_dir():
            continue
        if place(p.name) is None:
            continue
        dest = folder / place(p.name)
        dest.mkdir(exist_ok=True)
        if (dest / p.name).exists():
            sys.exit(f"{dest / p.name} already exists; not overwriting it with {p}. Resolve by hand.")
        shutil.move(str(p), str(dest / p.name))
        moved.append(f"{p.name} -> {dest.name}/")
    write_readme(folder)
    print(folder)
    for m in moved:
        print("  " + m)
    print("  README.md rewritten")


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__)
        raise SystemExit(0 if a else 64)
    if a[0] == "root":
        r, why = root()
        print(r)
        print(f"({why})", file=sys.stderr)
    elif a[0] == "layout":
        print(__doc__.split("Layout of one title folder\n")[1])
    elif a[0] == "dir" and len(a) == 3:
        date, title = a[1], a[2]
        if date != "-" and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            sys.exit(f'The date must be YYYY-MM-DD or "-", not "{date}".')
        if not slug(title):
            sys.exit("The title has no letters or digits to name a folder with.")
        r, why = root()
        folder = r / (slug(title) if date == "-" else f"{date}-{slug(title)}")
        folder.mkdir(parents=True, exist_ok=True)
        print(folder)
        print(f"({why}; put files in study/, sermon/, slides/, _resources/, _assets/)", file=sys.stderr)
    elif a[0] == "tidy" and len(a) in (2, 3):
        tidy(a[1], "--index-only" in a)
    else:
        print(__doc__)
        raise SystemExit(64)


if __name__ == "__main__":
    main()
