# The question form for a class that has not read the lesson

Type: grilling
Status: resolved

## Question

Q2 established that members normally arrive **not having read the lesson**, and Q7 chose the
mechanism: **content-carrying questions** — the setup states the fact, the question opens the
judgment — alongside always reading the passage aloud, which the skill already mandates.

Q12 removed the other candidate lever: because the teacher faces a different congregation each
week, no accountability loop across weeks is possible. So this ticket carries the whole weight
of the not-read problem.

Settle:

- The canonical form. Charting assumed setup → question → why → expect → keep-open, adding one
  field to Section 5's existing shape. Confirm or replace.
- How much may the setup state before it becomes a lecture? A sentence? Two? Where is the line
  past which the teacher has answered their own question — which the skill already bans.
- Whether the **four question tests** in `teaching-methods.md` need a fifth: does this question
  still work for someone who has not read the lesson?
- Worked examples, retrofitted to Lesson 9, whose two big questions currently assume the class
  knows the shape of 2 Corinthians. That guide is the regression test.
- Whether the day cards' "if you only have two minutes" line needs the same treatment.

## Answer

**The pattern was already latent in the file's own examples and had never been named.** Every
entry in the Five Tests' "Live" column does it — *"Abram obeyed and it cost him his country.
Name the last thing obedience actually cost you."* So this resolved as naming and requiring a
practice the guide already modelled, not as new architecture.

**Lesson 9 scored 7 of 8.** Both big questions carry their own content; Q2 needs no prior
reading whatsoever. Only the Tuesday spare question fails — "mengapa rencana itu berubah?"
assumes you know there was a first plan. The earlier claim while charting, that Lesson 9's big
questions assume knowledge of 2 Corinthians, was wrong.

**Decided (Q16–Q18):**

- Pattern named **the self-contained question**; the new field is the **setup** / **pengantar**.
- **Setup ceiling: two sentences, facts only, never the conclusion.** Operational test — if the
  setup answers the question, it is exposition wearing a question mark.
- **A longer teaching stretch is legitimate** where the class could not infer the thing from the
  text in front of them: an assumed historical fact, a term whose ordinary meaning misleads,
  events from an earlier chapter. Capped at half a minute, said as narrative, never in the
  opening. Per Q17 — the absolute rule would break in practice, so the exception is written down
  and bounded rather than left as an unwritten allowance.
- **Four tests become five**, and Test 2 loses its assumed reader: "a member who has heard only
  the setup could give two different defensible answers."

**Applied:**

- `teaching-methods.md`: new section **The Self-Contained Question**; five tests; Test 2
  reworded; the concrete-recall entry question moved out of "questions that work" into a
  labelled exception for a class you know has read.
- `SKILL.md`: Section 5 skeleton gains the setup; Step 7 bullet; markup contract
  `<p class="setup" data-label="Pengantar">`; the day-card spare question must be self-contained;
  Final Pass items 4 and 5; a new anti-pattern.
- Fixed a **pre-existing dangling reference**: both `SKILL.md` and `lesson-anatomy.md` pointed at
  "the four tests in `SKILL.md` A5". No A5 section exists anywhere. Both now point at
  `teaching-methods.md`.

**Not done deliberately:** Lesson 9's Tuesday spare question is left as published. That guide was
taught on 29 August; editing a delivered artifact for a rule made afterwards is churn. It stands
as the worked example of what the rule catches.

**No new tickets surfaced.** The day cards' "points to hold" also assume some familiarity, but
they are teacher-facing notes rather than questions and are out of this ticket's scope.
