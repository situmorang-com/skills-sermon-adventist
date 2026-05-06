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

Two-tier approach:

1. **Tier 1 — Find a famous illustration that fits.** Search known wells: classic preachers (Spurgeon, Moody, Tozer, Lloyd-Jones, Whyte), Adventist heritage (Ellen White's experiences, Joseph Bates, William Miller, mission stories), history, science, biography, literature. Verify what's verifiable. If a quote is involved, never fabricate it.
2. **Tier 2 — Craft an original.** Only if Tier 1 doesn't yield a strong fit, write an original illustration. Make it specific, concrete, and emotionally honest. Label it as original (not a true story) so the preacher doesn't accidentally claim it as fact.

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

## Step 2: Tier 1 — Search for Famous Illustrations

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

For Ellen G. White content, follow the foundation's three-tier policy strictly. **Use WebFetch on egwwritings.org** when in doubt about exact wording.

---

## Step 3: Tier 2 — Craft an Original (Only If Needed)

If no famous illustration fits well, write an original. Originals work when:

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

## Step 4: Output Format

For each illustration (offer 2–4 candidates):

```
### Illustration [N]: [Short label]

**Source / type:** [Famous — attributed | Famous — verified anecdote | Original (invented for this sermon)]

**Setup** — 1–3 sentences establishing the scene or person.

**Tension / development** — 2–4 sentences building toward the point.

**Payoff** — 1–2 sentences delivering the moment.

**Bridge to the sermon point** — 1 sentence connecting it back to the point/theme.

**Approximate spoken length:** [X seconds at preaching pace]

**Notes:** [Any verification caveats. E.g., "Quote not verified — paraphrased." Or: "Spafford story well documented in standard hymn-history sources."]
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

---

## Reference Files

- `references/illustration-sources.md` — themed lists of well-known illustrations and where to look them up.

---

**Why this works:** Most AI-produced illustrations are either fabricated quotes or sentimental clichés. The user's instinct is right — famous illustrations resonate because they're already woven into the cultural fabric. They land harder than anything we can invent. Originals are the fallback, not the default. And the verification rule keeps the pulpit honest.
