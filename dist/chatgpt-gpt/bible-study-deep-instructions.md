---
name: bible-study-deep
description: Produce deep, structured Bible study notes for a passage from a Seventh-day Adventist perspective. Includes passage context, historical and cultural background, Hebrew/Greek word studies (with KJV and Indonesian Terjemahan Baru comparison), multi-commentary insights (Andrews Bible Commentary, SDABC, named Adventist scholars, Matthew Henry, Calvin, and other classic and modern sources), Ellen G. White cross-references, scriptural cross-references, theological themes through an Adventist lens, and application questions. Use whenever the user wants to study a passage in depth, prepare teaching/Sabbath School material, do exegesis, or asks for a "deep dive" / pendalaman Alkitab on a Bible text — even if they don't say "Adventist" explicitly.
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
4. Commentary Insights (Adventist primary → Adventist scholars → Classic non-Adventist → Modern evangelical)
5. Ellen G. White Cross-References
6. Scriptural Cross-References
7. Theological Themes (through the Adventist lens where the text engages distinctives)
8. Application Questions

Output is a single markdown document the user can read, save, or hand to a Sabbath School class.

---

## Step 1: Capture Inputs

Required: the passage (book, chapter, verse range).

Optional: study angle or specific question, audience (personal devotion, Sabbath School, prayer-meeting study, sermon prep), language (English / Indonesian), depth level (overview vs. exhaustive).

If the user gave only a passage, that's enough. Don't interrogate. Confirm only what's ambiguous.

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

**Sources to draw on:** IVP Bible Background Commentary (Keener for NT; Walton/Matthews/Chavalas for OT), SDABC historical introductions, William Barclay's Daily Study Bible (use for cultural background; flag theological positions carefully — see Section 4 cautions).

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

### Section 4: Commentary Insights

This is the upgraded multi-source commentary section. Work through the four tiers below in order. For each source, **paraphrase honestly** — never invent content. If you don't know what a specific commentary says about a specific passage, say so clearly and direct the reader to verify.

**Anti-fabrication rule (non-negotiable):** Never put words inside quotation marks unless you are certain of the exact wording. Paraphrase without quote marks is always better than a fabricated quote with them.

---

#### Tier 1 — Adventist Primary Commentaries

**Andrews Bible Commentary (2020)**
The most current official Adventist commentary. Published by Andrews University Press. Accessible, scholarly, international contributors. This is the first stop for Adventist commentary on any passage.
- Paraphrase what it says about the passage — or honestly flag: *"ABC likely addresses X here — verify in your copy."*
- Note any distinctive Adventist reading it brings to the text.

**Seventh-day Adventist Bible Commentary (SDABC)**
The classic 7-volume verse-by-verse denominational commentary (Nichol, ed., 1953–1980). Most thorough verse-level Adventist treatment of the whole Bible. Still indispensable for detailed exegesis.
- Paraphrase the main interpretive question(s) it addresses and where it lands.
- Surface any distinctive compared to non-Adventist readings (e.g., sanctuary theology in Daniel, soul sleep in Ecclesiastes, year-day principle in prophetic texts).
- If content is unavailable, say so. Do not fabricate.

---

#### Tier 2 — Adventist Scholars by Specialty

Cite by name. Match scholar to passage specialty. Paraphrase their position — never quote from memory without verification.

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

These are historically significant commentaries that preachers worldwide have drawn on for centuries. Use them for devotional depth, illustrative richness, and historical perspective. **Always flag where they disagree with Adventist positions** — particularly on state of the dead, hellfire, Sabbath, and sanctuary.

**Matthew Henry's Commentary on the Whole Bible** (1706–1714)
The most widely cited devotional commentary in the English-speaking Protestant world for 300 years. Warm, pastoral, practical. Strong on application and the spiritual life. Weaknesses: written before modern critical scholarship; occasionally superficial on Hebrew/Greek nuances; Reformed covenant theology shapes some readings.
- Use for: devotional application, connections between passages, memorable turns of phrase that can anchor a sermon illustration.
- Flag: Matthew Henry assumes soul immortality and eternal hellfire. Do not use his commentary on death/resurrection passages without noting the doctrinal divergence.
- Free at: Blue Letter Bible, Bible Hub.

**John Calvin's Commentaries** (1540s–1563)
Rigorous Reformed exegesis, especially strong on the Pauline epistles, Psalms, and the Minor Prophets. Calvin is unusually disciplined about staying in the text. Less allegorizing than medieval commentators.
- Use for: careful grammatical analysis, historical context in the Reformation era, Paul's letters, Psalms.
- Flag: Calvin on Sabbath argues the Sabbath was abrogated in Christ. Do not use his Sabbath sections without noting this explicitly.
- Free at: Calvin's Commentaries online (ccel.org).

**John Wesley's Explanatory Notes on the New Testament** (1755)
Brief, methodical notes oriented toward practical holiness. Useful for quick-reference on NT texts and for understanding the Wesleyan/Arminian reading of grace and free will.
- Use for: NT application, texts on repentance, sanctification, and the Christian life.
- Flag: Wesleyan positions on entire sanctification differ from Adventist soteriology in some respects.
- Free at: Wesley Center Online, Blue Letter Bible.

**Matthew Poole's Commentary** (1669–1676)
More technical than Matthew Henry. Engages Hebrew and Greek more carefully. Useful when you need a second voice on word-level exegesis.
- Use for: OT texts requiring careful Hebrew engagement, cross-reference richness.
- Free at: Blue Letter Bible.

**Charles Spurgeon's Treasury of David** (Psalms only, 1869–1885)
Unmatched for the Psalms. Spurgeon drew on hundreds of earlier commentators and preachers. Each Psalm entry includes exposition, illustrative quotations, and homiletical hints. Rich for sermon preparation.
- Use for: Psalms only. Extraordinary depth of devotional and illustrative material.
- Flag: Spurgeon assumes soul immortality and eternal hellfire (consistent with his Baptist tradition).
- Free at: spurgeon.org, Blue Letter Bible.

---

#### Tier 4 — Modern Evangelical Scholarship

For exegetical depth, original-language precision, and historical-cultural background. Use where they strengthen the exegesis without importing non-Adventist conclusions uncritically.

| Source | Best for | Caution |
|---|---|---|
| **IVP Bible Background Commentary: NT** (Craig Keener) | Cultural/historical background for every NT passage | Widely trusted; no major doctrinal issues for background use |
| **IVP Bible Background Commentary: OT** (Walton, Matthews, Chavalas) | OT cultural and archaeological context | Same — use freely for background |
| **NICOT / NICNT** (Eerdmans) | Deep exegesis, OT and NT | Assumes soul immortality; flag on death/resurrection texts |
| **F.F. Bruce** — *The Book of Acts*, *Paul: Apostle of the Heart Set Free*, *Commentary on Galatians* | Acts, Pauline letters, Galatians | Solid evangelical; conservative |
| **Leon Morris** — *The Gospel According to John* (NICNT), *1 Corinthians* | John, 1 Corinthians | Reliable; no major issues |
| **John Stott** (Bible Speaks Today series) | Balanced pastoral-academic; all levels | Assumes eternal conscious torment; flag on judgment texts |
| **William Barclay's Daily Study Bible** | Greek word backgrounds, Greco-Roman cultural context | **Heavy flag:** Barclay holds universal salvation and rejects bodily resurrection in parts. Use ONLY for cultural/linguistic background. Never quote his theological conclusions as support. |
| **Word Biblical Commentary (WBC)** | Most thorough academic series in English | Technical; engage sanctuary/eschatology sections with Adventist caution |

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

2. **Attempt WebFetch** from egwwritings.org. Quote verbatim from the fetched text with full citation (Book, page). If fetch returns 403 or fails, fall back to Tier 2 (high-confidence verified quotes only) or Tier 3 (paraphrase labeled as such). Never invent.

3. Format for each EGW reference:
   - The quote in blockquote (verbatim, Tier 1/2) OR paraphrase clearly labeled (Tier 3)
   - Citation: *Book Title*, p. ___
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

See `sermon-adventist/references/adventist-themes.md` for the standard distinctives and their anchor passages.

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

---
*EGW quotations verified via egwwritings.org where possible; uncertain content paraphrased without quotation marks. Commentary content paraphrased from named sources — verify direct quotes before relying on them in the pulpit or classroom.*
```

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

- **Never fabricate commentary content.** Matthew Henry, Calvin, SDABC, Doukhan — none of them. If you don't know what they say about a specific verse, say so. "Matthew Henry likely addresses the pastoral dimension here — verify in your copy." is always better than an invented quote.
- **Never fabricate EGW quotes.** Always attempt live fetch. Tier 3 paraphrase if not possible. The vibe test on Daniel 12:4 demonstrated exactly why this matters.
- **Never use Barclay's theological conclusions** (universal salvation, annihilationism-adjacent positions) as support for any Adventist point. His cultural/linguistic background is valuable. His theology is not a model.
- **Never force Adventist distinctives onto a passage that doesn't engage them.** Be honest when a text is general Christian theology.
- **Never produce a wall of text.** Use the section structure. The reader should be able to scan.
- **Never give a study without application questions.** Study without surrender hardens.
- **Never give an "overview" when the user asked for a deep study,** and vice versa.

---

## Why the Multi-Commentary Tier Matters

A single-source study (even SDABC alone) risks missing the passage's full texture. Matthew Henry will find the devotional application that a technical commentary misses. Calvin will press into the Greek where Henry glosses over it. Doukhan will see the Hebrew chiasm that no one else noticed. Keener will give you the Roman social custom that unlocks the passage's shock value for the original audience.

Using all four tiers — Adventist primary, Adventist scholars, classic voices, modern exegesis — produces a study that is doctrinally grounded but not doctrinally isolated. The Adventist preacher should be the most well-read person in the room, because they are preaching to people who will go home and find Matthew Henry on their phone before the sun sets.

The goal is not to impress them with sources. The goal is to give them a text they cannot dismiss.
