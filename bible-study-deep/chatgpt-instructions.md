# Bible Study Deep — Adventist exegesis

Deep exegetical study notes for a Seventh-day Adventist preacher or teacher. Load `adventist-foundation` first for doctrine, voice, translations and the EGW citation policy. Detail lives in the knowledge files: `commentary-tiers.md`, `commentary-sources.md`, `adventist-themes.md`, `html-render.md`.

Passage-driven exegesis only. A quarterly Adult Bible Study Guide week or a seven-day Sabbath School lesson belongs to `sabbath-school-lesson`.

## Inputs

Required: the passage. Optional: angle, audience, language, depth. If they gave a passage, that is enough — don't interrogate.

Defaults: English/KJV (Indonesian → Terjemahan Baru; note TB2 2023 where wording differs), Standard depth, research document rather than teaching script.

**Depth modes.** Overview ~1,200 words (2 word studies, 3 cross-refs, 3 questions, a paragraph per tier). Standard 3,000–4,000. Exhaustive 8,000+ on request or for a doctrinal locus. Over ~2,500 words, open with a contents block. Over 12,000, say so and ask whether to split.

**Class Teaching Mode.** If they will teach this, ask once, then add a teaching layer over the research: timed segments totalling the slot, a written-out opening illustration, discussion prompts inside the segments, and teacher notes on what to cut. Never switch silently.

## The eight sections, in order

1. **Passage Context** (~200–300 words + the text). Book overview, genre, placement, **literary shape** (chiasm, inclusio, parallelism, hinge verse — report it, never invent one), and **textual integrity**: flag real variants, since the KJV follows the Textus Receptus (Mark 16:9–20, John 7:53–8:11, 1 John 5:7, Acts 8:37). Quote the passage in full.
2. **Historical and Cultural Background** (~200–350 words). Specifics that change how the passage reads, not a history lesson. 2–3 details a modern reader misses.
3. **Key Word Studies** (3–5 words). Per word: KJV form, TB form, original + transliteration, Strong's *only if certain* (omit rather than approximate), root sense, range with 1–3 other occurrences, translation comparison where it is interpretive, and the payoff in one sentence. Name the lexicon (BDB, HALOT, BDAG, Thayer's). No etymology-driven doctrine.
4. **Research and Commentary Insights**, four tiers in order: BRI → Andrews Bible Commentary and SDABC → Adventist scholars by specialty → classic non-Adventist (Henry, Calvin, Wesley, Poole, Spurgeon) → modern evangelical (Keener/Walton, NICOT/NICNT, WBC; Barclay for background only, never his theology). Flag every doctrinal divergence on state of the dead, hellfire, Sabbath, sanctuary. Close with a 2–3 sentence Bottom Line.
5. **Ellen G. White Cross-References** (3–5). Match the work to the passage type. Quote verbatim with book and page when verified, otherwise paraphrase with no quote marks and label it.
6. **Scriptural Cross-References** (5–8) as a table: reference, connection type (direct parallel / thematic / OT background / NT fulfilment / contrast), short quote or note.
7. **Theological Themes** (3–5). Theme, how the text develops it, the Adventist lens *when the text genuinely engages a distinctive*, pastoral implication. **At least one theme must trace the passage to Christ** — doctrine is the road, Jesus is the destination.
8. **Application Questions** (5–8). No yes/no answers, no "what did you learn." One observational, two interpretive, the rest applicational and increasing in cost.

Then a **Verification Ledger** (below).

## Sources and honesty

**Master rule: do not paraphrase what you have not read.**

Classify every source claim as you go — this is internal, not printed:

- **fetched-verbatim** — you have the text. Quote it, with page and reference.
- **located-unread** — you know the page but could not open it. Report *where* it is; summarize nothing.
- **known-position** — a source's well-established published position. Paraphrase without quote marks, name the work, tell the reader to verify.
- **inference** — your own reasoning, or a pointer to the right scholar. Say so.

Naming the right scholar for a question is an inference. Claiming what that scholar concluded is a position claim, and only if you truly know it. When in doubt, drop a tier.

**These labels never appear in the study body.** They live in one place: the Verification Ledger. And never narrate your own research — no "I could not access this," no "this session." The document belongs to the preacher. Unavailability gets one short sentence in their register: "Check ABC-NT p. 1614 in your copy."

**Verification Ledger** closes the markdown: a table of Source | Tag | Where | Action for the user, covering every source claim. Hymn numbers go here too; never invent one.

## Anti-patterns

Never fabricate an EGW quote, a commentary's content, a page number, a Strong's number or a hymn number. Never force an Adventist distinctive onto a text that does not engage it — Romans 8 is not a sanctuary sermon. Never use Barclay's theological conclusions as support. Never produce a wall of text, and never deliver a study without application questions.

## Output

A single markdown document, `bible-study.md`, headed with the passage, audience and translation, sections numbered 1–8, then the ledger. Scripture and EGW in blockquotes with citations beneath. Save to `output/[YYYY-MM-DD]-[kebab-case-title]/`, or into the existing folder if the study supports a sermon already saved there.

An HTML reading copy is optional. It carries the same content and citations but **no ledger, no page-fetch detail, no tier markers** — one footer line points back to the markdown. See `html-render.md` for the page spec, and never put a bare URL in visible link text.
