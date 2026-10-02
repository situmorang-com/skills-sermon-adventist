---
name: sermon-illustrations
description: Find or craft sermon illustrations for Seventh-day Adventist preaching. First searches the local illustration library on this machine (over 100,000 records including the Adventist pioneers, Ellen G. White and the Adventist Mission stories, queried with illus.mjs), then famous, well-attested illustrations from history, biography, classic preachers, Adventist heritage, and literature; if nothing fits, crafts an original engaging one. Use whenever the user asks for an illustration, story, analogy, opening hook, or "something to bring this point home" for a sermon, Bible study, or lesson — even if they don't say "illustration" but say "I need a story for this point" or "how do I open this sermon."
---

# Sermon Illustrations

Search the local library first. Then find a famous illustration that fits. If none fits, craft an original one. Always with attribution where possible, never with fabricated quotes.

**Requires:** the `adventist-foundation` skill is loaded for voice, EGW citation policy, and banned phrases.

---

## What This Skill Does

Given a sermon point, theme, or theological concept, this skill produces 2–4 candidate illustrations the preacher can choose from. Each illustration is workshopped: setup, tension, payoff, and a clear bridge back to the sermon point.

Three-tier approach:

0. **Tier 0 — Search the local library.** Over 100,000 illustrations are indexed on this machine
   by Scripture span, subject taxonomy, hymn and full text, including the Adventist pioneers' own
   writings, Ellen G. White and every Adventist Mission story since 2016. Search them before
   searching the web. Finding one here does not exempt it from the verification rule below.
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

If the preacher has already given enough in their initial prompt, skip the questions and proceed. If you cannot ask (a one-shot run, a scheduled task, a preacher who said "just give me options"), proceed anyway: search without a length filter, then state each candidate's spoken length and the slot it suits so the preacher can choose. Do not block on the foundation's context variables when the congregation, language and passage are already given.

---

## Step 2: Tier 0 — Search the Local Library First

The library at `/Users/edmundsitumorang/DEV/illustration-library/` indexes over 100,000
illustrations from nearly forty sources by Scripture span, an 11-facet subject taxonomy, 682 hymns
and full text. Search it before you search the web.

```bash
/Users/edmundsitumorang/DEV/illustration-library/bin/illus.mjs find "PROBE" "PROBE" "PROBE" --ref "PASSAGE"
```

The script is executable as written; prefixing `node` also works. `illus.mjs find --help` prints the
flag list and the **current record count**. Every count in this
file was measured on 2026-10-02 and the library keeps growing, so when the CLI and this file
disagree, the CLI is right. If the command is missing or exits 3, the library isn't on this
machine: go straight to Tier 1 and don't mention it.

`references/illustration-sources.md` carries a **measured probe set for every sermon theme**, with
the record ids that fit, the ones that are wrong, and what the library does not hold. Read the
theme's block before you search; it saves a round of guessing.

### Probes: short, lexically diverse, and phrases in quotes

The index ANDs every word, so a sentence collapses to noise. Measured on this library:

| Probe | Hits |
|---|---|
| `"God pursues us even when we run away from him"` | 56; the tool strips it to `God pursues run away` and says so in a NOTE. Several top rows happen to be Jonah pieces, but the agreement signal that ranks results is gone |
| `"running from God"` | 2,291, led by *The Hound of Heaven* |
| `'"hound of heaven"'` | 26, all on point |

So vary the *wording*, not just the phrasing. A good set covers four angles:

1. a plain restatement — `"running from God"`
2. a biblical image — `"prodigal son"`
3. a known idiom — `'"hound of heaven"'`
4. a named exemplar — `"Jonah fleeing Tarshish"`

Four paraphrases of one sentence is the failure mode. Agreement across differently-worded probes
is the entire ranking signal, and it is printed on every result: a record tagged
`running from God+"hound of heaven"` matched two probes and is strong evidence; one tagged with a
single probe is weak. The CLI takes at most four probes and prints at most 20 results (`-n`).

Five rules that come from measuring where probes went wrong:

- **A multi-word probe is ANDed words, not a phrase.** `"father ran"` matches Peter Pan;
  `"least of these"` matches Ellen White's "least commandments"; `"soul sleep"` matches Spurgeon on
  Gethsemane. To search a phrase, put literal double quotes *inside* the shell argument:
  `'"hound of heaven"'` (26 hits). The CLI passes a quoted probe through untouched, and a phrase
  the library does not hold returns 0 and exits 1: Heschel's `'"palace in time"'` is not there.
- **Stemming is aggressive.** *prodigal* matches *prodigality*, *cross* matches *crossing*,
  *temperance* matches *temper*, *diet* matches the Diet of Worms, *timor* matches *timorous*, and
  *Luther* alone pulls Martin Luther King. Pair every generic word with a specific one and read the
  `matched 2+ probes` count, not the raw per-probe totals.
- **Proper nouns are probes, not vocabulary.** `vocab spafford` exits 1; the plain probe
  `"spafford"` finds 12. Surnames collide (*newton* is also Isaac), so pair the name with a place
  or object: `"spafford" "daughters"`, `"Corrie ten Boom" "Ravensbruck"`.
- **A probe returning 0 means that vocabulary isn't in the library, not that the idea isn't.**
  `"Hiram Edson cornfield"` returns 0; the text says "shocks of corn in a field". `"Hiram Edson"`
  returns 12, led by Loughborough's own 1909 account (#81605). Rephrase before you give up.
- **Run `vocab` first, but read what it resolved to.** `illus.mjs vocab grace` lists the real
  `--tag`, `--concept` and `--hymn` names with counts. Concept slugs can be truncated
  (`joseph-bate`, `children-sermon`), and a hit can be the wrong sense: `vocab job` is employment,
  `vocab hus` is husbands, `vocab advent` leads with the Adventist facet. `vocab` exits 1 for any
  word that is not a tag, concept or hymn name, common words included (`vocab record`); that exit
  means "use it as a plain probe", not failure.

### Reading the output

Real output for `find "running from God" '"hound of heaven"' -n 2`:

```
"running from God" "\"hound of heaven\"" | running from God=2291  "hound of heaven"=26
2 of 64 pooled | 2 matched 2+ probes

[52007] The Hound of Heaven
  story/93w · running from God+"hound of heaven" · The Pastor's Workshop
  ref Genesis 3:8-9; Psalm 139:7-10; Hosea 3:1
  tag Believing in God · God's Love · God's Majesty · God's Presence · God's Pursuit · God's Sovereignty · Running from God
  …own mind; and in the mist of tears I hid *from* Him, and under *running* laughter…
[38690] You Can’t Outrun God In An Excavator
  story/385w · running from God+"hound of heaven" · Holwick / Kerux
  ref Psalm 119:32; Psalm 139:5-7; Jonah 1:3
```

- **Header, line 1:** the per-probe counts are diagnostic, and the header echoes every filter as
  the CLI *resolved* it (`tag=form:statistic`, `tradition=seventh-day adventist`). Read it: a tag
  that resolved to something other than what you typed is the first thing to notice.
  **Line 2:** `pooled` is the ranked candidate pool after reprints are collapsed, not the hit
  total; `K matched 2+ probes` is the real relevance signal, and it is inflated when probes overlap
  (`"Corrie"`, `"ten Boom"`, `"Corrie ten Boom"` is one probe three times).
- `story/93w` — **the word count is the length signal.** At preaching pace 30 seconds ≈ 75 words,
  2 minutes ≈ 300, 5 minutes ≈ 750. Bound it with `--max-words 300` / `--min-words 100`. About an
  eighth of the library is under 40 words, mostly Barna and Gallup statistics and one-line stubs.
  The type marker is one of `story`, `quote`, `humor`, `statistic`, `study`, `poem` (three stray
  records carry `other` or `analogy`). For the
  Adventist sources it is a per-source label (every Ellen G. White row is `quote`, every Adventist
  Mission row is `story`); elsewhere it is a rough call, and four fifths of the library is `story`
  whatever it is: nine-word Holwick sermon-outline stubs, bare Heschel and Bonhoeffer quotations
  and 6,000-word manuscripts all carry it. Read the words, not the label.
- **The probe slot** (`running from God+"hound of heaven"`) names the probes the record matched.
  It reads `@Luke 15:11-32` for a passage probe and `--filter` when the search had only flags.
- **Markers that appear only when they apply:** `×2 attested` (two independent compilers carried
  it: this library's own version of "famous", and what `--attested` restricts to; it reads `×3` or
  `×4` when more did); `SDA` (an Adventist source); `hymn-story`; and `<- matches` on the `ref`
  line, naming the reference that actually overlapped your `--ref`.
- **`NOTE` lines** tell you what the CLI did to your query: stripped filler words, dropped a fifth
  probe, or fell back from a thin passage tier to the whole-book set ("topical, not textual"). They
  are usually the reason a search returned something other than what you expected. A probe that
  parses as a reference is promoted to passage mode silently; the header shows it as `ref=John 3:16`.
- **`NARROW:`** appears only on a single-probe or filter-only search and lists real, counted
  `--tag` options that are true subsets of the result you just saw. Use those rather than guessing
  tag names.
- **Piping the output through `head` replaces the exit code with head's.** Run the CLI unpiped
  when the exit code matters, or read `PIPESTATUS`. Run each `find` or `show` as its own command
  rather than chaining several on one line; a chain that stops silently looks like a search that
  returned nothing.

### The flags that matter

| Flag | Use |
|---|---|
| `--ref "Romans 8:28"` | The sermon passage. A **mode switch**, not a text filter: returns what the library indexes to that span, including cross-chapter ranges like `Hebrews 11:39-12:2` and whole chapters. Records that reach the passage only through a whole-book citation are suppressed and counted; `--wide` reinstates them. When the precise tier is thin the CLI falls back to wide on its own and says so in a NOTE. With text probes present the passage runs as one more probe, OR-pooled with the others, so read `probe+@ref` in the probe slot. A small passage index (Mark 2:27, Galatians 2:16) is precise; a large one (Romans 3, Hebrews 11) needs `--max-words 300` or you get sermon manuscripts. Single-chapter books need the chapter: `"3 John 1:2"`, not `"3 John 2"`. |
| `--max-words` / `--min-words` | The preacher's length budget from Step 1. `--max-words` rarely changes a top ten (short rows already outrank); `--min-words 150` is how you find narrative under a pile of epigrams. |
| `--attested` | Only illustrations more than one compiler thought worth keeping. **Always pair it with `--max-words 300`**: alone it floats 11,000-word anthologies that matched two probes by accident. **Never combine it with `--tradition sda`**: no Adventist source is cross-compiled, so the intersection is empty. |
| `--tradition sda` | Only the ten Adventist sources (next section). Other values: `evangelical`, `christian` (a small bucket: the Cybersalt and *Funnies* joke lists, Bible Topics A-Z and the SermonWriter children's sermons; not a superset of evangelical), `baptist`, `pd`. |
| `--tag form:story` / `form:quote` / `form:humor` / `form:statistic` / `form:hymn-story` | The form axis. **There is no `form:study`**: that word resolves to `form:statistic` and the header shows it. Read the `study` type marker in the row instead. |
| `--tag <name>` | A subject term. **ANDs with the probes**, so it cuts hard: `"day of atonement"` alone is 411 hits, with `--tag the-sanctuary` it is 2, and neither of the two is about the sanctuary. A bare `--tag history` is ambiguous across axes and exits 2 with the choices; a misspelling exits 2 with a suggestion, and the suggestion can be wrong (`sanctury` → `sanctification`). Holwick sermon manuscripts carry subject tags too, so `--tag` plus `--max-words 300` is the working form. |
| `--concept <slug>` | The compilers' own vocabulary, when no taxonomy term fits. `--concept children-sermon` is how you reach the SermonWriter object lessons. |
| `--hymn "It Is Well With My Soul"` | Illustrations linked to a hymn (title or SDAH number). The header prints the SDAH number, which the Lagu Sion database maps to an LSEL number. Links are by *mention*, so a fifth of the rows are off-topic; add `--tag form:hymn-story` for the hymn's own story. A title that starts with an apostrophe (`'Tis So Sweet`) fails; drop it. About 300 of the 682 hymns have linked records. |
| `-n 20` | More rows (default 8, max 20, capped silently). |

**Search broadly first.** Probes and `--ref` only. Add `--tag` or `--tradition` on a *second*
pass, using the counted options the `NARROW:` line offers. `illus.mjs vocab --facets` lists the
eleven subject facets; `illus.mjs vocab sda` lists the Adventist one.

### What the library holds (measured 2026-10-02)

| | |
|---|---|
| Records | 107,176 (`story` 86,592 · `statistic` 9,711 · `humor` 4,920 · `quote` 4,380 · `study` 1,430 · `poem` 140) |
| Attested by 2+ compilers | 4,658 |
| With a click-through URL | about half; the rest are book and database compilations with a free-text `attribution` field |
| Largest wells | Holwick/Kerux 37,543 · Precept Austin 12,068 · Our Daily Bread 9,656 · Barna 9,442 · Tan's *7,700 Illustrations* 7,680 · *10,000 Sermon Illustrations* 7,468 · The Pastor's Workshop 4,473 · *Cyclopedia of Illustrations* (1910) 3,531 · Cybersalt clean jokes 3,456 |

The most dependable hand-overs, measured across fourteen themes, are **Our Daily Bread** records:
150 to 300 words (usually 200 to 230), named author, date and URL, and on death and resurrection
generally compatible with Adventist teaching. Fewer than one in ten is attested by a second
compiler, so do not expect the `×2` marker on them, and their stored URLs now return 404 without a
`/US/` segment (`odb.org/US/YYYY/MM/DD/slug`): rewrite and check before you hand one over. Three
non-story wells are worth knowing by name:

- **Statistics** (`--tag form:statistic`): Barna and Gallup, typically a 10- to 35-word slice of
  an article (some run to 150) with the publication date in the attribution line. A statistic is a
  dated claim, nearly always about Americans: preach the year with the number, and open the URL
  before you quote a figure, because a slice can be arithmetically incomplete on its own. Older
  figures from 1987 to 2003 sit in Ministry127 and Holwick rows, some typed `statistic`, some
  buried inside longer `story` records.
- **Humor** (`--tag form:humor`): Cybersalt and *The Funnies*, none Adventist. The safe cut is
  `--attested --max-words 75`. Afterlife jokes assume the dead are conscious, coffee jokes assume
  coffee, most jokes say "Sunday morning", and English puns do not survive translation into
  Indonesian or sign. Read before you tell.
- **Hymn stories** (`--hymn`, then `--tag form:hymn-story`): Osbeck's *Amazing Grace: 366 Hymn
  Stories* carries the documented accounts; Our Daily Bread carries two-minute versions with dates.
  Compare twins before choosing: the library holds nine Spafford tellings and one of them (#19803)
  has three daughters and a storm instead of four and a collision.

### The Adventist shelf: ten sources, three shapes, and two rules

| Source | Records | Type | What it is |
|---|---|---|---|
| Adventist Pioneer Writings | 2,131 | `story` 1,082 · `study` 1,049 | Bates's *Autobiography* (1868), James White's *Life Incidents* (1868) and *Sketches of William Miller* (1875), Loughborough's *Rise and Progress* (1892) and *Great Second Advent Movement* (1909), Spicer's *Miracles of Modern Missions* (1926) and *Youthful Witnesses* (1921), Olsen's *Origin and Progress* (1925). Public domain, OCR'd from archive.org scans. |
| Ellen G. White | 1,890 | `quote` | *Patriarchs and Prophets* 887 · *The Great Controversy* 734 · *Education* 269. Three books only. |
| Adventist Mission "Inside Story" | 521 | `story` | The weekly mission story from the Adult Bible Study Guide, 2016 to 2026, bylined and **dated to the Friday that closes its lesson week** (the day before the Sabbath it is read on), with the official URL. |
| It Is Written | 209 | `story` | Short modern illustrations, Scripture-indexed, about half under 150 words. **The richest preachable Adventist source.** |
| ScienceShorts (AIIAS) | 125 | `story` | Science and nature pieces. |
| Amazing Facts sermons | 43 | `story` | |
| Children's Mission Quarterly | 24 | `story` | The children's edition of the mission report: concrete, scene-driven. |
| Voice of Prophecy, Adventist Stewardship, GC Evangelism | 13 | | Several Voice of Prophecy records are truncated mid-sentence. |

**Three shapes, three ways in.**

- **Ellen G. White passages** are chapter chunks titled "Chapter Name (n)", 150 to 450 words, with
  the source's footnote markers like `(977)` left in the text and **no page number**, only a
  Gutenberg URL. Reach them by text probes plus `--tradition sda`, or by `--ref` where the passage
  is indexed (about half of *Patriarchs and Prophets* is, *The Great Controversy* mostly is not,
  *Education* never is). Adjacent ids are adjacent paragraphs. To cite a page, take a phrase of
  eight or more words that is unique to the book to the foundation's `egw-fetch.sh search` (a short
  phrase returns other books first), confirm the paragraph with `egw-fetch.sh para <id>`, strip the
  HTML span markup the API wraps links in, and cite the refcode (GC 484.2). For any other Ellen G.
  White book use `egw-fetch.sh` directly; it works on this machine. Do not scrape egwwritings.org
  pages or call its API anonymously.
- **Pioneer passages** are heritage source text, not illustrations, and the `study`-typed half is
  expository by design. They are for **checking a heritage claim before you preach it** (next
  section). Expect OCR noise (`Lord» our God`, stray bracketed years like `1844]`, inline footnotes
  and page footers), chunks that start or stop mid-sentence (`show` the adjacent id), titles that
  are just the first line of the chunk, and the same passage under two ids from two Loughborough
  books (#81605, #82065).
- **Adventist Mission stories** are the only Adventist *narrative* illustrations in volume:
  350 to 480 words, named person, dated, URL. Only about a third carry a Scripture reference, so
  `--ref` reaches some and misses the rest, and their only tag is `missions`. Reach them with
  `--tag missions --tradition sda` plus **concrete nouns** (orphanage, hospital, village, tobacco;
  died, cancer, accident), never the theme word. A few dozen end with a Thirteenth Sabbath
  Offering paragraph: trim it when present, and carry the full date from the attribution line
  whenever you name one, even to reject it. Spicer's *Miracles of Modern Missions* (1926) is the
  hidden well for the early Asian field: the Java volcano and the tithe (#84165), Nommensen among
  the Batak at Silindong (#84126), Indian and Philippine rice fields spared from storm and locusts
  (#84162, #84163) and the Tagudin harvest (#84171).

**Two rules, both measured.**

1. **Search the Adventist shelf by text, not by the Adventist tags.** `--tag the-sanctuary` holds
   10 records: church buildings, the Jerusalem Temple and two Jewish Day-of-Atonement memoirs, none
   the heavenly sanctuary; `investigative-judgment` and `sabbath-school` hold 0; `state-of-the-dead`
   holds 4, none Adventist; `the-remnant` 7, none Adventist; `mark-of-the-beast` 1, a news article;
   `health-message` 20, all non-Adventist temperance, diet and alcohol pieces.
   The populated ones are `adventist-heritage` (2,132), `great-controversy` (734) and
   `three-angels-messages` (393, trustworthy only with `--tradition sda`). `spirit-of-prophecy`
   (2,124) is **not** Adventist-only; Holwick records carry it. So on an Adventist-distinctive
   subject: text probes plus `--tradition sda`, and passage mode. `"investigative judgment"` is 92
   hits led by *Great Controversy*; `--ref "Daniel 8:14"` is 19, mixing Loughborough, Olsen and
   Ellen White; `"Joseph Bates" --tradition sda` is 157.
2. **A subject `--tag` combined with `--tradition sda` collapses to It Is Written.** Ellen White
   records carry only `Ellen G. White · <book>` tags, pioneers only `adventist-heritage`, Mission
   stories only `missions`. `--tag resurrection --tradition sda` is 0 hits; `--tag grace
   --tradition sda` is 2. Drop the tag and rely on probes.

Use the type split deliberately: `--tradition sda --tag form:story` is the 2,016 Adventist
illustrations; `--tradition sda --tag form:quote` is the 1,890 Ellen G. White passages, when you
want a citation rather than a story (only 52 are under 150 words, so expect to excerpt). Without
the split a Sabbath search returns pioneer exposition beside one illustration, which reads like the
library is answering but is mostly handing you source text. And there is no Adventist humor, no
Adventist statistic and no Adventist prop lesson in the library at all; the one `form:hymn-story`
hit under `--tradition sda` is a mis-tagged Spicer chapter (#83905).

### Then pull the two or three worth reading

```bash
illus.mjs show 52007 39057
```

`find` prints snippets for triage; `show` prints the whole illustration with its attribution,
every Scripture reference, and the click-through URL where one exists. It cuts off at 1,200 words
and says so; `show <id> --full` prints the rest.

Only a record you passed to `show` counts as read. One you saw as a `find` snippet is *seen*: do
not list it as read, and do not attribute to it a Scripture reference you did not see on its
`ref` line. If a record's click-through URL is dead, search the source site for the title before
quoting from the record alone, and say in the Notes where the text now lives.

### When to give up on Tier 0

The exit code is the gate: `0` means candidates, `1` means nothing — go to Tier 1. (`2` is a bad
flag, an unknown hymn or an ambiguous tag, with the fix on stderr; that is your error, not an
empty library.)

Also go to Tier 1 when the counts are honest but thin. Measured per theme, the library is deep on
grace, the cross, forgiveness, faith in trial, grief and the Second Coming; it is thin, as
*stories*, on the sanctuary service, the state of the dead, justification, health and Adventist
heritage beyond the pioneers, and it holds nothing on Loma Linda as a Blue Zone, NEWSTART, Jones
and Waggoner at Minneapolis, or Mother Teresa, Wilberforce, Nightingale, Spafford and C. S. Lewis
from an Adventist source. A sanctuary question answered with three borrowed courtroom analogies is
a thin answer, and worth saying so to the preacher. It is still better than a vivid one you made up.

Tier 0 **supplements** Tier 1, it does not replace it. If fewer than two local records genuinely
fit, keep the ones that do and go to Tier 1 for the rest — a mixed answer is normal and good.
Running the search is not a reason to use what it returned.

**Don't offer one image three times.** Courtroom / courtroom / courtroom gives the preacher one
choice, not three. Vary the register — a legal picture, a heritage narrative, a domestic or
natural picture — so the candidates are genuinely different ways in.

### Heritage particulars: the library is now where you check them

Adventist heritage stories are told from memory in Adventist circles, which makes invented detail
feel like recollection. This is the easiest place in this skill to fabricate. Two measured
failures, both produced while reaching for heritage content the library did not then hold:

- "Edson had sold what he had and told his neighbours the world was ending" — invented as told.
  The pioneer records now in the library (#84443, #82086) do record that Edson and Cyrenius Smith
  sold their farms, each worth $3,500, **to fund the publishing work**, years after the
  Disappointment; nothing about neighbours or the end of the world, and the year is not in the
  text. Loughborough's account of the cornfield (#81605) has Edson praying and working out the
  sanctuary with Crosier; it says nothing about a sale.
- "Before he stepped behind the veil the high priest put on the jewelled breastplate" —
  Leviticus 16:4 says the opposite: plain linen for the Day of Atonement entry. The breastplate
  and ephod of Exodus 28 belong to the ordinary ministry in the Holy Place.

The pioneer writings in the library are primary or near-primary accounts, so the check is cheap:
before you narrate a date, a place, a sale, a conversation or a who-was-there, probe the name with
`--tradition sda` (or `--concept hiram-edson`, `--concept joseph-bate`), read the `story` and
`study` passages that come back, and keep only the particulars they carry. Know what you are
reading: most of it is Loughborough in 1909 relaying what Edson "told me", not Edson's own
manuscript, and one chunk (#81599) is titled for James White but quotes an editor who was not him.
**If the library and your memory disagree, the library's text wins; if neither has it, drop it or
say so to the preacher.** "The pioneers' own accounts don't mention X and I would want to check
before you preach it" is a useful answer. An unsourced narrative is not.

### The probe match does not screen theology

Nine of every ten records are evangelical, and a record that fits the theme can carry a doctrine
the preacher does not hold. Measured examples:

- **Death:** Moody's deathbed ("I have been within the gates", #65554) and *Two Daughters*
  (#27970, "her eternal existence with the Lord has already begun") assert conscious presence at
  death. The `state-of-the-dead` tag's four records are all evangelical: two argue against soul
  sleep, one surveys the annihilationism debate, one is a neutral outline.
- **Sabbath:** most evangelical Sabbath records mean Sunday; Eric Liddell was a Sunday-keeper;
  *Saturday Is the Sabbath* (#61814, attested three times) is J. Vernon McGee arguing *against*
  seventh-day observance.
- **Atonement:** *The Other Goat* (#88304) makes Jesus the scapegoat; *Great Controversy* (#78302)
  makes the scapegoat Satan.
- **1844:** evangelical Millerite records (#57441, #19825, #36522) repeat the hilltop, graveyard
  and suicide legends, get the dates wrong (April 1843; 1842), and one cites Wikipedia and is
  openly hostile. Use the pioneer accounts (#81596, #81599, #81610) instead.

Frame such a record honestly (Liddell as a model of conviction, not of the seventh day), replace
the sentence that carries the doctrine, or drop it. The foundation's doctrinal alignment applies to
borrowed stories as much as to your own sentences.

### Drop what doesn't fit — never pad the answer with near-misses

Tier 0 hands you a shortlist, not a set of candidates. Filter it hard.

**Every candidate must serve the whole point asked, not the topic it lives near.** If the
preacher asks for *records matter AND Christ is our Advocate right now*, a record that only
establishes "your file exists" is half an answer, and offering it as a candidate spends the
preacher's attention on something they cannot preach. A `--ref` hit is an index match, not a theme
match: *Isaiah 58:9-10* returns a piece about a critical spirit, *Psalm 22:4* a forgiveness story.
Two illustrations that land beat four that are adjacent.

### Tier 0 does not lower the bar

This is a compilation of nearly forty sources, many of them 20th-century collections that
reprinted stories without citing them. About half the records carry no click-through URL and
`attribution` is a single free-text field. **A record found here is a lead, not a verified fact.**

**Attestation measures circulation, not truth.** The C. S. Lewis "it's grace" anecdote is carried
by three compilers and rests entirely on Yancey's retelling; the cake-mix legend is attested three
times; Colonel Davenport and the candles (#3173, attested three times) dates the Dark Day to 1789
when it was 19 May 1780, which every Adventist hearer knows; *A Father Forgives Paco* (#10308,
attested three times) is Hemingway fiction and the record holds two versions that contradict each
other.

**Verify the details inside the record, not just that the record exists.** The library text
itself contains errors, and finding a story here is no evidence its details are right. A worked
example — record #34513, the John Newton conversion story (1,245 words), says in its opening
paragraph that "Their cargo was beeswax and wood, both lighter than water" and, seventeen
sentences later, that "Newton was on a slave ship returning from the tropics where they had
deposited their 'cargo.'" Both cannot be true, and the first is the correct one: the *Greyhound*
was not slaving on the 1748 voyage, and Newton captained slave ships only **after** his
conversion. Retelling that record faithfully puts a false and well-known-to-be-false detail in the
pulpit. The contradiction is visible in the record itself, to anyone who reads it before believing
it.

Record hygiene you will meet, none of it flagged in the row meta:

- composite records with an "Another version" block that disagrees with the first (#10308, #3224);
- records truncated mid-sentence (#82599, #82605, #45144) and chunks that start mid-story (#81685);
- OCR noise in the pioneer and Ellen White texts, footnote markers in the body, stray plate
  captions, and three adjacent Spicer chunks (#84166 to #84168) titled for the wrong volcano;
- email tails and "Posted From:" URLs in Holwick and *Funnies* rows, `\reference{}` markup in
  *5,000 New Sermon Illustrations*, Google-search links in SermonWriter lessons;
- a record in Czech (#19510), and a *Second Coming* tag that admits Advent-wreath ceremonies.

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

- **Ellen G. White's life and visions** — her conversion, the Great Disappointment of 1844, her healing experiences, the Civil War vision, her dream of the ship in the fog (a known illustration of guidance), encounters with poverty in her ministry. Verify via `egw-fetch.sh search` or *Life Sketches*.
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

For Ellen G. White content, follow the foundation's three-tier policy strictly. The 1,890 passages already in the local library (`--tradition sda --tag form:quote`: *Patriarchs and Prophets*, *The Great Controversy*, *Education*) are verbatim text without page numbers; take a distinctive phrase to the foundation's `egw-fetch.sh search` for the refcode. For any other book use `egw-fetch.sh`, which is the sanctioned API path and works on this machine. Do not scrape egwwritings.org pages or call its API anonymously (robots.txt disallows `/api/*`). If you cannot confirm the wording, say so rather than reconstructing it.

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

**Retelling a record adds nothing.** Every particular in your version must be in the record's text
or in a source you opened: no added quantities ("one loaf per family"), reactions ("the question
she never forgot") or places ("London" for "the Blitz"), and no turning the record's indirect
speech into a direct quote. Paraphrase may compress but may not substitute: staff stays staff, not
students. **Precedence:** a dated outside source you opened beats the library record; the record
beats your memory. When two sources split on a figure, keep the particular only if the story
survives either value, and flag the split once. **Cuts are yours to mark:** when you shorten a
quotation, mark every cut with an ellipsis, stop at a clause boundary rather than turning a colon
into a full stop, and never describe an elision you made as the source's own. When you quote a line
from a set-aside record, quote one record exactly and give its id; do not blend wordings across
versions.

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

**Source / type:** [Local library #ID, attributed | Local library #ID, verified | Local library #ID, unverified | Scripture (passage), reached via library #ID | Famous, attributed | Famous, verified anecdote | Original (invented for this sermon)]

**Setup:** 1–3 sentences establishing the scene or person.

**Tension / development:** 2–4 sentences building toward the point.

**Payoff:** 1–2 sentences delivering the moment.

**Bridge to the sermon point:** 1 sentence connecting it back to the point/theme.

**Approximate spoken length:** [X seconds at preaching pace]

**Notes:** [Any verification caveats. E.g., "Quote not verified — paraphrased." Or: "Spafford story well documented in standard hymn-history sources." For a local-library candidate, cite the id and say what you did or could not do to verify it: "Library #52007, attributed to Max Lucado; Thompson's poem is public domain and quoted accurately."]
```

After the candidates, add a one-line recommendation:
> Recommendation: [N] for the opening. It lands the tension early and your audience will feel the weight of it.

The recommendation is the last block of the answer. Records you read and set aside go above it, one
line each, or are left out; the preacher finishes reading on the decision. Count the spoken words
with `wc -w` over the setup-to-bridge prose and divide by 150; report the count rather than an
estimate, and say so if it falls outside the budget. "Attributed" means the record names a source
you have not checked; "verified" means you compared the record against that source or a primary
text and the Notes say what you compared. For Indonesian output translate the labels: Sumber /
jenis, Pembukaan, Ketegangan, Puncak, Jembatan ke pokok khotbah, Perkiraan panjang, Catatan.

---

## Indonesian Output

For Indonesian sermons, illustrations should:

- Use settings, names, and references that resonate culturally (Indonesian cities, Indonesian historical events, kampung life, traffic in Jakarta, fishing villages, Indonesian Adventist mission stories).
- Avoid heavy reliance on Western pop culture references unless the audience is bilingual urban Adventist youth.
- Indonesian Adventist heritage stories (e.g., the founding of UNAI / Klabat / Bandung Adventist work, mission to Sumatra and Sulawesi) are gold when verifiable. The library's Indonesian block in `references/illustration-sources.md` lists what it holds: Adventist Mission stories from Papua, Ambon and Klabat, Spicer's 1926 accounts of Java and the Batak, and the Our Daily Bread pieces set in Jakarta and Sulawesi.

**For a Deaf congregation** (Jemaat Efata Tuli, Jakarta), every illustration must be seen or touched: a prop, an object lesson, a live demonstration, a scene the interpreter can show. Nothing that depends on music, voices, whispers, tuning or sound, and no hearing-based verbs. The library's route to prop lessons is `--concept children-sermon` (the SermonWriter object lessons); its hymn stories and most of its humor are sound-based and do not transfer. Screen every record for sound words before offering it, and say in one clause per candidate which sound words you removed; the reference file's special-audience block has the measured commands and example records. Sign interpretation runs slower than speech: this congregation takes about 85 words a minute, so a 2-minute slot is roughly 170 words, not 300. When `--concept children-sermon` holds nothing for the passage, build the demonstration yourself from a fact a record or a Tier 1 source carries, and label it as staging designed for this sermon, with the fact's source.

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

- `references/illustration-sources.md` — per theme: the measured library probe sets, real vocabulary, record ids worth reading and the ones that are wrong, what the library does not hold, and the outside wells to go to next; plus a field guide of the CLI's gotchas and blocks for a Deaf congregation, statistics, humor, hymn stories and heritage checking.
- `/Users/edmundsitumorang/DEV/illustration-library/` — the local library (over 100,000 records; `illus.mjs --help` prints the live count) and its CLI. `README.md` there documents the query model and the sources; `bin/illus.mjs find --help` documents the flags; `node test-illus.mjs` is its regression suite.

---

**Why this works:** Most AI-produced illustrations are either fabricated quotes or sentimental clichés. The user's instinct is right — famous illustrations resonate because they're already woven into the cultural fabric. They land harder than anything we can invent. Originals are the fallback, not the default. And the verification rule keeps the pulpit honest.
