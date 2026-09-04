# The timed plan when attention is sequential

Type: grilling
Status: open

## Question

The deaf profile now asserts that **read-slots and sign-slots must be separate blocks in the
plan, never concurrent**, because deaf students show no successful divided attention. That
constraint was written into `teaching-methods.md` without resolving what it does to the plan
itself, which is a gap this ticket closes.

`## Timing Variants` currently offers 35, 25 and 45 minute shapes, all of which assume the class
can hear a passage while looking at something else. In a signed room they cannot.

Settle:

- Does the 35-minute plan gain a **deaf variant** with read and sign blocks separated, or does
  the existing plan simply carry a note?
- What does separating them actually cost? Reading 14 verses off a screen and *then* signing the
  setup is two blocks where a hearing class has one. If that costs three or four minutes, the
  plan has to give something up, and the skill's existing rule is that application never gets
  cut.
- Where the guide says "read the passage aloud, from the Bible, every time" — the deaf class
  reads together off the screen (established Q11), so the wording needs a profile-aware form
  rather than a flat "aloud".
- Whether the two-minute day-card lines are affected, since they are written as speech.

Depends on nothing further; the research is already in ticket 01.

## Evidence from the Lesson 10 two-profile test

Generated Section 3 + Section 5 twice from an identical spine, adults and deaf, 35 minutes each.

| | adults | deaf |
|---|---|---|
| Plan blocks | 7 | 8 |
| Minutes in dedicated read-slots | 0 | **7** |
| Big questions that fit | 2 | **1** |
| Shared spine | 100% identical | 100% identical |
| Section 3 + 5 overall | 38% similar, so 62% diverged | |

**Separating read from sign costs about seven minutes, which is exactly one big question.** The
deaf class structurally holds less in the same 35 minutes. So this ticket cannot resolve as "the
existing plan carries a note" — the plan table itself changes shape and content is dropped.

**This contradicts the Q6(a) decision.** A per-profile facilitation *section* cannot express "you
get one question instead of two", because that is the plan table, not the prose beside it. Q6(a)
looks sound for adults, young adults, seeker, baptismal and mixed; for deaf it does not hold.
Likely resolution: mostly (a), with generator-side branching for the deaf plan table only.
