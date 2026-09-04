# Facilitating a young-adult Sabbath School class — what the published Adventist material actually does

Research for issue `02-research-young-adult-facilitation.md`. Retrieved 4 September 2026.

Everything below is *what a source does or says*, not a recommendation. Denominational status is marked
on each source. Where something is not documented, it says so.

---

## Source inventory and status

| Source | Publisher | Status |
|---|---|---|
| **inVerse Young Adult Bible Study Guide** — <https://inverse.sspmadventist.org/> | GC Sabbath School & Personal Ministries Dept (SSPM) | Official denominational curriculum |
| **inVerse "For InVerse Teachers" page** — <https://inverse.sspmadventist.org/teach> | GC SSPM | Official, and the only published young-adult SS *facilitation* page found |
| **Cornerstone Connections** (student + Teacher's Guide) — <https://www.cornerstoneconnections.net/> | GC Sabbath School Dept, printed by Review & Herald / Pacific Press, ISSN 0742-8685 | Official denominational curriculum for teens |
| **Sabbath School Net** young-adult page — <https://ssnet.org/collegiate-young-adult/> | Independent supporting ministry (states it is not responsible for InVerse content) | **Not** denominational |
| Sabbath School app API (mirrors the official quarterlies) — `https://sabbath-school.adventech.io/api/v2/en/…` | Adventech, carries GC content | Delivery channel for the official text |
| *Sabbath School for the 70%* (public-campus young adults), Andrews CYE | Andrews University | **Could not retrieve** — digitalcommons.andrews.edu returns 403 to every fetch method tried |

Note on access: `ssnet.org` blocks direct fetching (Wordfence 403); its pages were read through a text-extraction
proxy. Content quoted from it is from the live page.

---

## 1. What Sabbath School Net's "collegiate / young adult" area actually is

**It does not publish young-adult weekly material of its own.** The page at
<https://ssnet.org/collegiate-young-adult/> is a link list, nothing more: inVerse home page, the current inVerse
lesson series, inVerse daily podcasts ("typically less than 4 minutes long"), the Hope Channel inVerse programme,
and young-adult mission links. It states plainly that the Collegiate Lesson Study was discontinued and replaced
by inVerse, and that inVerse is not an SSNet site.

This matters for the ticket's premise: SSNet has an *adult* house style (its weekly Discussion Starters,
Teaching Outlines, Hit the Mark, etc. all appear under the Adult SS menu), but it has **no separate young-adult
question style to characterise**. Anything about young-adult question style has to come from inVerse itself.

The announcement post confirming the switch: <https://ssnet.org/blog/collegiate-lesson-study-in-now-inverse-bible-study/>
(dated 17 October 2019).

---

## 2. inVerse: the actual published young-adult material

### Audience, stated explicitly

SSPM's own front page says inVerse is designed for **young adults ages 19–35**, for personal study *and* for
Sabbath School and Bible study groups (<https://inverse.sspmadventist.org/>). That age band is a published
denominational fact, not an inference.

### The seven-day structure — one passage, seven passes

Every inVerse week runs the same seven named days over **one passage**, not seven topics
(verified against the live 2026 Q3 quarterly *The Closing Scenes* and 2026 Q1 *Apologetics: Mars Hill*
via the Sabbath School API):

| Day | Name | What it does |
|---|---|---|
| 1 | **inTro** | A first-person narrative essay by the author, then **inScribe** — an instruction to *write the passage out by hand* and annotate it |
| 2 | **inGest** | Exposition of the passage's practical/contextual content, ending in two reflective prompts |
| 3 | **inTerpret** | The analytical/apologetic pass; also asks the student to memorise a passage |
| 4 | **inSpect** | A grid of cross-reference verses grouped under themes, to be studied against the main passage. Almost no prose |
| 5 | **inVite** | Reads the passage Christocentrically; closes with "Journal a personal prayer to God" |
| 6 | **inSight** | An Ellen G. White perspective on the passage. **Carries no discussion prompt at all** |
| 7 | **inQuire** | The discussion page (see below) |

The daily prompts are short, personal, and open. Real examples from 2026 Q3, lesson 7 (Gethsemane):
"In what ways do we fall asleep when Jesus needs us to be wide awake?"; and lesson 3:
"What misconceptions of the Father have you had, and how do Jesus' words help?"

Two observations about the question style, from reading four lessons across two quarters:

- **Almost every prompt is second-person and experiential** ("you", "your life", "have you ever"), and many are
  explicitly labelled *Personal reflection*. This is materially different from the Adult Bible Study Guide's
  Teachers Comments, which are addressed to the teacher about the class.
- **The interpretive question is asked of the student's own annotation, not of the teacher's outline.**
  The same prompt recurs weekly on inTerpret: what are your main takeaways, what questions emerge, what parts
  are difficult. The guide institutionalises "what parts are difficult" as a weekly, expected answer.

### inQuire is the teacher's page

The `/teach` page states that the inQuire page "has been enhanced to provide an organized outline of important
questions and key takeaways" for teachers and group leaders. Reading an actual inQuire day confirms the shape:

- Questions are grouped under **thematic sub-headings** within the week ("Understanding Christ's struggle",
  "The disciples asleep", "Arrest in the Garden") — i.e. the week is chunked into three or four movements,
  not thirteen days.
- Each question carries **its verse reference inline**.
- Interleaved among them, one *Personal reflection* question per movement — the costly one.
- The page ends with **"Key takeaways to remember"**: three declarative sentences the teacher can land on.
  This is the published equivalent of a one-sentence claim per section.

Example of the apologetics quarter's costly question, which pairs a doctrinal point with a personal one:
"Christ's repeated request for prayer shows personal vulnerability. How does this fit with the common view
that vulnerability is weakness?" (2026 Q3, lesson 7, inQuire).

### Pacing: the only published young-adult timing plan

<https://inverse.sspmadventist.org/teach> gives an explicit clock, and it is the single most useful document
found for this issue. Its shape:

| Block | Minutes | What the page says to do |
|---|---|---|
| Connect | 5 | Round the circle: a high point and a low point from the week. Mark birthdays, graduations, new jobs |
| Prayer | 5 | Take praises and requests, **name them in the prayer**, and text people during the week about them |
| Story | 5 | A mission video, *or* a church member telling **one** five-minute story — explicitly "not their whole testimony" |
| Bible study | 30 | The main event; the page insists the other blocks must never crowd it out |

Total 45 minutes, which is longer than the guide's 35-minute default. The 30-minute study block is close to
the guide's current weight-bearing allocation.

Inside the 30 minutes, the page prescribes: **prepare** (study until certain of the big idea); **intro** (open
with a story or a hard question, and — its words — let them wrestle with it rather than answering at the start);
**read the main passage** (give the context first "for guests and those that don't study the lesson", then
each person reads one or two verses **and may tap the next person if they don't want to read**); **ask questions
about the text** (from inQuire or your own); **summarise, appeal, and pray**.

Practices worth noting because they are concrete and denominationally published:
- **Consent-based reading aloud** (the tap-out). A named mechanic for not exposing a nervous or dyslexic reader.
- **Context first, for the sake of the person who didn't prepare** — stated as a routine, not a concession.
- **Handing the class over**: the page closes by telling teachers to involve young adults in teaching their own
  Sabbath School and give them real responsibility.

### Where inVerse's published stance conflicts with the guide's current rule

`teaching-methods.md` currently says: *"Do not appeal for a decision by pressure. Sabbath School is a study,
not an altar call."* The GC SSPM teacher page takes the opposite position and says so twice — that a teacher
should exhort as well as teach, and that without an appeal the lesson is unfinished. It also softens it: it
suggests an **open-ended** appeal, asking young adults what response *they* want to make.

This is a genuine, sourced disagreement with the house rule, not a nuance. Whatever the guide decides, it should
decide knowingly. (The page's own reasoning is 1 Timothy 6:2 plus Ellen White, *Counsels on Sabbath School Work*,
p. 165, which it quotes on drawing out the student's ability rather than imparting instruction.)

### Stance toward doubt

Two things are documented, and one is not.

**Documented — doubt is a scheduled topic, not an interruption.** Of the inVerse quarters visible in the API,
two per year follow the Adult Bible Study Guide's book study and two are young-adult topical quarters. The
topical ones have included:
- *Apologetics: Mars Hill* (2026 Q1) — thirteen weeks on skepticism, with lessons titled The Problem of Evil,
  Jesus and Hinduism / Buddhism / Islam, The Resurrection, The Bible, Hellfire, Doomsday Cults, Hope for
  Non-Christians. Its introduction says young adults stand at the crossroads of belief and skepticism, and
  lists "Addressing Doubts" as its first purpose.
- Earlier young-adult quarters listed by SSNet's summary of the change: basics of salvation, sexuality, purpose
  of education, stewardship for young adults, Sabbath issues for professionals, knowing God's will.

So the published denominational answer to "what do you do about doubt with young adults" is partly structural:
you give it a quarter of its own rather than handling it only as pushback in the room.

**Documented — the question style protects the doubter.** The recurring inTerpret prompt asks what parts are
difficult, every single week. The apologetics quarter asks students which evidence they find *weakest*, and
which parts of their own faith they feel unsure about. These are published prompts that make admitting
uncertainty the normal answer rather than the awkward one.

**Not documented.** No published inVerse or GC page found gives a teacher any procedure for handling a young
adult who *disagrees in the room* — no equivalent of the guide's "take it to the text, time-box it, don't fake
certainty." The `/teach` page's only nearby instruction is that answers should come from Scripture wherever
possible and that shallow or cliché answers do not work with young adults. Anything more specific than that
would be invention.

---

## 3. Is a 16-year-old and a 34-year-old one audience or two?

**In published curriculum, unambiguously two.** The GC publishes a ladder of separate products with stated
age bands:

| Guide | Ages | Publisher |
|---|---|---|
| RealTime Faith | 13–14 | GC (GraceLink) |
| **Cornerstone Connections** | **15–18** (site says "high school teens"; SSNet's youth page says 14–18) | GC Sabbath School Dept |
| **inVerse** | **19–35** | GC SSPM |

A 16-year-old's own published guide is Cornerstone Connections; a 34-year-old's is inVerse. There is no published
GC product that spans them, and no published GC guidance found on running a combined teens-and-thirties class.

**In published practice, combination is acknowledged only downward, and only by an independent site.**
SSNet's juniors/teens page notes that in smaller churches the 13–14 age group is usually combined with the
Junior group or with the Youth group (<https://ssnet.org/juniors-teens/>). That is the only statement found
anywhere about merging age divisions, it is from an independent ministry rather than the GC, and it is about
13–14-year-olds, not about teens sitting with thirty-somethings.

**Conclusion for the guide:** treating teens-through-thirties as one profile is a real-world necessity in small
and rotating congregations, but it has no published denominational model. Anything the guide says about it is
the guide's own construction and should be presented as such.

### What the teen material does differently, if a 16-year-old is in the room

The Cornerstone Connections Teacher's Guide (GC, quarterly, ISSN 0742-8685 — Q3 2026 examined in full) runs a
fixed structure that differs from inVerse in instructive ways:

*Preparing to Teach*: **I. Synopsis** (the teacher's own understanding), **II. Target** — the week's objective
split three ways as **Know / Feel / Respond**, **III. Explore** (usually the relevant Fundamental Belief quoted
in full).

*Teaching*: **I. Getting Started** (an activity from the student lesson, then a supplied illustration, with the
instruction to share it "in your own words"), **II. Teaching the Story** (Bridge to the Story → read *Into the
Story* → *Out of the Story for Teachers*, whose questions are often **physical annotation instructions**:
underline the warnings, circle the instructions, put a box around X → Sharing Context and Background),
**III. Closing** (an activity — e.g. rank eight items on a continuum of importance and defend the ranking —
then a written Summary the teacher paraphrases).

Three teen-specific mechanics worth borrowing knowingly:

1. **A stated affective target.** Know / Feel / Respond forces the teacher to name what the week should *feel*
   like, not only what it should teach.
2. **The debrief question is fixed.** The Teacher's Guide introduction names the key question to ask after the
   opening activity: why did you respond the way you did. It is a published, reusable second move.
3. **Ranking and continuum activities** instead of open discussion questions — a low-cost way to get a divided
   room to commit to a position before defending it.

**Rabbi 101** is a one-paragraph teaching tip printed in every weekly Teacher's Guide (archive:
<https://www.cornerstoneconnections.net/page2143>). Read across seven consecutive weeks of Q3 2026, its
recurring theme is *treat teens as near-adults*:

- Don't treat teens like children — in two or three years they will vote, marry, and leave home (L2).
- Critical Thinking Skills: give them autonomy, let them question and draw their own conclusions and grapple
  with issues "without threat of punishment or disapproval for a 'wrong answer'" (L6). This is the closest
  thing found in any GC publication to a published rule on handling disagreement with a young person.
- Show appreciation to the *group*, not the individual, because teens act out when singled out even for praise (L1).
- Speaking the Truth in Love: criticise the behaviour, never the person; be a "5-to-1" teacher (L7).
- Method tips: reenactment, mock trial, jigsawing the reading out to sub-groups, dioramas (L3, L4, L8).

Note the direction of the advice: the teen guide's worry is *humiliation*, and its remedy is autonomy and
group-level feedback. The young-adult guide's worry is *shallowness*, and its remedy is depth and an appeal.
A room holding both is being asked to satisfy both worries at once. No published source addresses that.

---

## 4. What is published on doubt and disagreement with young adults — and what is not

**Published, denominational:**
- inVerse gives doubt a whole quarter periodically (2026 Q1 apologetics) and asks weekly what parts of the
  passage are difficult. <https://inverse.sspmadventist.org/>
- inVerse's teacher page: open with a hard question and let them wrestle; answer from Scripture; do not give
  cliché answers. <https://inverse.sspmadventist.org/teach>
- Cornerstone Connections' Rabbi 101 (L6, Q3 2026): let teens question and reach their own conclusions without
  disapproval for a wrong answer.

**Published, but one author's opinion or independent commentary — mark as such if used:**
- *Ministry* and *Adventist Review* pieces on youth retention (e.g. "How Not to Keep Young Adults in the Church",
  Adventist Review; "Why young people are sticking with church", Ministry, March 2016;
  "Youth apostasy and recovery", Ministry, June 2002). These are bylined articles in denominational journals,
  which is not the same as departmental guidance. They are broadly consistent in saying churches should make
  room for questions, but they are opinion pieces and should be cited as authors' views, not as a house method.
- *Spectrum* items on young ex-Adventists are independent, not denominational.
- **Valuegenesis** (1990/2000/2010, NAD-commissioned research on Adventist academy youth) is real research and
  is denominationally sponsored, but it measures attitudes; it prescribes no facilitation method. Its most-cited
  finding in this area — that only around half of academy teens experienced their church as warm and caring, and
  fewer at ages 20–21 — is a diagnosis, not a technique.

**Not documented anywhere found:**
- Any GC procedure for a young adult who disagrees out loud in class.
- Any GC guidance on a mixed teen/adult young-adult class.
- Any published young-adult equivalent of the Adult Bible Study Guide's weekly Teachers Comments (inVerse's
  inQuire page is the substitute, and it is a question outline, not a teaching essay).
- Andrews University's *Sabbath School for the 70%* (public-campus young adults) — exists, could not be
  retrieved (403). Worth a second attempt if the mixed-age or campus case becomes load-bearing:
  <https://digitalcommons.andrews.edu/cgi/viewcontent.cgi?article=1043&context=cye-pubs>

---

## 5. What this suggests for `teaching-methods.md` (proposals, not findings)

Marked clearly as the researcher's synthesis. The sourced facts are above.

1. A young-adult profile section can be grounded in exactly two published documents: the inVerse `/teach` page
   and the Cornerstone Connections Teacher's Guide front matter. Both are quotable and denominational.
2. The most transferable inVerse mechanics: the 5/5/5/30 clock with the study block protected; consent-based
   reading aloud; context given before the passage for the person who did not prepare; a hard question posed at
   the open and deliberately left unanswered; three thematic movements per week rather than a day-by-day march;
   and a "key takeaways" landing of two or three declarative sentences.
3. The most transferable teen mechanics for a room that contains a sixteen-year-old: a Know/Feel/Respond target,
   the fixed debrief question ("why did you respond the way you did"), ranking/continuum activities, and
   group-level rather than individual praise.
4. The **appeal** question needs an explicit decision. GC SSPM says a young-adult Sabbath School lesson without
   an appeal is unfinished; the guide currently forbids pressure. An open-ended appeal — asking what response
   the person wants to make — is the form inVerse itself recommends and is compatible with the guide's rule
   against staging a decision. Whatever is chosen, cite the disagreement.
5. On the mixed-age question, the honest position is that the church publishes two products and no bridge.
   The guide can offer a construction, but should say it is one.

---

## Links

- inVerse (GC SSPM): <https://inverse.sspmadventist.org/>
- inVerse teacher page: <https://inverse.sspmadventist.org/teach>
- inVerse about (editors: Joe Reeves, Paige Swanson): <https://inverse.sspmadventist.org/about>
- Cornerstone Connections: <https://www.cornerstoneconnections.net/> · lessons + Teacher's Guide PDFs:
  <https://www.cornerstoneconnections.net/lessons> · Rabbi 101 archive:
  <https://www.cornerstoneconnections.net/page2143> · teaching teen SS:
  <https://www.cornerstoneconnections.net/page2099> · lesson anatomy:
  <https://www.cornerstoneconnections.net/page2118>
- RealTime Faith (13–14): <https://www.realtimefaith.net/>
- Sabbath School Net young adult: <https://ssnet.org/collegiate-young-adult/> · youth:
  <https://ssnet.org/youth-sabbath-school/> · juniors/teens: <https://ssnet.org/juniors-teens/>
- Sabbath School app API used to read the live inVerse text:
  `https://sabbath-school.adventech.io/api/v2/en/quarterlies/2026-03-cq/lessons/07/days/07/read/index.json`
  (quarterly ids ending `-cq` are inVerse, `-cc` Cornerstone Connections, `-rt` RealTime Faith)
- GC Sabbath School teacher training: <https://www.sabbathschoolpersonalministries.org/sabbath-school-teacher-training>
