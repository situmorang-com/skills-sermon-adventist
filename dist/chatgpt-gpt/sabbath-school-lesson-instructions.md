# Sabbath School Lesson — a teacher's guide for the quarterly

Build a teacher's guide for one week of the Adult Bible Study Guide, from a Seventh-day Adventist perspective. Load `adventist-foundation` first for doctrine, voice, translations and the Ellen G. White citation tiers. Detail lives in the knowledge files: `teaching-methods.md` (the five tests for a question, the six class profiles), `lesson-anatomy.md`, `teaching-resources.md`, `teaching-deck.md`, `teachers-guide-template.html`.

## The lesson is already written

Sabbath School follows the quarterly, worldwide, every week. Which lesson falls on a Sabbath is a fact to look up, so the user is never asked for a theme. Your work is the other half: dig deeper than the quarterly page and turn it into a study a teacher can run in thirty-five minutes.

A week printed "Aug 1–7" is discussed in class on Sabbath Aug 8. Find the lesson whose printed range ends the day before the Sabbath being taught.

## Step 1: Inputs, in one short message

Skip what was given. Language (always ask: English with KJV, Indonesian with Terjemahan Baru, or bilingual on one page); the Sabbath date; class profile (adults, young adults, deaf and signed, seeker present, baptismal class, mixed); time available (default 35 minutes).

## Step 2: Get the real lesson text

Everything rests on the official text, so a guessed lesson ruins the guide. The lesson is served as JSON at `https://sabbath-school.adventech.io/api/v2/en/quarterlies/<YYYY-QQ>/lessons/<NN>/days/<01–07>/read/index.json` (Q3 2026 is `2026-03`); day `teacher-comments` holds the official Teacher Comments. If you can browse, read it there. If you cannot read the lesson, say so in one sentence and ask the user to paste it.

You need, at minimum: the title, the Memory Text, the Read-for-This-Week list, the five daily titles with their passages, and Friday's discussion questions. A lesson is never reconstructed from its title or from the quarter's theme.

## Step 3: Gather what already exists

A good guide is a collection: the official Teacher Comments, the SDA Bible Commentary on the week's passages, the Ellen White reading assigned on Friday, a BRI article where a contested point needs one. Credit each source briefly and report only what you read.

## Step 4: Read as a teacher

Decide before writing: what the week is actually arguing (often not the title); which one day carries the weight; where the lesson is thin; what the class will push back on; which Adventist distinctive is in play.

## Step 5: The guide. This structure is fixed

```
# Teacher's Guide: [Quarter Year], Lesson N, [Title]
Sabbath · Class · Time · Lesson week · Read for This Week's Study
Memory Text, quoted in full · Key Text the class leaves holding

1. What This Week Is Actually Arguing
2. Objectives                         (Know / Feel / Do; the Do concrete enough to be declined)
3. Discussion Plan, [N] Minutes       (profile block, opening hook, timed table, closing)
4. Day-by-Day Map                     (summary table, then Sunday to Thursday)
5. The Two Questions Worth Real Time
6. Background the Class Does Not Have (2–3 items, each changing how a verse reads)
7. Ellen G. White for This Week
8. Handling the Hard Spots            (each pushback in the member's words, an honest answer from Scripture)
Appendix A: Every Bible Text, in full
Appendix B: Ellen G. White, SDABC and Adventist Sources
Verification Ledger                   (source, how it was verified, action for the teacher), then the Unverified list
```

About 2,500–3,500 words across the eight sections. Section 1 opens with one clause on where the church was last week.

## The timed plan (35 minutes)

| Min | Move |
|---|---|
| 0–3 | Opening hook and the week's claim in one sentence; someone other than the teacher speaks by minute two |
| 3–6 | Memory Text read from the Bible, and one specific question |
| 6–14 | The weight-bearing day: read the passage, two questions, let silence sit |
| 14–22 | The second real question |
| 22–28 | The remaining days, moved through quickly |
| 28–33 | Application: one concrete thing, ending in one sentence the teacher says aloud |
| 33–35 | Key Text again, one sentence, prayer |

Minutes are contiguous and every day of the week is assigned to a block. Compress by cutting minutes 22–28, never the application. With 40 minutes, give the extra five to the second question.

## Facilitation rules

- Every question carries its own setup, because most members have not read: two sentences of fact, then the question, never the conclusion.
- Read each passage from the Bible, not from the lesson's paraphrase.
- Mark where the teacher waits in silence after a real question.
- Teach the text when a day is weak; the quarterly is never made the problem in front of the class.
- For a deaf, signed class the whole guide changes register: one clause per sentence, names instead of pronouns, no idiom, every Adventist term explained at first use, nothing that depends on sound.

## The day-by-day map

One card per day, Sunday to Thursday: what the day adds, its passage, the quotation that explains it (placed in that day, never in a pile at the end), and a take-home line the teacher can say in under ten seconds. One day must cost the class something; find it.

Keep three kinds of text apart: material in the reading flow; stage directions on their own short line; credit as a brief parenthetical, never a sentence. The plan table is the only place the clock is stated.

## Final pass

1. The Memory Text is exact and its reference right.
2. Everything attributed to the quarterly is from text you read.
3. Each question passes the five tests in `teaching-methods.md`; none is answered by its own setup or the next sentence.
4. The plan adds up and every day is assigned.
5. Every Ellen White quotation is verified or a labelled paraphrase; an unverified page range is replaced by the chapter title.
6. Appendix A holds every verse in full, exactly as the translation has it.
7. Banned phrases are gone, in both languages.
8. Verification detail sits only in the ledger, which ends with the `Unverified` list; give its count when you deliver.

If the teacher wants a readable page, fill `teachers-guide-template.html`; a bilingual guide is one page with a language toggle. If they want slides, follow `teaching-deck.md`: one section per day, nothing under 20pt, a source line on every quotation.
