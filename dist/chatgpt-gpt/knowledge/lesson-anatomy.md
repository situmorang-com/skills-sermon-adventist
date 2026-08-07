# Anatomy of a Sabbath School Quarterly Week

Reference for the `sabbath-school-lesson` skill. The structural contract of one week in the Adult Bible Study Guide, part by part, plus the two editions and the Indonesian label set.

---

## The Two Editions

The quarterly ships as two documents for the same week. Confusing them is the most common structural error.

| | **Student edition** (Adult Bible Study Guide) | **Teachers edition** (Teachers Comments) |
|---|---|---|
| Read by | Every class member, during the week | The teacher, on Friday night |
| Contains | The seven-day lesson: Sabbath Afternoon through Friday | Overview, Commentary, Life Application |
| Voice | Devotional, second person, questions left open | Instructional, addressed to the teacher |
| Verification apparatus | **None.** Clean prose | The Verification Ledger lives here |
| Length | 3,000–4,000 words (English) | 1,000–1,500 words |
| In this skill | `sabbath-school-lesson.md` | `teachers-comments.md` |

The teachers edition never repeats the student lesson. It carries what the student lesson could not: the background that unlocks a verse, the objection the class will raise, the discussion plan.

---

## The Seven Sections

### 1. Sabbath Afternoon

The week's front door. Four elements, in this order, no exceptions:

| Element | Form | Notes |
|---|---|---|
| **Read for This Week's Study** | 4–6 passages, canonical order, comma-separated | These are the week's raw material, not a topical proof-text list. A week whose reading list jumps across five books is usually a topical study wearing quarterly clothes |
| **Memory Text** | One verse, full quotation, blockquote, reference + translation | Verbatim. Verify against a Bible text. The class memorizes this; an error propagates for the whole quarter |
| **Introduction** | 250–350 words (English), 220–300 (Indonesian) | The only genuinely writerly paragraph of the week |
| **Closing line** | *"Study this week's lesson to prepare for Sabbath, [date]."* | The quarterly's own convention. Keep it |

The introduction opens with a scene, a tension, or a question the text forces. It does **not** summarize the week. It lands on the week's central claim without announcing it as a thesis.

### 2–6. Sunday through Thursday

Five sections, one per day, each doing a distinct move in the week's argument.

**Heading form:**
```
## Sunday, August 9: The Call No One Asked For
## Minggu, 9 Agustus: Panggilan yang Tak Diminta
## Friday, August 14: Further Thought
## Jumat, 14 Agustus: Pendalaman
```

Day name, date, colon, then a concrete section title. A colon, not an em dash — the foundation bans em dashes in output. Titles are 3–7 words and name something in the passage, not an abstraction. "The Cost of Leaving" beats "Faith and Obedience."

**Internal shape:**

| Part | Length | Rule |
|---|---|---|
| Read prompt | One line: `Read Genesis 12:1–5.` | One passage, short enough to read aloud in class in under a minute |
| Exposition | 350–450 words | Prose. Word studies, background, and commentary dissolved into it. No visible scaffolding, no source tiers, no tags |
| Questions | 1–2, set off in bold or italic | The point of the day. See the four tests in `SKILL.md` A5 |

**The five moves.** A well-built week distributes work like this, though the order can vary by genre:

| Day | Typical function |
|---|---|
| Sunday | The setting, the problem, or the text's first turn. Establishes what is at stake |
| Monday | Develops the situation or introduces the complication |
| Tuesday | A second angle: a parallel passage, the other side, the background that reframes |
| Wednesday | The theological center. Usually the week's heaviest lifting |
| Thursday | Where it costs something. The day that is not comfortable |

If two days could swap without loss, the week has four moves and a repeat.

### 7. Friday — Further Thought

Three parts, in order:

**a. The Ellen G. White reading**, as a directive:
```
Read Ellen G. White, "The Call of Abraham," in Patriarchs and Prophets, pp. 125–131.
```

**The page-range rule:** a page range appears only if it was fetched and confirmed by refcode. Otherwise give the **chapter title and book** with no pages. Chapter titles are stable across editions and checkable in seconds; page numbers are not. An unverified page range is a fabrication, and it is the easiest one in the document for a class member to catch.

**b. One quoted EGW paragraph** — verbatim in a blockquote with the exact refcode, or clearly paraphrased with no quotation marks (foundation Tier 3). One or two sentences after it tie it to the week's claim. One paragraph, not three: a long quote read aloud on Sabbath morning loses the room.

**c. Discussion Questions** — exactly three, numbered.

These are a different instrument from the daily questions:

| | Daily questions | Friday discussion questions |
|---|---|---|
| Asked of | The individual reader, mid-week | The whole class, Sabbath morning |
| Assume | The passage just read | The whole week has been read |
| Scope | Inside the text | Text reaching into the congregation's actual life |
| Count | 1–2 per day | Exactly 3 |

At least one of the three must be genuinely answerable by someone who disagrees with the lesson's conclusion. Without that, the class performs agreement instead of thinking.

---

## Word Budgets

| Part | English | Indonesian |
|---|---|---|
| Sabbath Afternoon introduction | 250–350 | 220–300 |
| Each daily section (×5) | 450–600 | 400–520 |
| Friday Further Thought | 200–300 + 3 questions | 180–260 + 3 questions |
| **Student edition total** | **3,000–4,000** | **2,600–3,400** |
| Teachers Comments | 1,000–1,500 | 900–1,300 |

Indonesian expresses the same content in fewer words. Do not pad to match.

---

## Teachers Comments Structure

The teachers edition follows a fixed three-part shape.

| Part | Contains |
|---|---|
| **Key Text** | The one verse the class should leave holding. Often but not always the Memory Text |
| **Study Focus** | The week's passages |
| **Part I — Overview** | The lesson themes (2–4, named) and one sentence on what the week is actually about. Why the days are in the order they are |
| **Part II — Commentary** | Two or three headed subsections of exposition the student lesson could not carry: the unlocking background, the flattened word, the distinctive genuinely engaged, the objection a thoughtful member will raise |
| **Part III — Life Application** | The discussion plan: the opening question, the two questions worth real time, an activity where the class will do activities, and the closing move toward decision |
| **Verification Ledger** | Source / Tag / Where / Action — every tagged citation from both files |

An older format stated objectives as **Know / Feel / Do**. It is still useful and this skill keeps it in the Mode B teacher's guide, where a single teacher needs a target more than a themes list.

---

## Indonesian Label Set

Labels used in the Indonesian Sabbath School quarterly. **Verify against a current Indonesian edition** before printing a whole quarter's worth; divisional editions vary and the wording has shifted across years.

| English | Indonesian |
|---|---|
| Sabbath Afternoon | Sabat Sore |
| Sunday | Minggu |
| Monday | Senin |
| Tuesday | Selasa |
| Wednesday | Rabu |
| Thursday | Kamis |
| Friday | Jumat |
| Read for This Week's Study | Bacalah untuk Pelajaran Pekan Ini |
| Memory Text | Ayat Hafalan |
| Further Thought | Pendalaman |
| Discussion Questions | Pertanyaan Diskusi |
| Lesson N | Pelajaran N |
| Teachers Comments | Komentar Guru (teacher edition: Penuntun Guru) |
| Key Text | Ayat Kunci |
| Study Focus | Fokus Pelajaran |
| Life Application | Penerapan Hidup |
| Sabbath School | Sekolah Sabat |

**Indonesian month names** for day headings: Januari, Februari, Maret, April, Mei, Juni, Juli, Agustus, September, Oktober, November, Desember. Date order is day-then-month: `Minggu, 9 Agustus`.

**EGW book titles stay in English** in Indonesian output (*Patriarchs and Prophets*, *The Great Controversy*), since those are the canonical citation forms — even where an Indonesian translation exists. Chapter titles may be given in English with an Indonesian gloss if useful.

---

## Where the Official Lesson Lives (Mode B)

For building a teacher's guide, the official text is required input. Places it is published:

| Source | Form | Notes |
|---|---|---|
| Sabbath School Net (`ssnet.org`) | HTML, weekly | Posts the lesson plus independent teacher helps and commentary. Usually the most fetchable |
| Adult Bible Study Guide (`absg.adventist.org`) | HTML / PDF | The official General Conference edition |
| Adventech Sabbath School apps | App / API backend | Powers the mobile apps; reachability from a script varies |
| Local conference or division | PDF | The usual path for Indonesian editions |

**If none of these can be read, ask the user to paste the lesson.** Do not reconstruct a week from its title. A quarterly title tells you almost nothing about which passages the five days actually treat, and a guide built on a guess fails in front of the class.

Minimum needed before writing a guide: lesson title, Memory Text, Read-for-This-Week list, the five daily section titles with their passages, and the three Friday discussion questions.

---

## The Class Hour Around the Lesson

The lesson study is one part of the Sabbath School program, and knowing the surrounding blocks keeps the timing honest.

| Block | Typical minutes | Note |
|---|---|---|
| Song service, welcome, opening prayer | 10–15 | Congregational, before classes break out |
| Mission spotlight / mission story | 3–5 | Sometimes read in class, sometimes from the front |
| Superintendent's remarks, announcements | 3–8 | The block that runs long and eats the lesson |
| **Lesson study in class** | **30–40** | What this skill plans for |
| Closing | 2–3 | |

Plan the discussion for the shorter figure. The lesson study is the block that absorbs every overrun ahead of it.
