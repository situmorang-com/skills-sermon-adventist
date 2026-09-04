# SKILL.md still documents the retired two-file output

Type: task
Status: resolved

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

## Answer

The claim in the question was half stale: `SKILL.md` had already been updated to name a single
`teachers-guide.html`. What was actually missing was the *mechanism* — the bilingual page existed
only in one built output file and nowhere in the skill, so the next session would have rebuilt it
from scratch and rediscovered the `data-lang` collision.

Applied to `sabbath-school-lesson/SKILL.md`:

- **Step 1's language rule** (line 51) now ends at one page: one file, one slug, both languages
  behind an `EN`/`ID` toggle, no `-en` twin URL.
- **New `### A bilingual page is one page`** under HTML Render: both panes ship and CSS hides one
  via `:root[data-pagelang]`, persisted in `localStorage['ss-pagelang']`; `data-pagelang` is
  explicitly *not* `data-lang`, with the reason (the `.bq` quote-card tabs flip to the working
  translation) written down so it is not re-paid; ids suffixed per pane; the contents nav ships
  twice with its `.th` heading hidden below 1120px, which is the doubled-CONTENTS bug named at
  its cause.
- **Render checklist item 20**: switch to `EN` and read the whole page — leftover Indonesian is an
  unwrapped pane — then confirm the quote cards did not flip and no contents link lands in the
  hidden pane.

Also fixed in passing: the publish section pointed at "Final Pass item 16" for the render, which
has been item 19 since the deck was added.

The template itself still has no toggle, and that is correct — it is a single-language skeleton,
and the merge is a build step, now documented as one.
