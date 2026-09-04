# Map: Sabbath School methodology that serves the listener

Label: `wayfinder:map`

## Destination

`sabbath-school-lesson` adapts its facilitation to the **congregation profile** it is being
taught to, and its questions **teach the lesson to a class that has not read it**. Reached when
`SKILL.md` and `references/` are changed in place so next week's generated guide differs by
profile and no longer assumes prior reading.

## Notes

- **Domain:** Seventh-day Adventist Sabbath School teaching. The lesson is fixed church-wide by
  the quarterly; only the teaching of it is ours to design.
- **Skills every session should consult:** `adventist-foundation` (voice, banned phrases, EGW
  citation policy), `grilling` + `domain-modeling` by default.
- **Execution override:** this effort **applies** its decisions, it does not only decide them.
  Wayfinder's plan-only default is deliberately overridden (Q9).
- **Standing constraints discovered while charting:**
  - The Adventech API returns its **HTML app shell with HTTP 200** for a language/quarterly
    combination that does not exist. Never test existence by status code; parse the payload.
    An Easy Reading edition exists at `<lang>/quarterlies/<qid>-er` — in English only.
  - Eight numbered sections is a hard cap: the HTML colour ramp has eight verified steps. A
    ninth section is forbidden, so new material folds into an existing section.
  - Output is one bilingual page (ID + EN) driven by `:root[data-pagelang]`. Every new element
    needs both languages.
  - The teacher serves a **different congregation each week**, so nothing may assume continuity
    of people. The lesson, however, is globally sequential — continuity of *content* is real.

## Decisions so far

<!-- one line per closed ticket -->

- [Facilitating a young-adult Sabbath School class](issues/02-research-young-adult-facilitation.md)
  — SSNet publishes nothing of its own here; inVerse is the only primary source and its
  `/teach` page the only published young-adult SS facilitation guidance found. Published
  curriculum splits teens from young adults three ways, so Q10's collapse is a construction.
  Surfaced the appeal question.

- [Facilitating discussion in a deaf, signed Sabbath School class](issues/01-research-deaf-class-facilitation.md)
  — no Adventist source exists, so the subsection is ours. Turn-taking is gaze; refusing eye
  contact beats small groups for the dominant talker, and small groups have no evidence here.
  Attention is strictly sequential, so reading and signing never overlap — a constraint on order,
  not on the clock (see ticket 11, which corrected a later overreach on this). Silence survives
  but our 4–6s is borrowed. All evidence is ASL/NGT/BSL/Libras, none Bisindo.

- [The question form for a class that has not read the lesson](issues/04-content-carrying-questions.md)
  — named **the self-contained question**: setup states the fact, ask opens the judgment. Two
  sentences of fact, never the conclusion; a longer stretch allowed but capped at half a minute
  and never in the opening. Four tests became five. Applied to `SKILL.md` and
  `teaching-methods.md`. Lesson 9 already scored 7/8, so this named an existing practice rather
  than inventing one.

- [What actually differs per congregation profile](issues/03-profile-subsections.md) — split
  *dynamics* (situations, any room) from *profiles* (audiences), then wrote six: adults as the
  named baseline, young adults, deaf-signed, seeker, baptismal, and members-mixed-with-seekers.
  One primary profile plus a bounded overlap block. Absorbed the duplicated seeker advice and
  fixed a universal small-groups recommendation the deaf research contradicts.

- [Wire the profile through generation so it cannot be ignored](issues/07-wire-profile-into-generation.md)
  — the collect-and-discard defect is closed. Six-profile enum at Step 1, a `.profile` block
  emitted first in Section 3 (before the hook, which is itself profile-dependent), techelet
  chip in the template, markup contract row, Final Pass item 12, and an anti-pattern against
  collecting inputs the output ignores.

- [The timed plan when attention is sequential](issues/11-deaf-timing-variant.md) — the premise
  was my own error. A signed class reads off a screen at about the rate a hearing class reads
  aloud, and the standard plan already budgets for reading, so there is **no seven-minute cost and
  no lost question**; the 35-minute plan runs unchanged and only the order differs. This dissolves
  the Q6 contradiction the test claimed. The read-aloud rule is now about the source, not the
  channel. And the class reads screen prose comfortably, which widens the teacher's options.

- [Simplified Indonesian register](issues/10-simplified-indonesian-register.md) — write so a
  twelve-year-old could **read** it, never as though one were **thinking**: doctrine, weight and
  cost unchanged, sentences changed. Seven rules ported from the church's own Easy Reading edition;
  the eighth (swap the Bible translation) does not port, so Terjemahan Baru stays unparaphrased
  with hard words glossed after the verse. Adventist vocabulary is the highest-risk category and
  gets an in-line gloss at first use. This profile changes the prose of the **whole** guide.

- [The two listener-facing moves](issues/05-listener-facing-moves.md) — both already existed. The
  two-minute line **was** the take-home; the chip was doing two jobs because Step 8 told it to put
  stage direction in the same slot. Renamed rather than rebuilt, so every guide already written
  gains it; stage direction gets its own quieter `.howto` chip. The weekly challenge folds into the
  application block rather than becoming a third statement of one instruction. Q14's quote-first
  rule is reversed: the take-home is the teacher's own sentence, governed by a shape rule — name
  what the passage does, then turn it, and never tell the member how to feel.

## Not yet specified

- **A listener-facing artifact.** A page or handout the member reads themselves. Held as fog
  deliberately: the diagnosis (Q2) is that members do not read what they already have, so
  adding a second thing to not-read needs evidence first. Revisit once the methodology changes
  have been taught at least once.
- **Whether the profile treatment should propagate** to `bible-study-deep`, `sermon-adventist`
  and `sermon-illustrations`, which have the same teacher-only skew (listener 2, student 1
  mentions across all five skills).
- **Two publisher-blocked sources worth one browser retry**: a Cogent Education 2023 study on
  deaf teaching strategies in Jakarta special schools, and the unverified figure that Indonesian
  deaf 17–18-year-olds write at a hearing 9–10-year-old level.
- **Section 4 may be profile-sensitive after all.** Q6 scoped the day map as invariant, but its
  two-minute lines are written as *speech* and its illustrations carry imagery. A deaf class
  needs visual-only illustration with no sound imagery, which makes those elements profile-
  dependent even though the exegesis is not. Surfaced by the Lesson 10 two-profile test.
- **Andrews University, *Sabbath School for the 70%*** (public-campus young adults). Exists but
  403s to every automated fetch. Worth one retry only if the campus or mixed-age case becomes
  central to a profile subsection.
- **Per-profile illustration sourcing.** A deaf class needs visual-only illustrations with no
  sound imagery; a young-adult class needs different reference points. This may be a
  `sermon-illustrations` concern rather than a Sabbath School one.

## Out of scope

- **A quality audit across all five skills.** A different effort with a different destination;
  ruled out while naming this one (Q4).
- **Rebuilding the retired student pipeline** (`create-lesson.mjs` + `lesson-data/`). Retiring
  it was correct: hand-authored JSON for two lessons does not scale against the Adventech API,
  and its one real feature (verse pop-ups) now lives in the teacher's guide. Only the two
  genuinely listener-facing moves it carried are being recovered, inside the guide (Q3).
