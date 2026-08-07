**And check that similar titles are actually the same book.** Resolve the book id and read its catalogue record; do not reason from the title. A worked example from Q3 2026 lesson 6, where three items share a name and **none of them is what it looks like**:

| Book | Title | Author | Year |
|---|---|---|---|
| 1340, code SGL | *Spiritual Gifts* | **J. N. Loughborough** | 1899 |
| 104, code 1SG | *Spiritual Gifts, vol. 1* | Ellen G. White | 1858 |
| pp. 5–16 inside book 104 | *Spiritual Gifts* | **Roswell F. Cottrell** | — |

A quote fetched from 1340 is Loughborough's. The lesson's Friday reading is Cottrell's essay printed inside White's volume. Neither is Ellen White writing about spiritual gifts, and a guide that says "Ellen White says" over either one is wrong in front of a class that can check in a minute.

Getting this right took `GET /content/books/<id>` and reading the `author` field, which costs one call. Guessing cost two wrong attributions in a row: first "vol. 1," then "probably Cottrell." **When two references share a title, resolve every book id before writing any of them down.**

---
name: sabbath-school-lesson
description: Build a Seventh-day Adventist Sabbath School teacher's guide for a quarterly Adult Bible Study Guide lesson. The lesson itself is already written and used church-wide, so this skill never invents one: it locates the official lesson for a given Sabbath, then digs deeper through SDABC, Ellen G. White, the Biblical Research Institute and Adventist scholarship to build a guided study the teacher can run in about thirty-five minutes. Produces a markdown guide plus a readable HTML page, in English (KJV) or Indonesian (Terjemahan Baru), with a timed discussion plan, a day-by-day map carrying each day's own sources, the two questions worth real time, predicted pushback, and every Bible text in full. Use whenever the user is teaching or preparing a Sabbath School lesson, quarterly lesson, lesson study, Adult Bible Study Guide week, teachers guide, or class study plan, including Indonesian phrasings like pelajaran Sekolah Sabat, penuntun guru, pendalaman pekan ini, or when they say they are teaching the lesson this Sabbath.
---

# Sabbath School Lesson

Sabbath School is not a sermon with chairs in a circle. It is a *discussion* built on a text, run in about thirty-five minutes, in front of people who read the lesson (or did not) and who will talk if the questions are good and sit silent if they are not. This skill produces material for that room.

**Requires:** the `adventist-foundation` skill is loaded for doctrinal alignment, translation defaults, voice, banned phrases, and the Ellen G. White citation policy. Do not restate those rules here — apply them.

**Related skills:** `bible-study-deep` for the exegetical engine behind a lesson, `sermon-illustrations` for the opening hook, `sermon-adventist` when the ask is actually a sermon.

---

## The Lesson Is Already Written

Sabbath School follows the quarterly Adult Bible Study Guide, worldwide, every week. A local teacher does not write their own seven-day lesson; they teach the lesson the whole church is studying.

**So never ask the user for a theme.** There is no theme to choose. Which lesson falls on a given Sabbath is a fact to look up, not a decision to make, and asking for one signals that you do not understand how Sabbath School works.

The work is the other half: digging deeper than the quarterly page, through SDABC, Ellen G. White, the Biblical Research Institute and Adventist scholarship, and turning that into a guided study a teacher can actually run in thirty-five minutes.

| | |
|---|---|
| The ask sounds like | "I'm teaching this week's lesson" · "Help me teach lesson 6" · "penuntun guru untuk pelajaran pekan ini" · "buat pelajaran Sekolah Sabat" |
| You need | The actual lesson text. See Step 2 |
| You produce | `teachers-guide.md` + `teachers-guide.html` |
| Length | ~2,500–3,500 words across the eight sections; the appendices add whatever the sources require and are not counted against that |

**All the danger is in the input.** Everything downstream is built on the official lesson text, so a wrong or invented lesson poisons the whole guide. Never invent it. See Step 2.

**Working out which lesson.** A quarterly week is *read* across its printed date range and *discussed in class the following Sabbath*: the week printed "Aug 1–7" is taught on Sabbath Aug 8, which is why its Sabbath Afternoon section closes by pointing to that later date. So find the lesson whose date range *ends the day before* the Sabbath being taught. Do not assume the quarter starts on the first Sabbath of the month; Q3 2026 began June 27, which shifts every lesson number by one.

---

## Step 1: Capture inputs

One short conversational message. Skip anything already given.

| Field | Notes |
|---|---|
| **Language** | **Always ask.** English (KJV) / Indonesian (Terjemahan Baru) / bilingual |
| The lesson identity | Quarter, year, lesson number and title |
| Sabbath date being taught | Required, ISO `YYYY-MM-DD`. Drives the day headings and the folder name |
| Class profile | Adults, young adults, youth, seekers/baptismal class, mixed |
| Class size and talk culture | Affects question count and whether you plan small groups |
| Time available | Default 35 minutes of lesson study |
| Series context | Which quarter |

**Language is asked every time, not inherited.** A Sabbath School class often differs in language from the preacher's own default, and mixed-language congregations are normal. If the answer is bilingual, produce one document with the Indonesian section following each English section, never two half-documents.

Do not interrogate beyond the table. If the user named the Sabbath and the language, that is enough to go and find the lesson.

---

## Step 2: Get the actual lesson text. Do not proceed without it.

This is the failure point of the whole mode. A guide built on a guessed lesson is worse than no guide, because the teacher discovers the mismatch in front of the class.

**Fetch it from the Adventech API.** This is the backend the official GC Sabbath School app runs on, and it serves the whole lesson week as JSON. It is the reliable path, not a fallback:

```bash
B=https://sabbath-school.adventech.io/api/v2/en/quarterlies/2026-03
curl -s "$B/lessons/index.json"                        # 13 lessons with date ranges
curl -s "$B/lessons/06/index.json"                     # the day list for one lesson
curl -s "$B/lessons/06/days/01/read/index.json"        # Sabbath Afternoon
curl -s "$B/lessons/06/days/04/read/index.json"        # a weekday
curl -s "$B/lessons/06/days/07/read/index.json"        # Friday, Further Thought
```

Quarterly id is `YYYY-MM` with `MM` the quarter's first month, so Q3 2026 is `2026-03`. Days `01`–`07` are the week; each returns `{id, date, title, bible, content}` with `content` as HTML. Strip the tags. Day `01` carries the Read-for-This-Week list and the Memory Text; day `07` carries Further Thought and the discussion questions.

**Do not scrape `absg.sspmadventist.org`.** It is a JavaScript shell and returns an empty page to any script. The API serves the same official content.

Secondary sources, useful for cross-checking a date or a title:

- Sabbath School Net (`ssnet.org`) posts each week's lesson in plain HTML, at `/lessons/<yy><q>/less<NN>.html`
- `fustero.es/en_<year>t<quarter>.pdf` holds the whole quarter as a PDF
- For Indonesian, the local conference or division quarterly. The API's `id` language endpoint exists but did not carry this quarter, so check rather than assume

**Hard rule:** if you cannot read the lesson, say so in one sentence and ask the user to paste it. Do **not** reconstruct a lesson week from its title. Do **not** infer the daily sections from the quarter's theme. Do **not** produce a guide "based on what lesson 6 likely covers." A quarterly title tells you almost nothing about which passages the five days actually treat.

What you minimally need before writing: the lesson title, the Memory Text, the Read-for-This-Week list, the five daily section titles with their passages, and the three Friday discussion questions.

## Step 3: Gather the best of what already exists

**A good teacher's guide is a collection, not an invention.** The official Teacher Comments ships every week, ssnet publishes four named columns, video walkthroughs go deeper than either, and SDABC and Ellen G. White sit behind all of it. Every one of those is on the internet and none of them is in the room with the teacher on Sabbath morning.

**That is the job: bring the good material into one document the teacher can actually work from, credit it, and add what is missing.** Not "say something nobody else said." A teacher does not want novelty; they want everything worth knowing about this week in one place, organized for the clock.

So the test for including something is **not** "is this original?" It is:

1. **Is it good?** Then take it, and say whose it is.
2. **Does it help in the room?** A brilliant point that needs three screens of context is worse than a plain one the teacher can say out loud in ten seconds.
3. **Is it verified?** Attribution without checking is how a wrong name gets read aloud.

The one thing to refuse is **restating without adding and without crediting**. Copying the official commentary into your own words, unattributed, produces a document that is both derivative and dishonest. Taking the official's Greco-Roman background, naming it as theirs, and setting it next to SDABC's verse notes and a timed plan produces something none of the sources is: usable.

**The official Teacher Comments is fetchable, through the API that powers the official app.** Do not settle for asking the user to paste it, and do not scrape `absg.sspmadventist.org`: that site is a JavaScript shell and returns nothing.

```bash
B=https://sabbath-school.adventech.io/api/v2/en/quarterlies/2026-03
curl -s "$B/lessons/index.json"                              # 13 lessons, ids 01-13, with dates
curl -s "$B/lessons/06/index.json"                           # days for one lesson
curl -s "$B/lessons/06/days/teacher-comments/read/index.json"  # the official Teacher Comments
```

The quarterly id is `YYYY-MM` where `MM` is the quarter's first month: Q3 2026 is `2026-03`. The `days` list for a lesson holds `01`–`07` for the week itself, plus three extras worth knowing about:

| Day id | What it is |
|---|---|
| `teacher-comments` | **The official Teacher Comments.** Part I Overview, Part II Commentary, Part III Life Application |
| `hope-ss` | The Hope Sabbath School outline for that week |
| `inside-story` | The week's mission story |

Each returns `{id, date, title, bible, content}` with `content` as HTML. Strip the tags and read it.

Then answer this before writing, in one sentence:

> If a teacher had all of these open in tabs, what would my guide save them?

A good answer sounds like: *it puts the official's historical background next to the verse-level notes nobody publishes, in their language, on a clock that fits their class.* A bad answer is *it says the same things in different words* — that is the one failure mode, and it is a failure of assembly, not of originality.

**The gap the official leaves is structural, not a failing of the writers.** Written a year or more ahead, by one author, for every class on earth, it cannot know your clock, your room, what your class will argue about, which day carries the weight, or where the lesson is thin. It also stays shallow at verse level and is monolingual. Fill those, and keep everything good it does supply.

### Gather the weekly helps

Once the official comments are read, sweep the ecosystem. Full annotated list in `references/teaching-resources.md`; the short form:

- **[Sabbath School Net](https://ssnet.org/)** publishes named columns per lesson: Teaching Outline (Bruce Cameron), Teaching Plan (William Earnhardt), Discussion Starters (Robert Nohr), and Singing with Inspiration (Corinne Knopper) for hymns. Its shorter/longer sample outlines are worth reading for what gets cut first when the hour is eaten.
- **Video walkthroughs go deeper than any printed help.** Deep Made Simple for depth on the passage; **Hope Sabbath School for watching facilitation done well**, which is the harder half of teaching and the one no written help conveys.
- Pull a transcript with `yt-dlp --write-auto-sub --sub-lang en --skip-download`, save it beside the guide as `transcript.md`, and treat it as **paraphrase-only**: auto-captions mis-hear names and carry no punctuation, so never quote a presenter verbatim from them and never pin a doctrinal position on caption evidence.

**Depth still comes from the primary sources,** not from the helps. SDABC verse by verse, BRI on contested points, Ellen G. White, named scholars. The helps tell you what has already been said and show you how others run the hour; they are not a substitute for reading the text.

### Study the lesson three times

The ecosystem's own best advice, and it maps onto the steps that follow:

1. **For yourself.** What does this text do to you? Skip this and the class hears a report, not a witness.
2. **For the one point.** What must this class not leave without? That becomes the weight-bearing day in Step 6.
3. **For the questions.** Build questions that let the class arrive where you arrived, rather than being told.

---

## Step 4: Read the lesson as a teacher, not a reader

Before planning, answer these for yourself:

- **What is this week actually arguing?** Often not what the title says.
- **Which day carries the weight?** Usually one of the five does; the others support it. Teach that one properly and let the others move.
- **Where is the lesson thin?** A day that asserts something the text does not quite say, or skips the hard part of a passage. You will need to handle it honestly without undermining the quarterly in front of the class.
- **What will the class push back on?** Name it in advance. Every class has one member who has been waiting all week to raise it.
- **Which distinctive is in play?** And is the lesson engaging it or gliding past it?

## Step 5: Write `teachers-guide.md`

**This structure is fixed. Eight numbered sections, two appendices, the ledger.** Do not improvise a different shape per lesson: the teacher learns where things live, and a guide they can navigate under time pressure beats a better-organized one they have to read. The section count is eight because the HTML render's verified colour ramp has eight steps. If a lesson seems to need a ninth section, fold two together rather than adding one.

```markdown
# Teacher's Guide: [Quarter Year], Lesson N, [Title]

**Sabbath:** [YYYY-MM-DD] · **Class:** [profile] · **Time:** [minutes]
**Lesson week:** [printed date range] (discussed in class on Sabbath, [date])
**Read for This Week's Study:** [the lesson's passage list]
**Memory Text, [ref]:** [quoted in full, blockquote]
**Key Text the class leaves holding, [ref]:** [quoted in full, blockquote]

## 1. What This Week Is Actually Arguing
[3–5 short paragraphs. The lesson's claim in your own words, the setting that
makes it land, and explicitly what the lesson is NOT saying. Close by naming
where the week is heading, which is often not what the title says.]

## 2. Objectives
[Know / Feel / Do table. The Do must be concrete enough to be declined.]

## 3. Discussion Plan, [N] Minutes
[The opening hook as an h3, then the timed table, then the closing as an h3.
Hook and closing belong here: they are the first 90 seconds and last 2 minutes
of this plan, not separate topics. State where to compress. Confirm in one line
that every day of the week is assigned to a block.]

## 4. Day-by-Day Map
[A summary table: day | title | passages | which block it lands in. Then one
subsection per day, Sunday through Thursday. See Step 8.]

## 5. The Two Questions Worth Real Time
[For each: the question as you will actually say it, why it matters, what
answers to expect, and how to keep it open when someone closes it with a
Sabbath-School answer.]

## 6. Background the Class Does Not Have
[2–3 items only, numbered. Each must change how a verse reads, not decorate it.
Word study, translation choice, historical detail, or the distinctive in play.]

## 7. Ellen G. White for This Week
[The assigned Friday reading, the paragraph worth reading aloud, and where to
stop reading. Attribution cautions go here, attached to the quote they concern.]

## 8. Handling the Hard Spots
[Each predicted pushback in the member's own words, then an honest answer from
Scripture. Include a "before class" note for anything the teacher must read
tonight. If the lesson is thin somewhere, say how to teach the text faithfully
without making the quarterly the problem.]

## Appendix A: Every Bible Text in [translation]
[See Step 9.]

## Appendix B: Ellen G. White, SDABC, and Adventist Sources
[See Step 9.]

## Verification Ledger
[Source | Tag | Where | Action for the user]
```

## Step 6: The timed discussion plan

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

## Step 7: Facilitation, not presentation

A teacher's guide that produces a monologue has failed regardless of its content quality. Build these in:

- **Someone else talks in the first two minutes.** A show of hands, a one-word answer around the circle, a question with an easy entry point. A class that stays silent for ten minutes has decided its role for the whole hour.
- **Plan the silence.** After a real question, four to six seconds of nothing is the question working. Note in the guide where to wait.
- **Read the passage aloud, from the Bible, every time.** Not from the lesson's paraphrase.
- **Have a plan for the dominant talker** and for the class that will not speak. Small groups of three for four minutes solves both, and belongs in the guide when the class profile calls for it.
- **Do not defend the quarterly.** If a day is weak, teach the text.
- **The teacher's own study is not the lesson.** Background goes in only where it changes a reading.

See `references/teaching-methods.md` for the fuller set: question sequencing, mixed-language classes, the mission story slot, seeker-present classes, and what to do when a doctrinal argument breaks out.

## Step 8: The day-by-day map (Section 4)

The teacher has read the lesson. What they lack is a per-day judgment of what matters and what can be dropped. Section 4 supplies exactly that, and it is the section they will actually use in the room.

Open with a scan table: day, title, passages, and **which block of the timed plan it lands in**. That last column is what makes the section operational rather than decorative, and building it will expose any day you failed to assign a slot. Every one of the five days must appear.

Then one subsection per day, Sunday through Thursday, each in this fixed shape:

| Part | What goes in it |
|---|---|
| **What this day is doing** | One line on its function in the week's argument. Not a summary of its content |
| **Points to hold** | 2–4 items. The unlocking background, the translation choice, the verse that is stronger than the class realizes, the caution where a popular reading is not demonstrated exegesis |
| **Quotes for this day** | **Every Ellen G. White, SDABC, commentary, and Adventist-research source that illuminates this day, all of them.** See below |
| **If you only have two minutes** | **The single sentence to say out loud.** For the surveyed days this is the whole treatment, so write it as speech, not as a note. For the two long blocks, write "You have ten minutes; this is the weight-bearing day" instead |
| **Spare question** | One question if the discussion stalls or runs short |

### Quotes go in the day they explain, never in a pile

**This is the rule that matters most in Section 4.** Do not collect Ellen G. White, SDABC, Matthew Henry, BRI, or Adventist scholarship into an appendix and leave the days bare. A teacher working Monday's block should find Monday's Ellen White paragraph in Monday, not three screens away. Every day gets a **"Kutipan untuk hari ini"** block carrying every source that illuminates *that day's passages*.

- **All of them, not one.** If four sources bear on Tuesday, print four. Picking a favourite and dropping the rest is the writer editing the teacher's options away. Where a day has more than three, open the block with one line on which to reach for first and which to keep in reserve.
- **Each quote earns a sentence of use.** Not "here is a quote" but what it does: which minute of the plan it belongs to, where to stop reading, what objection it answers, what it is *not* evidence for.
- **Keep the source's own colour.** Ellen G. White is `blockquote.egw`, gold. SDABC, Henry, BRI and scholarship are `blockquote.cited`, neutral. Gold is Spirit of Prophecy and nothing else, in a day card exactly as in a section.
- **Verbatim and paraphrase look different.** A fetched EGW paragraph goes in quotation marks in a bilingual card. An SDABC first-paragraph extraction rendered into Indonesian is a paraphrase: no quotation marks, and the note says it is a paraphrase and that the volume holds more.
- **Attribution cautions ride with their quote,** not in a distant section. The *Spiritual Gifts* attribution flag belongs directly under the *Spiritual Gifts* quote, in scarlet.
- **A day with no Ellen G. White is normal.** Say so in one line and let SDABC carry it. Do not stretch a quote from another chapter to cover a day it does not address.

What is left for Appendix B is the *apparatus*, not the quotes: which sources landed on which day, what could not be read, further reading, and links. And Section 7 keeps only what is genuinely week-level — the assigned Friday reading, the attribution caution, and how to read a quote aloud.

Two more rules for this section. **Cross-reference, do not repeat:** if a point already lives in Section 6 as background or Section 8 as a hard spot, point to it in one clause rather than restating it. And **the day titles are the lesson's, not yours.** If you are working from an English edition and writing in Indonesian, your translated titles are a convenience, so say so and tell the teacher to use the titles printed on their own lesson sheet.

## Step 9: The two appendices

A teacher mid-argument will not open ten browser tabs. Everything they might need to reach for goes at the bottom of the one document they already have open. Both appendices come after Section 8 and before the ledger.

### Appendix A: every Bible text, in full

Not references. **The actual verse text**, fetched and verbatim. A reference the teacher has to look up is a reference they will skip while someone is waiting for an answer.

Group by function, not by canonical order: memory and key text first, then the lesson's own chapters, then the parallel passages, then the doctrinal texts the hard spots depend on. Two presentation modes:

- **A continuous passage meant to be read aloud** goes as one block with inline verse numbers, unbroken by commentary. The teacher reads straight down it.
- **Scattered verses for reference** go in a two-column table, reference and text.

Fetch every verse. A Bible text site such as alkitab.mobi for Terjemahan Baru, or Blue Letter Bible / Bible Hub for KJV, one chapter per request. **Where a fetch returns a truncated verse, mark the cut with an ellipsis and log it as `located-unread`** rather than completing it from memory. Add one or two sentences of teaching note per group where the text itself carries an argument the teacher should point at, such as an inclusio or a list whose contents undercut the class's expectation.

If the guide's hard spots cite the tests of a prophet, or any other cluster of texts a member will dispute, **those go in Appendix A in full.** That is the cluster most likely to be needed and least likely to be looked up.

### Appendix B: Ellen G. White, SDABC, and Adventist sources

Everything the guide draws on, in one place, with provenance attached to each item rather than deferred to the ledger:

1. **Verified EGW quotes** with book, page, and a line saying which block of the plan each is used in. Keep the `para_id` in the markdown; it does not go into the HTML. For non-English output, the English is the verified text and any translation you supply is labelled a working translation, not a quote from a published edition.
2. **The assigned Friday reading**, plus any attribution caution attached directly to the quote it concerns.
3. **Further EGW reading.** Where SDABC supplies its own cross-reference list, you may pass it on, saying the page numbers come from SDABC rather than from your own check of each page.
4. **An SDABC table, verse by verse** — but only for the verses whose text you actually retrieved. A verse logged as fetched in an earlier study, whose content you do not have in front of you, is left out. Do not fill it in from what SDABC probably says.
5. **BRI and Adventist scholarship**, with live links, and the argument summarized well enough to use in the room.
6. **Pointers**, clearly labelled as pointers: the right scholar for a question is not a claim about their conclusion.

---

## Output Format

Markdown. Scripture in blockquotes with translation cited. EGW in blockquotes with full citation. Headings follow the quarterly's own conventions — day names as section headings, `Read [passage]` as a directive line, discussion questions numbered.

For Indonesian output, use the quarterly's Indonesian labels (Sabat Sore, Minggu, Senin, Ayat Hafalan, Pendalaman, Pertanyaan Diskusi). The full label table, including what to verify against a current Indonesian quarterly, is in `references/lesson-anatomy.md`.

The **markdown** guide ends with a **Verification Ledger**. The HTML render never carries one.

---

## Final Pass

Before delivering, check:

1. **Memory Text is verbatim** and the reference is right. Check it against a Bible text, not memory.
2. **Every EGW page range was fetched.** Any unverified range is replaced by a chapter title, or dropped.
3. **No fabricated lesson content.** Everything attributed to the quarterly is from the text you actually read.
4. **Questions pass the four tests in A5.** Count them. Delete the dead ones rather than rewriting them into life.
5. **No question is answered in the next sentence.**
7. **One day costs something.** Find it. If you cannot, the week is not finished.
8. **Word budgets hit** (A3), Indonesian not padded.
9. **No provenance tags, no HTTP codes, no "this session"** in any body text. Ledger only. **`para_id` goes in the markdown only, never in the HTML** — it is a re-fetch handle for desk work, and on the page it competes with the page number for the teacher's eye.
10. **AI-slop swept** per the foundation's banned list, both languages. No em dashes in output prose.
11. **Timed plan adds up**, the minutes are contiguous, **every day of the week is assigned to a block**, and application survives compression.
12. **Adventist lens honest** — engaged where the text engages it, absent where it does not.
13. **Eight numbered sections, in order**, then Appendix A, Appendix B, ledger last.
14. **Every verse in Appendix A was fetched**, and any truncated fetch is marked with an ellipsis and logged, not completed from memory.
15. **Appendix B's SDABC table lists only verses whose text you actually have.**
16. **`teachers-guide.html` rendered** from `references/teachers-guide-template.html`, and its checklist run.

Then deliver plainly:

> `teachers-guide.md` and `teachers-guide.html`, built on the lesson text you provided. Quotes sit in the day they explain. The 35-minute plan compresses at minutes 22–28 if the superintendent runs long.

---

## Save the Output

```
/Users/edmundsitumorang/DEV/skills-sermon-adventist/output/
└── [YYYY-MM-DD]-ss-[kebab-case-title]/
    ├── teachers-guide.md            (the workshop copy: ledger, para_id)
    └── teachers-guide.html          (the copy used in the room)
```

The `ss-` prefix is deliberate. A Sabbath School lesson and a sermon can fall on the same Sabbath and are different material, so they get different folders. Do not write Sabbath School files into a sermon folder.

`teachers-guide.html` is also what gets published to `ss.situmorang.com`; the folder name becomes the archive slug, with `-ss-` collapsed. See **Publish** below.

- Date is the Sabbath the lesson is taught, ISO `YYYY-MM-DD`.
- Title in kebab-case, keeping words like "God" and "Christ": lesson "The Call of Abraham" on 2026-08-15 → `2026-08-15-ss-the-call-of-abraham`.
- No date given: use the title alone and tell the user no date was recorded.
- Confirm the paths back to the user.

---

## HTML Render: `teachers-guide.html`

A teacher's guide is read at a table on Sabbath morning, often on a phone, often while someone is talking. Render an HTML copy beside the markdown every time, since the markdown is the workshop and the page is what actually gets used in the room.

**Start from `references/teachers-guide-template.html`.** Copy it and fill it in. Do not design a new page: the template shares its palette, measure, and type scale with `bible-study-deep`'s template, so a guide and a study read as one series. The whole stylesheet, the theme and mono toggles, the contents scroll-spy and the print rules are already in it.

The filename is deliberately not `html-template.html`. `scripts/build-dist.sh` flattens every skill's `references/` into a single `dist/*/knowledge/` folder, so two skills shipping the same filename would silently overwrite each other. Any new reference file in this collection needs a name unique across all five skills.

| | `teachers-guide.md` | `teachers-guide.html` |
|---|---|---|
| Read by | You, preparing and verifying | You, in the room |
| Verification Ledger | Yes | **No.** Removed entirely, like a Bible study render |
| `para_id` | Yes, everywhere it helps | **No. Nowhere** |
| HTTP codes, API and site names | Yes | Only where they tell the teacher something ("belum dibeli", "buka di browser"). Never as raw plumbing |
| Provenance tags | Ledger only | **None.** The distinction survives as plain words on the quote: "verbatim" versus "parafrase" |
| Verbatim vs paraphrase | Tagged in the ledger | Stated in each quote's note, in the day it sits in |
| Attribution cautions | Yes | Yes, in scarlet, attached to the quote they concern |

**The HTML carries no verification apparatus at all**, exactly as in `bible-study-deep`. I argued once that a teacher's guide should be the exception and keep the ledger, because someone about to read a quote aloud wants to know it is verified. That was wrong, for two reasons that only became clear once the page existed. First, the answer to "is this safe to quote" belongs *beside the quote* — which is what the day cards do: each source labelled verbatim or paraphrase, each caution riding with the quote it concerns. A ledger at the foot is a second, worse copy of that. Second, on a phone it is a long table nobody scrolls to mid-class. The markdown is the audit trail; the page is for the room.

**Same reasoning kills `para_id`.**

### Section and colour scheme

Eight numbered sections map to the eight verified ramp steps, `data-hue="1"` through `"8"`. The two appendices and the ledger sit **outside** the ramp as `<section class="sec apx">` with letter badges (A, B, ✓) in techelet. All sixteen ramp steps were contrast-checked on glass; **do not interpolate a ninth step by eye.** If the content wants a ninth section, fold two together.

### Markup contract

| Guide element | Markup |
|---|---|
| Numbered section | `<section class="sec" data-hue="N">` with `<h2 id="sN"><span class="num">N</span> Title</h2>` |
| Appendix or ledger | `<section class="sec apx">` with `<span class="num">A</span>` / `B` / `✓` |
| Header facts (Sabbath, time, class) | `<ul class="facts">` with `<span class="k">` label and `<span class="v">` value |
| Memory text, key text, readings | `<dl class="meta">` in the header |
| **The timed plan** | `<div class="tablewrap plan"><table class="plan-t">` — minutes in column 1. Add `class="key"` to the two weight-bearing rows and `class="cut"` to the row that gets dropped when time is short |
| A day in the day-by-day map | `<div class="day">` holding `<h3>`, `<p class="when">`, `<p class="refs">`, `<h4>` groups |
| "If you only have two minutes" | `<div class="twomin" data-label="2 menit">` — the most-used element on the page |
| Know / Feel / Do | `<ul class="objectives">` with `<span class="k">` |
| A question worth real time | `<div class="qbig">` with `<p class="ask">` for the question itself, `<h4>` for why / expect / keep-open |
| Predicted pushback and answer | `<div class="hard">` with `<p class="push">` for the objection |
| Read-this-tonight note | `<div class="tonight" data-label="Sebelum kelas">` |
| Scripture quote | `<blockquote class="scripture">` + `<p class="note">` with reference and translation |
| **Any English quotation** | `<div class="bq">` holding a `.tabs` pair and two `.lang` panes, `data-l="en"` and `data-l="id"`. **Never leave an English quotation monolingual.** See below |
| Ellen G. White quote | `<blockquote class="egw">` + `<p class="note">` with title and page, no `para_id`, inside the `en` pane |
| **A verse reference in prose** | `<a class="v" data-v="1Kor13:5,1Kor13:6,1Kor13:7" data-ref="1 Korintus 13:5-7">13:5-7</a>`. Every reference in sections 1–8 gets one. **The link text stays as the prose wrote it; `data-ref` is always the full canonical reference** |
| Other commentary | `<blockquote class="cited">` |
| Caution or attribution flag | `<div class="flag">` — scarlet, and the only scarlet on the page |
| Appendix passage read aloud | `<div class="passage">` with `<p><b>7</b> "…"</p>` per verse, inline numbers |
| Appendix scattered verses | `<div class="tablewrap"><table class="verses">` |
| Ledger | `<div class="tablewrap"><table class="ledger grid">` with tags in `<code>` |
| Any table at all | **Always** inside `<div class="tablewrap">` so it scrolls on a phone instead of breaking the page |

**Chip labels are language-aware.** The CSS defaults to English, and any `data-label` attribute overrides it. For Indonesian output set them: `data-label="Ayat Alkitab"`, `"Roh Nubuat"`, `"Komentar"`, `"Perhatian"`, `"2 menit"`, `"Sebelum kelas"`. Do not edit the CSS to change a label.

### Bilingual quotations — every English quote, no exceptions

An Indonesian class needs the Indonesian; the provenance discipline needs the English. So both ship in one card with tabs.

- **Tabs, not side by side.** An EGW paragraph runs 80–120 words. Two columns inside a 68ch measure gives each about 34 characters per line, far below the 50–75 band. Tabs keep the full measure for whichever pane is showing.
- **English is the default pane**, because it is the verified text. The Indonesian pane's chip reads `Terjemahan kerja` and its note says it is not from a published Indonesian edition. Never present a working translation as the quotation.
- **The `EN` button in the controls** cycles `EN → ID → EN+ID` and drives every card at once; a card's own tab click overrides it for that card only. The choice persists in `localStorage`.
- **Print shows both panes,** stacked, tabs hidden. A hidden tab must never vanish from paper.
- **No-JS default shows English.** Start from `.bq .lang[data-l="id"]{display:none}`, never from `display:none` on both panes, or a page with JavaScript off shows no quotations at all.

### Linking Ellen G. White readings

A "further reading" list without links is a list of homework the teacher will not do. Link every one, and link the **website, never a PDF**. The site jumps to an exact paragraph, its pagination matches the `hlm. 314` style of the references, and it does not ask someone on a phone to download several megabytes. A PDF only wins for offline use, which is not the case a guide is written for.

| Need | URL |
|---|---|
| A specific paragraph you hold the id for | `https://text.egwwritings.org/read/<book>.<para>` |
| A book to browse | `https://m.egwwritings.org/en/book/<book>/toc` |

The `para_id` you recorded in the markdown **is** the deep link: `127.1407` becomes `text.egwwritings.org/read/127.1407`. Putting it inside an `href` is not the same as printing it as visible apparatus, so this does not conflict with keeping `para_id` out of the HTML.

**You can resolve a page reference you never fetched.** Do not settle for linking a book's front matter because you only have "Ev 314". Full-text search is the wrong tool here — searching `"Ev 314"` returns pages that *cite* Ev 314, not the page itself. Use the API's structure instead, with the token from `egw-fetch.sh token`:

1. `GET /content/books/<book>/toc` returns every chapter with a `para_id` and a `refcode_short` such as `Ev 315`. Parse the trailing page number and pick the chapter with the greatest start page that is still less than or equal to your target.
2. `GET /content/books/<book>/content/<element>?limit=400&direction=down` from that chapter, where `<element>` is the `para_id` **with the book prefix stripped** — `30.1728` is requested as `1728`. Passing the dotted form 404s or silently returns page 1.
3. Walk the returned paragraphs for the first whose `refcode_short` page equals your target. Its `para_id` is your exact-page deep link.

That resolved all eight of SDABC's cross-references for 1 Corinthians 14:40 to the exact page. The verification is at the data level: the API reported `Ev 314.1` for paragraph `30.1728`, so the link is right regardless of whether you can open it from a script.

While you are in the TOC, **keep the chapter title and print it.** It tells the teacher what is about to open, and it sometimes reveals that a cross-reference is not where you assumed: SDABC's Ev 314 for a verse about orderly worship sits in "Baptism and Church Membership."

Two rules that are not optional:

- **Verify every book number, one at a time.** Do not infer them from a pattern. Search for the title and read the number out of a real URL.
- **Say which links are precise and which are not.** Label a paragraph link differently from a book link. If a reference genuinely cannot be resolved, say why rather than quietly linking the book and hoping.

**And check that similar titles are actually the same book.** `Spiritual Gifts, vol. 1` is book 104; a separate item titled `Spiritual Gifts` with refcode SGL is book 1340. A quote fetched from one of them is not evidence about the other. This exact trap cost a wrong citation in the Q3 2026 lesson 6 guide: a quote from SGL was written up as "vol. 1" because the quarterly's Friday reading happened to be vol. 1. If two references share a title, resolve both book numbers before you write either one down, and if you cannot establish they are the same text, say so in the guide rather than merging them.

### Clickable verse references

Every reference in sections 1–8 opens the verse in place, from data embedded in the page. No network.

- Emit `<a class="v" data-v="KEY[,KEY…]" data-ref="label">label</a>`. Keys are `BookChapter:Verse` with no spaces: `1Kor12:7`, `Ef4:13`, `Ul18:22`, `Why19:10`.
- Ship the text as `<script>window.__VERSES={"1Kor12:7":{"n":"7","t":"…"},…}</script>` immediately before the main script block.
- **Build that object from Appendix A rather than retyping the verses.** The appendix already holds every verse you fetched; parse it. Retyping is how a wrong word gets in.
- For a range, list every key in it. Keys with no stored text are fine: the popup shows what it has and appends a line telling the teacher to open their Bible. That is honest and better than a dead link.
- **A comma continues the chapter.** `1 Kor 14:5, 13, 26, 27` is four verses of chapter 14, not one verse followed by three stray numbers. `12:8-10, 28` is chapter 12 verses 8, 9, 10 and 28. Match the whole expression in **one** anchor and emit every key, or the comma tail silently drops out of the document. This is the single easiest thing to get wrong here, and it looks fine until someone reads the page. The pattern needs a repeating group: `(\d+):(\d+(?:-\d+)?(?:\s*,\s*\d+(?:-\d+)?)*)`.
- **Show the verse numbers so discontinuity is visible.** One popup for the whole list is right, but it must render `5` `13` `26` `27` as separate numbered verses, never as flowing text, or the reader assumes a continuous passage.
- **When the emitted set is smaller than the reference asks for**, pass a `data-note` saying only the fetched verses are shown. A popup that quietly displays 1 of 2 requested verses is worse than one that admits it.
- **`data-ref` is the popup's heading, so it must always be the full canonical reference**, even when the prose says only `13:5-7` or an abbreviation like `Rm 12:6-8`. A heading reading "13:5-7" with no book is useless to someone glancing at it mid-class. Derive it from the keys rather than from the matched text: first and last key give book, chapter, and the verse span. Book codes map to full Indonesian names — `1Kor` → 1 Korintus, `Ef` → Efesus, `Rm` → Roma, `1Ptr` → 1 Petrus, `Why` → Wahyu, `Ul` → Ulangan, `Yes` → Yesaya, `Mat` → Matius, `1Yoh` → 1 Yohanes. Leave the visible link text exactly as the sentence wrote it; only the heading expands.
- Desktop gets a centred modal, phone gets a bottom sheet. Escape, backdrop click, and the close button all dismiss; focus returns to the reference.

### Mobile and tablet

Three real ranges, not two. The tablet band must not fall through to the phone rules.

| Range | Behaviour |
|---|---|
| **≥1120px** | Sticky glass contents sidebar, full ramp spines |
| **721–1119px (tablet)** | Contents collapses to a `<details>`, measure capped at `min(68ch, 92vw)`, facts and objectives go three-up, wider gutters |
| **≤720px (phone)** | Verse popup becomes a bottom sheet, facts two-up, controls and tabs shrink, safe-area insets applied |
| **≤620px** | **The plan table and the verse tables stop being tables** and become stacked blocks. The timed plan is the most glanceable thing on the page and must never require horizontal scrolling |
| `hover:none` | Row hover removed, contents links get 44px targets, dotted underlines become solid |

Also required: `viewport-fit=cover` in the viewport meta, `env(safe-area-inset-*)` on the article and the controls, and a minimum 38–44px touch target on every button, tab, and contents link.

### Before you hand it over

1. Measure capped at `68ch`. No full-bleed text column.
2. Every table wrapped in `.tablewrap`.
3. Every contents link resolves to an `id` on the page.
4. The timed plan's minutes are contiguous and sum to the stated total.
5. Every day of the week appears in the day-by-day map.
6. **No ledger, no provenance tag, no HTTP code, no "this session"** anywhere in the file. **Zero `para_id`** — grep for it and expect no hits. In the ledger's "Where" column name the source system instead: `EGW Writings API`, `bibletools.info`, `alkitab.mobi`. The publish step's scrub stays as a safety net, but the render should never give it anything to remove.
7. Links show titles, not bare URLs.
8. Mono toggle leaves no colour behind: no hex values outside the theme blocks.
9. Reduced motion honoured; content still visible with reveals disabled.
10. Ordered lists count correctly. Markdown converters emit one `<ol>` per item, which restarts every list at "1." — merge them.
11. Scarlet appears only on cautions.
12. Tags balance and the file ends with `</html>`.
13. **Every English quotation is inside a `.bq` card with both panes.** Count them: `<blockquote class="egw">` should equal `class="bq"` times two.
14. **No nested anchors.** Check with `<a[ >][^>]*>(?:(?!</a>).)*<a[ >]` — note the space, or the pattern matches `<article>` and reports a false positive.
15. **Every `data-v` key resolves** or is knowingly absent; the popup must never open empty.
15b. **Every `data-ref` names its book.** A popup headed "13:5-7" tells the teacher nothing. Grep for `data-ref="[0-9]\+:` and expect no hits — note the colon: without it the pattern also matches the perfectly correct `1 Korintus` and `1 Petrus`, and you will chase 45 phantom failures. Same trap as `<a[^>]*>` matching `<article>`: when a check fires on everything, suspect the check.
16. **JavaScript parses.** Extract each `<script>` block and run `node --check`. The popup and both toggles are load-bearing now.
17. At ≤620px the plan table renders as stacked blocks, not a horizontal scroll.
18. **No Verification Ledger section, and no `#ledger` entry in the contents.** The footer points at the markdown for provenance instead.
19. **Every day in Section 4 carries its own "Kutipan untuk hari ini" block.** A day with sources available and none printed is a failure; a day whose sources were piled into an appendix instead is the same failure.

---

## Publish: `ss.situmorang.com`

The guide is a page before it is a file, so it can go on the web. `ss.situmorang.com` is a GitHub Pages site served from the public repo `situmorang-com/sabbath-school`. It is **not** on a VPS, and it needs no credentials beyond the `gh` login that is already in place.

Publishing needs `teachers-guide.html` to exist. Render it first — Final Pass item 16 — and run its checklist. There is nothing to publish from the markdown.

```sh
cd "/Users/edmundsitumorang/Library/Mobile Documents/iCloud~md~obsidian/Documents/BIBLE STUDY/200 Seedbox/ss"

# Always look before you ship.
node scripts/publish-guide.mjs \
  /Users/edmundsitumorang/DEV/skills-sermon-adventist/output/[YYYY-MM-DD]-ss-[slug]/teachers-guide.html \
  --dry-run

# Then publish.
node scripts/publish-guide.mjs \
  /Users/edmundsitumorang/DEV/skills-sermon-adventist/output/[YYYY-MM-DD]-ss-[slug]/teachers-guide.html
```

The script removes the Verification Ledger and its contents entry, appends the LAI attribution footer, writes the guide as both the homepage and `lessons/<slug>/`, rebuilds the archive index, commits, and pushes. Cautions stay — they are exactly what a teacher needs when deciding whether to read a quote aloud.

It also scrubs any `para_id` locator it finds, in both the `(para_id 127.1407)` and `, para_id 14192.30685` forms. That is a **safety net, not a licence**: per the render checklist the HTML should contain none to begin with. A `para_id` left in running prose is not scrubbed — the script aborts and shows you the sentence, because rewriting prose is your job, not the script's.

It refuses to run on a dirty tree or a branch behind origin, and aborts rather than publish if teacher-only material survives the strip. Republishing the same guide is a no-op. Pages caches for ten minutes, so the live page can lag the push.

**The site is public.** The ledger comes out automatically; nothing else does. A name from the class, a pastoral confidence, an unresolved attribution you were still arguing with — if it is in the guide, it is world-readable and indexable. Decide that before publishing, not after.

Ask before the first publish of a week. Do not publish a guide the user has not seen.

This step exists only in Claude Code. The `dist/` bundles for Claude Projects and ChatGPT ship without the script, so skip it there and hand over the files.

---

## Anti-Patterns

- **Never restate a source without crediting it, and never leave good material out just because someone else said it first.** Both are failures. The guide is a collection: take the official's best background, take ssnet's sharpest question, name whose they are, and set them beside the depth and the timed plan that nothing else supplies. Avoiding a point because it is not original serves the writer's vanity, not the teacher.
- **Never quote a video presenter verbatim from auto-captions.** They mis-hear names and carry no punctuation. Paraphrase, and say it came from the video.
- **Never ask the user for a theme.** Sabbath School has no theme to choose: the quarterly set it, church-wide. Asking for one shows you do not know how Sabbath School works. Find which lesson falls on that Sabbath instead.
- **Never reconstruct an official quarterly lesson you could not read.** The one unforgivable failure. Ask for a paste instead.
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
- `references/teaching-resources.md` — where teaching helps come from: what the official Teacher Comments covers and where it stops, ssnet's named weekly columns, video walkthroughs and how to transcribe them, method sources, and the source order for a guide
- `references/teaching-methods.md` — facilitation: question sequencing, timing variants, silence, dominant talkers, mixed-language and seeker-present classes, doctrinal arguments, the mission story slot
- `references/teachers-guide-template.html` — the `teachers-guide.html` skeleton: full stylesheet, theme and mono toggles, and markup examples for the plan table, day cards, two-minute callouts, question cards, hard spots, and appendix passages. Copy it rather than designing a new page
- `bible-study-deep/SKILL.md` — the exegetical engine and the provenance/ledger discipline this skill inherits
- `commentary-tiers.md` (ships with `bible-study-deep`) — commentary sources by tier, lexicons, cautions
- `adventist-themes.md`, `commentary-sources.md` (ship with `sermon-adventist`) — distinctives mapped to texts, and the Adventist source list
- `HOWTO_EGW_LaguSion.md` (ships with `sermon-adventist`) — operating the EGW API helper

---

**Why this works:** The quarterly format looks like a container for content. It is actually a container for *questions*, and the prose exists to make eight to twelve good questions possible. A lesson fails when the writer treats the daily sections as the deliverable and the questions as decoration. This skill inverts that: fix the spine, earn each day, and spend the real effort on the questions the class will still be arguing about in the parking lot.
