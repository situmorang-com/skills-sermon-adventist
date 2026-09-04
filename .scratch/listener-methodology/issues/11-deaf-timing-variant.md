# The timed plan when attention is sequential

Type: grilling
Status: resolved

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

## Answer

**The premise was wrong, and it was my error rather than the research's.**

Q19: a signed class reads a passage off the screen **at about the rate a hearing class reads it
aloud.** The Lesson 10 two-profile test claimed the deaf plan lost seven minutes and therefore one
of its two big questions. That figure was an estimate I built, never a measurement, and it came
from counting the hearing class's reading as free while counting the deaf class's as an extra
cost. The standard plan already pays for reading inside its blocks — the guide's own Tuesday card
says "fourteen verses takes about two minutes, leave eight for questions".

So: **no seven-minute cost, no lost question, and the 35-minute plan runs unchanged.**

The research file was careful and is vindicated: it called the *sequencing* well-evidenced and
said explicitly that read-slot **duration** was undocumented and depended on a reading rate nobody
had measured. The overreach was mine in interpreting it.

**What is real, and stays:** attention is single-channel, so reading and signing never overlap.
The class reads, eyes come back, then you sign. You cannot talk over the reading the way a hearing
teacher can. That is a constraint on *order*, not on the clock.

**This also dissolves the Q6 contradiction** this ticket claimed to have found. A per-profile
facilitation section can express "never concurrent" perfectly well; no generator-side branching of
the plan table is needed. Q6(a) stands as chosen.

**Q20 — the read-aloud rule is now about the source, not the channel.** "Read the passage from the
Bible, every time. Not from the lesson's paraphrase. Aloud, or displayed and read together."
Rewritten at every instruction site: `SKILL.md` Step 7 and its plan table, and three in
`teaching-methods.md` (the 35-minute table, the baptismal bullet, the closing).

**Q21 — this class reads screen prose comfortably**, not only Scripture. That widens the
teacher's options rather than narrowing them: a two-minute line or a summary can be displayed
instead of signed, buying attention back. Recorded in the deaf profile with the instruction to
ask the room rather than assume.

**Applied:** the deaf profile in `teaching-methods.md` now says the clock is unchanged and only
the order differs; `Timing Variants` gains a short "A signed class" entry saying the same; Final
Pass item 12 asks whether any block makes the class read and watch at once, rather than asking for
separate slots.
