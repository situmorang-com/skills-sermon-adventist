---
name: sabbath-school-lesson
description: Build Seventh-day Adventist Sabbath School material in the real quarterly format. Two modes — (A) write an original seven-day lesson from scratch (weekly theme, Read for This Week's Study, Memory Text, Sabbath Afternoon introduction, Sunday–Thursday daily sections with discussion questions, Friday Further Thought with Ellen G. White readings, plus a Teachers Comments edition), or (B) build a teacher's guide for an existing Adult Bible Study Guide lesson (learning objectives, timed discussion flow, participation questions, illustrations, closing appeal). Produces English (KJV) or Indonesian (Terjemahan Baru) output. Use whenever the user wants to write, teach, or prepare a Sabbath School lesson, quarterly lesson, lesson study, Adult Bible Study Guide week, teachers guide, or class study plan — including Indonesian phrasings like pelajaran Sekolah Sabat, penuntun guru, pendalaman pekan ini, or when they say they are teaching the lesson this Sabbath.
---

# Sabbath School Lesson

Sabbath School is not a sermon with chairs in a circle. It is a *discussion* built on a text, run in about thirty-five minutes, in front of people who read the lesson (or did not) and who will talk if the questions are good and sit silent if they are not. This skill produces material for that room.

**Requires:** the `adventist-foundation` skill is loaded for doctrinal alignment, translation defaults, voice, banned phrases, and the Ellen G. White citation policy. Do not restate those rules here — apply them.

**Related skills:** `bible-study-deep` for the exegetical engine behind a lesson, `sermon-illustrations` for the opening hook, `sermon-adventist` when the ask is actually a sermon.

---

## Two Modes

Ask which one first. It changes everything downstream.

| | **Mode A — Original Lesson** | **Mode B — Teacher's Guide** |
|---|---|---|
| The ask sounds like | "Write a Sabbath School lesson on Abraham" · "I need a seven-day lesson for our class series" · "buat pelajaran Sekolah Sabat" | "I'm teaching this week's lesson" · "Help me teach lesson 6" · "penuntun guru untuk pelajaran pekan ini" |
| You are writing | The lesson itself, in quarterly format | A plan for presenting a lesson that already exists |
| Deliverables | `sabbath-school-lesson.md` + `teachers-comments.md` | `teachers-guide.md` |
| You need | Theme or passage | The actual lesson (see Mode B, Step 1) |
| Length | ~3,000–4,000 words + ~1,200 for the teacher edition | ~1,500–2,200 words |

**Mode B is the default. Assume it unless told otherwise.** Sabbath School follows the quarterly Adult Bible Study Guide, worldwide, every week. A local teacher does not write their own seven-day lesson; they teach the lesson the whole church is studying. So "I need a Sabbath School lesson" almost always means "help me teach *this week's* lesson," and the right first move is to work out which lesson falls on that Sabbath and get its text.

Mode A is for the genuine exception: a custom study series, a youth or small-group track running outside the quarterly, or a lesson written for a class that has no quarterly available. Confirm that before writing an original week.

Mode B is also the more dangerous mode, because it depends on the official lesson text. Never invent that text. See Mode B, Step 1.

**Working out which lesson.** A quarterly week is *read* across its printed date range and *discussed in class the following Sabbath*: the week printed "Aug 1–7" is taught on Sabbath Aug 8, which is why its Sabbath Afternoon section closes by pointing to that later date. So find the lesson whose date range *ends the day before* the Sabbath being taught. Do not assume the quarter starts on the first Sabbath of the month; Q3 2026 began June 27, which shifts every lesson number by one.

---

## Step 1: Capture Inputs (both modes)

One short conversational message. Skip anything already given.

| Field | Mode A | Mode B |
|---|---|---|
| Mode | Required | Required |
| **Language** | **Always ask.** English (KJV) / Indonesian (Terjemahan Baru) / bilingual | Same |
| Theme or passage | Required | Comes from the lesson |
| The lesson identity | n/a | Required: quarter, year, lesson number and title |
| Sabbath date being taught | Required (ISO `YYYY-MM-DD`) — drives the day headings and the folder name | Required |
| Class profile | Adults, young adults, youth, seekers/baptismal class, mixed | Same |
| Class size and talk culture | Affects question count and whether you plan small groups | Same |
| Time available | Default 35 minutes of lesson study | Same |
| Series context | Lesson N of a quarter, or standalone | Which quarter |

**Language is asked every time, not inherited.** A Sabbath School class often differs in language from the preacher's own default, and mixed-language congregations are normal. If the answer is bilingual, produce one document with the Indonesian section following each English section, never two half-documents.

Do not interrogate beyond the table. If the user gave a theme and a date, that is enough to start Mode A.

---

# MODE A — Write an Original Seven-Day Lesson

## A1: Fix the week's spine before writing a word of prose

A quarterly week is one argument delivered in six moves. Decide the whole spine first, then write. Lessons that get written day-by-day wander, repeat themselves on Tuesday and Thursday, and arrive at Friday with nothing left to land.

Write this out and show it to the user for confirmation:

```
## Lesson Spine

**Lesson N: [Title]**            (4–7 words, concrete, not abstract)
**Week of:** [date range]
**Sabbath:** [YYYY-MM-DD]
**Language:** [English / Indonesian / bilingual]

**Central claim:** [one declarative sentence the whole week argues]
**Memory Text:** [reference — the verse that carries the claim]
**Read for This Week's Study:** [4–6 passages, in canonical order]

Sun    — [move 1: usually the problem, the setting, or the text's first turn]
Mon    — [move 2]
Tue    — [move 3]
Wed    — [move 4 — often the theological center]
Thu    — [move 5 — usually where it costs something]
Fri    — Further Thought [the EGW reading and the three discussion questions]

**Adventist lens:** [the distinctive genuinely engaged, or "general Christian — none forced"]
**Where the week gets uncomfortable:** [the day that is not safe]
```

Ask: "Spine look right before I write the week?"

Two rules on the spine:

- **Five distinct moves, not five restatements.** If Monday and Wednesday could swap places without loss, the spine is broken. Each day must do something the others do not.
- **One day must cost something.** A week that is agreeable on all five days was not built from Scripture. Name that day in the spine so it does not get sanded down during drafting.

## A2: Research the week

Run the passages through the machinery in `bible-study-deep` before drafting: word studies where translation carries interpretive weight, BRI on anything doctrinally contested, Andrews Bible Commentary and SDABC on the key verses, EGW for Friday.

Two things to fetch early, because they gate the writing:

**The Ellen G. White reading for Friday.** Every quarterly week points to a specific EGW reading. Use `egw-fetch.sh` per the foundation's Tier 1 workflow. See the page-range rule in A4 (Friday) before you write a single page number.

**The Memory Text wording.** Verbatim, from KJV or Terjemahan Baru. The class memorizes this verse. A wrong word in the Memory Text is the most visible error the document can contain, and it propagates: people quote it back for thirteen weeks. Confirm the wording against a Bible text (Blue Letter Bible, Bible Hub, STEP Bible) rather than typing it from memory.

Apply the source provenance discipline from `bible-study-deep` — `fetched-verbatim`, `located-unread`, `known-position`, `inference` — as internal working categories. **The tags never appear in the lesson body.** They live in the Verification Ledger in `teachers-comments.md`. A lesson handed to a class must read as devotional prose, not as a build log.

## A3: Word budgets

Hit these. The quarterly format is tight on purpose, and a class has thirty-five minutes.

| Part | English | Indonesian |
|---|---|---|
| Sabbath Afternoon introduction | 250–350 | 220–300 |
| Each daily section (Sun–Thu) | 450–600 | 400–520 |
| Friday Further Thought | 200–300 + 3 questions | 180–260 + 3 questions |
| **Week total** | **3,000–4,000** | **2,600–3,400** |
| Teachers Comments | 1,000–1,500 | 900–1,300 |

Indonesian runs shorter for the same content. Do not pad it to match the English count.

## A4: Write the seven sections

### Sabbath Afternoon

Opens the week. In order:

1. **Read for This Week's Study:** the passage list, canonical order, comma-separated.
2. **Memory Text:** the verse quoted in full, in a blockquote, with reference and translation.
3. **The introduction itself** (250–350 words). This is the only place in the week you get to be a writer. Open with a scene, a question the text forces, or a tension a real person carries — not with a summary of what the week will cover. Land on the central claim without stating it as a thesis sentence.
4. **The closing line**, the quarterly's own convention: *"Study this week's lesson to prepare for Sabbath, [date]."*

Never open with "This week we will study..." That is a table of contents wearing a paragraph's clothes.

### Sunday through Thursday

Each day is a titled section. Heading format — day name, date, colon, then a concrete title of 3–7 words that names something in the passage rather than an abstraction ("The Cost of Leaving" beats "Faith and Obedience"). A colon, not an em dash, since the foundation bans em dashes in output.

- English: `## Sunday, August 9: The Call No One Asked For`
- Indonesian: `## Minggu, 9 Agustus: Panggilan yang Tak Diminta`
- Friday: `## Friday, August 14: Further Thought` / `## Jumat, 14 Agustus: Pendalaman`

Each day, in this shape:

1. **The read prompt** — `Read Genesis 12:1–5.` One passage, short enough to actually read aloud in class.
2. **Exposition** (350–450 words) — what the text says, what the original hearers would have caught, what the words carry. This is where word studies, background, and commentary land, written as prose. No source tiers on the page, no scaffolding visible.
3. **One or two questions**, set off in bold or italic per the quarterly convention. See A5 — these questions are the entire point of the day.

Discipline for the daily sections:

- **The text drives, not the theme.** Each day is anchored in its own passage. A day that quotes six scattered verses to support an idea is a topical sermon fragment, not a lesson section.
- **Do not answer your own question.** The quarterly's worst habit is asking a question and then supplying the answer in the next sentence. Ask it and stop. The class supplies the answer, or the teacher draws it out.
- **Paragraphs of four sentences or fewer.** People read this on a phone at 6 a.m.
- **EGW belongs on Friday.** A short quote mid-week is fine when it genuinely opens the text, but the weight goes to Friday. A lesson with an EGW quote every day reads as proof-texting.

### Friday — Further Thought

The week's landing. Three parts:

1. **The Ellen G. White reading**, named as a directive: `Read Ellen G. White, "The Call of Abraham," in Patriarchs and Prophets, pp. 125–131.`

   **The page-range rule, and it is hard:** give a page range *only* if you fetched it and the refcodes confirm it. If you have not verified the pages, name the **chapter title and the book** and stop. Chapter titles are stable and checkable; page numbers vary by edition and are the single easiest thing in this document to get wrong. A chapter title with no pages is correct and useful. An invented page range is a fabrication that a class member will find in ninety seconds.

2. **One EGW paragraph quoted** — verbatim in a blockquote with the exact refcode, or, if the fetch path is exhausted, clearly paraphrased with no quotation marks per the foundation's Tier 3. Follow it with one or two sentences tying it to the week's claim.

3. **Discussion Questions** — numbered, usually three or four. Real quarterlies vary; count them rather than assuming. These differ from the daily questions: they are for the whole class on Sabbath morning, they assume the week has been read, and they should reach past the text into the congregation's actual life. At least one must be answerable by someone who disagrees with the lesson's conclusion, or the class will perform agreement instead of thinking.

## A5: The questions are the lesson

Everything else is setup. A quarterly week lives or dies on eight to twelve questions.

**A question earns its place if it passes all four:**

1. It cannot be answered "yes," "no," or "Jesus."
2. A person who read the passage carefully could give two different defensible answers.
3. It names something real — a decision, a relationship, a fear, a cost — not an abstraction.
4. The teacher does not already know what the class will say.

| Dead question | Live question |
|---|---|
| "Do we need to trust God?" | "Abram left without knowing the destination. Name one thing you are being asked to do right now without knowing how it ends." |
| "What can we learn from Abram's faith?" | "Abram lied about Sarai in Egypt two chapters after this call. Does that change how you read verse 4?" |
| "Isn't God's promise wonderful?" | "The promise was land, offspring, and blessing. Abram died owning a burial cave. Was the promise kept?" |
| "Why is the Sabbath important?" | "Your coworker says the Sabbath was for Israel. You have four minutes before the meeting starts. What do you actually say?" |

Distribute the question types across the week: one or two observational (what does the text *say*), three or four interpretive (why this, not that), and the rest applicational, increasing in cost as the week goes on. Thursday should be the expensive one.

## A6: Write `teachers-comments.md`

The Teachers Edition of the quarterly. Separate file, separate audience: the person standing up front. Structure:

```markdown
# Teachers Comments — Lesson N: [Title]

**Key Text:** [the one verse the class must leave holding]
**Study Focus:** [passages]

## Part I — Overview

Lesson themes (2–4, named), and the one sentence that says what this week is
actually about. Where the week is heading and why the order of days is what it is.

## Part II — Commentary

Two or three headed subsections of exposition the teacher needs and the student
lesson could not carry: the background that unlocks a verse, the word that the
translation flattened, the Adventist distinctive the passage genuinely engages,
the objection a thoughtful class member will raise and how to meet it honestly.

## Part III — Life Application

The discussion plan: an opening question that gets someone talking in the first
ninety seconds, the two questions worth spending real time on, an activity if the
class is one that will do activities, and the closing move that asks for a
decision without manipulating for one.

## Verification Ledger

[table — every tagged citation from the lesson and these comments]
```

The Verification Ledger is the same table as in `bible-study-deep`: Source | Tag | Where | Action for the user. It is the only place provenance tags appear, and it goes in this file, never in the student lesson.

---

# MODE B — Teacher's Guide for an Existing Lesson

## B1: Get the actual lesson text. Do not proceed without it.

This is the failure point of the whole mode. A guide built on a guessed lesson is worse than no guide, because the teacher discovers the mismatch in front of the class.

**Ask for it directly first:** "Paste the lesson text, or tell me the quarter, year, and lesson number and I'll try to pull it."

**If attempting to fetch**, the lesson is published in several places. Try them, and treat failure as a normal outcome:

- Sabbath School Net (`ssnet.org`) — posts each week's lesson and teacher helps in HTML
- The Adult Bible Study Guide site (`absg.adventist.org`)
- The Sabbath School app's backend used by Adventech's apps, if reachable
- For Indonesian, the local conference or division quarterly, often as a PDF

**Hard rule:** if you cannot read the lesson, say so in one sentence and ask the user to paste it. Do **not** reconstruct a lesson week from its title. Do **not** infer the daily sections from the quarter's theme. Do **not** produce a guide "based on what lesson 6 likely covers." A quarterly title tells you almost nothing about which passages the five days actually treat.

What you minimally need before writing: the lesson title, the Memory Text, the Read-for-This-Week list, the five daily section titles with their passages, and the three Friday discussion questions.

## B2: Read the lesson as a teacher, not a reader

Before planning, answer these for yourself:

- **What is this week actually arguing?** Often not what the title says.
- **Which day carries the weight?** Usually one of the five does; the others support it. Teach that one properly and let the others move.
- **Where is the lesson thin?** A day that asserts something the text does not quite say, or skips the hard part of a passage. You will need to handle it honestly without undermining the quarterly in front of the class.
- **What will the class push back on?** Name it in advance. Every class has one member who has been waiting all week to raise it.
- **Which distinctive is in play?** And is the lesson engaging it or gliding past it?

## B3: Write `teachers-guide.md`

```markdown
# Teacher's Guide — [Quarter Year], Lesson N: [Title]

**Sabbath:** [YYYY-MM-DD]  ·  **Class:** [profile]  ·  **Time:** [minutes]
**Memory Text:** [verse, quoted, with translation]
**Key Text for the class to leave holding:** [one verse]

## What This Week Is Arguing
[3–4 sentences. The lesson's claim in your own words, plus what it is not saying.]

## Objectives
| | |
|---|---|
| **Know** | one fact or interpretation they did not have before |
| **Feel** | the affective shift the text asks for |
| **Do** | one concrete action, nameable in a sentence, doable this week |

## Discussion Plan
[The timed table — see B4.]

## The Two Questions Worth Real Time
[For each: the question, why it matters, what answers to expect, and how to keep
it open when someone tries to close it with a Sunday-school answer.]

## Background the Class Does Not Have
[2–3 items only. The word study, the historical detail, the Adventist distinctive.
Each one should change how a verse reads, not decorate it.]

## Ellen G. White for This Week
[The Friday reading, plus one paragraph worth reading aloud — verbatim with
refcode if fetched, or clearly paraphrased. Note where to stop reading; a long
quote read aloud loses the room.]

## Handling the Hard Spots
[The pushback you predicted in B2, and an honest answer. If the lesson is thin
somewhere, how to teach the text faithfully without making the quarterly the
problem.]

## Opening Hook
[The first ninety seconds. See B5.]

## Closing
[How the class ends: the return to the Key Text, the one-sentence summary, the
specific decision or action, and the prayer cue.]

## Verification Ledger
[table]
```

## B4: The timed discussion plan

Sabbath School lesson study is typically 30–40 minutes and it is *always* shorter than planned. Plan for the shorter number.

**35-minute plan:**

| Min | Move | Notes |
|---|---|---|
| 0–3 | Opening hook + the week's claim in one sentence | Someone other than you speaks by minute two |
| 3–6 | Memory Text read aloud, and one question about it | Not "what does it mean" — something specific |
| 6–14 | The weight-bearing day | Read the passage. Two questions. Let silence sit |
| 14–22 | The second real question | This is where the class does its own thinking |
| 22–28 | The remaining days, moved through quickly | Name what they add. Do not re-teach them |
| 28–33 | Application: the one concrete thing | Specific enough that someone could refuse it |
| 33–35 | Key Text again, one sentence, prayer | Ends on the text, not on your summary |

Compress by cutting minutes 22–28, never by cutting application.

**If the class runs 40 minutes**, add the extra five to the second real question, not to your exposition.

## B5: Facilitation, not presentation

A teacher's guide that produces a monologue has failed regardless of its content quality. Build these in:

- **Someone else talks in the first two minutes.** A show of hands, a one-word answer around the circle, a question with an easy entry point. A class that stays silent for ten minutes has decided its role for the whole hour.
- **Plan the silence.** After a real question, four to six seconds of nothing is the question working. Note in the guide where to wait.
- **Read the passage aloud, from the Bible, every time.** Not from the lesson's paraphrase.
- **Have a plan for the dominant talker** and for the class that will not speak. Small groups of three for four minutes solves both, and belongs in the guide when the class profile calls for it.
- **Do not defend the quarterly.** If a day is weak, teach the text.
- **The teacher's own study is not the lesson.** Background goes in only where it changes a reading.

See `references/teaching-methods.md` for the fuller set: question sequencing, mixed-language classes, the mission story slot, seeker-present classes, and what to do when a doctrinal argument breaks out.

---

## Output Format (both modes)

Markdown. Scripture in blockquotes with translation cited. EGW in blockquotes with full citation. Headings follow the quarterly's own conventions — day names as section headings, `Read [passage]` as a directive line, discussion questions numbered.

For Indonesian output, use the quarterly's Indonesian labels (Sabat Sore, Minggu, Senin, Ayat Hafalan, Pendalaman, Pertanyaan Diskusi). The full label table, including what to verify against a current Indonesian quarterly, is in `references/lesson-anatomy.md`.

Every document ends with a **Verification Ledger** — except the student lesson in Mode A, which stays clean and carries its ledger in `teachers-comments.md`.

---

## Final Pass

Before delivering, check:

1. **Memory Text is verbatim** and the reference is right. Check it against a Bible text, not memory.
2. **Every EGW page range was fetched.** Any unverified range is replaced by a chapter title, or dropped.
3. **No fabricated lesson content in Mode B.** Everything attributed to the quarterly is from the text you actually read.
4. **Questions pass the four tests in A5.** Count them. Delete the dead ones rather than rewriting them into life.
5. **No question is answered in the next sentence.**
6. **Five distinct daily moves** (Mode A). No two days interchangeable.
7. **One day costs something.** Find it. If you cannot, the week is not finished.
8. **Word budgets hit** (A3), Indonesian not padded.
9. **No provenance tags, no `para_id`, no "this session"** in any body text. Ledger only.
10. **AI-slop swept** per the foundation's banned list, both languages. No em dashes in output prose.
11. **Timed plan adds up** and application survives compression (Mode B).
12. **Adventist lens honest** — engaged where the text engages it, absent where it does not.

Then deliver plainly:

> Mode A: two files — `sabbath-school-lesson.md` for the class, `teachers-comments.md` for you (ledger inside). EGW pages verified where shown; chapter titles given where they were not.
>
> Mode B: `teachers-guide.md`, built on the lesson text you provided. The 35-minute plan compresses at minutes 22–28 if the superintendent runs long.

---

## Save the Output

```
/Users/edmundsitumorang/DEV/skills-sermon-adventist/output/
└── [YYYY-MM-DD]-ss-[kebab-case-title]/
    ├── sabbath-school-lesson.md     (Mode A)
    ├── teachers-comments.md         (Mode A)
    └── teachers-guide.md            (Mode B)
```

The `ss-` prefix is deliberate. A Sabbath School lesson and a sermon can fall on the same Sabbath and are different material, so they get different folders. Do not write Sabbath School files into a sermon folder.

- Date is the Sabbath the lesson is taught, ISO `YYYY-MM-DD`.
- Title in kebab-case, keeping words like "God" and "Christ": lesson "The Call of Abraham" on 2026-08-15 → `2026-08-15-ss-the-call-of-abraham`.
- No date given: use the title alone and tell the user no date was recorded.
- Confirm the paths back to the user.

---

## Anti-Patterns

- **Never reconstruct an official quarterly lesson you could not read.** Mode B's one unforgivable failure. Ask for a paste instead.
- **Never invent an EGW page range.** Chapter title and book, or nothing.
- **Never mis-quote the Memory Text.** The class memorizes it.
- **Never write a lesson that is a sermon in seven pieces.** Sabbath School is discussion. If the class only listens, the material was wrong.
- **Never ask a question you already know the answer to** and then supply it in the next sentence.
- **Never let all five days agree with the class.** A week with no cost was not built from the text.
- **Never make Monday and Wednesday the same day** with different verses.
- **Never print provenance tags or narrate your research** in the lesson body. Ledger only.
- **Never force an Adventist distinctive** onto a week that does not engage one, and never glide past one that the passage puts directly in front of you.
- **Never pad Indonesian** to match the English word count.
- **Never plan a discussion that cannot survive losing five minutes.** It will lose five minutes.

---

## Reference Files

- `references/lesson-anatomy.md` — the quarterly week's structure part by part, word budgets, heading conventions, the student/teacher edition split, and the Indonesian label table
- `references/teaching-methods.md` — facilitation: question sequencing, timing variants, silence, dominant talkers, mixed-language and seeker-present classes, doctrinal arguments, the mission story slot
- `bible-study-deep/SKILL.md` — the exegetical engine and the provenance/ledger discipline this skill inherits
- `commentary-tiers.md` (ships with `bible-study-deep`) — commentary sources by tier, lexicons, cautions
- `adventist-themes.md`, `commentary-sources.md` (ship with `sermon-adventist`) — distinctives mapped to texts, and the Adventist source list
- `HOWTO_EGW_LaguSion.md` (ships with `sermon-adventist`) — operating the EGW API helper

---

**Why this works:** The quarterly format looks like a container for content. It is actually a container for *questions*, and the prose exists to make eight to twelve good questions possible. A lesson fails when the writer treats the daily sections as the deliverable and the questions as decoration. This skill inverts that: fix the spine, earn each day, and spend the real effort on the questions the class will still be arguing about in the parking lot.
