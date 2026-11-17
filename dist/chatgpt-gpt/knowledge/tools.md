# Tools

Command-line tools the skills call by bare name. They are on PATH after `scripts/install.sh` has been run once in the skills repo (`skills-sermon-adventist`).

**When a name is "command not found":** call it by path, `<skills repo>/scripts/<name>` (the repo is where this skill's folder really lives; `egw-fetch.sh` and `sdabc-fetch.sh` live in `~/.config/scripts/`). When the repo is not on this computer at all, do the same job with web search and fetch, and record in the ledger that the tool was unavailable.

| Tool | Job | Reach for it when |
|---|---|---|
| `bible.py pack "<passage>"` | Text in KJV, BSB and AYT; every Hebrew or Greek word with Strong's number, parsing and gloss; KJV-versus-NA28 differences; brief lexicon; top cross-references | Starting any study, word study or cross-reference list. Add `--brief` to leave out the per-word table |
| `bible.py words` / `strongs` / `xref` / `verse` | One lookup at a time | You need one word, one lexicon entry, or more cross-references (`xref -n 20`) |
| `helloao-fetch.py commentary "<passage>"` | Seven classic commentaries on the span | Before naming a classic commentator |
| `sdabc-fetch.sh <Book> <chapter> <verse>` | Every SDABC paragraph on one verse | Any SDABC claim. Exit 2 is a network failure: retry |
| `egw-fetch.sh search` / `para` | Ellen G. White, verbatim with refcode; `lang=id` searches the Indonesian editions | Any Ellen White quotation |
| `bri-fetch.py search` / `get <url> [--grep term,term]` | Biblical Research Institute articles through the Wayback Machine | Any BRI claim. `--grep` prints only the paragraphs that mention every term |
| `sermon-out.py dir <date> "<title>"` | Creates and prints the folder a sermon or study is saved in | Before writing the first file. `sermon-out.py tidy <folder>` files loose items and writes the index |
| `render-study.py <bible-study.md>` | Writes the reading copy, `bible-study.html` | The study markdown is final |
| `sermon-deck <deck.json>` | Builds the sermon PowerPoint | The slides are final. `sermon-deck --example` prints the format |
| `check-quotes.py <folder>` | Compares every cited KJV or TB quotation with the Bible | The final pass, every time |

`bible.py` reads a local database and falls back to free APIs without it; its first output line says which. Terjemahan Baru text comes from bolls.life (`https://bolls.life/get-text/TB/<book number>/<chapter>/`).

## Where output is saved

`sermon-out.py` is the single source of truth for the location. On the preacher's own computer it is the sermon library's inbox in OneDrive; elsewhere it is the repo's `output/`. One folder per title:

```
[YYYY-MM-DD]-[title-in-kebab-case]/
├── README.md        index, written by `sermon-out.py tidy`
├── study/           bible-study.md, bible-study.html
├── sermon/          research-notes.md, sermon-outline.md, sermon-manuscript.md
├── slides/          slides.md, deck.json, the .pptx
├── _resources/      source texts fetched for the work, one file per source
└── _assets/         images and other media
```

A Sabbath School guide's folder (`[date]-ss-[title]`, from `sermon-out.py dir <date> "ss <Lesson Title>"`) stays flat: `teachers-guide.md`, `teachers-guide.html` and `slides/`, because the publisher names the lesson after the folder that holds the page.

A study and the sermon built on it share one folder. Fetched source text you relied on (an SDABC entry, a BRI article, the verses in Terjemahan Baru) is saved to `_resources/` so the next session reads the file instead of fetching again. Build folders (`node_modules`, a Python venv) stay out of this tree: it syncs to the cloud.
