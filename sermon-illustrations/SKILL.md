---
name: sermon-illustrations
description: Find or craft sermon illustrations for Seventh-day Adventist preaching. First searches for famous, well-attested illustrations from history, biography, classic preachers, Adventist heritage, and literature; if no fitting famous illustration exists, crafts an original engaging one. Use whenever the user asks for an illustration, story, analogy, opening hook, or "something to bring this point home" for a sermon, Bible study, or lesson — even if they don't say "illustration" but say "I need a story for this point" or "how do I open this sermon."
---

# Sermon Illustrations

Find a famous illustration that fits. If none fits, craft an original one. Always with attribution where possible, never with fabricated quotes.

**Requires:** the `adventist-foundation` skill is loaded for voice, EGW citation policy, and banned phrases.

---

## What This Skill Does

Given a sermon point, theme, or theological concept, this skill produces 2–4 candidate illustrations the preacher can choose from. Each illustration is workshopped: setup, tension, payoff, and a clear bridge back to the sermon point.

Three-tier approach:

0. **Tier 0 — Search the local library.** 78,573 illustrations are indexed on this machine by
   Scripture reference, subject taxonomy and full text. Search them before searching the web.
   Finding one here does not exempt it from the verification rule below.
1. **Tier 1 — Find a famous illustration that fits.** Search known wells: classic preachers (Spurgeon, Moody, Tozer, Lloyd-Jones, Whyte), Adventist heritage (Ellen White's experiences, Joseph Bates, William Miller, mission stories), history, science, biography, literature. Verify what's verifiable. If a quote is involved, never fabricate it.
2. **Tier 2 — Craft an original.** Only if Tiers 0 and 1 don't yield a strong fit, write an original illustration. Make it specific, concrete, and emotionally honest. Label it as original (not a true story) so the preacher doesn't accidentally claim it as fact.

---

## Step 1: Capture the Point

Ask the preacher:

| Field | What |
|---|---|
| Sermon point or theme | The exact point this illustration is for |
| Where in the sermon | Opening hook, mid-sermon, application, closing appeal |
| Audience | Adventist regulars, evangelistic, youth, mixed |
| Length budget | 30 seconds, 2 minutes, 5 minutes told from pulpit |
| Tone needed | Convicting, comforting, surprising, humorous, sober |
| Restrictions | E.g., "no sports," "nothing political," "must work in Indonesian" |

If the preacher has already given enough in their initial prompt, skip the questions and proceed.

---

## Step 2: Tier 0 — Search the Local Library First

78,573 illustrations sit on this machine, indexed by Scripture span, an 11-facet subject
taxonomy, 682 hymns and full text. Search them before you search the web.

```bash
/Users/edmundsitumorang/DEV/illustration-library/bin/illus.mjs find "PROBE" "PROBE" "PROBE" --ref "PASSAGE"
```

Run `illus.mjs find --help` for the full flag list. If the command is missing or errors with
exit 3, the library isn't available on this machine — go straight to Tier 1 and don't mention it.

### Send 3–4 short, lexically diverse probes — never one sentence

The index ANDs every word, so a sentence collapses to noise. Measured on this library:

| Probe | Hits |
|---|---|
| `"God pursues us even when we run away from him"` | 50, mostly irrelevant (the tool strips the filler words and tells you it did) |
| `"running from God"` | 1,873, led by *The Hound of Heaven* |
| `"hound of heaven"` | 24, all on point |

So vary the *wording*, not just the phrasing. A good set covers four angles:

1. a plain restatement — `"running from God"`
2. a biblical image — `"prodigal son"`
3. a known idiom — `"hound of heaven"`
4. a named exemplar — `"Jonah fleeing Tarshish"`

Four paraphrases of one sentence is the failure mode. Agreement across differently-worded
probes is the entire ranking signal, and it's printed on every result: a record tagged
`running from God+"hound of heaven"` matched two probes and is strong evidence; one tagged with
a single probe is weak.

### Reading the output

Real output for `find "running from God" '"hound of heaven"'`:

```
"running from God" "\"hound of heaven\"" | running from God=1873  "hound of heaven"=24
1 of 61 pooled | 3 matched 2+ probes

[52007] The Hound of Heaven
  story/93w · running from God+"hound of heaven" · The Pastor's Workshop
  ref Genesis 3:8-9; Psalm 139:7-10; Hosea 3:1
  tag Believing in God · God's Love · God's Presence · God's Pursuit · Running from God
  …own mind; and in the mist of tears I hid *from* Him, and under *running* laughter…
```

- `93w` — **word count is the length signal, not the type.** 73,632 of 78,573 records are typed
  `story` regardless of what they are. At preaching pace: 30 seconds ≈ 75 words, 2 minutes ≈ 300,
  5 minutes ≈ 750. Bound it with `--max-words 300` / `--min-words 100` (the floor matters — the
  library holds 5,374 records under 40 words, many of them one-line stubs).
- `running from God+"hound of heaven"` — this record matched **both** probes. That is the
  relevance evidence; `3 matched 2+ probes` on line 2 says how many did.
- Two fields appear only when they apply: `×2 attested` (two independent compilers carried it —
  this library's own version of "famous", and what `--attested` restricts to, 2,117 records) and
  `<- matches` on the `ref` line, which names the reference that actually overlapped your `--ref`.
- The header's per-probe counts are diagnostic. **A probe returning 0 means that vocabulary
  isn't in the library, not that the idea isn't** — rephrase and retry before giving up.

### The flags that matter

| Flag | Use |
|---|---|
| `--ref "Romans 8:28"` | The sermon passage. This is a *mode switch*, not a text filter: it returns what the library indexes to that verse span, including cross-chapter ranges like `Heb 11:39-12:2`. |
| `--max-words` / `--min-words` | The preacher's length budget from Step 1. |
| `--attested` | Only illustrations more than one compiler thought worth keeping. |
| `--tradition sda` | The 1,207 Adventist records — but 995 are EGW passages typed `quote`. Add `--tag form:story` for the 211 that are actual illustrations. |
| `--tag form:quote` / `form:story` | The quotation/illustration split. `form` mirrors `illustration_type`: story 73,632, quote 3,191, humor 1,186, hymn-story 649, testimony 233, poem 139. |
| `--tag <name>` | A taxonomy term. **ANDs with the probes** — `"day of atonement"` alone is 366 hits, with `--tag the-sanctuary` it is 2. |

**Search broadly first.** Probes and `--ref` only. Add `--tag` or `--tradition` on a *second*
pass, using the counted options the `NARROW:` line offers — those numbers are true subsets of
what you just saw. `illus.mjs vocab <word>` gives real tag, concept and hymn names with counts.

### Then pull the two or three worth reading

```bash
illus.mjs show 52007 39057
```

`find` prints snippets for triage; `show` prints the whole illustration with its attribution,
every Scripture reference, and the click-through URL where one exists.

### When to give up on Tier 0

The exit code is the gate: `0` means candidates, `1` means nothing — go to Tier 1.

Also go to Tier 1 when the counts are honest but thin. **Adventist-distinctive material is the
weakest part of this library** — 211 usable illustrations out of 78,573 records. Probing
`"Hiram Edson cornfield"` returns 0; `--tag the-sanctuary` holds 10 records total.

**The 1,207 figure overstates what you can preach.** Broken down: 995 are Ellen G. White
passages typed `quote`, 209 are It Is Written illustrations, 2 Adventist Stewardship, 1 other.
So there are **211 Adventist illustrations**, not 1,207. And the 995 EGW records are passages to
mine rather than quotations to deliver — only 13 of them are under 150 words.

Use the split deliberately:

- `--tradition sda --tag form:story` — the 211 actual illustrations.
- `--tradition sda --tag form:quote` — the EGW passages, when you want a citation rather than a
  story. Expect to excerpt: most run 150–300+ words.

Without that filter a Sabbath search returns three *Great Controversy* excerpts and one
illustration, which reads like the library is answering but is mostly handing you source text.

One caveat on the marker: for EGW and It Is Written the type is a **uniform per-source label**,
not a per-record judgement — every EGW row is `quote`, every It Is Written row is `story`. So it
separates those sources reliably and tells you nothing *within* one. Elsewhere (Holwick carries
6 types, Ministry127 5) it is a real per-record call, though still a rough one.

So on an **Adventist-distinctive** subject — the sanctuary, the investigative judgment, the
three angels' messages, the 1844 experience, the state of the dead, the pioneers — Tier 0 will
usually return little or nothing, and the Adventist heritage well in Tier 1 is where to go.

**But heritage material must be sourced like anything else, and it is the easiest place in this
skill to fabricate.** These stories are told from memory in Adventist circles, which makes
invented detail feel like recollection. Measured failures when this was pushed too hard:

- "Edson had sold what he had and told his neighbours the world was ending" — invented. He sold
  his Port Gibson farm in **1850**, to support the movement, six years after the Disappointment.
- "Before he stepped behind the veil the high priest put on the jewelled breastplate" —
  Leviticus 16:4 says the opposite: plain linen for the Day of Atonement entry. The breastplate
  and ephod of Exodus 28 belong to the ordinary ministry in the Holy Place.

Both were produced while reaching for heritage content the library does not hold. So:

> Offer a heritage illustration when you can point to a real source — Ellen White's own account
> with a citation, the SDA Encyclopedia, a documented biography, the Edson manuscript's actual
> provenance and its scholarly cautions. **If you cannot source it, say so to the preacher
> rather than narrating it.** "The library holds almost nothing on Hiram Edson and I would want
> to check the primary account before you preach detail from it" is a useful answer. An
> unsourced cornfield narrative is not.

A sanctuary question answered with three borrowed courtroom analogies is a thin answer, and worth
saying so to the preacher. It is still better than a vivid one you made up.

**Don't offer one image three times.** Courtroom / courtroom / courtroom gives the preacher one
choice, not three. Vary the register — a legal picture, a heritage narrative, a domestic or
natural picture — so the candidates are genuinely different ways in.

### Drop what doesn't fit — never pad the answer with near-misses

Tier 0 hands you a shortlist, not a set of candidates. Filter it hard.

**Every candidate must serve the whole point asked, not the topic it lives near.** If the
preacher asks for *records matter AND Christ is our Advocate right now*, a record that only
establishes "your file exists" is half an answer, and offering it as a candidate spends the
preacher's attention on something they cannot preach. Two illustrations that land beat four
that are adjacent.

Tier 0 **supplements** Tier 1, it does not replace it. If fewer than two local records genuinely
fit, keep the ones that do and go to Tier 1 for the rest — a mixed answer is normal and good.
Running the search is not a reason to use what it returned.

### Tier 0 does not lower the bar

This is a compilation of 19 sources, many of them 20th-century collections that reprinted
stories without citing them. 71% of records carry no click-through URL and `attribution` is a
single free-text field. **A record found here is a lead, not a verified fact.**

**Verify the details inside the record, not just that the record exists.** The library text
itself contains errors, and finding a story here is no evidence its details are right. A worked
example — record #34513, the John Newton conversion story, says:

> "Newton was on a slave ship returning from the tropics where they had deposited their 'cargo'"

and four sentences later says the cargo was **"beeswax and wood."** Both cannot be true, and the
second is the correct one: the *Greyhound* was not slaving on the 1748 voyage, and Newton
captained slave ships only **after** his conversion. Retelling that record faithfully puts a
false and well-known-to-be-false detail in the pulpit. The contradiction is visible in the record
itself, to anyone who reads it before believing it.

So: `illus.mjs show <id>` and read the whole thing. Check the named dates, places, cargoes and
quotes against a real source before you retell them. The verification rule in Tier 1 applies here
unchanged: if the story is presented as true and you cannot point to a real source, label it
"a frequently told story" or drop it. If it carries a quote you cannot verify, paraphrase it or
leave it out. **Never write "verified" next to a detail you took from the library and did not
check** — a library id is a provenance record, not a fact-check.

**Scope every verification note to exactly what you checked.** "No verification risk, it is the
biblical text" is false the moment the retelling adds detail the text does not contain — that
someone carried Mephibosheth to every meal, that soldiers arrived with a summons. Say which part
is quoted and which part is reconstruction: *"KJV quotations are verbatim; the detail about being
carried to the table is inference from 2 Samuel 9:13, not stated."* A blanket assurance stretched
over a mixed claim is worse than no note, because the preacher stops checking.

---

## Step 3: Tier 1 — Search for Famous Illustrations

Cast a wide net across these wells:

### Adventist heritage and Spirit of Prophecy

- **Ellen G. White's life and visions** — her conversion, the Great Disappointment of 1844, her healing experiences, the Civil War vision, her dream of the ship in the fog (a known illustration of guidance), encounters with poverty in her ministry. Verify via egwwritings.org or *Life Sketches*.
- **Pioneers**: Joseph Bates and his Sabbath conviction; William Miller and his Bible study leading to the 1844 movement; James White's perseverance; Hiram Edson's cornfield experience and the heavenly sanctuary.
- **Mission stories**: classic Adventist mission accounts (e.g., John Tay and Pitcairn Island, the Solusi mission, mission stories from *Adventist Review*, *Mission* quarterly).

### Classic preachers and theologians

- Charles Spurgeon — vast trove of illustrations, often verifiable in his sermons
- D.L. Moody — many well-attested stories
- A.W. Tozer, Martyn Lloyd-Jones, Alexander Whyte
- Augustine, Luther, Wesley (use with care; verify before quoting)
- Adventist preachers: H.M.S. Richards, Morris Venden, Doug Batchelor, Mark Finley (more recent — easier to verify)

### History and biography

- Famous historical episodes that genuinely illuminate a point: Lincoln's pardons, the Titanic, Corrie ten Boom, Dietrich Bonhoeffer, Eric Liddell, the Wright brothers, Apollo 13.
- Verifiable historical detail beats apocryphal motivational-poster stories. If a story is widely circulated but unverified (e.g., the "starfish on the beach" story, the violinist in the subway), label it as "a frequently told story" rather than presenting it as fact.

### Literature and the arts

- Classical and modern literature with known passages: Tolstoy, Dostoevsky, Lewis, MacDonald, Bunyan's *Pilgrim's Progress*. Cite the work.
- Hymn stories — many well-documented (e.g., "It Is Well with My Soul" — Horatio Spafford; "Amazing Grace" — John Newton).

### Science and nature

- Verified natural phenomena that map cleanly to a theological truth: the immune system, ecosystems, astronomy, animal behavior. Cite where possible. Avoid pop-science clichés.

### What NOT to use as a "famous illustration"

- Fabricated quotes from Einstein, Lincoln, Mother Teresa, C.S. Lewis. The internet is full of these. If you can't verify, don't quote.
- Apocryphal "true stories" widely circulated without source. Either label them as such or skip.
- Stories that have become cliché from overuse (the lighthouse-and-ships story, the carrot-egg-coffee story). They land as pulpit kitsch.

### Verification rule

For any quote attributed to a real person, you must be able to point to a reasonable source — a sermon, book, biography, or verified collection. If you can't, paraphrase the idea and frame it as "a teaching attributed to" or skip the quote entirely.

For Ellen G. White content, follow the foundation's three-tier policy strictly. **Do not fetch egwwritings.org** — it disallows automated agents site-wide in robots.txt, and its API requires OAuth. Use the 995 EGW passages already in the local library (`--tradition sda --tag form:quote`), or ask the preacher to check the wording. If you cannot confirm the wording, say so rather than reconstructing it.

---

## Step 4: Tier 2 — Craft an Original (Only If Needed)

If neither the local library nor a wider search turns up a fitting illustration, write an
original. Originals work when:

- The point is too specific or too contemporary for a classic illustration
- The preacher wants something fresh
- Famous options feel forced or cliché

How to write a strong original:

1. **Specific over generic.** A 47-year-old welder named David in Surabaya beats "a man in our city."
2. **Sensory.** Sights, sounds, textures. Let the listener see it.
3. **Tension before resolution.** Most failed illustrations skip the tension. Without tension, there's no payoff.
4. **One clear bridge.** Don't make the listener guess how it connects. Bridge it: "And that's the question this passage puts to us today."
5. **Honest about being original.** Say "Imagine with me…" or "Here's a scenario:" — never present an invented story as a true story.

---

## Step 5: The Verification Gate

Run this over every candidate before you write it, whatever tier it came from. It is a rule
about what you may **assert**, not about what you must find. Withholding a detail is always
allowed and is the right move whenever the check fails.

For every **named particular** — a date, a year, a place, a sum of money, a transaction, a
garment, an object, who was present, what happened to someone, a cause of death — ask:

1. **Where did this come from?** A library record, a source I actually read, or my own memory?
2. **If memory:** can I name a source? If not, drop it. Memory that feels like recollection is
   exactly how invented detail gets in.
3. **If a library record:** does the record's own text hold together, and did I read the whole
   thing? The library contains errors and self-contradictions.
4. **If Scripture:** does the passage actually say this, or is it a familiar picture assembled
   from several passages?

When a particular fails, you have three honest moves, in this order:

- **Drop it.** "Edson was a farmer near Port Gibson" carries the illustration without the
  unverified sale. Most failed particulars are not load-bearing and nobody misses them.
- **Generalise it.** "Years later" instead of a date you cannot source.
- **Flag it,** once, in the Notes: "I could not verify X — check it before you preach it."

Never keep the detail and hope. A vivid particular is exactly what a preacher repeats from the
pulpit, and exactly what a visitor checks afterwards.

**Two real failures of this skill, both caught by this gate:**

| Asserted | Why it failed |
|---|---|
| Edson "sold what he had and told his neighbours the world was ending" before 1844 | Memory, no source. He bought the Port Gibson farm in 1832 and sold it in **1850** — six years *after* the Disappointment, to fund the movement. |
| "Before he stepped behind the veil the high priest put on the jewelled breastplate" | Scripture says the opposite. Leviticus 16:4 prescribes plain linen for the Day of Atonement; the breastplate and ephod of Exodus 28 belong to the ordinary Holy Place ministry. |

Note what these have in common: neither is a quote, so the quote rule above never fired. The
gate exists because **the dangerous fabrications in this domain are specifics, not quotations.**

**Keep the gate quiet.** It produces *silence* about unverified particulars, not a wall of
disclaimers. Do not caveat what you did verify, and say each caveat once. An answer hedged
everywhere is as unusable as one invented everywhere.

---

## Step 6: Output Format

For each illustration (offer 2–4 candidates):

```
### Illustration [N]: [Short label]

**Source / type:** [Local library #ID — attributed | Local library #ID — unverified | Famous — attributed | Famous — verified anecdote | Original (invented for this sermon)]

**Setup** — 1–3 sentences establishing the scene or person.

**Tension / development** — 2–4 sentences building toward the point.

**Payoff** — 1–2 sentences delivering the moment.

**Bridge to the sermon point** — 1 sentence connecting it back to the point/theme.

**Approximate spoken length:** [X seconds at preaching pace]

**Notes:** [Any verification caveats. E.g., "Quote not verified — paraphrased." Or: "Spafford story well documented in standard hymn-history sources." For a local-library candidate, cite the id and say what you did or could not do to verify it: "Library #52007, attributed to Max Lucado; Thompson's poem is public domain and quoted accurately."]
```

After the candidates, add a one-line recommendation:
> Recommendation: [N] for the opening — it lands the tension early and your audience will feel the weight of it.

---

## Indonesian Output

For Indonesian sermons, illustrations should:

- Use settings, names, and references that resonate culturally (Indonesian cities, Indonesian historical events, kampung life, traffic in Jakarta, fishing villages, Indonesian Adventist mission stories).
- Avoid heavy reliance on Western pop culture references unless the audience is bilingual urban Adventist youth.
- Indonesian Adventist heritage stories (e.g., the founding of UNAI / Klabat / Bandung Adventist work, mission to Sumatra and Sulawesi) are gold when verifiable.

---

## Anti-Patterns

- **Never fabricate quotes** attributed to real people.
- **Never present an invented story as fact.** "There was a young woman in our church who…" — if she didn't exist, don't say it.
- **Never use clichéd illustrations** as the only option (lighthouse, starfish, carrot-egg-coffee, the dash on the tombstone). If you mention them, mention them to *replace* them.
- **Never give an illustration without a bridge.** The bridge is what makes it a sermon illustration instead of a story.
- **Never ignore the audience.** A stockbroker illustration falls flat in a rural village congregation.
- **Never treat a local-library hit as pre-verified.** It is a compilation, not a fact-checked archive. Finding a story in it changes how fast you found it, not how much you know about whether it happened.

---

## Reference Files

- `references/illustration-sources.md` — themed lists of well-known illustrations and where to look them up.
- `/Users/edmundsitumorang/DEV/illustration-library/` — the local library (78,573 records) and its
  CLI. `README.md` there documents the query model; `bin/illus.mjs find --help` documents the flags.

---

**Why this works:** Most AI-produced illustrations are either fabricated quotes or sentimental clichés. The user's instinct is right — famous illustrations resonate because they're already woven into the cultural fabric. They land harder than anything we can invent. Originals are the fallback, not the default. And the verification rule keeps the pulpit honest.
