# What actually differs per congregation profile

Type: grilling
Status: resolved
Blocked by: 01, 02

## Question

Write the six profile subsections into `references/teaching-methods.md`: **deaf**, **young
adults**, **adults**, **seeker**, **baptismal**, **mixed**.

The decision is not "write six sections" but **what genuinely differs**, so that each
subsection changes a teacher's behaviour rather than restating the general advice at a
different volume. Per Q6 the guide gets a generated per-profile section, so this file is its
source and must be specific enough to emit from.

For each profile settle: the hook that works and the hook that fails; whether the two big
questions change; illustration constraints; timing effects; and the failure mode peculiar to
that room.

Two existing sections, "The seeker or visitor present" and "The baptismal or seeker class",
already overlap the new seeker/baptismal profiles. Decide whether they are absorbed, rewritten,
or kept alongside — do not leave three overlapping treatments.

Note the constraint that a profile subsection must not silently duplicate the general
facilitation advice already in the file.

## Constraints from research

- **Young adults (from ticket 02).** Published curriculum splits this band three ways —
  RealTime Faith 13–14, Cornerstone Connections 15–18, inVerse 19–35 — with no published
  bridge. Q10 collapses teens into young adults; that is a construction and the subsection must
  say so rather than imply denominational backing. inVerse's stated band is 19–35.
- Draw on inVerse `/teach` for evidenced practice: consent-based reading aloud, context before
  passage for the unprepared (which corroborates ticket 04's mechanism from an independent
  source), open with a hard question and do not answer it.
- Handling a young adult who **disagrees out loud** is undocumented denominationally. Anything
  written there is ours, and must be labelled as ours.
- Cornerstone Connections' "Rabbi 101" is the closest published rule on disagreement: let teens
  question and reach their own conclusions without disapproval for a wrong answer.

## Constraints from research — deaf (ticket 01)

- **No Adventist source exists** for facilitating a deaf class. The subsection is ours, built on
  general deaf-education research, and must say so.
- **Turn-taking is gaze.** Arc sweep = everyone; gaze at one person = everyone else stands down.
  The teacher's eyes are the microphone.
- **Dominant talker: withhold eye contact to refuse a bid.** Documented, and quieter than the
  small groups the guide currently prescribes — for which there is **no evidence at all** in a
  signed class. Prefer the gaze move; do not assert small groups work here.
- **Silence: keep it, label the number as borrowed** from hearing-classroom research. Add the
  real difference — a signing teacher has no neutral place to put her eyes mid-pause.
- **Attention is sequential, never divided.** Read-slots and sign-slots must be separate blocks
  in the timed plan. This is a timing constraint, not a style note.
- **All evidence is ASL/NGT/BSL/Libras; nothing on Bisindo.** State that limit in the subsection.
- Register is handled separately in "Simplified Indonesian register".
- **Interaction with the self-contained question (ticket 04):** attention is sequential, so in a
  deaf class the setup and the ask cannot be signed while text is on the screen. The setup is
  part of the sign-slot, not the read-slot.

## Answer

**Structural finding the ticket did not anticipate:** `## Class Dynamics` conflated two kinds of
thing. A dominant talker and a silent class are *situations* that occur in any room; seeker and
baptismal are *audiences*. Split accordingly (Q19): `## Class Dynamics` keeps the two
situations, and a new `## Congregation Profiles` holds the six, absorbing the old seeker and
baptismal sections. That also removed the duplicate seeker advice the file already carried in
two places.

**Six profiles written**, each saying only what changes:

- **Adults** — deliberately thin, and named as the baseline the rest of the file is written for.
  Two differentiators confirmed as real (Q20): they have studied this cycle three or four times,
  so the enemy is recognition rather than comprehension; and officers in the room make being
  wrong publicly costly, so ask for readings before verdicts and let a second reading arbitrate
  rather than correcting anyone yourself. Candidates (c), (d) and (e) were put to the user and
  not confirmed, so they are not in the file.
- **Young adults** — consent-based reading turns, context before the passage, open with a hard
  question and do not answer it, doubt gets room rather than a rebuttal, no disapproval for a
  wrong answer. States plainly that treating teens and thirties as one room is *our*
  construction against three published age bands, and that handling a young adult who disagrees
  out loud is undocumented denominationally.
- **Deaf, signed** — turn-taking is gaze; refuse a bid by withholding eye contact rather than
  reaching for small groups; attention is sequential so read-slots and sign-slots separate;
  silence kept with the number labelled as borrowed; the no-neutral-place-for-the-eyes point.
  Opens by stating that no Adventist source exists and that nothing here comes from Bisindo.
  Carries the rejection of the 2001 abstraction claim so it cannot be reintroduced.
- **Seeker or visitor present** and **Baptismal class** — absorbed unchanged; they were already
  at the right specificity.
- **Mixed: members and seekers together** (Q21) — new. Ask the newer member second, never first;
  never let a fluent in-group answer close a question; and the self-contained question matters
  more here than anywhere else, because one setup serves both halves of the room.

**Overlaps (Q22):** one primary profile plus a short "If you also have" block covering the two
commonest additions, a visitor and a second language, with an explicit stop rule.

**Two consistency defects found and fixed while writing:**

- `Class Dynamics` recommended small groups of three universally, which the deaf profile
  contradicts. Now carries an explicit exception pointing at the gaze move.
- `SKILL.md`'s two pointers to this file still advertised "seeker-present classes" as the
  organising idea. Both now name the six congregation profiles.

**Left deliberately for ticket 07:** Step 1's profile enum still reads "Adults, young adults,
youth, seekers/baptismal class, mixed". Changing it is that ticket's job, and it is now
unblocked.

**Surfaced ticket 11, "The timed plan when attention is sequential"** — this ticket asserted that
read-slots and sign-slots must be separate without resolving what that does to the 35-minute
plan, or to the instruction to read the passage "aloud".
