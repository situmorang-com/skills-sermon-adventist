---
name: sermon-adventist
description: Prepare a complete Seventh-day Adventist sermon — produces THREE documents per sermon: (1) research notes (word studies, commentaries, EGW, cross-references, theological themes, thinking prompts), (2) sermon outline, and (3) full manuscript. Begins with an interactive seven-question brainstorm asked one question at a time. Supports multiple structures (expository, topical, narrative, biographical, textual, three-point), produces output in English (KJV) or Indonesian (Terjemahan Baru), integrates Ellen G. White citations from egwwritings.org, draws from Andrews Bible Commentary, SDA Bible Commentary, and Adventist scholars (Doukhan, LaRondelle, Stefanovic, etc.), and ALWAYS includes strong bookend illustrations (opening icebreaker + closing reinforcement). Use this skill whenever the user wants to write a sermon, prepare a Sabbath message, plan a divine service message, or asks for help preaching a passage — even if they don't say "Adventist" but mention Sabbath service, divine hour, ibadah, khotbah, week of prayer, evangelistic series, or Spirit of Prophecy.
---

# Sermon Adventist

Prepare a complete sermon package: research notes → interactive brainstorm → outline → full manuscript. Three deliverables, one cohesive workflow. Adventist in theology, faithful in citation, ready to preach.

**Requires:** the `adventist-foundation` skill is loaded for doctrinal alignment, voice, banned phrases, and EGW citation policy. Do not duplicate those rules here — apply them.

---

## What This Skill Produces

Four documents per sermon, in this order:

1. **`research-notes.md`** — exegetical and pastoral research the preacher can review, study, and reference. Includes passage context, historical background, key word studies, commentary insights from multiple Adventist sources, EGW cross-references, scriptural cross-references, theological themes, and thinking prompts that pressure-test the sermon.
2. **`sermon-outline.md`** — service header block (title, main verse, responsive reading, opening + closing hymns) followed by a sermon outline appropriate to the chosen structure, with **strong bookend illustrations** at the opening and the closing.
3. **`sermon-manuscript.md`** — the actual words the preacher will say, in the chosen language, with both bookend illustrations woven in, all Scripture and EGW quotes properly cited.
4. **`slides.md`** — a slide-by-slide deck, formatted as copy-paste text for **Gamma AI** (gamma.app). One idea per slide, slides separated by `---`, with Scripture quoted verbatim and `[GAMBAR: …]` visual suggestions. Includes a paste-ready block and a verification notes section.

---

## Workflow Overview

```
Step 1: Capture intent (one short conversational message)
        ↓
Step 2: Generate research-notes.md  ← preacher reviews while you brainstorm
        ↓
Step 3: Interactive brainstorm (7 questions, ONE at a time)  ← THE HEART OF THE SKILL
        ↓
Step 4: Sermon brief (preacher confirms direction)
        ↓
Step 5: Find/draft bookend illustrations (opening + closing)
        ↓
Step 6: Generate sermon-outline.md
        ↓
Step 7: Generate sermon-manuscript.md
        ↓
Step 8: Generate slides.md (Gamma AI deck)
        ↓
Step 9: Final pass (verify citations, AI-slop, hymn numbers, illustration bookends)
        ↓
Step 10: Auto-save to /DEV/skills-sermon-adventist/output/[YYYY-MM-DD]-[kebab-case-title]/
```

---

## Step 1: Capture Intent

Ask the preacher these as a single short message at the start. Skip any item they already provided in their initial prompt.

| Field | What to capture | Notes |
|---|---|---|
| Passage / topic | The text or theme | Required |
| Date of delivery | The Sabbath/date the sermon will be preached (ISO `YYYY-MM-DD`) | Required — used in the folder name and documented in every file |
| Location | Church / venue where it will be delivered (e.g., "Jemaat Bandung Timur", "Loma Linda University Church") | Required — documented in every file |
| Sermon structure | expository, topical, narrative, biographical, textual, three-point | If unclear, recommend based on passage |
| Language | English or Indonesian | Default per `PRIMARY_LANGUAGE` |
| Audience | Sabbath main service, evangelistic, youth/AY, Sabbath School, week of prayer, etc. | Affects tone and depth |
| Length | Minutes (typical: 20–45) | Maps to manuscript word count |
| Occasion | Communion, baptism, anniversary, special week, ordinary Sabbath | Optional |
| Series context | If part of a series | Optional |

Keep this conversational. One message, not a form.

---

## Step 2: Generate `research-notes.md` FIRST

**Before the brainstorm**, produce the research document. This serves two purposes:
1. Gives the preacher something substantive to review while you work through the brainstorm questions
2. Informs your follow-up questions during brainstorm — you'll know what the text actually says before asking the preacher about it

The research notes follow this exact structure (see `references/research-notes-template.md` for the full template):

### 1. Passage Context (~150-250 words)
- Book overview (author, audience, date, purpose)
- Genre
- Placement in book (what comes before/after)
- The passage itself, quoted in full from KJV (English) or Terjemahan Baru (Indonesian), with translation cited

### 2. Historical and Cultural Background (~200-350 words)
Specifics that change how the passage reads. Political setting, religious context, cultural practices, 2-3 details modern readers miss.

### 3. Key Word Studies (3-5 words)

For each word, produce this table:

| Field | Content |
|---|---|
| English (KJV) | as it appears |
| Indonesian (TB) | as it appears |
| Original (Heb/Greek) | with transliteration |
| Strong's # | if known |
| Literal/root meaning | basic sense |
| Range of meaning | how used elsewhere in Scripture (cite 1-3 occurrences) |
| Translation comparison | KJV vs TB vs NKJV/NIV/NASB/ESV where interpretively different |
| Why this matters here | one sentence on the interpretive payoff |

Pick words with interpretive weight — words where translation matters, where theological meaning is loaded, or where the original shifts the reading.

### 4. Commentary Insights (~250-400 words)

Draw from **multiple Adventist sources** in this order, plus carefully-selected non-Adventist scholarship. See `references/commentary-sources.md` for the full list.

**Primary Adventist sources:**
- **Andrews Bible Commentary** (2020, 2 vols) — most current Adventist commentary
- **Seventh-day Adventist Bible Commentary (SDABC)** — classic 7-volume reference
- **Andrews Study Bible** notes
- **SDA International Bible Commentary (SDAIBC)** — newer scholarly Adventist work

**Adventist scholars to reference by passage type:**
- **Daniel/Revelation:** Jacques Doukhan, Hans LaRondelle, Ranko Stefanovic, Jon Paulien, William Shea, C. Mervyn Maxwell ("God Cares")
- **Sanctuary/Judgment:** Roy Adams, Richard Davidson, Clifford Goldstein
- **Sabbath:** Sigve Tonstad, Samuele Bacchiocchi
- **Salvation/Righteousness by Faith:** Edward Heppenstall, Hans LaRondelle, Woodrow Whidden
- **Hermeneutics/General:** Gerhard Hasel, Richard Davidson

**Non-Adventist scholarship to use carefully (verify before quoting):**
- Background: IVP Bible Background Commentary (Keener for NT, Walton for OT)
- Exegetical: NICOT/NICNT, Word Biblical Commentary (when consistent with Adventist hermeneutics)
- Pastoral: NIV Application Commentary

For each commentary insight, present:
- The interpretive question or insight
- What the commentator says (paraphrased — never fabricate quotes)
- Source name (e.g., "Andrews Bible Commentary on Daniel 12")
- Whether it strengthens, complicates, or challenges the typical Adventist reading

**Anti-fabrication rule:** Do not invent commentary content. If you don't know what a specific commentary says about this passage, say so honestly: *"Andrews Bible Commentary likely addresses X here — verify in your physical or digital copy before relying on it."*

### 5. Ellen G. White Cross-References (3-5 references)

Apply the **Tier 1/2/3 policy** from the foundation strictly.

For each EGW reference:
- Quote (verbatim, in blockquote) OR paraphrase (clearly labeled, no quote marks)
- Citation: *Book Title*, p. ___
- One sentence on how it illuminates the passage

Use WebFetch on egwwritings.org to verify when possible. If fetch fails (403, etc.), fall back to high-confidence paraphrase with explicit honesty about uncertainty.

### 6. Scriptural Cross-References (5-8 references)

For each:
- **Reference** — book, chapter, verse
- **Quote or summary** — short, in chosen translation
- **Connection type** — exactly one of:
  - *Direct parallel* — same event/teaching
  - *Thematic connection* — same idea developed
  - *OT background* — for NT passages, the OT being quoted/alluded to
  - *NT fulfillment* — for OT passages, the NT outcome
  - *Contrast* — illuminates by what differs

### 7. Theological Themes (3-5 themes)

For each:
- **Theme name** — short, clear label
- **In the text** — where and how the passage develops it
- **Adventist lens** — connection to a 28 Fundamental Belief WHEN the text genuinely engages it (don't force)
- **Pastoral implication** — one sentence on what this means for a real Adventist hearer

### 8. Thinking Prompts (5-7 questions)

These are interpretive **pressure tests** for the preacher. NOT brainstorm questions for the audience. They push the preacher to think before structuring the sermon.

Examples of the kind of question:
- What assumption might your congregation bring to this text that the original audience would not have had?
- Where is the natural application of this passage too easy? Where might it be harder than it looks?
- What does this passage demand that your congregation probably does not want to hear?
- If your congregation walks out feeling good about this sermon, did you preach the whole text?
- What is the most common way this passage is mishandled, and how do you avoid it?
- Is there a distinctive Adventist truth this passage engages that is easy to soft-pedal?

Tailor questions to the specific passage. Generic prompts don't help.

---

## Step 3: Interactive Brainstorm — ONE QUESTION AT A TIME

This is the heart of the skill. **Read this section carefully — most of the value comes from doing this right.**

### The seven mandatory questions

These seven questions are the backbone. Skip a question only if the preacher already answered it in their initial prompt. Otherwise, ask all seven, **one at a time**, **in order**:

1. **What's the passage / topic you're working with?** *(Skip if given.)*
2. **What jumped out at you when you first read this text?** *(Their gut response — usually closer to the sermon than commentaries are.)*
3. **What's your congregation wrestling with right now that this passage speaks to?** *(Real people, real moment. Push for specifics.)*
4. **If your hearers remember one sentence on Monday morning, what should it be?** *(The Big Idea. Force a single declarative sentence.)*
5. **Where's the tension in this text? What does it disrupt or demand?** *(The thing the passage refuses to let people stay comfortable about.)*
6. **How does this passage point to Christ, the gospel, and the Adventist hope?** *(Even doctrinal texts. Even OT. The cross is not optional.)*
7. **What do you want them to DO differently after Sabbath?** *(Concrete behavior — not "grow in faith.")*

### How to ask

**ASK ONE QUESTION. WAIT FOR THE ANSWER. THEN ASK THE NEXT.**

Do not batch questions. Do not say "and a few brainstorm questions: 1) ... 2) ... 3) ...". That defeats the purpose. The questions are designed to surface clarity through the act of speaking — batching them lets the preacher answer hastily or skip the hard ones.

Each question should be its own short message. Conversational tone. Examples:

> Question 2 of 7: What jumped out at you when you first read this text? Not what you're supposed to notice — what actually caught your attention this week.

> Question 4 of 7: If your hearers remember one sentence on Monday morning, what is it? Say it badly if you have to. We'll sharpen it.

Number them so the preacher knows where they are in the flow. The structure builds momentum.

### When to push back

If an answer is short, vague, or generic — **follow up before moving on**. A sermon built on thin answers will be a thin sermon.

Example:
> Preacher: "The tension is that people need to trust God."
> You: "Hold on — trust God in WHAT specifically? What are they actually afraid of? What's the real cost of trusting Him here?"

### What to do with the research notes during brainstorm

You already produced `research-notes.md` in Step 2. Use it. If the preacher's gut response (Q2) is interesting but they didn't notice something the historical context shows, mention it briefly and let them respond. This is collaborative — your job is to help them find the sermon already in their head, not impose a sermon on them.

### When to stop and move to the brief

You can stop early if:
- The preacher has answered enough that the Big Idea, tension, and desired response are clear
- The preacher explicitly says they're ready
- You've gone through all seven questions

Do NOT stop early if:
- The Big Idea is still vague
- The application is still abstract
- The Adventist lens hasn't been touched (when the text engages a distinctive)

---

## Step 4: Sermon Brief

Output the brief so the preacher confirms direction before you write outline + manuscript:

```
## Sermon Brief

**Passage:** [passage]
**Date:** [YYYY-MM-DD]
**Location:** [church / venue]
**Structure:** [chosen structure]
**Language:** [English / Indonesian]
**Length:** [target minutes]
**Audience:** [audience]

**Big Idea:** [one declarative sentence]
**Key Tension:** [what the text disrupts or demands]
**Audience Need:** [what they're carrying]
**Desired Response:** [what you want them to do differently]
**Adventist Lens:** [the distinctive doctrine engaged, or "general Christian — no specific distinctive"]
**Opening Illustration Idea:** [one seed]
**Closing Illustration Idea:** [one seed]
```

Ask: "Look right? Anything to tweak before I find/draft the bookend illustrations and build the outline?"

---

## Step 5: Bookend Illustrations — REQUIRED

**Every sermon must have a strong illustration at TWO points:**

1. **Opening illustration / icebreaker** — the first 3-5 minutes. Hooks attention. Could be:
   - A famous story (Tier 1 — see `sermon-illustrations` skill for the source taxonomy)
   - An interactive activity (group discussion, quiz, show-of-hands) for AY/youth contexts
   - A vivid scene or scenario
2. **Closing illustration / reinforcement** — the last 2-4 minutes. Reinforces the Big Idea so it lands and sticks. Should be different in flavor from the opening — if the opening was an activity, the closing should be a story; if the opening was a famous story, the closing might be a return to that story or a fresh sealing image.

**Sourcing rule (mirrors sermon-illustrations skill):**
- **Tier 1 first** — find a famous, attributable illustration (Adventist heritage, classic preachers, biblical biography, history, literature, science). Verify before using.
- **Tier 2 if Tier 1 fails** — craft an original. Label it as original ("Imagine with me…") so the preacher doesn't accidentally claim it as fact.

**Anti-fabrication rule:** No invented quotes attributed to real people. No invented "true stories." Cliché illustrations (lighthouse, starfish, carrot-egg-coffee) only if used as foils to be replaced.

For each bookend, produce:
- **Source / type:** Famous-attributed / Famous-anecdote / Original
- **Setup, tension/development, payoff, bridge to point**
- **Verification notes**
- **Approximate spoken length**

These will be woven into the manuscript at the appropriate spots.

---

## Step 6: Generate `sermon-outline.md`

The outline opens with the **service header block** at the very top, then the sermon outline proper.

### Service Header Block (always at the top)

```
**Sermon Title:** [Short, evocative title]
**Date:** [YYYY-MM-DD, optionally with day name — e.g., "2026-07-04 (Sabbath)"]
**Location:** [Church / venue where it will be delivered]
**Main Verse / Ayat Inti:** [One verse, quoted in full, with translation]
**Responsive Reading / Ayat Bersahutan:** [Theme + one continuous passage of 5–7 verses, antiphonally voiced]
**Opening Hymn:** [SDAH #___ — Title] / [Lagu Sion Edisi Lengkap #___ — Judul]
**Closing Hymn:** [SDAH #___ — Title] / [LSEL #___ — Judul]
```

> **Label convention:** In Indonesian sermons render the labels as **"Ayat Inti"** (the main verse) and **"Ayat Bersahutan"** (the responsive reading). In English sermons use "Main Verse" and "Responsive Reading."

#### Main Verse / Ayat Inti
One verse, drawn from the preaching passage, that the entire sermon orbits. Echoed throughout.

#### Responsive Reading / Ayat Bersahutan
**One continuous passage** of about 5–7 verses (sweet spot; min 3, max 10). The verses **must come from a single passage** — the same chapter, or adjacent/closely related verses within the same book (e.g., Yohanes 1:1-6). **Do NOT stitch together scattered verses from different books.** Read the passage straight through, split antiphonally across the voices (Leader / Congregation / All; or Pemimpin / Jemaat / Bersama-sama in Indonesian). Choose a passage whose flow *prepares* the heart for the sermon, not one that summarizes it. Where possible, pick a range that does not center on the Ayat Inti so the main verse still lands fresh during the sermon.

#### Opening and Closing Hymns
Recommend hymn pairs by **theme**:
- **English (Adventist Hymnal, 1985 SDA Hymnal)** — number + title
- **Indonesian (Lagu Sion Edisi Lengkap)** — nomor + judul

**Never invent hymn numbers.** If unsure, name the hymn by title and flag for verification: *"verify number with your songbook."*

### Sermon Outline Proper

After the service header block:

- **Title** (already in header)
- **Introduction** — *the OPENING ILLUSTRATION goes here*, followed by context, Big Idea statement
- **Body** — main movements/points appropriate to the structure (see `references/structures.md`)
  - Each point: stated as a complete sentence, with its supporting passage and 1–2 sub-points
  - Word study insights from research-notes.md woven in where relevant
- **Application** — concrete, specific calls to action
- **Conclusion** — *the CLOSING ILLUSTRATION goes here*, return to the Big Idea, appeal/call
- **Closing prayer cue** (one line)

### Length guideline
- 20-min sermon: ~2,500–3,000 words manuscript
- 30-min sermon: ~3,800–4,500 words manuscript
- 40-min sermon (with interactive elements): ~3,500–4,500 words manuscript + interactive scripts
- 45-min sermon: ~5,500–6,500 words manuscript

(English speaking pace ≈ 130 wpm; Indonesian ≈ 110-120 wpm. Adjust word counts down ~15% for Indonesian.)

After outputting the outline, ask: "Want me to proceed to the full manuscript, or revise the outline first?"

---

## Step 7: Generate `sermon-manuscript.md`

Once the outline is approved, produce the full manuscript — **the actual words the preacher will say**.

**Carry the service header block over to the top of the manuscript** so the preacher has the whole worship flow in one document.

Manuscript requirements:

- Spoken language, not written prose. Short sentences. Repetition is fine. Direct address.
- **Opening illustration** is fully written out at the start, woven into the introduction
- **Closing illustration** is fully written out near the end, woven into the conclusion
- Scripture quotations in blockquotes with translation cited
- EGW quotations in blockquotes with full citation, fetched live from egwwritings.org when used
- Stage directions sparingly in italics: *(pause)*, *(slowly)*, *(read scripture from screen)*
- Application is **concrete** — name the specific behavior
- **Appeal** at the end of evangelistic and decision-oriented sermons

### Indonesian manuscripts

- Natural Indonesian preaching cadence, not translated English
- "Saudara-saudari" or "jemaat yang dikasihi Tuhan" — earn it, don't pad
- Quote Terjemahan Baru by default
- Adventist-specific terms used without translation: "hari Sabat," "bait suci surgawi," "Tiga Pesan Malaikat," "Roh Nubuat"

---

## Step 8: Generate `slides.md` (Gamma AI Deck)

Once the manuscript is approved, produce a slide deck **formatted for Gamma AI** (gamma.app). This file is copy-paste ready: the preacher pastes it into Gamma → "Paste in text" and Gamma builds the presentation.

The deck follows the sermon's flow — it does NOT invent new content. Pull title, Ayat Inti, points, Scripture, EGW, illustrations, and Big Idea straight from the outline and manuscript.

### File structure

```
# Outline Presentasi untuk Gamma.app
## "[Sermon Title]" — [Passage]

---

## CARA PAKAI
1. Buka gamma.app → New → "Paste in text" → mode "Card-by-card".
2. Salin teks antara "=== MULAI SALIN ===" dan "=== AKHIR SALIN ===".
3. Setelan: Format: Presentation · Language: [Indonesian/English] · Amount of text: [Medium / for Tuli: Brief]. Biarkan tema/visual dipilih Gamma.
4. Tiap blok dipisah `---` = satu slide.

---

=== MULAI SALIN ===

# [Judul Khotbah]
### [Passage] — [subtitle]

---

[... slide-per-slide: judul + beberapa baris fokus, tanpa arahan gambar ...]

=== AKHIR SALIN ===

---

## Catatan Verifikasi (jangan disalin ke Gamma)
[List each EGW quote / paraphrase status, hymn numbers, and a reminder to re-check every verse after Gamma generates.]
```

### Slide rules

**Focus on the WORDS, one slide at a time.** Gamma chooses the visuals/theme/background — do NOT prescribe them.

- **One idea per slide.** Slides separated by `---`. Aim for ~15–22 slides for a full sermon.
- **Each slide = a clear headline + a few focused lines.** Short. Punchy. The preacher speaks the rest. No dense paragraphs (a paste that looks like the outline is too heavy — break it up).
- **Do NOT add `[GAMBAR: ...]` or any background/image/theme directives.** Let Gamma decide the look. The file is words only.
- **Scripture verbatim**, with reference and translation, in blockquotes.
- **EGW quotes** only if verified; mark paraphrases as paraphrase (no quote marks).
- Keep the paste region **clean** so Gamma's "Card-by-card" mode makes one good card per `---` block. Keep CARA PAKAI and verification notes OUTSIDE the `=== MULAI SALIN ===` / `=== AKHIR SALIN ===` markers so they don't become slides.
- Cover the arc: title → opening illustration → Big Idea → each body point (with its Scripture/word study) → application → closing illustration → final Big Idea + appeal.
- The **Big Idea** appears on its own slide near the start, and again near the end.
- A **verification notes** section at the bottom, clearly marked "jangan disalin ke Gamma."

### For Tuli / simplified-language sermons

- Set "Amount of text: Brief" in Gamma.
- Keep slides **short phrases**, not sentences — match the simplified vocabulary of the manuscript (short, concrete words).
- Fewer words per slide, more slides — let each small idea breathe on its own card.

After outputting, tell the preacher how to paste it into Gamma (Card-by-card mode, copy between the MULAI/AKHIR markers).

---

## Step 9: Final Pass

After producing the four documents:

1. Re-read manuscript for **AI-slop phrases** (see foundation banned list). Strip them.
2. Verify **every Scripture citation** has book, chapter, verse, and translation.
3. Verify **every EGW quote** has a verified citation. Convert uncertain quotes to paraphrase with no quote marks.
4. Check the **Big Idea** appears at least three times across the manuscript (intro, mid-pivot, conclusion).
5. Confirm the **service header block** is at the top of both outline and manuscript.
6. Confirm **OPENING illustration AND CLOSING illustration** are both present, both fully written, both with verification notes if attributed.
7. Confirm the **Main Verse echoes back** in intro and conclusion of the manuscript.
8. Confirm `research-notes.md` exists with all 8 sections present.
9. Confirm the **Date and Location** appear in all files (header block on outline + manuscript; header line on research notes) and match what the preacher gave.
10. Confirm `slides.md` exists, every verse on a slide matches the manuscript, and the verification-notes section is present and marked "jangan disalin ke Gamma."

Deliver all four documents:
> Four documents ready: research-notes.md (review while you pray), sermon-outline.md (service flow), sermon-manuscript.md (what to preach), slides.md (paste into gamma.app for the deck). EGW quotes fetched from egwwritings.org where possible, otherwise paraphrased with notes. Hymn numbers flagged where unverified. Pray over it and make it yours.

---

## Step 10: Auto-Save to Output Directory

After the preacher approves the final manuscripts, save all four files to the output directory:

**Path structure:**
```
/Users/edmundsitumorang/DEV/skills-sermon-adventist/output/
└── [YYYY-MM-DD]-[sermon-title-in-kebab-case]/
    ├── research-notes.md
    ├── sermon-outline.md
    ├── sermon-manuscript.md
    └── slides.md
```

**Workflow:**
1. Convert sermon title to kebab-case (lowercase, hyphens instead of spaces; keep special words like "God", "Christ")
   - "The Place Whereon Thou Standest Is Holy" → `the-place-whereon-thou-standest-is-holy`
2. Prefix the folder name with the **date of delivery** in ISO `YYYY-MM-DD` form so sermons sort chronologically
   - Date `2026-07-04` + title above → `2026-07-04-the-place-whereon-thou-standest-is-holy`
   - If the preacher never gave a date, fall back to the title alone and tell them no date was recorded
3. Create the folder if it doesn't exist
4. Write the four .md files into it — each (except slides.md) already carries the **Date** and **Location** in its service header block (see Step 6)
5. Confirm to the preacher with the file paths

**Example output:**
> Sermon saved to `/Users/edmundsitumorang/DEV/skills-sermon-adventist/output/2026-07-04-the-place-whereon-thou-standest-is-holy/`
> - research-notes.md
> - sermon-outline.md
> - sermon-manuscript.md
> - slides.md
> Delivery: 2026-07-04 at [location] — recorded in each file's header.

---

## Anti-Patterns

This skill will not:

- **Produce a sermon without research notes.** Skipping research produces ChatGPT-flavored sermons.
- **Batch the brainstorm questions.** Each question, one at a time, conversationally — or you've defeated the brainstorm's purpose.
- **Skip the brainstorm entirely** even when the user gave a lot upfront. At minimum confirm the Big Idea, tension, and desired response.
- **Force Adventist distinctives** into every text. Romans 8 is not a sanctuary sermon. Let the text speak.
- **Fabricate** EGW quotes, commentary content, hymn numbers, or "true stories." Ever.
- **Produce a sermon with one illustration or none.** Always two: opening + closing. Always.
- **Write generic application.** "Trust God more" is not application.
- **Sound like a TED talk in church clothes.** Pastoral warmth over performance.
- **Soften Adventist truth** to please non-Adventist ears.

---

## Reference Files

- `references/structures.md` — six sermon structures, when to use each
- `references/adventist-themes.md` — doctrines mapped to texts and EGW works
- `references/commentary-sources.md` — Adventist and non-Adventist commentaries with descriptions
- `references/research-notes-template.md` — exact template for the research-notes.md document

---

**Why this works:** A sermon's quality is decided by clarity, not eloquence. Clarity comes from three disciplines: knowing the text deeply (research notes), knowing what you want to say (the seven brainstorm questions, asked one at a time so the preacher discovers their own conviction), and giving the message two anchor points the audience can grip (bookend illustrations). The skill enforces all three. The preacher does the hard part — owning the message before God. The skill clears the underbrush.
