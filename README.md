# Adventist Sermon & Bible Study Skills

Four Claude AI skills for Seventh-day Adventist sermon preparation, Bible study, and illustration research. Built on the Claude skill-creator framework.

**Live Repo:** https://github.com/situmorang-com/skills-sermon-adventist

---

## What's Included

### 1. **adventist-foundation** — Shared Theological Foundation
Loads once; shared across all other skills.

**What it provides:**
- 28 Fundamental Beliefs guardrails
- 3-tier Ellen G. White citation policy (Tier 1: live fetch from egwwritings.org; Tier 2: verified quotes; Tier 3: paraphrase)
- KJV (English) & Terjemahan Baru (Indonesian) translation defaults
- Banned AI-slop phrases (English & Indonesian)
- Anti-fabrication rules: never invent commentary, EGW quotes, hymn numbers, or illustrations
- Adventist-specific doctrinal infiltrations list (anti-Trinitas, Lunar Sabat, Hebrew Roots, Bumi Datar, etc.)

---

### 2. **sermon-adventist** — Full Sermon Preparation Workflow

**When to use:** You have a Scripture passage and want a complete sermon (research → outline → manuscript).

**What it produces:** Three documents per sermon
1. `catatan-penelitian.md` / `research-notes.md` — 8-section exegetical research (in Indonesian or English)
2. `sermon-outline.md` — Structured outline with service header block
3. `sermon-manuscript.md` — Full spoken manuscript (~3,500–4,500 words)

**Workflow (8 steps):**
1. Capture sermon intent (passage, audience, duration, language)
2. Generate **research notes first** (8 sections: context, background, word studies, commentary, EGW, cross-references, themes, thinking prompts)
3. Interactive brainstorm — **one question at a time**, not batched (7 mandatory questions, smart-skip already-answered ones)
4. Sermon brief (title, idea, structure)
5. Find/draft **bookend illustrations** (opening icebreaker + closing reinforcement, different flavors)
6. Generate outline
7. Generate manuscript with illustrations woven in
8. Final quality pass

**Key Features:**
- **6 choosable sermon structures** (Expository, Topical, Narrative, Biographical, Textual, Three-Point)
- **Mandatory bookend illustrations** — strong opening (grab attention) + strong closing (call to action)
- **Service header block** — Title, Main Verse, Responsive Reading (5–7 verses, antiphonal), Opening/Closing Hymns (both SDAH & LSEL recommendations)
- **Hebrew/Greek word studies** — KJV + TB + original language + Strong's + range of meaning + translation comparison
- **Multi-commentary insights** — Andrews Bible Commentary + SDABC + named Adventist scholars
- **EGW citations** — fetched live from egwwritings.org or paraphrased (never fabricated)
- **Adventist-specific infiltration doctrines** mentioned explicitly where relevant
- **No AI-slop** — clean, direct language

**Example prompts:**
- "I'm preaching Romans 8:1-11 this Sabbath. Expository sermon, 30 minutes, mixed ages, 120 members."
- "Khotbah evangelisasi tentang kedatangan Yesus untuk anak muda. 40 menit. Bahasa Indonesia."
- "Youth program on Joseph in Genesis 39 — integrity when no one's watching. Narrative style, 20 minutes."

**Output location:** `sermon-adventist/output/`

---

### 3. **bible-study-deep** — Deep Exegetical Study Notes

**When to use:** You want to study a passage in depth for personal devotion, Sabbath School prep, or sermon background.

**What it produces:** Single markdown document with 8 sections
1. Passage Context
2. Historical & Cultural Background
3. Key Word Studies (3–5 words)
4. **Commentary Insights** (4-tier framework)
5. Ellen G. White Cross-References
6. Scriptural Cross-References
7. Theological Themes
8. Application Questions

**Commentary 4-Tier Framework:**
| Tier | Sources |
|---|---|
| **Tier 1** — Adventist Primary | Andrews Bible Commentary (2020), SDABC |
| **Tier 2** — Adventist Scholars | Doukhan, LaRondelle, Stefanovic, Tonstad, Heppenstall, Davidson (mapped by specialty) |
| **Tier 3** — Classic Non-Adventist | **Matthew Henry**, Calvin, John Wesley, Matthew Poole, Charles Spurgeon (Psalms), William Barclay* |
| **Tier 4** — Modern Evangelical | F.F. Bruce, Leon Morris, John Stott, Keener (IVP), WBC |

*Barclay flagged: use cultural background only; avoid his theology (universal salvation).

**Key Features:**
- **Word studies** — English (KJV) + Indonesian (TB) + original language + Strong's + usage range + translation comparison
- **Multi-source commentary** — never relies on a single voice
- **EGW live-fetched** from egwwritings.org (Tier 1) or paraphrased (Tier 3)
- **Honest about gaps** — if commentary unknown, says so rather than fabricates
- **Application questions** — 5–8 questions designed to move from study to surrender (not just "what did you learn?")
- **Adventist lens** — notes where passage engages distinctives; doesn't force them where absent

**Example prompts:**
- "Deep study on Daniel 8:13-14. Want word studies on the Hebrew, EGW references, and sanctuary doctrine connection."
- "Mark 2:23-28. Cultural context on Pharisaic halakhah, word studies, Adventist Sabbath theology."
- "Romans 8:1-11. Greek word studies, EGW on righteousness by faith, theological themes for the congregation."

---

### 4. **sermon-illustrations** — Illustration Research & Creation

**When to use:** You need a strong opening story, closing illustration, or sermon illustration to reinforce a theme.

**What it produces:** Illustration with source, type, setup/tension/payoff/bridge, spoken length, verification notes.

**Approach:**
- **Tier 1 (Famous-Attributed)** — Search well-known illustration sources first (Adventist heritage, classic preachers, history, literature, science)
- **Tier 2 (Original)** — If no Tier 1 fit, create original illustration labeled clearly

**Themed Sources:** Grace, Sabbath, Second Coming, State of Dead, Sanctuary, Faith/Trial, Service, Suffering, Forgiveness, Salvation, Health, Cross, End-time, plus Indonesian-context illustrations.

**Key Features:**
- Never fabricate "true stories" — verify or label as original
- Track source and type (historical, parable, modern analogy, etc.)
- Spoken length noted (~2–4 minutes typical for sermon opening)
- Bridge to sermon theme explicit

---

## How to Load & Use These Skills

All skills require Claude's skill-creator framework. Load them in Claude Code or via `@skills` in conversation.

### Load Sequence

1. **Always load `adventist-foundation` first** — it's the shared context layer
2. Then load the specific skill you need:
   - `@sermon-adventist` — for sermon prep
   - `@bible-study-deep` — for deep Bible study
   - `@sermon-illustrations` — for illustrations

### Example Session

```
@adventist-foundation
@sermon-adventist

[Prompt] I'm preaching Exodus 20:8-11 this Sabbath. 
Audience: mixed ages, ~100 people. 
Duration: 35 minutes. 
Structure: Expository. 
Language: English/KJV.
Theme: Why the Sabbath still matters for Adventists today.
```

The skill will:
1. Generate research-notes.md (8 sections)
2. Ask 7 brainstorm questions ONE AT A TIME
3. Generate outline
4. Generate full manuscript with bookend illustrations
5. Produce three documents

---

## Key Guarantees & Anti-Fabrication Rules

These skills are built to **never invent content**:

| Content Type | Rule |
|---|---|
| Ellen G. White quotes | Fetched live from egwwritings.org (Tier 1), or paraphrased & labeled (Tier 3). Never put paraphrase in quotation marks. |
| Commentary content | Paraphrased from named sources (Andrews, SDABC, Doukhan, etc.) or flagged: *"[Source] likely addresses X — verify in your copy."* Never fabricated. |
| Hymn numbers | Verified or flagged as uncertain. Never invented. |
| Illustrations | Either famous/attributed with source traced, or labeled clearly as original. Never "true story" without verification. |
| Sermon structure | Chosen from 6 well-defined structures (Expository, Topical, Narrative, Biographical, Textual, Three-Point). Not invented per sermon. |

**If a guarantee is broken in output, that's a bug.** Report it.

---

## File Structure

```
skills-sermon-adventist/
├── README.md (this file)
├── .gitignore
│
├── adventist-foundation/
│   └── SKILL.md (shared theological foundation)
│
├── sermon-adventist/
│   ├── SKILL.md (full sermon workflow)
│   ├── evals/
│   │   └── evals.json (3 test cases: Romans 8, Second Coming, Genesis 39)
│   ├── references/
│   │   ├── structures.md (6 sermon structures, when to use each)
│   │   ├── adventist-themes.md (28 Fundamentals mapped to anchor texts & EGW)
│   │   ├── commentary-sources.md (Adventist + non-Adventist commentaries)
│   │   └── research-notes-template.md (exact template for 8-section research)
│   └── output/
│       ├── catatan-penelitian.md (vibe test: Daniel 12:4 research notes in Indonesian)
│       ├── sermon-outline.md (vibe test: Daniel 12:4 outline)
│       └── sermon-manuscript.md (vibe test: Daniel 12:4 full manuscript)
│
├── bible-study-deep/
│   ├── SKILL.md (8-section deep study, 4-tier commentary)
│   └── evals/
│       └── evals.json (3 test cases: Daniel 8:13-14, Mark 2:23-28, Romans 8:1-11)
│
└── sermon-illustrations/
    ├── SKILL.md (Tier 1 famous → Tier 2 original)
    ├── evals/
    │   └── evals.json
    └── references/
        └── illustration-sources.md (themed illustration sources)
```

---

## Quick Examples

### Example 1: Sermon Prep (English, Expository)

```
@adventist-foundation
@sermon-adventist

I'm preaching Daniel 12:4 to an AY (Adventist Youth) program 
this Sabbath. 40 minutes. Indonesian. Focus: knowledge and 
worship at the end of time — how social media/information 
overload relates to seeking real knowledge of God.
```

**Output:** 
- `catatan-penelitian.md` — 8 sections on Daniel 12:4
- Brainstorm (7 Qs, one at a time) on theme, structure, illustrations
- `sermon-outline.md` — expository outline with service block
- `sermon-manuscript.md` — ~4,000 word manuscript with opening (Alexandria) & closing (Huguenot) illustrations

### Example 2: Deep Bible Study (Mark 2)

```
@adventist-foundation
@bible-study-deep

Mark 2:23-28. I want to understand the Pharisaic halakhah, 
what Jesus was really saying about the Sabbath, and how 
Adventists read this.
```

**Output:**
- Passage context (Mark 1–3, genre, placement)
- Historical background (39 categories of Sabbath work, Mishnah, halakhic reasoning)
- Word studies (Sabbath, Son of Man, Lord)
- Commentary Insights (Andrews + SDABC + Tonstad + Matthew Henry + IVP Background)
- EGW from *Desire of Ages*
- Scriptural cross-references (Gen 2, Ex 20, Mark 3, John 5, Heb 4)
- Theological themes (Sabbath for humanity, Christ's authority, not abolished)
- 8 application questions

### Example 3: Illustration for "Truth in End-Times"

```
@adventist-foundation
@sermon-illustrations

I need a strong opening illustration for a sermon on 
"Guarding Truth in an Age of Deception" (end-time context). 
Youth audience. About 2 minutes spoken.
```

**Output:**
- Tier 1 search: historical Adventist illustrations on truth/deception (e.g., story from *Great Controversy*)
- Or Tier 2: original story about discernment in digital age
- Type, source, setup/payoff, bridge to sermon theme

---

## Requirements

- **Claude Code** with skill-creator framework
- **egwwritings.org API** access (for live EGW fetches in sermon-adventist & bible-study-deep)
- **Blue Letter Bible** / **Bible Hub** (for free word-study reference tools, cited but not required for execution)

---

## Notes on Theology & Stance

These skills are built for **Seventh-day Adventist preachers and teachers**. They:
- Affirm the 28 Fundamental Beliefs of the SDA Church
- Use Ellen G. White as authoritative on SDA theology & practice
- Engage Adventist distinctives: Sabbath, Sanctuary & Investigative Judgment, Spirit of Prophecy, state of the dead, three angels' messages, etc.
- Flag doctrinal disagreements with non-Adventist sources (soul immortality, hellfire, Sabbath abrogation) when relevant
- Never force an Adventist distinctive onto a passage that doesn't engage it

---

## Testing & Vibe Test

All skills have been tested with evaluation cases in `evals/` directories. The `sermon-adventist` skill has a full vibe-test output: a sermon on Daniel 12:4 for an Indonesian AY program, demonstrating the complete workflow.

To run your own vibe test: pick a Scripture passage, load the skills, and follow the prompts.

---

## Contributing & Feedback

**Known issues / areas for improvement:**
- egwwritings.org returns 403 on automated fetches; workaround uses Tier 2/3 fallback
- Hymn numbers (SDAH & LSEL) need manual verification — skill flags uncertainties
- Commentary sources assume English access; non-English commentary sources welcome

---

## License & Attribution

These skills were built with Claude AI (Claude Sonnet 4.6) and are provided as-is for Adventist sermon and Bible study preparation.

**Created by:** Edmund Situmorang  
**Repository:** https://github.com/situmorang-com/skills-sermon-adventist  
**Last updated:** May 6, 2026

---

## Quick Links

- [28 Fundamental Beliefs of the SDA Church](https://www.adventist.org/beliefs/fundamental-beliefs/)
- [Ellen G. White Writings (egwwritings.org)](https://www.egwwritings.org/)
- [Andrews Bible Commentary](https://www.andrews.edu/)
- [Seventh-day Adventist Bible Commentary](https://www.adventist.org/resources/sabbath-school/)
- [Blue Letter Bible (word studies)](https://www.blueletterbible.org/)
- [SDA Hymnal & Lagu Sion Edisi Lengkap](https://www.hymnal.net/)

---

**Questions?** Open an issue on GitHub or contact the repository maintainer.
