---
name: bible-study-deep
description: Produce deep, structured Bible study notes for a passage from a Seventh-day Adventist perspective. Includes passage context, historical and cultural background, Hebrew/Greek word studies (with KJV and Indonesian Terjemahan Baru comparison), Biblical Research Institute (BRI) research, multi-commentary insights (Andrews Bible Commentary, SDABC, named Adventist scholars, and classic and modern sources), Ellen G. White cross-references, scriptural cross-references, theological themes through an Adventist lens, and application questions. Use whenever the user wants to study a passage in depth, prepare teaching/Sabbath School material, do exegesis, or asks for a "deep dive" / pendalaman Alkitab on a Bible text — even if they don't say "Adventist" explicitly.
---

# Bible Study Deep

Deep exegetical study notes for an Adventist preacher or teacher. Structured, citation-rich, multi-source, and faithful to both Scripture and the Spirit of Prophecy.

**Requires:** the `adventist-foundation` skill is loaded for translation defaults, EGW citation policy, and voice.

---

## What This Skill Produces

A structured Bible study document in markdown, with these eight sections in order:

1. Passage Context
2. Historical and Cultural Background
3. Key Word Studies (3–5 words, with translation comparison)
4. Research and Commentary Insights (BRI → Adventist commentaries → Adventist scholars → Classic non-Adventist → Modern evangelical)
5. Ellen G. White Cross-References
6. Scriptural Cross-References
7. Theological Themes (through the Adventist lens where the text engages distinctives)
8. Application Questions

Plus a **Verification Ledger** at the end: every source claim with its provenance tag, so the preacher knows at a glance what is safe to read aloud and what still needs checking.

The primary output is `bible-study.md` — the preacher's working document, ledger included. An optional `bible-study.html` render (Step 4) is the *reading* copy: same study, no verification apparatus.

---

## Step 1: Capture Inputs

Required: the passage (book, chapter, verse range).

Optional: study angle or specific question, audience (personal devotion, Sabbath School, prayer-meeting study, sermon prep), language (English / Indonesian), depth level (overview vs. exhaustive).

If the user gave only a passage, that's enough. Don't interrogate. Confirm only what's ambiguous.

When this skill is invoked from a sermon workflow that already selected a responsive reading, prompt the user with a single clarifying question before proceeding: whether to study a single passage of their choosing or to use the responsive-reading passage. Use the ask_user pattern: ask one question with explicit choices, for example:

- "Use the responsive-reading passage Hebrews 8:1-6 for this study?" Choices: ["Use Hebrews 8:1-6 (Recommended)", "I'll provide a different passage"]

Only proceed after the user answers. If they choose "I'll provide a different passage", request the passage (book, chapter, verse range) and continue. This keeps the interaction single-question-at-a-time and avoids surprising the user with multiple prompts.

Defaults if not specified:
- Language: English (per `PRIMARY_LANGUAGE` from foundation)
- Translation: KJV (English) or Terjemahan Baru (Indonesian)
- Depth: full study (all 8 sections); offer "overview" mode if they want shorter

---

## Step 2: Section-by-Section Workflow

Produce each section in order. Each section has a target length and concrete deliverables. Do not skip sections; if a section yields little for a particular passage (e.g., no OT background for a NT passage), say so briefly and move on.

---

### Section 1: Passage Context

What the passage is and where it sits.

- **Book overview** (2–3 sentences): author, audience, date, purpose
- **Genre** (1 sentence): epistle, narrative, poetry, prophecy, apocalyptic, wisdom
- **Placement** (2–3 sentences): what comes before and after; how this passage fits the book's argument or story
- **The passage itself** — quote it in full from the chosen translation in a blockquote, with attribution

Length: ~150–250 words plus the quoted passage.

---

### Section 2: Historical and Cultural Background

The world the passage was written in. Not a general history lesson — specifics that change how the passage reads.

- Political and social setting
- Religious and cultural context (what assumptions did the original audience carry?)
- 2–3 specific details a modern reader would miss but that the original audience would have caught immediately

Length: ~200–350 words. Dense and specific.

**Sources to draw on:** BRI articles when they address the passage or its interpretive setting, IVP Bible Background Commentary (Keener for NT; Walton/Matthews/Chavalas for OT), SDABC historical introductions, and William Barclay's Daily Study Bible (use for cultural background; flag theological positions carefully — see Section 4 cautions).

---

### Section 3: Key Word Studies

Pick 3–5 words from the passage that carry interpretive weight. For each:

| Field | What |
|---|---|
| English word | As it appears in KJV |
| Indonesian word | As it appears in Terjemahan Baru |
| Original (Hebrew/Greek) | With transliteration |
| Strong's number | If known |
| Literal / root meaning | The basic sense |
| Range of meaning | How the word is used elsewhere in Scripture (cite 1–3 other occurrences) |
| Translation comparison | KJV vs. TB vs. one or two others (NKJV, NIV, NASB, ESV) where the difference is interpretive |
| Why this word matters here | One sentence on the interpretive payoff |

Format as a sub-heading per word with the table. The point is not to make the user look smart — it's to surface interpretive choices the translation has already made for them.

Free tools for word studies (use live where possible): Blue Letter Bible (blueletterbible.org), Bible Hub (biblehub.com), STEP Bible (stepbible.org).

---

### Section 4: Research and Commentary Insights

This is the upgraded multi-source commentary section. Work through the four tiers below in order. For each source, **paraphrase honestly** — never invent content. If you don't know what a specific commentary says about a specific passage, say so clearly and direct the reader to verify.

**Anti-fabrication rule (non-negotiable):** Never put words inside quotation marks unless you are certain of the exact wording. Paraphrase without quote marks is always better than a fabricated quote with them.

---

#### Source Provenance — Internal Discipline, Ledger-Only Output

Classify every source claim as you research. The classification governs what you are allowed to write.

**The tags never appear in the body of the study.** They are working categories, not printed labels. They surface in exactly one place: the tag column of the Verification Ledger at the end. A study handed to a Sabbath School class must read as pastoral prose, not as a build log with inline `[located-unread]` chips scattered through it.

| Tag | Meaning | What you may write |
|---|---|---|
| `[fetched-verbatim]` | You retrieved the actual text this session | Quote inside quotation marks, with page/refcode and the `para_id` for re-fetching |
| `[located-unread]` | Search found the page or paragraph, but the body was inaccessible (403, paywall, no access) | Report *where* it is and that you have not read it. No paraphrase of its content. |
| `[known-position]` | You are summarizing a source's well-established published position, not a specific sentence | Paraphrase without quote marks, name the work, tell the reader to verify |
| `[inference]` | Your own exegetical reasoning, or a pointer to the right scholar for a question | Say so plainly. Never let it read as a source's claim. |

One rule governs all four: **do not paraphrase what you have not read.** Naming the right scholar for a question is an inference. Claiming what that scholar concluded is a position claim, and only if you genuinely know it. When in doubt, drop a tier.

Collect every classified citation into the **Verification Ledger** at the end of the document (see Output Format). That table is where the tags live.

#### How to say it in the body

Unavailability gets **one short sentence in the preacher's own register**, then move on. Never narrate your own research session — the document belongs to the preacher, not to you, and a reader in a Sabbath School class has no idea what "this session" refers to.

| Don't write | Write instead |
|---|---|
| "BRI holds directly relevant material, but **I could not read it this session.**" | "Four BRI articles bear directly on this passage. Read them in a browser before teaching chapter 14:" (then the list) |
| "`[located-unread]` — I have not read these and will not paraphrase their arguments." | "Not summarized here — open them yourself; see the ledger." |
| "I have not read these pages and will not guess what they argue." | "Check ABC-NT pp. 1614, 1644 in your copy." |
| "I did not fetch Fee, NICNT, Keener, or Barclay this session, so nothing here is a paraphrase of them." | "Fee (NICNT) is the standard technical commentary on these chapters; nothing is claimed about its contents here." |
| "`[fetched-verbatim]` for the SDABC point; `[known-position]` for the imperial-cult background." | *(nothing — this belongs in the ledger)* |

Banned in the body: `[fetched-verbatim]`, `[located-unread]`, `[known-position]`, `[inference]` as printed labels; the words "this session"; and any first-person account of what you did or did not retrieve. Where a caution genuinely helps the teacher, phrase it as instruction to them ("verify before asserting this from the pulpit"), not as a confession about you.

The honesty is not reduced by any of this — it moves to the ledger, where it is scannable in one place instead of interrupting the study eight times.

---

#### Fetching Source Text — Do This Before Writing Tier 1

**BRI first:** `scripts/bri-fetch.py get <url>` (see Tier 1). It clears the 403 that WebFetch and curl both hit.

The EGW Writings API serves more than Ellen White. **Andrews Bible Commentary, SDABC, Matthew Henry, and Vine's Expository Dictionary are all indexed there**, so the same helper the foundation uses for EGW is the first stop for commentary text:

```bash
egw-fetch.sh search "scarlet cord Rahab window"
# → refcode + para_id, e.g. 2SDABC p. 184.7 (para_id 12511.1441), ABC-OT p. 368.6

egw-fetch.sh para 12511.1441 4
# → verbatim paragraphs with refcodes
```

**Search hits are visible even for works this account has not purchased; the paragraph body then returns HTTP 403.** That is a useful result, not a failure — you now know exactly which page answers the question. Handle it in two places:

- **In the body**, one line in the preacher's register: "SDABC treats the scarlet cord at 2SDABC p. 184 — check your volume."
- **In the ledger**, the full detail: `2SDABC p. 184.7 | located-unread | para_id 12511.1441, 403 not purchased | Check your copy before citing`.

**Second path for SDABC:** `sdabc-fetch.sh` (Bash script, `~/.config/scripts/`) scrapes bibletools.info. First-paragraph extraction only — adequate for study context, not for extended treatment. See `sdabc-guide.md`.

If both paths fail for a source, it is located-unread or absent. It is never a position claim by default.

---

#### Tier 1 — Adventist Institutional Research and Primary Commentaries

**Biblical Research Institute (BRI)**
Treat [adventistbiblicalresearch.org](https://adventistbiblicalresearch.org/) as a first-tier source, especially when the text raises an Adventist doctrinal, prophetic, hermeneutical, or disputed interpretive question.
- **The live site 403s every automated request.** Do not record BRI as unreadable — use `scripts/bri-fetch.py get <url>`, which reads the article via the Wayback Machine and unpacks the Next.js payload. You will usually get the full text, footnotes included.
- Search for the passage reference, book name, and theological theme (`bri-fetch.py search "<keyword>"` lists archived URLs).
- Prefer the original BRI article, document, or committee report over summaries on other sites.
- Cite the snapshot date in the ledger alongside the URL. Some pages archive only as empty client-rendered shells; those genuinely are located-unread.
- Record the author, article title, publication date, and direct URL.
- Paraphrase the relevant argument and explain how it affects the interpretation of the passage.
- Distinguish official statements from signed staff articles or study papers. Do not present every BRI article as a voted position of the world church.
- If no relevant BRI material is found, state that briefly rather than forcing a citation.

**Andrews Bible Commentary (2020)**
The most current official Adventist commentary. Published by Andrews University Press. Accessible, scholarly, international contributors. This is the first stop for Adventist commentary on any passage.
- Search the API first (`egw-fetch.sh search`, refcode prefix `ABC-OT` / `ABC-NT`). If the body fetches, quote it verbatim with the page.
- If search locates the page but the body 403s: one line in the body naming the page to check, full detail in the ledger. Do not guess the content of a paragraph you could not open.
- Note any distinctive Adventist reading it brings to the text.

**Seventh-day Adventist Bible Commentary (SDABC)**
The classic 7-volume verse-by-verse denominational commentary (Nichol, ed., 1953–1980). Most thorough verse-level Adventist treatment of the whole Bible. Still indispensable for detailed exegesis.
- Try the API (refcodes `1SDABC`–`7SDABC`), then `sdabc-fetch.sh` for the bibletools.info text.
- When you have the text: paraphrase the main interpretive question(s) it addresses and where it lands.
- Surface any distinctive compared to non-Adventist readings (e.g., sanctuary theology in Daniel, soul sleep in Ecclesiastes, year-day principle in prophetic texts).
- If content is unavailable, say so and name the volume and page to check. Do not fabricate.

---

#### Tier 2 — Adventist Scholars by Specialty

Cite by name. Match scholar to passage specialty. Paraphrase their position — never quote from memory without verification.

**Keep two different moves distinct.** Saying *"Davidson is the right voice for the typology question, and his method insists a valid type is one Scripture itself authorizes"* is a pointer plus a known methodological commitment. Saying *"Davidson argues the scarlet cord prefigures the blood of Christ"* is a claim about a specific published statement. The first is an inference or a known methodological position; the second requires that you actually know it. When a section is only pointers, close it with a line that says so:

> These are pointers to the right scholars and their known methodological commitments, not paraphrases of specific published statements about this passage. Consult the works before citing.

| Specialty | First-choice scholar(s) |
|---|---|
| Daniel / Revelation / Apocalyptic | Jacques Doukhan, Hans LaRondelle, Ranko Stefanovic, Jon Paulien, C. Mervyn Maxwell |
| Sanctuary / Atonement / Investigative Judgment | Richard Davidson, Roy Adams, Clifford Goldstein, Ángel Rodríguez |
| Sabbath | Sigve Tonstad, Samuele Bacchiocchi, Skip MacCarty |
| Salvation / Righteousness by Faith | Edward Heppenstall, Hans LaRondelle, George Knight, Woodrow Whidden |
| OT Narrative / Pentateuch | Richard Davidson, Gerhard Hasel |
| Hermeneutics / Systematic Theology | Gerhard Hasel, Fernando Canale, Norman Gulley, Raoul Dederen (ed., *Handbook of SDA Theology*) |
| Health / Education / Family | George Knight (*Philosophy and Education*) |

---

#### Tier 3 — Classic Non-Adventist Commentaries

Historically significant voices preachers worldwide have drawn on for centuries. Use them for devotional depth, illustrative richness, and historical perspective. **Always flag where they disagree with Adventist positions** — particularly on state of the dead, hellfire, Sabbath, and sanctuary.

| Source | Use for | Doctrinal flag |
|---|---|---|
| **Matthew Henry** (1706–1714) | Devotional application, cross-passage connections, memorable phrasing that can anchor an illustration | Assumes soul immortality and eternal hellfire. Never use on death/resurrection texts unflagged. |
| **John Calvin** (1540s–1563) | Grammatical rigor; Pauline epistles, Psalms, Minor Prophets | Argues the Sabbath was abrogated in Christ. Flag explicitly in any Sabbath section. |
| **John Wesley**, *Explanatory Notes* (1755) | Brief NT notes; repentance, sanctification, Christian life | Wesleyan entire sanctification diverges from Adventist soteriology. |
| **Matthew Poole** (1669–1676) | Word-level OT exegesis, Hebrew engagement, cross-reference richness | Pre-critical, but fewer direct conflicts than Henry or Calvin. |
| **Spurgeon**, *Treasury of David* (1869–1885) | Psalms only. Unmatched devotional and illustrative depth. | Assumes soul immortality and eternal hellfire. |

Matthew Henry is indexed in the EGW Writings API, so he is often the one classic voice you can quote verbatim. Editions, access notes, and fuller descriptions: `references/commentary-tiers.md`.

---

#### Tier 4 — Modern Evangelical Scholarship

For exegetical depth, original-language precision, and historical-cultural background. Use where they strengthen the exegesis without importing non-Adventist conclusions uncritically. Full table with per-source cautions: `references/commentary-tiers.md`. Three carry hard rules:

- **IVP Bible Background Commentary** (Keener for NT; Walton/Matthews/Chavalas for OT) — use freely for cultural and archaeological background. No doctrinal issues in background use.
- **William Barclay**, *Daily Study Bible* — **heavy flag.** Greek word backgrounds and Greco-Roman context only. Barclay holds universal salvation and rejects bodily resurrection in parts. Never cite his theological conclusions as support for an Adventist point.
- **NICOT/NICNT, WBC, Stott** — strong exegesis; they assume soul immortality and eternal conscious torment, and do not hold the Adventist sanctuary reading. Flag on death, resurrection, judgment, and sanctuary texts.

When a word study leans on a lexicon, **name it** (BDB, HALOT, BDAG, Thayer's). "The Hebrew means" with nothing behind it is an assertion, not a study. See `references/commentary-tiers.md` for the lexicon list and the root-fallacy caution.

---

#### Section 4 Closing: Bottom Line

After working through the tiers above, write a 2–3 sentence synthesis:
- What is the consensus across sources on the main interpretive question?
- Where is there genuine tension — and what is the Adventist distinctive reading?
- What does a preacher or teacher most need to know from all this?

---

### Section 5: Ellen G. White Cross-References

Follow the **Tier 1/2/3 EGW policy** from `adventist-foundation`. For 3–5 references that genuinely illuminate the passage:

1. **Identify likely sources** by passage type:
   - Gospel narratives → *Desire of Ages*
   - OT narratives → *Patriarchs and Prophets* or *Prophets and Kings*
   - End-time texts → *The Great Controversy*
   - Salvation/sanctification → *Steps to Christ*, *The Acts of the Apostles*, *Selected Messages*
   - Education/character → *Education*, *Testimonies for the Church*
   - Health → *Ministry of Healing*, *Counsels on Diet and Foods*

2. **Fetch via the official API.** The public egwwritings.org site 403s automated requests — do not use WebFetch on it. Use the helper:

   ```bash
   egw-fetch.sh search "reverence for the house of God"   # → para_id + refcode (page)
   egw-fetch.sh para 113.2411 12                          # → verbatim paragraphs
   ```

   Search a distinctive phrase, not a topic. Then fetch the paragraph and quote verbatim with the exact refcode. If the helper fails on credentials, follow the Keychain troubleshooting in `adventist-foundation` before giving up. Only after the fetch path is genuinely exhausted may you fall back to Tier 2 (high-confidence verified wording) or Tier 3 (paraphrase, labeled). Never invent.

3. Format for each EGW reference:
   - The quote in blockquote (verbatim, Tier 1/2) OR paraphrase clearly labeled (Tier 3)
   - Citation: *Book Title*, p. ___ — plus the `para_id` so the preacher can re-fetch and confirm
   - The tier, stated: **Tier 1, verbatim** / **Tier 3, paraphrase**
   - One sentence on how it illuminates the passage

**Reminder from the Daniel 12:4 vibe test:** If you cannot verify exact wording, do not put text in quotation marks. A false EGW quote is worse than no EGW quote. Paraphrase is always the safe fallback.

---

### Section 6: Scriptural Cross-References

5–8 related passages, each with:

- **Reference** — book, chapter, verse
- **Quote or summary** — short
- **Connection type** — one of:
  - *Direct parallel* — same event or teaching
  - *Thematic connection* — develops the same idea
  - *OT background* — for NT passages, the OT text being quoted, alluded to, or assumed
  - *NT fulfillment* — for OT passages, the NT outcome
  - *Contrast* — illuminating the passage by what differs

Format as a table (Reference | Connection Type | Quote/Note) — easier to scan than a list.

---

### Section 7: Theological Themes

3–5 major themes in the passage, each with:

- **Theme name** — short, clear label
- **In the text** — where and how the passage develops it
- **Adventist lens** (when applicable) — how this theme connects to a distinctive Adventist doctrine. Don't force it; if the passage doesn't engage a distinctive, say: *"general Christian theology — no specific Adventist distinctive engaged here."*
- **Pastoral implication** — one sentence on what this means for a real Adventist church member today

For the standard distinctives and their anchor passages, see the `adventist-themes.md` reference shipped with the `sermon-adventist` skill (in a dist package it sits in the `knowledge/` folder).

---

### Section 8: Application Questions

5–8 questions designed to push the reader from study to surrender. A good study question:

- Cannot be answered "yes" or "no" alone
- Names a real area of life (not abstract)
- Connects the text to a specific decision, posture, or relationship
- Avoids "What did you learn?" — too soft and too safe

Mix of question types:
- One observational ("What does the text actually *say* about ___?")
- Two interpretive ("Why does the author move from X to Y, rather than to Z?")
- Three or four applicational, increasing in cost and specificity

---

## Output Format

Single markdown document. Header structure:

```markdown
# Bible Study: [Passage Reference]

*Prepared for: [audience if given]*
*Translation: KJV (English) / Terjemahan Baru (Indonesian)*

## 1. Passage Context
...

## 2. Historical and Cultural Background
...

## 3. Key Word Studies

### 3.1. [Word]
[table]

## 4. Commentary Insights

### Biblical Research Institute
...

### Andrews Bible Commentary (2020)
...

### Seventh-day Adventist Bible Commentary (SDABC)
...

### Adventist Scholars
...

### Classic Commentary Voices
...

### Modern Evangelical Scholarship
...

### Bottom Line
...

## 5. Ellen G. White Cross-References
...

## 6. Scriptural Cross-References
[table]

## 7. Theological Themes
...

## 8. Application Questions
...

## Verification Ledger
[table — every tagged citation from Sections 2, 4, and 5]

---
*EGW and commentary text fetched via the official EGW Writings API where accessible; anything not read is marked located-unread with its page and para_id. Uncertain content is paraphrased without quotation marks. Verify direct quotes before relying on them in the pulpit or classroom.*
```

### Verification Ledger

Close the markdown with this table. It is the document's audit trail, and **the only place provenance tags appear** (and it does not go into the HTML render at all) — the preacher scans one table instead of re-reading eight sections to find out what is safe to say out loud.

| Source | Tag | Where | Action for the user |
|---|---|---|---|
| *My Life Today*, p. 277.4 | `fetched-verbatim` | para_id 12345.678 | Safe to read aloud as quoted |
| 2SDABC p. 184.7 | `located-unread` | para_id 12511.1441, 403 not purchased | Check your copy before citing |
| Richard Davidson on typology | `known-position` | *A Song for the Sanctuary* | Verify before attributing a specific claim |
| Chiastic reading of vv. 3–7 | `inference` | This study's own analysis | Your call whether it preaches |

Hymn numbers, if the study recommends any, go in the ledger too — never invent them (use the Lagu Sion database; see `sermon-adventist/HOWTO_EGW_LaguSion.md`).

---

## Step 3: Save the Study

Once the study is delivered and the user is satisfied with it, write it to the repo output tree so it sits alongside the sermon material.

**Path structure:**
```
/Users/edmundsitumorang/DEV/skills-sermon-adventist/output/
└── [YYYY-MM-DD]-[kebab-case-title]/
    └── bible-study.md
```

**Workflow:**
1. **If the study supports a sermon that already has a folder, write `bible-study.md` into that existing folder.** Do not create a second folder for the same message.
2. Otherwise create a new folder: teaching/delivery date in ISO `YYYY-MM-DD` form, then the study title in kebab-case (lowercase, hyphens for spaces; keep words like "God" and "Christ").
   - "The Sanctuary and the Plan of Salvation" on 2026-08-01 → `2026-08-01-the-sanctuary-and-the-plan-of-salvation`
3. If no date was given, use the title alone and tell the user no date was recorded.
4. Confirm the path back to the user.

The filename is always `bible-study.md` — that is what the sermon workflow and the rest of the output tree expect.

---

## Step 4: Optional HTML Render — `bible-study.html`

When the user wants a readable or shareable version, render a styled `bible-study.html` beside the markdown. **The two files have different audiences and are not the same document.**

| | `bible-study.md` | `bible-study.html` |
|---|---|---|
| Read by | The preacher, preparing and verifying | The preacher reading, or the class |
| Verification Ledger | Yes — full table | **No. Removed entirely.** |
| `para_id`, HTTP codes, API and site names | Yes | **Never.** These are workshop tools, not content |
| Tier markers after quotes | Yes | No — the page citation alone |
| Page citations (*Desire of Ages* p. 25, 6SDABC on 12:11) | Yes | Yes. Real citations stay in both |
| Doctrinal flags (Henry on soul immortality, Barclay) | Yes | Yes. Teaching content, not provenance |
| Short teacher notes ("read this before teaching ch. 14") | Yes | Yes |
| Provenance statement | The ledger | One closing line, pointing to the markdown |

The HTML footer carries the whole provenance story in one sentence:

> Scripture quoted from the KJV and Terjemahan Baru. Ellen G. White, SDABC, and Matthew Henry quotations are verbatim from the sources cited. The full source ledger, including what could not be accessed, is in `bible-study.md`.

**Links.** Every link gets descriptive anchor text. The URL lives in the `href` and never in the visible text.

- Wrong: `"The Gift of Tongues in 1 Corinthians 14" — adventistbiblicalresearch.org/materials/the-gift-of-tongues-in-1-corinthians-14/`
- Right: `<a href="https://adventistbiblicalresearch.org/materials/the-gift-of-tongues-in-1-corinthians-14/">The Gift of Tongues in 1 Corinthians 14</a>`

Same rule in the markdown: `[The Gift of Tongues in 1 Corinthians 14](url)`, not a bare URL in running text.

### Building the page

**Start from `references/html-template.html`.** Copy it and fill in the content — do not design a new page each time. The template carries the whole stylesheet and the theme-toggle script, so consecutive studies look like one series instead of eight different documents.

Fill the four header placeholders (`{{LANG}}`, `{{PASSAGE}}`, `{{TITLE}}`, `{{AUDIENCE}}`, `{{TRANSLATION}}`), then convert the markdown section by section using the markup contract below.

### Markup contract

| Study element | Markup |
|---|---|
| Numbered section (1–8) | `<section class="sec" data-hue="4">` wrapping `<h2 id="..."><span class="num">4</span> Research and Commentary Insights</h2>`. The `data-hue` is the section number — it drives every color inside |
| Sub-heading (a word study, an EGW reference, a theme) | `<h3 id="...">` with a matching id |
| Scripture quotation | `<blockquote class="scripture">` + `<p class="note">` carrying reference and translation |
| Ellen G. White quotation | `<blockquote class="egw">` + `<p class="note">` carrying *Book Title*, p. 000 |
| Other commentary quotation | `<blockquote class="cited">` + `<p class="note">` naming the source |
| Word study (label/value pairs) | `<div class="tablewrap"><table class="spec">` — first column is the label |
| Data table (cross-references, argument structure) | `<div class="tablewrap"><table class="grid">` — has a `<thead>` |
| Any table at all | **Always** wrapped in `<div class="tablewrap">` so it scrolls on a phone instead of breaking the page |
| Numbered list (application questions, argument steps) | **One** `<ol>` holding every `<li>`. Markdown converters routinely emit one `<ol>` per item, which restarts the count so every question renders as "1." — merge adjacent single-item lists and check the numbering runs 1…n |
| Section divider | `<hr class="rule">` |
| Aside, citation line, teacher note | `<p class="note">` |
| Contents nav | `<nav class="toc">`: sections as `<li data-hue="N">`, sub-headings as `<li class="l3" data-hue="N">` carrying their parent's hue. Include for studies over ~2,500 words |

Greek and Hebrew go in as real Unicode (χαρίσματα, תִּקְוָה) with the transliteration in `<em>`.

### Design spec — do not improvise on these

A study runs 3,000–10,000 words. Every value below is set for sustained reading, not for looking designed. The template already encodes them; if you hand-build a page, hit these numbers.

| Decision | Value | Why |
|---|---|---|
| **Measure** | `68ch` (~66 characters) | 50–75 CPL is the readability optimum and WCAG 1.4.8 caps at 80. A full-width 900px column runs ~97 CPL and reads as a wall — this is the single biggest thing that makes a study page feel heavy |
| **Body type** | 18.5px / 1.72 sans; Scripture quotes set 20px serif | 18–20px is the long-form sweet spot; 1.5 is the line-height minimum, more when lines are long. The serif is reserved for Scripture so the text being studied reads differently from the notes about it |
| **Headings** | Sentence case, sans, 26px (h2) / 18.5px (h3); `h1` is gradient display type | Never all-caps: caps cost 10–20% reading speed and flatten word shape, and headings are exactly what a browsing reader navigates by |
| **Section separation** | Colored rule + number badge above each `h2` | The eight sections are the map of the document; they should be visible from a scroll position, not just readable |
| **Contrast** | Every text/background pair ≥ 4.5:1, hues included | WCAG AA for body text. Compute it, don't eyeball it — the template's 8 hues were checked on paper and on their own tint, light and dark |
| **Dark mode** | The default. Linen on onyx `#070b14`, rim-lit glass over the aurora | Never `#fff` on `#000`. The ramp is bright enough to glow and still lands 5.8–9.5:1 on every glass surface |
| **Depth** | Translucent cards (`--card`) with hairline edges over the aurora; `backdrop-filter` only on the fixed controls and the sticky sidebar | Blur is expensive. Two blurred surfaces read as glass; thirty of them stutter on scroll |
| **Motion** | Progress bar, section reveal on entry, animated nav dot — all killed by `prefers-reduced-motion` | Motion is garnish. It must never be load-bearing, and it must be switchable off |
| **Browsing** | Sticky glass contents sidebar ≥1120px, plain list below; gradient reading-progress bar at the top | The nav is how a 6,000-word study becomes browsable. Sub-headings hide on narrow screens |

### The color system — the sanctuary palette

**The palette is fixed and it means something.** Exodus 26:31 specifies the veil of the sanctuary: "blue, and purple, and scarlet, and fine twined linen." Exodus 25 adds the gold. Those five are the entire palette of this page. Nothing else gets in — no free-choice hues, no rainbow.

| Name | Role | Dark | Light |
|---|---|---|---|
| **techelet** — blue | Structure: headings, links, contents, Scripture | `#71cdf4` | `#1d6e90` |
| **argaman** — purple | The far end of the section ramp | `#bc7af5` | `#601f98` |
| **zahav** — gold | Ellen G. White / Spirit of Prophecy, always and everywhere | `#e8b44a` | `#8a6410` |
| **shani** — scarlet | Cautions and doctrinal flags **only** — it is rare so that it lands | `#f2707a` | `#b02832` |
| **shesh** — linen | The text itself | `#eef1f7` | `#141922` |
| **onyx** | The surface everything floats on | `#070b14` | `#f5f6f9` |

**Section wayfinding is a ramp, not a spectrum.** Eight steps walk techelet (198°) to argaman (272°) as `--s1`…`--s8`. One analogous family, so section 3 and section 6 are still distinguishable while the page reads as a single palette. Wrap each section as `<section class="sec" data-hue="4">` and its step flows to the badge, heading, gradient rule, left spine, table heads and list markers, and to its entries in the contents rail.

All sixteen steps were checked on glass: **5.8–9.5:1 dark, 5.6–10.6:1 light**. The mid-ramp indigos need a lightness lift to clear AA — that is already baked into the values above; don't interpolate a fresh ramp by eye.

**Content types hold a fixed color anywhere in the document:**

| Content | Class | Color |
|---|---|---|
| Scripture | `blockquote.scripture` | Techelet, serif, soft glow |
| Ellen G. White | `blockquote.egw` | Gold |
| Other commentary (SDABC, Henry, scholars) | `blockquote.cited` | Neutral |
| Doctrinal flag / caution | `div.flag` | Scarlet — the only scarlet on the page |

Each card labels itself: the chip on its top edge ("Scripture", "Spirit of Prophecy", "Commentary", "Caution") comes from CSS `::before`, so the markdown conversion never has to add it.

**Body prose always stays linen.** Color marks structure and source; it never tints running text.

**The aurora** is three blurred radial sources only — techelet top-left, argaman top-right, one ember of gold low centre — over a masked 60px techelet grid. Fixed at `z-index:-2`. Atmosphere, not motion.

**Monochrome button.** Sets `data-mono="on"`, which re-points the eight ramp steps plus `--techelet`, `--argaman`, `--zahav`, `--shani`, `--scripture`, `--sop`, `--link`, and zeroes `--aurora` and `--glow`. Every tint, glow, gradient and aurora source derives from those variables through `color-mix()`, so one override desaturates the whole page and the gradient `h1` reverts to flat ink. Keep it that way: no hard-coded hex outside the theme blocks.

### Rules

- **Self-contained.** Inline CSS, no external fonts, no CDN, no scripts beyond the two toggles and the contents scroll-spy already in the template. The file must render correctly opened straight off disk with no network.
- **Light and dark both readable.** The template handles this with `prefers-color-scheme` plus a `data-theme` override the toggle sets. Don't hard-code colors — use the CSS variables.
- **Printable.** The template's `@media print` rules flatten the page and avoid breaking blockquotes and table rows. Keep them.
- **No verification apparatus.** Per the table above: no ledger, no `para_id`, no HTTP codes, no tier markers, no bare URLs as link text.
- **Every `href` has a matching `id`.** A contents nav with a dead link is worse than no nav.
- **Never regenerate the HTML from an older markdown.** If you edit the study, edit both files or re-render.

### Before you hand it over

1. Measure is capped (`68ch`) — no full-bleed text column.
2. Every table wrapped in `.tablewrap`.
3. Every nav link resolves to an id on the page.
4. No `para_id`, no `located-unread`, no "HTTP 403", no "this session" anywhere in the file.
5. Links show titles, not URLs.
6. Footer names the translation and points to `bible-study.md`.
7. No all-caps headings anywhere.
8. Mono toggle leaves no color behind — no hex values outside the theme blocks.
9. Reduced-motion honored: reveals and transitions disabled, content still visible.
10. Ordered lists count correctly — no run of single-item `<ol>` blocks all showing "1."
11. Tags balance and the file ends with `</html>`.

---

## Indonesian Output

When `PRIMARY_LANGUAGE` is Indonesian, the entire study is in Indonesian, with:

- **Passage quoted in Terjemahan Baru** (and KJV alongside if interpretively useful)
- **Word studies** show TB and KJV side by side, plus original language
- **Commentary content** (SDABC, EGW, Matthew Henry, etc.) paraphrased into Indonesian; cite the English source title. Direct quotes remain in English with a parenthetical Indonesian translation if useful.
- Section headers and prose in Indonesian
- Application questions phrased for the Indonesian Adventist reader
- EGW sources cited in their English titles (e.g., *The Great Controversy*, *Patriarchs and Prophets*) since those are the canonical reference forms

---

## Anti-Patterns

- **Never paraphrase what you have not read.** This is the master rule. A located-but-unopened paragraph gets reported as located-unread with its page and para_id. It does not get summarized from what the source "probably" says.
- **Never fabricate BRI or commentary content.** BRI, Matthew Henry, Calvin, SDABC, Doukhan — none of them. If you cannot access a source, say so rather than guessing what it likely argues.
- **Never fabricate EGW quotes.** Always attempt the API fetch (`egw-fetch.sh`), never WebFetch on the public site. Tier 3 paraphrase if the fetch path is exhausted. The vibe test on Daniel 12:4 demonstrated exactly why this matters.
- **Never let a scholar's name do work their argument hasn't done.** Pointing to the right specialist is not the same as reporting their conclusion. Label which one you are doing.
- **Never omit the Verification Ledger.** Untagged citations are how a study becomes a liability three weeks later in the pulpit.
- **Never put verification apparatus in the HTML render.** No ledger, no `para_id`, no HTTP codes, no bare URLs as link text. The markdown is the workshop; the HTML is the reading copy.
- **Never print provenance tags in the body, and never narrate your own research session.** No `[located-unread]` chips between paragraphs, no "I could not read this," no "this session." The study is the preacher's teaching document, not a report on how it was assembled. All of that goes in the ledger.
- **Never use Barclay's theological conclusions** (universal salvation, annihilationism-adjacent positions) as support for any Adventist point. His cultural/linguistic background is valuable. His theology is not a model.
- **Never force Adventist distinctives onto a passage that doesn't engage them.** Be honest when a text is general Christian theology.
- **Never produce a wall of text.** Use the section structure. The reader should be able to scan.
- **Never give a study without application questions.** Study without surrender hardens.
- **Never give an "overview" when the user asked for a deep study,** and vice versa.

---

## Reference Files

- `references/commentary-tiers.md` — Tier 3 and Tier 4 sources in full, lexicon list, the root-fallacy caution, free digital tools
- `scripts/bri-fetch.py` — reads BRI articles the live site blocks, via the Wayback Machine
- `references/html-template.html` — the `bible-study.html` skeleton: full stylesheet, theme toggle, markup examples for every element. Copy it rather than designing a new page
- `adventist-themes.md` (ships with `sermon-adventist`) — Adventist distinctives mapped to anchor passages and EGW works
- `commentary-sources.md` (ships with `sermon-adventist`) — the Adventist side: BRI, ABC, SDABC, SDAIBC, Adventist scholars by specialty, periodicals
- `HOWTO_EGW_LaguSion.md` (ships with `sermon-adventist`) — operating the EGW API helper and the Lagu Sion hymn database

---

## Why the Multi-Commentary Tier Matters

A single-source study (even SDABC alone) risks missing the passage's full texture. Matthew Henry will find the devotional application that a technical commentary misses. Calvin will press into the Greek where Henry glosses over it. Doukhan will see the Hebrew chiasm that no one else noticed. Keener will give you the Roman social custom that unlocks the passage's shock value for the original audience.

Using all four tiers — BRI and Adventist primary sources, Adventist scholars, classic voices, and modern exegesis — produces a study that is doctrinally grounded but not doctrinally isolated. The Adventist preacher should be the most well-read person in the room, because they are preaching to people who will go home and find Matthew Henry on their phone before the sun sets.

The goal is not to impress them with sources. The goal is to give them a text they cannot dismiss.
