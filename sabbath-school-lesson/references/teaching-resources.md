# Sabbath School Teaching Resources

Reference for the `sabbath-school-lesson` skill. Where teaching helps come from, what each one is good for, and the one thing this guide has to do that none of them do.

**The premise: the teacher's guide already exists.** The official Adult Bible Study Guide ships a Teacher Comments section every week, and a healthy ecosystem publishes more every Monday. Writing another generic teacher's guide adds nothing. This skill earns its place only by going past what is already free.

---

## What the official Teacher Comments already does

**It is fetchable, through the API behind the official app.** Do not scrape [absg.sspmadventist.org](https://absg.sspmadventist.org/): it is a JavaScript shell that returns an empty page to any script. Use Adventech's Sabbath School API instead, which is what the official GC app runs on:

```bash
B=https://sabbath-school.adventech.io/api/v2/en/quarterlies/2026-03
curl -s "$B/lessons/06/days/teacher-comments/read/index.json"
```

Quarterly id is `YYYY-MM` with `MM` as the quarter's first month, so Q3 2026 is `2026-03`. Alongside the seven day ids for the week itself, each lesson exposes `teacher-comments`, `hope-ss` (the Hope Sabbath School outline) and `inside-story` (the mission story). Content comes back as HTML in a `content` field.

A second route, useful when you want the whole quarter at once: [fustero.es](https://www.fustero.es/index_en.php) hosts the quarterly as a PDF at `https://www.fustero.es/en_<year>t<quarter>.pdf`, so Q3 2026 is `en_2026t3.pdf`. Verified reachable; roughly 6 MB.

Its fixed shape:Its fixed shape:

| Part | Contains |
|---|---|
| **Key Text** and **Study Focus** | The verse and the week's passages |
| **Part I — Overview** | Lesson themes, what the week argues |
| **Part II — Commentary** | Two or three headed expositions of the main passages |
| **Part III — Life Application** | Discussion and activity suggestions |

Older editions also stated objectives as **Know / Feel / Do**, which is still the sharpest target a single teacher can carry into a room.

### Where it stops, and why

None of the following is a criticism of the writers. It is a structural consequence of what the document is: written a year or more ahead, by one author, for every Sabbath School class on earth.

| The official comments cannot know | So the guide must supply |
|---|---|
| How many minutes you actually get | A timed plan that survives losing five minutes |
| Who is in your room | Visitors present, seekers, a dominant talker, mixed language |
| What *your* class will argue about | The predicted pushback, named, with an honest answer ready |
| Which day carries the weight for you | One weight-bearing day, chosen and defended |
| Where the lesson itself is thin | Said plainly, with how to teach the text without undermining the quarterly |
| Verse-level depth | SDABC verse by verse, word studies, BRI on contested points |
| Your language | Terjemahan Baru alongside the English, and quotes you can read aloud |

**That gap is the whole product.** Before writing, state to yourself in one sentence what this guide gives that the official Teacher Comments does not. If the answer is "the same thing, reworded," stop and go deeper instead.

---

## Weekly helps published for every lesson

[Sabbath School Net](https://ssnet.org/) is the densest single stop. Its [Adult Teacher Resources](https://ssnet.org/study-guides/adult-teacher-resources/) index and its [teacher-aids feed](https://ssnet.org/blog/category/teacher-aids/) carry recurring columns, published per lesson, each by a named author:

| Column | What it gives | Author |
|---|---|---|
| **Teaching Outline** | A full outline for the class hour | Bruce Cameron |
| **Teaching Plan** | Key texts plus study questions, structured | William Earnhardt |
| **Discussion Starters** | Question prompts to open the room | Robert Nohr |
| **Singing with Inspiration** | Hymns tied to the week's themes | Corinne Knopper |
| **Weekly Teaching Ideas and Outlines** | Sample outlines for a *shorter* and a *longer* class | ssnet |

The shorter/longer pair is worth reading even when you do not use it: it shows what gets cut first when the class hour is eaten, which is exactly the judgment a timed plan has to make.

Also on ssnet: **Keys to Sabbath School Teaching**, a downloadable compilation of Ellen G. White counsels aimed specifically at Sabbath School teachers.

*The column names and authors above were read from the teacher-aids index. Confirm the current week's post actually exists before citing it; a column can skip a week.*

---

## Video: where the depth is

Video walkthroughs routinely go deeper than any printed help, and a transcript is searchable in a way a video is not.

| Source | Shape | Best for |
|---|---|---|
| **Deep Made Simple** ([channel](https://www.youtube.com/@deepmadesimple/videos)) | ~30–40 min per lesson, plain explanation | Depth and clarity on the passage itself. The reason to reach for video at all |
| **Hope Sabbath School** ([Hope Channel](https://hopetv.org/shows/hopess)) | Hour-long real class, Derek Morris facilitating | **Watching facilitation done well.** Downloadable PDF outlines. Study this for *how to run a room*, not only for content |
| **Sabbath School University** | Half-hour, young-adult register | A different audience's angle on the same week |
| **Hit the Mark** and **It Is Written** panels (embedded on ssnet) | Panel discussion, sometimes with the lesson author | Hearing the disagreements out loud, and occasionally the author's own intent |

### Pulling a transcript

`yt-dlp` is available on this machine and is the right tool:

```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download \
       --output '%(title)s' 'https://www.youtube.com/watch?v=VIDEO_ID'
```

Then convert the `.vtt` to prose and save it beside the study as `transcript.md`, with a header naming channel, video URL, publish date, length, and passage.

**Auto-captions are not the presenter's script.** They carry no punctuation of their own, they mis-hear proper nouns, and they will happily turn a name into a common word. So:

- Treat a transcript as `located-unread`'s more useful cousin: good enough to know *what was argued*, not good enough to quote verbatim.
- Never put a presenter's words in quotation marks from auto-captions. Paraphrase, and say the paraphrase came from the video.
- Never attribute a doctrinal position to a presenter on caption evidence alone. Watch the passage if it matters.
- A vivid phrase from a video is usually the presenter's illustration, not the passage's meaning. Do not let it become the guide's exegesis.

---

## Method, not content

Three sources on *how to teach*, worth reading once and applying every week:

- **Ellen G. White's counsels to Sabbath School teachers** (ssnet's "Keys to Sabbath School Teaching" compilation).
- **Howard Hendricks, _Teaching to Change Lives_** and **Bruce Wilkinson, _The Seven Laws of the Learner_**, both recommended by ssnet. Their common thesis matches this skill's: the teacher's job is to make the learner do the work.
- ssnet's own summary of the discipline: **guide the discussion, give the class something to talk about, and do not lecture.**

### Study the lesson three times

The best single piece of preparation advice in the ecosystem, and it maps directly onto this skill's steps:

1. **First read for yourself.** What does this text do to *you*? Skip this and the class hears a report, not a witness.
2. **Second read for the one point.** What is the single thing this class must not leave without? That becomes the weight-bearing day.
3. **Third read for the questions.** Build questions that let the class arrive where you arrived, instead of being told where you arrived.

---

## Source order for a guide

1. **The official lesson** for that week. Non-negotiable input; never reconstructed.
2. **The official Teacher Comments.** Read to know what is already covered, so the guide can aim past it.
3. **Exegesis:** SDABC verse by verse, Andrews Bible Commentary, BRI on anything contested, Ellen G. White, named Adventist scholars. This is where the depth actually comes from.
4. **Weekly helps** from ssnet's named columns, for outlines, discussion starters, and hymn suggestions.
5. **Video walkthroughs** for depth and for watching facilitation, transcript pulled and treated as paraphrase-only.
6. **Method sources** for how the hour is run.

Hymn numbers get looked up in the Lagu Sion database, never recalled from memory, whichever column suggested them.
