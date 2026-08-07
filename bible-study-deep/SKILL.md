---
name: bible-study-deep
description: Produce deep, structured Bible study notes for a passage from a Seventh-day Adventist perspective. Includes passage context, historical and cultural background, Hebrew/Greek word studies (with KJV and Indonesian Terjemahan Baru comparison), Biblical Research Institute (BRI) research, multi-commentary insights (Andrews Bible Commentary, SDABC, named Adventist scholars, and classic and modern sources), Ellen G. White cross-references, scriptural cross-references, theological themes through an Adventist lens, and application questions. Use whenever the user wants to study a passage in depth, do exegesis, prepare their own teaching notes on a text, or asks for a "deep dive" / pendalaman Alkitab on a Bible passage — even if they don't say "Adventist" explicitly. This skill is passage-driven exegesis. For a quarterly Adult Bible Study Guide week, a seven-day lesson, or a teacher's guide in Sabbath School format, use `sabbath-school-lesson` instead.
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

The primary output is `bible-study.md` — the preacher's working document, ledger included. An optional `bible-study.html` render (Step 5) is the *reading* copy: same study, no verification apparatus.

---

## Step 1: Capture Inputs

Required: the passage (book, chapter, verse range).

Optional: study angle or specific question, audience (personal devotion, Sabbath School, prayer-meeting study, sermon prep), language (English / Indonesian), depth level (overview vs. exhaustive).

If the user gave only a passage, that's enough. Don't interrogate. Confirm only what's ambiguous.

When a sermon workflow has already chosen a responsive reading, ask one question before starting: use that passage, or a different one? Offer the responsive reading as the recommended option, wait for the answer, and if they want another passage, ask for it.

Defaults if not specified:
- Language: English (per `PRIMARY_LANGUAGE` from foundation)
- Translation: KJV (English) or Terjemahan Baru (Indonesian)
- Depth: **Standard** (see below)
- Form: research document, not a teaching script (see Class Teaching Mode)

### Depth modes

Pick one and hold to its budget. "As long as it needs to be" produces a 32,000-word study nobody reads.

| Mode | Body words | What changes |
|---|---|---|
| **Overview** | ~1,200 | All 8 sections, but 2 word studies, 3 cross-references, 3 questions, one paragraph per commentary tier. No sub-headings inside sections |
| **Standard** (default) | 3,000–4,000 | The full spec as written below |
| **Exhaustive** | 8,000+ | Only on request, or when the passage genuinely carries it (a doctrinal locus like Daniel 8 or Hebrews 8–9). Add sub-headings, more scholars, an appendix if useful |

Any study over ~2,500 words opens with a short contents block after the header. Above 12,000 words, say so and ask whether to split the study or cut scope: past that length it stops being a study and becomes a book chapter.

### Class Teaching Mode

If the user is going to *teach* this (Sabbath School class, prayer meeting, small group) rather than study it, ask once, then produce the research document **plus** a teaching layer:

- A flow at the top: segments with minute counts adding to the stated slot (typically 45 or 60)
- An opening illustration or hook, written out
- Discussion prompts placed inside the segments, not saved for the end
- Teacher notes: what to skip if time runs short, and which question to protect
- The eight research sections stay underneath as the teacher's own preparation

Do not silently switch to this form. A study document and a lesson plan are different deliverables.

**Not the same as a quarterly lesson.** If the user wants an Adult Bible Study Guide week, a teacher's guide for the current quarterly, or anything in the seven-day Sabbath School format, that is the `sabbath-school-lesson` skill. Hand it over rather than approximating it here.

---

## Step 2: Section-by-Section Workflow

Produce each section in order. Each section has a target length and concrete deliverables. Do not skip sections; if a section yields little for a particular passage (e.g., no OT background for a NT passage), say so briefly and move on.

---

### Section 1: Passage Context

What the passage is and where it sits.

- **Book overview** (2–3 sentences): author, audience, date, purpose
- **Genre** (1 sentence): epistle, narrative, poetry, prophecy, apocalyptic, wisdom
- **Placement** (2–3 sentences): what comes before and after; how this passage fits the book's argument or story
- **Literary shape** (2–4 sentences): how the passage is *built*. Chiasm, inclusio, parallelism, repeated refrain, a hinge verse, an argument that turns on a single conjunction. Name the structure and say what it does to the meaning. Hebrew narrative and poetry are shaped deliberately, and Adventist scholarship (Doukhan above all) reads that shape as carrying weight. If the passage has no notable structure, say so in a clause and move on rather than inventing a chiasm
- **The passage itself** — quote it in full from the chosen translation in a blockquote, with attribution
- **Textual integrity** — flag a significant variant when there is one. The KJV follows the Textus Receptus, so passages like Mark 16:9–20, John 7:53–8:11, 1 John 5:7, Acts 8:37 and Matthew 6:13b read differently in the critical text. Say plainly which witnesses support what, and never build a doctrinal point on a disputed reading without noting the dispute. Most passages need nothing here; say nothing rather than manufacture a controversy

Length: ~200–300 words plus the quoted passage.

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
| Indonesian word | As it appears in Terjemahan Baru. Note which TB: the 1974 TB and the 2023 revision (TB2) differ in wording often enough to matter in a word study |
| Original (Hebrew/Greek) | With transliteration |
| Strong's number | Only if you are certain. Omit the row rather than approximate: a wrong Strong's number sends the reader to the wrong word |
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

Collect every classified citation into the **Verification Ledger** at the end of the document (Step 3). That table is where the tags live.

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

**BRI first:** `scripts/bri-fetch.py get <url>` from the repo root (see Tier 1 for the manual fallback). It clears the 403 that WebFetch and curl both hit.

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
- **The live site 403s every automated request.** Do not record BRI as unreadable. Run the repo tool `scripts/bri-fetch.py get <url>` (path is relative to the repo root, not to this skill), which reads the article through the Wayback Machine and unpacks the Next.js payload. You will usually get the full text, footnotes included.
- **If that script is not present** (the skill installed on its own), do it by hand: `web.archive.org/cdx/search/cdx?url=<page>&filter=statuscode:200&fl=timestamp` for a snapshot, fetch `web.archive.org/web/<timestamp>id_/<page>`, and read the article out of the `__NEXT_DATA__` JSON at `props.pageProps.page.resources.Article.body` — the archived HTML shell holds only the title.
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

**At least one theme must trace the passage to Christ.** Not as a decoration bolted to the end, and not by allegorizing a detail into a type Scripture never authorizes. Show the actual line: what this text reveals about the character, work, or claim of Jesus, or how it sits in the plan of salvation. The foundation's rule is that doctrine is the road and Jesus is the destination; a study that never arrives has not finished. On a text that resists it, say what the honest connection is rather than forcing a stronger one.

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

## Step 3: Assemble the Document

**Output format.** 
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

## 4. Research and Commentary Insights

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

## Step 4: Save the Study

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

## Step 5: Optional HTML Render — `bible-study.html`

When the user wants a readable or shareable version, render a styled page beside the markdown.

**The two files are not the same document.** `bible-study.md` is the workshop: it carries the Verification Ledger, `para_id`s, tier markers, HTTP codes. `bible-study.html` is the reading copy: same study, same citations, same doctrinal flags, **none of the verification apparatus**. The ledger does not go into the HTML at all; a single footer line points back to the markdown for it.

Build it from `references/html-template.html` — copy the template and fill it in, never design a fresh page. It carries the stylesheet, both toggles (theme and monochrome), the contents scroll-spy and the progress bar, so consecutive studies read as one series.

**`references/html-render.md` is the full spec** and you should open it before rendering: the eight placeholders, the markup contract for every element, the design numbers (68ch measure, 18.5px/1.72 body, sentence-case headings, AA contrast on every pair), the sanctuary palette and its section ramp, and a twelve-point checklist to run before handing the file over.

Two rules worth stating here because they are the ones most often broken:

- **Descriptive link text.** The URL belongs in the `href`, never in the visible text — in the markdown too: `[The gift of tongues in 1 Corinthians 14](url)`, not a bare address in running prose.
- **One `<ol>` per list.** Markdown converters emit one list per item, which restarts the count and renders every application question as "1."

---

## Indonesian Output

When `PRIMARY_LANGUAGE` is Indonesian, the entire study is in Indonesian, with:

- **Passage quoted in Terjemahan Baru** (and KJV alongside if interpretively useful). State which edition when it matters: TB (1974) is the default; TB2 (2023) revises wording in places, and a word study built on the older phrasing can mislead a reader holding the new Alkitab
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
- **Never give an "overview" when the user asked for a deep study,** and vice versa. Pick a depth mode and hold its word budget.
- **Never end a study without arriving at Christ.** At least one theme has to trace the line. Doctrine is the road, not the destination.
- **Never quietly hand back a lesson plan instead of a study.** Class Teaching Mode is a declared choice, and a quarterly week belongs to `sabbath-school-lesson`.
- **Never build a point on a disputed text without saying it is disputed.** The KJV follows the Textus Receptus; where that matters, say so.
- **Never invent a chiasm.** Literary structure is reported when the text has it, not manufactured to look scholarly.

---

## Reference Files

- `references/commentary-tiers.md` — Tier 3 and Tier 4 sources in full, lexicon list, the root-fallacy caution, free digital tools
- `references/html-render.md` — the full HTML spec: placeholders, markup contract, design numbers, sanctuary palette, pre-delivery checklist
- `references/html-template.html` — the page skeleton itself. Copy it rather than designing a new page
- `scripts/bri-fetch.py` — **repo root, not this folder.** Reads BRI articles the live site blocks, via the Wayback Machine
- `adventist-themes.md` (ships with `sermon-adventist`) — Adventist distinctives mapped to anchor passages and EGW works
- `commentary-sources.md` (ships with `sermon-adventist`) — the Adventist side: BRI, ABC, SDABC, SDAIBC, Adventist scholars by specialty, periodicals
- `HOWTO_EGW_LaguSion.md` (ships with `sermon-adventist`) — operating the EGW API helper and the Lagu Sion hymn database

---

## Why the Multi-Commentary Tier Matters

A single-source study (even SDABC alone) risks missing the passage's full texture. Matthew Henry will find the devotional application that a technical commentary misses. Calvin will press into the Greek where Henry glosses over it. Doukhan will see the Hebrew chiasm that no one else noticed. Keener will give you the Roman social custom that unlocks the passage's shock value for the original audience.

Using all four tiers — BRI and Adventist primary sources, Adventist scholars, classic voices, and modern exegesis — produces a study that is doctrinally grounded but not doctrinally isolated. The Adventist preacher should be the most well-read person in the room, because they are preaching to people who will go home and find Matthew Henry on their phone before the sun sets.

The goal is not to impress them with sources. The goal is to give them a text they cannot dismiss.
