# The Teaching Deck: `slides/*.pptx`

A guide is read at a table. A deck is read from six metres away by people who did not do the
reading. They are different artifacts and the deck is not a summary of the guide.

**Requires the `pptx` skill** for the PowerPoint mechanics. A working generator ships beside this file as `teaching-deck-generator.js` — the Lesson 10 deck, labelled as a worked example; copy it and replace the content. This file carries what that skill
cannot know: what a Sabbath School deck is *for*, and the traps this collection has already hit.

---

## The one rule everything else follows

**The slide carries what the class sees. The speaker notes carry what the teacher needs.**

That is the same split as `SKILL.md`'s three-kinds-of-text rule, applied to a projector:

| | Slide | Speaker notes |
|---|---|---|
| The question | yes, in full | how long to wait, what answers to expect, how to reopen it |
| Scripture | yes, read together | which verse is the hinge |
| A quote | yes, with its source | where to stop reading, what it is *not* evidence for |
| The clock | on the day divider only | everything else about timing |
| Predicted pushback | never | yes, with the honest answer |
| Provenance and cautions | source line only | the full caution |

A slide that carries stage direction is a slide the class is reading instead of listening. A deck
with empty notes has thrown away the half the teacher actually needs.

---

## Structure: day by day

Indonesian classes expect to walk the lesson **day by day**, and they expect substance on the
screen. Give them that. The shape is fixed:

```
1   Title
2   Memory Text
3   The week at a glance — five days, one line each
    ┌─ per day, Minggu through Kamis ─────────────────
4     Day divider (dark): day, date, title, minutes
5     Scripture, read together
6     Meat: background, a verified quote, or an illustration   ← 1 to 3 slides
7     The day's question (dark)
    └─────────────────────────────────────────────────
n-1 Application: the one concrete thing
n   Key text, and stop
```

Roughly **6 to 8 slides per day, 30 to 35 in total.** The weight-bearing day gets one more
slide of meat and says so on its divider.

**Every day gets at least one piece of meat.** A day with only Scripture and a question is the
day the class feels short-changed, and it is usually the day nobody remembers. Meat is one of:

- a **verified Ellen G. White quote**, with book and page
- a **famous voice** — a reformer, a martyr, a historical figure — quoted accurately
- an **illustration** that is a real story, not a hypothetical
- **background** the class cannot get from the text: a word study, a cultural fact, a custom

---

## Two clocks. Say which one you are on.

The guide's plan spends ten minutes each on two deep questions and surveys the other three days.
The deck walks all five days at about seven minutes each. **These are different plans and mixing
them overruns the hour.**

Put the deck's clock on each day divider, and put this in the title slide's notes: *this deck
runs day by day; the guide concentrates on two questions; pick one.*

---

## Quote discipline, on a screen

The foundation's citation policy applies with one addition: **a screen is worse than a page.** A
class can read a misattributed quote off the wall and check it on a phone before the hour ends.

- **Every quote on a slide is verbatim with a source line on the same slide.** Book and page, or
  periodical and date. No exceptions, no "adapted from".
- **Fetch it.** Verify through the EGW Writings API and keep the refcode in the generator's
  comments. A quote you remember is not a quote you have.
- **Do not pad with famous quotations.** If you can verify one famous voice for the week, use it
  and leave the other days to Ellen G. White, SDABC and illustration. Four plausible-sounding
  Luther lines are worse than one real Huss letter.
- **Follow the attribution chain and print it.** Ellen G. White quoting John Huss quoting nobody
  is still Huss: the slide says *"John Huss, letter to his friends at Prague, 1414, quoted in The
  Great Controversy, p. 105"*. Never let a quoted voice read as hers.
- **A compilation is not the original.** Prefer the source Ellen G. White actually wrote in.
  `Review and Herald, 7 September 1886` beats `God's Amazing Grace, p. 122`, which is a
  posthumous devotional compilation and should say "quoted in".
- **Working translations are labelled.** The verified text is the English; an Indonesian
  rendering says `terjemahan kerja` on the source line.

---

## Legibility

**Nothing below 20pt, and check it in the XML rather than trusting your eye.** This overrides the
`pptx` skill's 14–16pt body guidance, which is written for a deck read on a laptop.

| Element | Size |
|---|---|
| Day divider title | 44–54pt |
| Slide title | 32–40pt |
| Question on a dark slide | 36pt |
| Scripture and quote body | 22–26pt |
| Card label, source line, kicker | 20pt — the floor |

```bash
python3 -c "
import sys,zipfile,re,collections
z=zipfile.ZipFile(sys.argv[1]); c=collections.Counter()
for n in z.namelist():
    if re.match(r'ppt/slides/slide\d+\.xml$',n):
        for m in re.finditer(r'sz=\"(\d+)\"',z.read(n).decode()): c[int(m.group(1))//100]+=1
print('sizes:',dict(sorted(c.items())),'| below 20:',[k for k in c if k<20] or 'none')
" deck.pptx
```

One language per deck. Two languages on a projected slide halves the type size for both.

---

## Look

Dark day dividers and question slides, light content between them — the sandwich the `pptx` skill
describes. It also gives the class a rhythm: dark means *stop and answer*.

**Palette from the lesson, not from a default.** Lesson 10 is treasure in earthen vessels, so
terracotta `B85042` with cream `F4EFE7` cards. Pick again next week from that week's own image.
Keep gold `8A6410` for Spirit of Prophecy labels, matching the guide's convention.

**The motif is a labelled card**, never an edge stripe. A rounded cream rectangle, a 20pt
uppercase label in the label's own colour, the text, then the source. That one component carries
Scripture, quotes, background and illustration, distinguished only by its label:
`TERJEMAHAN BARU` · `ROH NUBUAT` · `KUTIPAN` · `ILUSTRASI` · `SDABC`.

Numbered circles for enumerations — the five contrasts, the four pairs, the week at a glance.

---

## Generator gotchas this collection has already paid for

Beyond the `pptx` skill's own list:

- **`pptxgenjs` is not preinstalled here.** `npm install pptxgenjs` in the working directory
  first; the skill's claim that it is preinstalled does not hold in this environment.
- **`validate.py` and `thumbnail.py` need `defusedxml`,** and this machine's Python is
  PEP-668 managed. Make a venv: `python3 -m venv .venv && .venv/bin/pip install defusedxml lxml
  Pillow "markitdown[pptx]"`, then run the scripts with `.venv/bin/python`.
- **A zero-height shape renders as a hairline.** Do not use one as an invisible container: it
  comes out as a rule under the title, which is exactly the accent-line the `pptx` skill bans.
  If a card needs no background, do not add a shape at all.
- **Never hardcode a y-position after a variable-height card.** Have the card helper *return* the
  next free y and use it. Hardcoding is how a caption ends up printed through a source line, and
  it will not show up in validation — only in the render.
- **Text-fit maths for Calibri:** `charsPerLine ≈ (boxWidth - 2*pad) * 124 / fontSize`. Calibrated
  against the LibreOffice render at 24pt across 11.2 inches. An estimate three times too small
  balloons the card off the slide; too large overflows it. Clamp the height to the slide either
  way: `h = Math.min(estimate, 7.5 - y - 1.05)`.
- **Long quotes get excerpted, not shrunk.** If a quote will not fit at 22pt, cut it to the
  sentence that carries the point and keep the ellipsis honest. Never drop below the floor.

---

## Before you hand it over

1. **Font floor**: run the size check above; expect `below 20: none`.
2. **`validate.py` passes.** Run it in the venv.
3. **Visual QA on every slide.** Render to images and look. Do not skip this: the two defects this
   deck actually shipped with — a hairline rule and a caption printed through a source line —
   were both invisible to validation and obvious in the render.
4. **Speaker notes on every slide.** Count them: notes slides should equal content slides.
5. **Every quote slide has its source on the same slide.**
6. **No day is meat-free.** Five days, five pieces of substance at minimum.
7. **The day dividers carry the minutes**, and they sum to the stated total.
8. **One language.** No bilingual slides.
9. **Ship a PDF beside the `.pptx`** — the projector laptop may not have PowerPoint, and a PDF
   cannot reflow or lose a font.
