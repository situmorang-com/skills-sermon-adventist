# Simplified Indonesian register, with no Indonesian Easy Reading to copy

Type: grilling
Status: resolved

## Question

The GC publishes an Easy Reading edition of the quarterly and it is fetchable from the API the
skill already uses (`en/quarterlies/<qid>-er`, verified). It is a worked model of what the
denomination itself considers appropriate simplification, and diffing it against the standard
edition yielded eight transformations: question before reference, one clause per sentence,
repeat the name instead of pronouns, replace Latinate and religious vocabulary, gloss proper
nouns in-line, strip idiom, switch to a simple-English Bible version, concretise the
application.

**It exists in English only.** No Indonesian Easy Reading quarterly exists for any quarter
2019–2026, and no simplified Indonesian Bible comparable to WE/ERV/EASY was found — so
transformation 7 does not port, and the other seven have to be applied by us in Indonesian
rather than copied.

Settle:

- Whether the deaf profile's guide is generated from the **Easy Reading** English edition rather
  than the standard one, given both are fetchable and ER is the denomination's own answer.
- What the Indonesian equivalents of the seven portable transformations are. Sentence length is
  not the lever — mean length barely moved, 14.2 to 11.8 words; the work is in the longest
  sentences and the vocabulary.
- What happens to Scripture. Terjemahan Baru is the house default and there is no simplified
  Indonesian Bible to switch to. Options: keep TB and gloss hard words, or gloss nothing and
  rely on the screen-read being collective.
- Whether simplified register is deaf-only or should also be offered for seeker classes, where
  the same access argument partly applies.

Frame it as language access, not cognitive capacity — see the rejected 2001 claim in ticket 01.

## Answer

**Target set by the user: write so a twelve-year-old could read it.** Resolved with one boundary
made explicit, because the request can be heard two ways and only one is right:

> Write so a twelve-year-old could **read** it. Do not write as though a twelve-year-old were
> **thinking**. The doctrine, the weight and the cost of the week stay exactly as they are.

That is not caution for its own sake. It is the denomination's own instruction — *"Do not treat
the deaf adult like a child"* (Evans & Jordan, 2016) — and the 2001 *Ministry* line about deaf
members finding abstraction difficult is contradicted both by the church's later material and by
the current literature. It is also what the GC's **Easy Reading edition** actually does: it
simplifies the language and leaves the theology alone.

**The reason is language, not capacity.** Written Indonesian is a **second language** to a Bisindo
signer, standing to their first language roughly as written English stands to an ASL signer, and
formal deaf education in Indonesia has largely run on SIBI, an artificial manual coding of spoken
Indonesian. The reported figure that Indonesian deaf 17–18-year-olds write at a hearing
nine-to-ten-year-old level is recorded as **unverified** — the source would not load — but the
direction is not in question.

**Seven rules ported from the Easy Reading diff**, and the diff's own lesson about which lever
matters: mean sentence length barely moves, 14.2 words to 11.8. **The control is vocabulary,
pronouns and ordering, not uniform shortening.** Question before reference; one clause per
sentence; repeat the name instead of a pronoun; replace Latinate vocabulary rather than defining
it; gloss in-line what cannot be replaced; remove idiom; concretise the application.

**Adventist in-group vocabulary is the highest-risk category** — simultaneously essential and
impossible to shorten away — so it is glossed in brackets at first use: *bait suci (rumah Allah di
Perjanjian Lama)*, *pengadilan pemeriksaan*, *Roh Nubuat (tulisan Ellen G. White)*.

**The eighth rule does not port, and the guide says so rather than pretending.** English Easy
Reading also swaps the Bible translation, to WE/NLV/ERV/EASY. There is no Indonesian Easy Reading
quarterly and no simplified Indonesian Bible, so **Terjemahan Baru stays and is never paraphrased**;
hard words get glossed after the verse instead of replaced inside it.

**A conflict found and resolved.** `Mixed-Language Classes` says an Adventist term may stay
Indonesian inside an English sentence and that this is normal register, not an error. True for
hearing bilinguals, **false for a signed class**, where an unglossed term is a barrier. Both
sections now point at each other.

**Applied:**

- New `### Simplified Indonesian for a signed class` in `teaching-methods.md`, with the seven
  rules, the Adventist-vocabulary rule, the unportable eighth, and a worked Indonesian
  before/after taken from the Lesson 10 guide.
- `SKILL.md` Step 7: for this profile the **whole guide's prose changes register**, not just
  Section 3. This is the one place a profile genuinely reaches past its own block, and it is prose
  rather than the plan table, so it does not reopen Q6 or ticket 11.
- Final Pass item 13 spot-checks three paragraphs from different sections, and explicitly fails a
  guide whose Section 3 is simplified and whose Section 6 is not.
- `teaching-deck.md`: slide text follows the same register, and since this class reads screen prose
  comfortably, a summary can be displayed rather than signed.

**Not done:** no guide has been generated in this register yet. The first real test is the next
Efata Tuli week, and the teacher's own read of the room outranks every source above — the research
found no documentation of this congregation, or of any Indonesian Adventist deaf congregation.
