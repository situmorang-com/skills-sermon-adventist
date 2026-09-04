# SKILL.md still documents the retired two-file output

Type: task
Status: open

## Question

`sabbath-school-lesson/SKILL.md` describes the output as `teachers-guide.md` +
`teachers-guide.html` in two single-language variants. As of this session the deliverable is
**one bilingual page** with an `EN`/`ID` toggle, built by merging an ID and an EN render.

In scope because it is the same file every other ticket edits, and a stale description of the
output contract will actively mislead the next session.

Record:

- One bilingual page is the deliverable; the single-language renders are intermediates.
- The page toggle uses `:root[data-pagelang]` and **must not** reuse `:root[data-lang]`, which
  already drives the English/working-translation tabs inside `.bq` quote cards. Reusing it
  flips those cards to the working translation whenever the page is read in Indonesian. This
  cost a debugging pass and would recur.
- Element ids are suffixed per pane (`s1__id`, `s1__en`) because two copies of the contents nav
  otherwise collide and every anchor jumps to the hidden pane.
- Publishing is one file to one slug; the separate `-en` URL was retired.
