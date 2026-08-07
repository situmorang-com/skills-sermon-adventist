# Rendering `bible-study.html`

Everything needed to build the reading copy of a study. The SKILL.md keeps only the decision (when to render, and the md/html split); the how lives here.

Start from `html-template.html` in this folder. Copy it and fill in the content. Do not design a new page each time — the template carries the whole stylesheet, both toggles, the contents scroll-spy and the progress bar, so consecutive studies look like one series instead of eight unrelated documents.

---

## The two files are not the same document

| | `bible-study.md` | `bible-study.html` |
|---|---|---|
| Read by | The preacher, preparing and verifying | The preacher reading, or the class |
| Verification Ledger | Yes, full table | **No. Removed entirely.** |
| `para_id`, HTTP codes, API and site names | Yes | **Never.** Workshop tools, not content |
| Tier markers after quotes | Yes | No — the page citation alone |
| Page citations (*Desire of Ages* p. 25, 6SDABC on 12:11) | Yes | Yes. Real citations stay in both |
| Doctrinal flags (Henry on soul immortality, Barclay) | Yes | Yes. Teaching content, not provenance |
| Short teacher notes ("read this before teaching ch. 14") | Yes | Yes |
| Provenance statement | The ledger | One closing line pointing to the markdown |

The HTML footer carries the whole provenance story in one sentence:

> Scripture quoted from the KJV and Terjemahan Baru. Ellen G. White, SDABC, and Matthew Henry quotations are verbatim from the sources cited. The full source ledger, including what could not be accessed, is in `bible-study.md`.

---

## Placeholders

The template has eight. Fill every one; a `{{...}}` left in a delivered page is a bug.

| Placeholder | Value |
|---|---|
| `{{LANG}}` | `en` or `id` |
| `{{PASSAGE}}` | The reference, e.g. `1 Corinthians 12–14` |
| `{{TITLE}}` | The study's title line |
| `{{AUDIENCE}}` | Who it was prepared for |
| `{{TRANSLATION}}` | e.g. `the KJV and Terjemahan Baru` |
| `{{REFERENCE}}` | Citation under the sample Scripture block |
| `{{WORDS}}` | Body word count, comma-grouped |
| `{{MINUTES}}` | Reading time, words ÷ 200, rounded |

---

## Markup contract

| Study element | Markup |
|---|---|
| Numbered section (1–8) | `<section class="sec" data-hue="4">` wrapping `<h2 id="..."><span class="num">4</span> Research and Commentary Insights</h2>`. `data-hue` is the section number and drives every color inside |
| Sub-heading (word study, EGW reference, theme) | `<h3 id="...">` with a matching id |
| Scripture quotation | `<blockquote class="scripture">` + `<p class="note">` with reference and translation |
| Ellen G. White quotation | `<blockquote class="egw">` + `<p class="note">` with *Book Title*, p. 000 |
| Other commentary quotation | `<blockquote class="cited">` + `<p class="note">` naming the source |
| Doctrinal flag / caution | `<div class="flag">` — the only scarlet on the page |
| Word study (label/value pairs) | `<div class="tablewrap"><table class="spec">` — first column is the label |
| Data table (cross-references, argument structure) | `<div class="tablewrap"><table class="grid">` — has a `<thead>` |
| Any table at all | **Always** inside `<div class="tablewrap">` so it scrolls on a phone instead of breaking the page |
| Numbered list (application questions, argument steps) | **One** `<ol>` holding every `<li>`. Markdown converters routinely emit one `<ol>` per item, which restarts the count so every question renders as "1." Merge adjacent single-item lists and check the numbering runs 1…n |
| Section divider | `<hr class="rule">` |
| Aside, citation line, teacher note | `<p class="note">` |
| Contents nav | `<nav class="toc">`: sections as `<li data-hue="N">`, sub-headings as `<li class="l3" data-hue="N">` carrying their parent's step. Include for studies over ~2,500 words |

Greek and Hebrew go in as real Unicode (χαρίσματα, תִּקְוָה) with the transliteration in `<em>`.

---

## Design spec — do not improvise on these

A study runs 3,000–10,000 words. Every value below is set for sustained reading, not for looking designed.

| Decision | Value | Why |
|---|---|---|
| **Measure** | `68ch` (~66 characters) | 50–75 CPL is the readability optimum and WCAG 1.4.8 caps at 80. A full-width 900px column runs ~97 CPL and reads as a wall. This is the single biggest thing that makes a study page feel heavy |
| **Body type** | 18.5px / 1.72 sans; Scripture quotes 20px serif | 18–20px is the long-form sweet spot; 1.5 is the line-height floor, more when lines are long. The serif is reserved for Scripture so the text being studied reads differently from the notes about it |
| **Headings** | Sentence case, sans, 26px (h2) / 18.5px (h3); `h1` is gradient display type | Never all-caps: caps cost 10–20% reading speed and flatten word shape, and headings are exactly what a browsing reader navigates by |
| **Section separation** | Colored rule + glowing number badge above each `h2` | The eight sections are the map of the document. They should be visible from a scroll position, not merely readable |
| **Contrast** | Every text/surface pair ≥ 4.5:1, ramp steps included | WCAG AA for body text. Compute it, don't eyeball it. All sixteen ramp steps were checked on glass: 5.8–9.5:1 dark, 5.6–10.6:1 light |
| **Dark mode** | The default. Linen on onyx `#070b14`, rim-lit glass over the aurora | Never `#fff` on `#000`. The ramp is bright enough to glow and still clears AA on every glass surface |
| **Depth** | Translucent cards with hairline edges and an inset top highlight; `backdrop-filter` only on the fixed controls and the sticky sidebar | Blur is expensive. Two blurred surfaces read as glass; thirty of them stutter on scroll |
| **Motion** | Progress bar, section reveal on entry, animated nav dot — all killed by `prefers-reduced-motion` | Motion is garnish. Never load-bearing, always switchable off |
| **Browsing** | Sticky glass contents sidebar ≥1120px, plain list below; gradient reading-progress bar at the top | The nav is how a 6,000-word study becomes browsable. Sub-headings hide on narrow screens |

---

## The color system — the sanctuary palette

**The palette is fixed and it means something.** Exodus 26:31 specifies the veil: "blue, and purple, and scarlet, and fine twined linen." Exodus 25 adds the gold. Those five are the entire palette. Nothing else gets in — no free-choice hues, no rainbow.

| Name | Role | Dark | Light |
|---|---|---|---|
| **techelet** — blue | Structure: headings, links, contents, Scripture | `#71cdf4` | `#1d6e90` |
| **argaman** — purple | The far end of the section ramp | `#bc7af5` | `#601f98` |
| **zahav** — gold | Ellen G. White / Spirit of Prophecy, always and everywhere | `#e8b44a` | `#8a6410` |
| **shani** — scarlet | Cautions and doctrinal flags **only** — rare, so it lands | `#f2707a` | `#b02832` |
| **shesh** — linen | The text itself | `#eef1f7` | `#141922` |
| **onyx** | The surface everything floats on | `#070b14` | `#f5f6f9` |

**Section wayfinding is a ramp, not a spectrum.** Eight steps walk techelet (198°) to argaman (272°) as `--s1`…`--s8`. One analogous family, so section 3 and section 6 stay distinguishable while the page reads as a single palette. The mid-ramp indigos need a lightness lift to clear AA; that is already baked into the template values. **Don't interpolate a fresh ramp by eye.**

**Content types hold a fixed color anywhere in the document:**

| Content | Class | Color |
|---|---|---|
| Scripture | `blockquote.scripture` | Techelet, serif, soft glow |
| Ellen G. White | `blockquote.egw` | Gold |
| Other commentary | `blockquote.cited` | Neutral |
| Doctrinal flag / caution | `div.flag` | Scarlet |

Each card labels itself: the chip on its top edge ("Scripture", "Spirit of Prophecy", "Commentary", "Caution") comes from CSS `::before`, so the markdown conversion never has to add it.

**Body prose always stays linen.** Color marks structure and source; it never tints running text.

**The aurora** is three blurred radial sources — techelet top-left, argaman top-right, one ember of gold low centre — over a masked 60px techelet grid, fixed at `z-index:-2`. Atmosphere, not motion.

**Monochrome button.** Sets `data-mono="on"`, re-pointing the eight ramp steps plus `--techelet`, `--argaman`, `--zahav`, `--shani`, `--scripture`, `--sop`, `--link`, and zeroing `--aurora` and `--glow`. Every tint, glow, gradient and aurora source derives from those variables through `color-mix()`, so one override desaturates the page and the gradient `h1` reverts to flat ink. Keep it that way: **no hard-coded hex outside the theme blocks**, or mono leaks color.

---

## Rules

- **Self-contained.** Inline CSS, no external fonts, no CDN, no scripts beyond the two toggles, the scroll-spy and the progress bar already in the template. It must render correctly opened straight off disk with no network.
- **Light and dark both readable.** `prefers-color-scheme` plus a `data-theme` override the toggle sets. Use the CSS variables; never hard-code a color.
- **Printable.** The `@media print` rules flatten the page, drop the aurora and nav, and avoid breaking blockquotes and table rows. Keep them.
- **No verification apparatus.** No ledger, no `para_id`, no HTTP codes, no tier markers, no bare URLs as link text.
- **Descriptive link text.** The URL lives in the `href`, never in the visible text. `<a href="…">The gift of tongues in 1 Corinthians 14</a>`, not the naked address. Same rule in the markdown: `[Title](url)`.
- **Every `href` has a matching `id`.** A contents nav with a dead link is worse than no nav.
- **Never regenerate the HTML from an older markdown.** Edit both files or re-render.

---

## Before you hand it over

1. Every `{{placeholder}}` filled.
2. Measure is capped (`68ch`) — no full-bleed text column.
3. Every table wrapped in `.tablewrap`.
4. Every nav link resolves to an id on the page.
5. No `para_id`, no `located-unread`, no "HTTP 403", no "this session" anywhere in the file.
6. Links show titles, not URLs.
7. Footer names the translation and points to `bible-study.md`.
8. No all-caps headings anywhere.
9. Mono toggle leaves no color behind — no hex outside the theme blocks.
10. Reduced-motion honored: reveals and transitions disabled, content still visible.
11. Ordered lists count correctly — no run of single-item `<ol>` blocks all showing "1."
12. Tags balance and the file ends with `</html>`.
