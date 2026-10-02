# Illustration Sources by Theme

Two kinds of pointer per theme. **Library (Tier 0)** is what the local illustration library
actually returns for the theme: the probe sets that worked, the real vocabulary, the records worth
handing over and the ones that are wrong, and what is not there. **Wells (Tier 1)** are the
well-attested outside sources to go to when the library is thin. Use both; verify before using
either. Quotes must be checked; unverifiable material gets paraphrased or dropped.

Every library figure here was **measured on 2026-10-02 and re-checked on 2026-10-03** by running the CLI. The library grows, so
treat counts as the shape of the shelf, not the inventory; the header the CLI prints is the truth
on the day. Commands are given as the arguments to `illus.mjs` (`find …`, `show …`, `vocab …`);
the full path is `/Users/edmundsitumorang/DEV/illustration-library/bin/illus.mjs`. Record ids are
stable.

---

## Field guide: how the library behaves

Read this once. Every theme block below assumes it.

**Probes**

- A multi-word probe is ANDed words, not a phrase. `"father ran"` matches Peter Pan. To search a
  phrase, nest literal quotes inside the shell argument: `'"hound of heaven"'`.
- Stemming is aggressive: prodigal→prodigality, cross→crossing, temperance→temper, diet→Diet of
  Worms, timor→timorous, "it is finished"→"its finish"; unquoted `second coming` (891 hits) admits
  rows the phrase form (570) excludes. Numbers are weak probes (`1888` is 135 hits led by a yawn
  record) and initials are rejected outright (`E. J.` exits 2: one-character tokens are dropped);
  `seventy times seven` tokenises into a Daniel prophecy passage.
- Proper nouns are not vocabulary: `vocab spafford` exits 1, the plain probe works. Surnames
  collide (Isaac Newton, Walt Mueller, Martin Luther King, Joyce Brothers): pair a name with a
  place or object. Spelling variants do not fold (`Mueller` 159 vs `Muller`/`Müller` 54; the
  primary source uses *Mueller*).
- Only rows that matched 2+ probes are reliably on theme. Single-probe hits on a common word
  (`grace` 6,474, `judge` 3,052, `cross` 5,487, `why god` 8,012) are filler. Overlapping probes
  inflate the count without adding relevance.

**Filters**

- `--attested` and `--tradition sda` are mutually exclusive in practice: no Adventist source is
  cross-compiled, so every combination measured returned 0. Run them as separate passes.
- Pair `--attested` with `--max-words 300`: alone it floats 11,000- and 15,000-word anthology
  records (#72498, #108379) that matched two probes by accident.
- A subject `--tag` with `--tradition sda` collapses to It Is Written, because Ellen White
  records carry only `Ellen G. White · <book>`, pioneers only `adventist-heritage`, Mission
  stories only `missions`. `--tag resurrection --tradition sda` = 0.
- Any `--tag` without `--max-words` admits Holwick sermon manuscripts (1,000 to nearly 11,000
  words) that carry subject tags.
- `--tag form:study` resolves to `form:statistic`; the header shows it. There is no way to filter
  to the `study` type; read the row marker.
- `--tradition christian` is a small bucket (Cybersalt, the SermonWriter children's sermons, Bible
  Topics A-Z, *The Funnies*, the fact sheets; about 5,000 records), not a superset of `evangelical`.
- `--tag spirit-of-prophecy` is not Adventist-only (Holwick and The Pastor's Workshop carry it).

**Passage mode**

- `--ref` with probes is an OR pool, not a filter: rows matching only a probe still appear; read
  `probe+@ref` in the probe slot. It is an appender, not a reranker; passage-indexed rows appear
  where the text matches leave room.
- Small passage indexes are precise (Mark 2:27 is 31 records, Isaiah 58:13-14 26, Galatians 2:16
  52, Genesis 45 34); large ones are swamped by long records (Romans 3, Hebrews 11 at 912,
  Ephesians 2:8-9 at 299). Add `--max-words 300` to any passage pass.
- Single-chapter books need the chapter: `--ref "3 John 1:2"` (24 verse-indexed hits). When a
  precise tier holds fewer than three records the CLI falls back to the book-wide set and prints
  the NOTE "topical, not textual" (`--ref "Nahum 3:1"` shows it); that NOTE is the only warning the
  hits are not verse-specific, and `--wide` adds nothing once it has fired.
- About a third of Adventist Mission records (156 of 521) carry a Scripture reference; `--ref`
  reaches those (#80914 via Luke 15:11-32) and misses the rest.

**Hymns**

- `--hymn` links are made by exact title (478) or by the hymn's first line (636), so a share of
  rows merely mention the hymn; add `--tag form:hymn-story` for its own story. The header's SDAH
  number maps to LSEL through the Lagu Sion database.
- A title with a leading apostrophe (`'Tis So Sweet`) exits 2; drop it. Probes AND with the hymn
  link, so a hymn with two linked records can return 0 with probes.
- Adventist hymn links are rare (13 first-line matches: 8 pioneer, 5 Ellen White) and none is a
  hymn story; `--hymn … --tradition sda` is almost always 0.

**Records**

- Attestation measures circulation, not truth: #3173 (×3) misdates the Dark Day to 1789; #10308
  (×3) is Hemingway fiction with two contradictory versions in one record; #73252 (×3) rests on
  Yancey's retelling; #43045 (×2) is the "no word for forgiveness" trope.
- Twins across compilers differ in citation quality: #29911 carries the Craddock page number that
  its twin #54182 lacks. When a story exists in several versions (Spafford ×9), compare them with
  one `--hymn` or `--tag` call before choosing.
- Hygiene: "Another version" blocks that disagree (#10308, #3224); truncation mid-sentence
  (#82599, #82605, #45144); chunks starting mid-story (#81685, `show 81684`); OCR noise and
  footnote markers in pioneer and Ellen White text; `\reference{}` markup; email tails; a Czech
  record (#19510); Precept Austin snippets cut from longer pages.
- The row type is unreliable for "is this a narrative": Holwick nine-word outline stubs, Pastor's
  Workshop bare quotations and pioneer exposition are all `story`. Word count is the honest signal.
- Ellen White chunks give book and year but **no page**; take a distinctive phrase to
  `egw-fetch.sh search` for the refcode before citing.
- Our Daily Bread records are the most dependable hand-overs: 150 to 300 words (usually 200 to
  230), author, date, URL; only about one in twelve is attested. Stored URLs now return 404 without
  a `/US/` segment: rewrite to `odb.org/US/YYYY/MM/DD/slug` and check before handing one over.

---

## Grace / Undeserved Favor

**Library (Tier 0).**

```
find "undeserved" "grace" "prodigal" "mercy" --attested --max-words 300 -n 10
find --hymn "Amazing Grace" --tag form:hymn-story -n 10
find "prodigal" "grace" "undeserved" --ref "Luke 15:11-32" --tradition sda -n 10
find "grace" "pardon" --tag form:story --attested --max-words 300 -n 10
```

Vocabulary: `--tag grace` (426), `--tag forgiveness` (736), `--tag legalism` (279), `--tag lostness`
(136), `--concept prodigal-son` (40), `--concept cheap-grace` (38), `--hymn "Amazing Grace"` (SDAH
108, 21 linked), `--hymn "Come, Thou Fount of Every Blessing"` (SDAH 334, 13), `--hymn "Marvelous
Grace"` (SDAH 109, 2).

Worth reading: #87100 (Our Daily Bread, 207w, Newton's 1748 storm; correctly says he left the
slave trade "in time") · #54182 / #29911 (Craddock's lawyer who thinks the prodigal should get six
years; #29911 has the page cite) · #80914 (Adventist Mission 2018, *Prodigal Daughter*, Trinidad
congregation stops the sermon to sing; dated, named) · #39018, #39072, #39033 (It Is Written short
grace stories; #39033 is the seeking father, a lost-sheep text indexed to Luke 15:22-24) · #86567
(Our Daily Bread, indexed to Ephesians 2:8-9) · #9364 (a ten-second grace/mercy couplet).

Wrong or weak: #19803 (Spafford with three daughters and a storm, both wrong); #705 (Napoleon's
mother, attribution literally "Unknown"); #73252 (Lewis "it's grace", ×3 but only via Yancey);
#6055 (Scottish doctor, unnamed); #63432 (a 909-word composite: a seven-point outline followed by three full stories).

Adventist coverage: thin but real. `--tag grace --tradition sda` is 2 hits; the productive route
is `--ref "Luke 15:11-32" --tradition sda`. No Adventist hymn story for Newton or Spafford.

Lost sheep (Luke 15:1-7): the best Adventist record, #39033 (Guo Gangtang's 24-year search, It Is
Written Vol. 2), quotes Luke 15:4-7 in full but is indexed to Luke 15:8-10 and 15:22-24, so
`--ref "Luke 15:1-7"` misses it; `find "ninety-nine" --tradition sda` reaches it (1 hit). #38996
(the ring in the sewer, It Is Written) is indexed to Luke 15 and does surface under the passage.

**Wells (Tier 1).**

- **John Newton** and "Amazing Grace"; **Horatio Spafford** and "It Is Well with My Soul": both
  well documented in standard hymn histories (Osbeck is in the library).
- **Charles Spurgeon** on grace, verifiable in his published sermons.
- **Ellen White**, *Steps to Christ*: "The Sinner's Need of Christ", "Repentance", "Confession",
  "Consecration". Fetch with `egw-fetch.sh`; *Steps to Christ* is not in the library.
- **Augustine**, *Confessions*: the pear tree.
- **The prodigal son** retold (Keller's *The Prodigal God*; cite him).

---

## Sabbath / Rest

**Library (Tier 0).**

```
find "sabbath" "rest" "delight" "seventh day" --ref "Mark 2:27" --max-words 300 -n 10
find "sabbath" "kept the sabbath" "seventh-day" --tradition sda --tag form:story --max-words 400 -n 15
find "liddell" "heschel" "bates" -n 10
find "sabbath" --concept joseph-bate -n 8
```

Vocabulary: `--tag sabbath` (118, only 3 inside `--tradition sda`), `--tag rest` (130), `--concept
sabbath-rest` (10), `--concept joseph-bate` (33, singular slug), `--tag adventist-heritage` (2,132).
Mark 2:27 (31 records) and Isaiah 58:13-14 (26) are precise passage indexes; Genesis 2:1-3 (148)
is swamped by long creation passages.

Worth reading: #39057 (It Is Written, *The Metronome*, 123w, indexed to all three anchor texts) ·
#83047 (*Patriarchs and Prophets*, God "rested, not as one weary, but as well pleased": the delight
note in Ellen White's words; PP 47) · #81679 (Loughborough: Bates on the New Bedford bridge, "the
seventh day is the Sabbath of the Lord our God") · #55059 and #55030 (Liddell, accurate; the camp
refereeing story is Sabbath as mercy) · #54742 (Heschel, "a whole people in love with the seventh
day") · #26160 (A. J. Jacobs discovers the Sabbath as joy; well documented) · #81166, #81295,
#81127 (Adventist Mission: Malawi exam, the monkeys that stayed away on Sabbath, the farmer who
found the Sabbath from Exodus 20 alone) · #54722 (two Shabbat candles, remember and observe).

Wrong or to frame: #61814 (×3, McGee arguing *against* the seventh day; useful only as the
objection); most evangelical Sabbath records mean Sunday, and Liddell was a Sunday-keeper; #70708
repeats the *Chariots of Fire* last-minute-swap falsehood; #54720 (Skylab "strike") is disputed;
#39120 reads as legend.

Adventist coverage: 750 hits under `--tradition sda`, most of them pioneer exposition on the
doctrine's history. "Delight" appears in 122 Adventist records but none co-occurs with "sabbath";
Heschel's "palace in time" is not in the library.

**Wells (Tier 1).**

- **Joseph Bates** (in the library via the pioneers); **Eric Liddell** (biographies; frame as
  conviction); **Heschel**, *The Sabbath* (cite him).
- **Ellen White**: *Patriarchs and Prophets* on Creation and Sinai (in the library); *Desire of
  Ages* on the Mark 2 / Luke 6 conflicts (fetch).

---

## Second Coming / Hope

**Library (Tier 0).**

```
find "second coming" "blessed hope" "Jesus returns" --max-words 300 -n 12
find "second coming" "blessed hope" "Jesus returns" --tradition sda -n 12
find "blessed hope" "glorious appearing" --ref "Titus 2:13" --max-words 300 -n 10
find "disappointment" "1844" "tarrying time" --tag adventist-heritage --max-words 300 -n 8
```

Vocabulary: `--tag second-coming` (346; admits Advent-wreath ceremonies), `--tag hope` (389),
`--tag disappointment` (101), `--concept william-miller` (40), `--concept hiram-edson` (12),
`--tag three-angels-messages` (393, only clean with `--tradition sda`), `--hymn "Mine Eyes Have
Seen the Glory"` (SDAH 647, 11), `--hymn "When the Roll Is Called Up Yonder"` (SDAH 216, 3).

Worth reading: #38938, #38939, #39089, #39091 (It Is Written: Nessie, the missed flight, short
and appeal-ready) · #85875 (Our Daily Bread, "You will deliver": certainty amid questions, includes
the resurrection) · #63804 (the caretaker's "Today, sir, today!"; anonymous) · #81596 (Loughborough,
"disappointed, but not discouraged": the first-person Disappointment) · #22388 (G. Campbell Morgan,
third-hand) · #3173 (Davenport and the candles, ×3: **fix the date to 19 May 1780**) · #11048 (the
bridegroom at midnight; dated moralising needs re-voicing).

Wrong: #57441, #19825, #36522 (evangelical Millerite records with graveyards, suicides and wrong
years; none mentions ascension robes; #36522 cites Wikipedia and is hostile). Use #81596, #81599, #81610 instead.

Adventist coverage: real but lopsided: It Is Written for stories, pioneers for Miller, Edson and
the Disappointment (mostly `study`), *Great Controversy* chunks for exposition. `"October 22 1844"`
is 6 hits; `"Hiram Edson"` 12.

**Wells (Tier 1).**

- **William Miller** and 1844 (pioneers in the library; *Great Controversy* ch. "An American
  Reformer"); **Hiram Edson** (Loughborough #81605; Edson's own manuscript via the White Estate).
- **C. S. Lewis**, *The Last Battle*, the closing chapters.

---

## State of the Dead / Resurrection Hope

**Library (Tier 0).**

```
find "sleep in Jesus" "dead know nothing" "resurrection morning" "Lazarus come forth" --max-words 300 -n 12
find '"sting of death"' "firstfruits" '"twinkling of an eye"' --ref "1 Corinthians 15" --max-words 300 -n 10
find "asleep in Jesus" "conditional immortality" "dead are asleep" --tradition sda -n 12
find "earth is receding" "Moody" -n 8
```

Vocabulary: `--tag resurrection` (610), `--tag death` (991), `--tag immortality` (43), `--tag
occasion:funeral` (151), `--concept life-after-death` (47), `--concept deathbed-conversion` (22),
`--hymn "When We All Get to Heaven"` (SDAH 633, 3). `--tag state-of-the-dead` has 4 evangelical
records: a neutral outline (#1635, quoting Luther for sleep), one on annihilationism (#20129) and
two leaning against soul sleep; `--tag resurrection --tradition sda` is 0.

Worth reading: #86096 (Our Daily Bread, *At the Cemetery*: "One day, Jesus will again be at the
cemetery", resurrection at the coming) · #13519 (the father's hand with the stinger, ×2; a parable)
· #89353 and #85438 (Our Daily Bread: reunion at the coming; Sartre's hope without foundation) ·
#78440 (*Great Controversy*, Luther: "the dead are asleep, and feel nothing at all"; footnote
markers in text) · #3521 ("Good night, Clarence!", via Campolo) · #82599 (Voice of Prophecy,
"Lazarus came OUT"; truncated, use the first paragraph) · #1635 (Luther, "Dr. Martin, get up!",
secondhand).

Wrong or to screen: #65554, #14018 (Moody "within the gates") and #58010 (the same deathbed
without that line): conscious entry at death;
#27970 ("her eternal existence has already begun": replace the sentence or drop); #43654; the
Spafford records disagree on the number of daughters (#64332 four, #19803 three). `--ref
"Ecclesiastes 9:5"` (70) leads with marriage humour; only #20129 touches conditional immortality.

Adventist coverage: solid for doctrine (*Great Controversy* "The First Great Deception" in chunks,
carrying Luther and Tyndale), one Adventist story (#82599). *Desire of Ages* on Lazarus and Jairus
is not in the library; fetch it.

**Wells (Tier 1).**

- **Ellen White**, *Great Controversy* "Can Our Dead Speak to Us?" (library); *Desire of Ages* on
  Nain, Jairus, Lazarus (fetch).
- **The widow of Nain, Jairus's daughter, Lazarus** retold with resurrection, not disembodied
  immortality, as the hope.

---

## The Sanctuary / Christ Our High Priest / Investigative Judgment

**Library (Tier 0).**

```
find '"high priest"' "sanctuary" "advocate" '"day of atonement"' --tradition sda -n 12
find "courtroom" '"defense attorney"' "lawyer pleads" --max-words 400 -n 8
find "scapegoat" '"two goats"' '"mercy seat"' --max-words 300 -n 8
find '"Hiram Edson"' "Crosier" "1844" --tradition sda -n 10
```

Vocabulary: `--tag atonement` (240), `--tag judgment` (372, mixes judgmentalism with eschatology),
`--tag great-controversy` (734), `--concept advocate` (24), `--concept intercession` (35),
`--concept hiram-edson` (12). `--tag the-sanctuary` (10) is church buildings; `--tag
investigative-judgment` is empty. `"Azazel"` is 1 record; use *scapegoat*.

Worth reading: #39094 (It Is Written, *When the Evidence Is Against You*: the affirmative defense,
Satan as prosecutor, Christ as Advocate; **indexed to Romans 3, so a 1 John 2:1 passage pass misses
it**) · #91103 (Our Daily Bread, Gideon v. Wainwright and the court-appointed advocate; the record
misspells Wainwright and dates the petition June 1962, usually January) · #78302 (*Great
Controversy*, the Adventist position in one paragraph: 1844, high priest, scapegoat as Satan) ·
#81605 (Loughborough's Edson account, for checking) · #84414 (Olsen 1925, the sanctuary and the
Sabbath, Leviticus 16) · #34722 (advocate who becomes judge: "before I was your advocate; now I am
your judge"; floating anecdote, preach as parable).

Wrong or to reframe: #88304 (Our Daily Bread, du Maurier's *Scapegoat*: makes Jesus the scapegoat;
Adventist reading makes it Satan, use the ceremony only); #12629 and #38513 (the two
`the-sanctuary` + "day of atonement" hits: Jewish legalism and a convert's Christmas, not the
doctrine).

Adventist coverage: the strongest `--tradition sda` pass of any theme (15 of 126 pooled matched two
probes) and almost all of it exposition: *Great Controversy* "What Is the Sanctuary?" and "In the
Holy of Holies" in chunks (#78291 to #78311), Loughborough, Spicer, Olsen. One Adventist story
(#39094). The narrative load falls on evangelical courtroom records; say so to the preacher.

**Wells (Tier 1).**

- **The Day of Atonement** in Second Temple practice (Mishnah *Yoma*; Edersheim, *The Temple*).
- **Ellen White**, *Patriarchs and Prophets* sanctuary chapters (library); *Great Controversy*
  sanctuary and judgment chapters (library).
- **Courtroom and advocate** scenes: use a real case you can verify (Gideon, #91103) or frame as
  "imagine".

---

## Faith / Trust in Trial

**Library (Tier 0).**

```
find '"fiery furnace"' '"lions den"' '"but if not"' --ref "Daniel 3" --max-words 300 -n 8
find "Habakkuk" '"fig tree"' '"yet I will rejoice"' --max-words 300 -n 8
find "Mueller" --min-words 200 -n 20
find '"Corrie ten Boom"' "Ravensbruck" "Betsie" -n 8
```

Vocabulary: `--tag faith` (861), `--tag trust` (425), `--tag trials` (609), `--tag persecution`
(350), `--tag providence` (380), `--concept bonhoeffer` (23), `--hymn "Tis So Sweet to Trust in
Jesus"` (SDAH 524, 4; no apostrophe), `--hymn "Great Is Thy Faithfulness"` (SDAH 100, 5), `--hymn
"Trust and Obey"` (SDAH 590, 3). The spelling is *Mueller*: the library holds his own *Answers to
Prayer* (1896) under that spelling, and it surfaces only with the bare name plus `--min-words 200`.

Worth reading: #87060 (Our Daily Bread, built on "But if not", Daniel 3:17-18) · #94832 and #94838
(Mueller's diary: 22 July 1838, £20 and Hebrews 13:8; "unbelief in the hour of trial" is the real
danger) · #89274 (Our Daily Bread on Habakkuk's choice) · #43663 (the farmer who stands and recites
Habakkuk 3:17-18; unnamed) · #10282 (Glenn Chambers' "WHY?" note, 1947; two versions stitched, use
the Swindoll half) · #108693 (Mueller's desk motto; use the Mueller paragraph only, not the song
lyric).

Pitfalls: Corrie ten Boom here is five retellings of the fleas story plus three longer pieces
(the 37-word "no pit so deep" line, #14815, surfaces only with `--max-words 40`); the guard story
lives under Forgiveness. Bare exemplar names return nine-word epigrams; pair the name with
Bristol, Ravensbruck, Betsie. The famous breakfast-table milk-cart story did not surface.

Adventist coverage: thin: *Great Controversy* "Time of
Trouble" and "Luther Before the Diet", *Education* on Hebrews 11, James White's tamed horse and the
lions (#81697, with a longer parallel #82074 from Loughborough's 1892 book), three short It Is Written trust pieces (#38976, #38993, #39006).

**Wells (Tier 1).**

- **Corrie ten Boom**, *The Hiding Place*; **Bonhoeffer** (Bethge); **Hudson Taylor**; **George
  Mueller** (his journals are in the library).

---

## Service / The Poor / Ministry

**Library (Tier 0).**

```
find '"least of these"' '"cup of cold water"' "mother teresa" --ref "Matthew 25:31-46" --max-words 300 -n 8
find '"pure religion"' "orphans" "widows" --ref "James 1:27" --max-words 300 -n 8
find "orphanage" "hospital" "clinic" "neighbor" --tag missions --tradition sda -n 10
find "poor" "hungry" "homeless" --tag compassion --max-words 300 -n 8
```

Vocabulary: `--tag servanthood` (568), `--tag compassion` (621), `--tag poverty` (366), `--tag
missions` (899), `--tag missionaries` (182), `--concept mother-teresa` (30), `--concept wilberforce`
(16), `--hymn "There's a Wideness"` (SDAH 114, 7), `--hymn "Rise Up, O Church of God"` (SDAH 615,
3). `--tag health-message` (20) is temperance essays, not medical mission. `"nightingale"` alone (49)
mixes the bird with Florence; `"florence nightingale"` (17) is clean.

Worth reading: #3181 (the boy's eggs and "how much do the rest of you care?", ×3, 113w) · #73236
(Claiborne among the homeless, ending on Teresa's "distressing disguise") · #52355 (Brengle set to
blacking boots; **the record's 1878 is wrong, 1887**) · #28285 / #19735 (the anti-Matthew-25
litany; #19735 without the folklore framing) · #3625 (Muggeridge and Teresa, compressed) · #83626
(*Patriarchs and Prophets* "God's Care for the Poor": "as if shown to himself"; PP ch. 51) · #81077
(Adventist Mission 2021, the physician taken in by an Adventist clinic) · #81332, #81002, #80931
(Adventist Mission orphanage and adoption stories) · #65333 (Nightingale's diary at 30) · #34491
(Wilberforce via Colson; "sixty charities" is usually 69).

Adventist coverage: Ellen White's "God's Care for the Poor" (#83625 to #83627) is reached by probe
(`find "poor" "benevolence" --tradition sda`: 3 of 77 pooled matched both), not by passage, since
the `--ref "Matthew 25:31-46" --tradition sda` pass returns nine *Great Controversy* and pioneer
chunks with nothing on the poor; pioneer `study` passages on the sanitarium and medical missionary college (for
checking, OCR noise); Mission stories reachable only by concrete nouns. Mother Teresa, Wilberforce
and Nightingale are absent from Adventist sources.

**Wells (Tier 1).**

- **Mother Teresa**: documented episodes, not meme quotes. **Wilberforce**, **Nightingale**.
- **Adventist medical mission**: Loma Linda and mission hospitals in *Adventist Heritage*; the
  pioneers in the library carry Battle Creek and Kellogg's 1891 charity figures (#81858).

---

## Suffering / Lament / Grief

**Library (Tier 0).**

```
find "spafford" "daughters" --hymn "It Is Well With My Soul" -n 11
find "died" "cancer" "accident" "funeral" --tag missions --tradition sda -n 10
find "lewis" "observed" "wife" "joy" -n 8
find '"thorn in the flesh"' '"grace is sufficient"' "weakness" --ref "2 Corinthians 12:9" --max-words 300 -n 8
```

Vocabulary: `--tag grief` (244), `--tag suffering` (552), `--tag comfort` (146), `--tag tragedy`
(261), `--tag problem-of-evil` (332), `--concept lament` (20), `--concept c-s-lewis` (23), `--hymn
"Be Still, My Soul"` (SDAH 461, 5), `--hymn "Does Jesus Care?"` (SDAH 181, 3), `--hymn "God Will
Take Care of You"` (SDAH 99, 4). `vocab job` is employment; `--ref "Job 1"` under `--tradition sda`
is 0. "Grief observed" tokenises into grief AND observed; Lewis's "God's megaphone" is there
(#16757, #60731) under the plain probe `"megaphone"` (37).

Worth reading: #64332 (Osbeck's full Spafford account; misspells *Ville du Havre*) · #62806 (the
one-minute Spafford, correct) · #12578 (John G. Paton loses wife and infant, 1859; dates compressed)
· #27970 (Branon's daughter and Jairus, 2002; replace the immediate-presence sentence) · #81025
(Adventist Mission 2020, *Losing Four Sons in Poland*, explicitly Job-shaped; contains a suicide,
handle pastorally) · #81060 (plane crash, 1 Thessalonians 4:13-14) · #90579 (Our Daily Bread,
refuses the glib Romans 8:28, then Fanny Crosby) · #86423 (the thorn, Oswald Sanders) · #10552
("Thank you for my hurting", sourced 1985) · #7963 (the genuine *Grief Observed* "door slammed"
passage, stops there) · #52800 (Lewis and loss, Digory and Aslan's tears) · #55110 (N. T. Wright on
lament) · #51746 (Tehillim is mostly laments) · #59510 (Edgar Jackson's definition of grief:
concrete, visual, works for a Deaf congregation).

Adventist coverage: no personal-grief story outside Adventist Mission; Ellen White gives Jacob
mourning Joseph (#83239) and doctrine. Spafford and Lewis are evangelical only; the hymn gazetteer
(SDAH 530, 461, 181) is the bridge.

**Wells (Tier 1).**

- **Job** retold from the ash heap; **Spafford**; **Lewis**, *A Grief Observed*.
- **Ellen White**, *Education* "Lessons of Life"; *Ministry of Healing* "In Contact with Nature"
  (fetch; *Education* is in the library).

---

## Forgiveness / Reconciliation

**Library (Tier 0).**

```
find "forgive" --tag forgiveness --attested --max-words 300 -n 15
find '"Corrie ten Boom"' "Ravensbruck" "guard" -n 12
find "forgive" "reconciled" "Joseph" "brothers" --tradition sda -n 15
find "forgive" '"seventy times seven"' "Joseph" --ref "Genesis 45" --max-words 300 -n 12
```

Vocabulary: `--tag forgiveness` (736), `--tag reconciliation` (214, Family facet), `--concept
unforgiveness` (33), `--concept racial-reconciliation` (30), `--concept joseph` (29; `vocab joseph`
offers Bates first), `--concept pardon` (52), `--hymn "There's a Wideness"` (SDAH 114, 7), `--hymn
"Depth of Mercy"` (SDAH 521, 1).

Worth reading: #52931 (the canonical ten Boom and the Ravensbrück guard, indexed to all three
anchors; paraphrase, the record quotes at length) · #43017 (the thirty-second version, 1947
Munich) · #83272 and #83273 (*Patriarchs and Prophets* on Genesis 50:15-21: "am I in the place of
God?" and "this fact did not lessen the guilt of his brothers") · #13774 (Korean War father takes in
his son's killer; unverifiable particulars) · #6055 ("Forgiven, too poor to pay") · #38491 (Brandt
Jean and Amber Guyger, Dallas 2019, named and dated; read Holwick's appended note on the
controversy) · #39118 (It Is Written, Professor Blackie's apology) · #38913 (It Is Written, the
prime minister's cat; thin).

Wrong or to screen: #10308 (Paco: Hemingway fiction, two contradictory versions); #17576 (van der
Broek TRC story: famous, unverifiable, two inconsistent versions); #43045 ("no word for
forgiveness", ×2, dubious); #1316 (Clara Barton, "Unknown").

Adventist coverage: Joseph typology from Ellen White is strong; It Is Written supplies "God forgives
you" anecdotes rather than reconciliation; no Adventist record touches ten Boom, and the only two
indexed to Luke 23:34 (#83157, Ellen White on Abraham's intercession; #81121, a Mission story at
chapter level) are not forgiveness illustrations.

**Wells (Tier 1).**

- **Corrie ten Boom** (library); **Joseph** (Genesis 45, 50; Ellen White in the library).
- **Lincoln**, "Do I not destroy my enemies when I make them my friends?": contested, verify.

---

## Salvation by Faith / Justification

**Library (Tier 0).**

```
find "justified" '"righteousness by faith"' --ref "Galatians 2:16" --max-words 300 -n 10
find "faith" "righteousness" --concept justification-by-faith -n 12
find "Aldersgate" '"strangely warmed"' -n 10
find '"justified by faith"' "imputed" '"Martin Luther"' "Minneapolis" --tradition sda -n 15
```

Vocabulary: `--tag justification` (81; 1 inside `--tradition sda`, the It Is Written courtroom record #39094), `--concept
justification-by-faith` (15), `--tag legalism` (279), `--concept works-righteousness` (73),
`--concept self-righteousness` (46), `--concept martin-luther` (20; bare *Luther* pulls King),
`--concept wesley` (26), `--concept reformation` (32), `--tag assurance` (258). Use `imputed` or
`robe of righteousness` rather than "righteousness of Christ", which tokenises loosely.

Worth reading: #15568 (red glass, blue glass: imputation in 83 words) · #14453 (Moody's Manchester
inquirer: Noah's feelings, Noah's righteousness, or the ark?) · #51459 (Luther's hours in the
confessional; genuine 1545 Preface phrases) · #12713 (the full Wesley arc with the accurate
journal entry; says "Oxford Seminary", it was the University) · #108536 (Packer: Aldersgate beside
Pascal's "FIRE", dates correct; trim one word) · #83430 (*Patriarchs and Prophets* "The Law and
the Covenants": "His obedience is accepted for us") · #77987 (*Great Controversy* on the effect of
Luther's preaching) · #69918 (Queen Victoria's rag room, "filthy rags" to white paper; "Selected") ·
#84826 (Olsen 1925: the only passage that names righteousness by faith at Minneapolis; `study`,
OCR-damaged, **does not name Jones or Waggoner**).

Wrong or to frame: #59071 (Luther's three scrolls: legend via Kurt Koch, ×2); #12775 (Scala Sancta
"just shall live by faith", the doubtful late recollection); #47524 (the "toilet" tower reading presented as
fact); #69804 (the "old blanket" image, retell without the dialect); #2897 (polemical).

Adventist coverage: Ellen White is strong for a Romans 5:1 or Luther sermon. **1888 as narrative is
essentially absent** (#84825, #84826 only). E. J. Waggoner and A. T. Jones appear only as names in
administrative lists (`'"E. J. Waggoner"'` 2 hits, `'"A. T. Jones"'` 3, none about Minneapolis); the
bare probe `Waggoner` mixes J. H. Waggoner with a Texas oilman, a LifeWay researcher and Aesop's
waggoner.

**Wells (Tier 1).**

- **Luther** (tower experience: be careful with wording); **Wesley**, Aldersgate, 24 May 1738
  (journal); **1888 Minneapolis**, Jones and Waggoner: Knight, *A User-Friendly Guide to the 1888
  Message*; Ellen White, *Selected Messages* vol. 1; *Christ's Object Lessons* on the Pharisee and
  the publican (fetch).

---

## Health and the Body

**Library (Tier 0).**

```
find '"body is a temple"' "temple" "health" --ref "1 Corinthians 6:19-20" --tradition sda -n 10
find '"body is a temple"' "Daniel" "vegetables" "diet" --tradition sda -n 12
find "temple" "sugar" "exercise" --tag health --max-words 300 -n 10
find "tobacco" "alcohol" "vegetarian" --tag missions --tradition sda -n 8
```

Vocabulary: `--tag health` (190), `--tag self-control` (202), `--concept diet` (34), `--concept
exercise` (30), `--concept temperance` (16; the probe *temperance* stems to *temper*). `--tag
health-message` (20) contains **zero Adventist records**. `--ref "3 John 1:2"` parses; `"3 John
2"` does not. `--ref "Daniel 1" --tradition sda` holds 0 precise records.

Worth reading: #77753 (*Education* "Study of Physiology": the body-as-temple passage itself) ·
#83417 (*Patriarchs and Prophets*, Nadab and Abihu, quotes 1 Corinthians 6:19-20 and 10:31) · #38970
and #39070 (It Is Written: the Harvard sugary-drink finding; the 2016 Boston Globe op-ed; both need
the source named) · #81842 (J. N. Andrews via Loughborough, "our bodies are the temples") · #4430
(Thoreau, "every man is the builder of a temple"; say "from *Walden*", not 1845) · #81289 and #81251
(Adventist Mission conversions through alcohol and tobacco), #80979 (a lifelong Adventist's
reconsecration after quitting drink).

Not in the library: Loma Linda as a Blue Zone (2 chronology lines), NEWSTART, the eight laws of
health, Kellogg as anything but institutional history (24 pioneer chunks, 10 typed `story` and 14 `study`, plus one Mission story, #80951).

**Wells (Tier 1).**

- **Daniel 1**; **Ellen White**, *Ministry of Healing*, *Counsels on Diet and Foods* (fetch).
- **Kellogg and Battle Creek** (verify specifics; Schwarz, *John Harvey Kellogg, M.D.*).
- **Blue Zones**: Buettner, *National Geographic* (2005); the Adventist Health Studies.

---

## Cross / Atonement

**Library (Tier 0).**

```
find "Calvary" "Barabbas" "substitute" --attested --max-words 300 -n 10
find "Barabbas" "substitute" "Lincoln" "ransom" --tag atonement --max-words 300 -n 10
find "Calvary" "Gethsemane" '"it is finished"' --tradition sda -n 12
find --hymn "Rock of Ages" --tag form:hymn-story -n 8
```

Vocabulary: `--tag the-cross` (360), `--tag atonement` (240), `--tag crucifixion` (276), `--tag
occasion:good-friday` (163), `--concept substitutionary-atonement` (28), `--concept propitiation`
(23), `--hymn "Rock of Ages"` (SDAH 300, 16), `--hymn "When I Survey the Wondrous Cross"` (SDAH
154, 15), `--hymn "There Is a Fountain"` (SDAH 336, 14), `--hymn "At the Cross"` (SDAH 163, 6).
`--attested` is excellent on this theme (6 of 10 rows on point).

Worth reading: #12234 (Lincoln's substitute: the Stroudsburg gravestone of John Summerfield
Staples, historically sound) · #6866 / #12229 (McNeill's imagined Barabbas; preach as his picture)
· #78546 and #78545 (*Great Controversy*: "the mystery of the cross explains all other mysteries";
"the science and the song of the redeemed"; GC 651-652) · #39002 (It Is Written, USS Indianapolis
and Captain McVay: blamed for what he could not control) · #64249 (Osbeck's documented Toplady
account, 1776 *Gospel Magazine*) · #64241 (Watts, 1707) · #3383 (the burned-over ground, Zahl) ·
#25246 (justice, mercy, grace at Calvary in 36 words).

Wrong or doubtful: the Burrington Combe cave legend (#89302 and #92063 disagree on the year; Osbeck
#64249 has the documented account); Gandhi asking for "When I Survey" (#85052, unverifiable); the
crown prince volunteering for 900 soldiers (#62380); #82605 (Voice of Prophecy, truncated before
Isaiah 53).

Adventist coverage: Ellen White strong at quotation level, reached only by probes plus
`--tradition sda`; story level thin (#39002, #82605). "Barabbas" is 0 in Adventist sources.

**Wells (Tier 1).**

- **Ellen White**, *Desire of Ages* on Gethsemane, the trial, the cross (fetch; verify DA 25, 753).
- **Toplady** and **Watts** (Osbeck in the library).

---

## End-Time / Three Angels' Messages / Reformation Heritage

**Library (Tier 0).**

```
find '"three angels"' '"everlasting gospel"' '"hour of his judgment"' --tradition sda -n 10
find '"William Miller"' "1844" '"midnight cry"' --max-words 300 -n 12
find "Wycliffe" "Huss" "Tyndale" '"ninety-five theses"' --max-words 300 -n 12
find '"wars and rumors"' '"fig tree"' '"thief in the night"' --ref "Matthew 24" --tradition sda -n 10
```

Vocabulary: `--tag three-angels-messages` (393), `--tag bible-prophecy` (139), `--tag
church-history` (89), `--concept william-miller` (40), `--concept reformation` (32), `--hymn "A
Mighty Fortress"` (SDAH 506, 8). `--tag the-remnant` (7, none Adventist), `--tag mark-of-the-beast`
(1, a news article) and `--tag investigative-judgment` (0) are useless. `"here I stand"` is 1,714
hits of noise; `"wycliffe"` and `"tyndale"` are inflated by publisher names.

Worth reading: #84017 (Spicer 1926: the Czechoslovak family who prayed for "the angel of
Revelation 14" and a colporteur walked in; **OCR scrambled the dialogue order**, re-sequence) ·
#60158 / #32392 (Hus at the stake, 1415, the paper crown; standard Foxe account) · #51973 (Luther
at Worms; say "is reported to have said", the sentence is absent from the earliest transcripts) ·
#57119 (Tyndale, 1536, "open the king of England's eyes"; "Vilford" is Vilvoorde) · #38978 (It Is
Written, the Vajont dam, unnamed in the text) · #39008 (the barometer that read "Hurricanes",
1938) · #81478 and #81480 (Loughborough on the 1833 Leonids) · #84400 (an editor who admits his former prejudice
against Miller and testifies to his sincerity) · #78229 (*Great Controversy* on the first angel's message, footnote markers in text).

Wrong: #3173 (Dark Day 1789: it was 1780); #67845 ("Morning Star of the Reformation" applied to
Hus, it is Wycliffe); #61272 (Hus's hand in the fire, unverifiable).

Adventist coverage: the theme lives under `--tradition sda` as exposition; narrative Adventist
illustrations are Spicer, Loughborough's sign accounts and It Is Written. The preachable 60- to
160-word Hus, Luther and Tyndale vignettes are all evangelical compilers.

**Wells (Tier 1).**

- **Miller** and the Millerites (pioneers in the library; *Great Controversy*).
- **Reformation**: Wycliffe, Hus, Tyndale, Luther (*Great Controversy* chapters in the library;
  Foxe for the martyrdoms, with care).

---

## Indonesian and Asian context

**Library (Tier 0).**

```
find "indonesia" "jakarta" "sumatra" "papua" -n 15
find "indonesia" "ambon" "klabat" "sulawesi" --tradition sda -n 15
find '"fishing boat"' '"rice field"' "village" "island" --tradition sda -n 12
find "nommensen" "batak" "sawi" '"peace child"' -n 10
```

No tag, concept or hymn exists for any Indonesian place name; everything is a plain probe. `papua`
is mostly Papua New Guinea (Children's Quarterly); `timor` stems to *timorous*; `java` matches a
programming joke; `manado` and `medan` are 0 but `klabat` works. `--attested "indonesia"` is 0.

Worth reading: #81053 (Adventist Mission 2020, Klabat student missionaries in a Papua village:
present as the students' testimony, the resurrection claim rests on their report) · #81342 and
#81343 (Ambon Bible worker Zeth Lekatompessy, 2026; the two records disagree on the number of his
children) · #81020 (Filipina sharecropper's rice spared in the storm; parallels Spicer's 1926
Telugu account #84162, do not present both as unique) · #92305 (Our Daily Bread 2020, Aldi adrift
49 days off Sulawesi, Luke 10) · #87332 (Our Daily Bread 2006, the Jakarta church wall with Luke
23:34 in Indonesian after 21 churches burned; the figure is the host pastor's) · #66549 (Tan 1979,
Nommensen among the Batak: "My Master gives the power to keep His laws") · #84126 (Spicer 1926,
Nommensen and the poison) · #84165 (Spicer 1926, the fruit-seller's tithe after the 1919 Kelud
eruption; continues in #84166, which is mis-titled "Bromo" and splices in South Australia) ·
#13834 / #7128 / #9885 (the Sawi Peace Child; #9885 never names Richardson) · #81042 (East Timor
store clerk forgives the man with the spear, 2020).

Pitfalls: about one Inside Story in twenty ends with a Thirteenth Sabbath Offering paragraph (trim); #90134
says "Indonesia" means "island" in Greek (it is *Indos* + *nesos*); Holwick news dumps on Suharto
and Jakarta are articles, not illustrations; Tan 1979 almanac trivia floods `--max-words 300`.

**Wells (Tier 1).**

- **Adventist work in Indonesia**: R. W. Munson at Padang, 1900 (Olsen's #84882 reports him; the
  Java missionary in Spicer's #84165 is Albert Munson), UNAI and Klabat history, the ESDA articles.
- **Mission** quarterly archives for Sumatra, Sulawesi, Papua.
- **Local touchpoints**: proverbs, kampung life, gotong-royong, the religious-minority experience.

---

## Special audiences and forms

### A Deaf congregation (Jemaat Efata Tuli): seen or touched, never heard

```
find "object" --concept children-sermon --max-words 300 -n 10
find "feel" "touch" "wrapped" --concept children-sermon -n 10
find '"hold up"' '"show the children"' --concept children-sermon -n 10
```

`--concept children-sermon` (801) is the gateway to the SermonWriter Children's Sermons, many of
which open with an "OBJECT(S) SUGGESTED" line (260 of 787). `--tag children` does not reach them.
There is no Adventist prop lesson in the library (`--concept children-sermon --tradition sda` is
0); take the prop and supply Adventist content. When the concept holds nothing for the passage,
build the demonstration yourself from a fact a record or a Tier 1 source carries (Bailey's rod and
staff, #53711, become two objects to hold up), label it as staging designed for this sermon with
the fact's source, and say which sound words you removed from any record you adapted. Sign
interpretation runs slower than speech: this congregation takes about 85 words a minute, so a
2-minute piece is roughly 170 words, not 300.

Worth reading: #109140 (identify satin, a pencil, an apple, an ice cube by touch, then the woman
who touched the cloak; **cut its "hearing with your ears" preamble**) · #109564 (a teapot wrapped in
a towel: faith as what you feel but cannot see) · #108989 (cut an apple across to show the star) ·
#109495 (a stone in the hand, Stephen) · #53711 (Bailey on rod and staff, two objects to hold up) ·
#86836 (Alexander burns the baggage: enactable with a heavy bag) · #81295 (the monkeys that stayed
away on Sabbath: visual) · #59510 (Jackson's concrete images of grief).

Screen every record for sound words; the library has no sound-free tag. Hymn stories are
sound-based (retell as biography: Spafford's loss, Newton's storm). Humor is mostly puns and
singing jokes; bulletin bloopers (#95111) are the one visual form. Strip the Google-search links
and the Sunday-school dialogue from SermonWriter texts.

### Statistics

```
find "church attendance" '"Bible reading"' --tag form:statistic -n 10
find "heaven" "hell" --tag form:statistic -n 10
```

Barna (9,442) and Gallup (184) rows are short slices (mostly 10 to 60 words; Barna runs 6 to 153)
with the date in the attribution line; `show` them and usually open the URL. Most are about
Americans, though Barna also carries Irish and global youth surveys. Older figures sit in
Ministry127 (27) and Holwick (14) rows typed `statistic`, and inside longer `story` records; they
cluster around 1987 to 2003. No Adventist statistic exists in the library; membership and baptism
figures come from ASTR.

### Humor

```
find --tag form:humor --attested --max-words 75 -n 12
find "church" "pastor" --tag form:humor --max-words 75 -n 10
```

None Adventist. Screen for afterlife jokes (conscious dead), coffee and alcohol, "Sunday morning",
and English-only puns. #95661 (the board meeting) travels; #8824 (hymns versus choruses) is about
singing and mildly divisive.

### Hymn stories

```
vocab "it is well"
find --hymn "It Is Well With My Soul" --tag form:hymn-story -n 5
find "<theme>" --tag form:hymn-story -n 8
```

`vocab <title word>` returns the exact title, SDAH number, author and tune. Osbeck rows embed the
full lyric and a devotional tail; trim. Ministry127 hymn stories are second-hand (its *It Is
Well*, #141, is itself credited to Osbeck's *101 Hymn Stories*; one is "Unknown"); prefer Osbeck (#64473 for *Great Is Thy Faithfulness*, #64332 Spafford, #64249 Toplady, #64241 Watts).

### Checking a heritage claim

```
find '"Hiram Edson"' --tradition sda -n 8
find "Bates" "Sabbath" --tradition sda --max-words 200 -n 8
find '"James White"' --tradition sda --max-words 250 -n 8
find "sanctuary" "1844" --tag adventist-heritage -n 8
```

Most of it comes back as Loughborough (1909), Spicer or Olsen; Bates's *Autobiography* and James
White's *Life Incidents* are first-person, but Edson's own manuscript is not in the library. Use it
to confirm the outline of a claim, then cite the primary source from the White Estate or the ESDA. Probe the event or the other person, not "Loughborough" (he authored the source, 811
hits). Even the folk phrasing *cornfield* works here (`find "cornfield" --tradition sda` reaches
Olsen's #84413 on Edson), but names and dates are more reliable. Chunk titles can mislead:
#81599 is titled for James White but quotes the editor of the *Midnight Cry*. Chunks cut
mid-story; `show` the adjacent id. `--concept hiram-edson` (12) and `--concept joseph-bate` (33)
exist.

---

## Sources NOT to use without verification

- **Einstein, Lincoln, Mother Teresa, Gandhi, C. S. Lewis quotes**: internet meme quotes are
  frequently fabricated. Verify via reputable sources or skip. The library's Lewis "it's grace"
  (#73252) is attested three times and still rests on one retelling.
- **"Starfish on the beach," "carrot-egg-coffee," "the lighthouse and the ships," "the dash on the
  tombstone"**: clichéd; if used, only as a foil.
- **Pop-psychology studies**: "the marshmallow test," "Milgram": often misremembered; check the
  research.
- **Famous falsehoods the library carries**: Spafford's three daughters and a storm (#19803); the
  Dark Day in 1789 (#3173); Liddell's last-minute swap (#70708); Hus as the Morning Star (#67845);
  Newton quitting the slave trade at conversion (a common retelling; none of the library's Newton rows asserts it, and #12700 corrects it); the Luther dream (#59071).

---

## When in doubt: paraphrase, attribute, and move on

A clean, briefly-told story with honest attribution beats a flashy story with a fabricated quote
every time. The pulpit is no place for "close enough."
