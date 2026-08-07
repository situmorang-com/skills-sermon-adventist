# Commentary Tiers for Deep Bible Study

Full detail for Tiers 3 and 4 of Section 4 in the `bible-study-deep` skill. The SKILL.md keeps only the load-bearing doctrinal flags; everything else lives here.

Companion file: `commentary-sources.md` (shipped with `sermon-adventist`) covers the Adventist side — BRI, Andrews Bible Commentary, SDABC, SDAIBC, Adventist scholars by specialty, and Adventist periodicals. This file covers the non-Adventist voices.

**Anti-fabrication rule:** knowing that a commentary exists is not knowing what it says about your passage. Tag every claim with a provenance tag (see "Source Provenance Tags" in SKILL.md Section 4). Do not paraphrase what you have not read.

---

## Tier 3 — Classic Non-Adventist Commentaries

Historically significant commentaries that preachers worldwide have drawn on for centuries. Use them for devotional depth, illustrative richness, and historical perspective. **Always flag where they disagree with Adventist positions** — particularly on state of the dead, hellfire, Sabbath, and sanctuary.

### Matthew Henry's Commentary on the Whole Bible (1706-1714)

The most widely cited devotional commentary in the English-speaking Protestant world for 300 years. Warm, pastoral, practical. Strong on application and the spiritual life. Weaknesses: written before modern critical scholarship; occasionally superficial on Hebrew/Greek nuances; Reformed covenant theology shapes some readings.

- **Use for:** devotional application, connections between passages, memorable turns of phrase that can anchor a sermon illustration.
- **Flag:** Henry assumes soul immortality and eternal hellfire. Do not use his commentary on death/resurrection passages without noting the doctrinal divergence.
- **Access:** indexed in the EGW Writings API (`egw-fetch.sh search`, refcodes like `Matthew Henry's Complete Bible Commentary, p. 190.9`). Also free at Blue Letter Bible and Bible Hub.

### John Calvin's Commentaries (1540s-1563)

Rigorous Reformed exegesis, especially strong on the Pauline epistles, Psalms, and the Minor Prophets. Calvin is unusually disciplined about staying in the text. Less allegorizing than medieval commentators.

- **Use for:** careful grammatical analysis, historical context in the Reformation era, Paul's letters, Psalms.
- **Flag:** Calvin argues the Sabbath was abrogated in Christ. Do not use his Sabbath sections without noting this explicitly.
- **Access:** free at ccel.org.

### John Wesley's Explanatory Notes on the New Testament (1755)

Brief, methodical notes oriented toward practical holiness. Useful for quick reference on NT texts and for understanding the Wesleyan/Arminian reading of grace and free will.

- **Use for:** NT application; texts on repentance, sanctification, and the Christian life.
- **Flag:** Wesleyan positions on entire sanctification differ from Adventist soteriology in some respects.
- **Access:** Wesley Center Online, Blue Letter Bible.

### Matthew Poole's Commentary (1669-1676)

More technical than Matthew Henry. Engages Hebrew and Greek more carefully. Useful when you need a second voice on word-level exegesis.

- **Use for:** OT texts requiring careful Hebrew engagement; cross-reference richness.
- **Flag:** pre-critical, but fewer direct doctrinal conflicts than Henry or Calvin.
- **Access:** Blue Letter Bible.

### Charles Spurgeon's Treasury of David (Psalms only, 1869-1885)

Unmatched for the Psalms. Spurgeon drew on hundreds of earlier commentators and preachers. Each Psalm entry includes exposition, illustrative quotations, and homiletical hints. Rich for sermon preparation.

- **Use for:** Psalms only. Extraordinary depth of devotional and illustrative material.
- **Flag:** Spurgeon assumes soul immortality and eternal hellfire, consistent with his Baptist tradition.
- **Access:** spurgeon.org, Blue Letter Bible.

---

## Tier 4 — Modern Evangelical Scholarship

For exegetical depth, original-language precision, and historical-cultural background. Use where they strengthen the exegesis without importing non-Adventist conclusions uncritically.

| Source | Best for | Caution |
|---|---|---|
| **IVP Bible Background Commentary: NT** (Craig Keener) | Cultural/historical background for every NT passage | Widely trusted; no major doctrinal issues for background use |
| **IVP Bible Background Commentary: OT** (Walton, Matthews, Chavalas) | OT cultural and archaeological context | Same — use freely for background |
| **NICOT / NICNT** (Eerdmans) | Deep exegesis, OT and NT | Assumes soul immortality; flag on death/resurrection texts |
| **F.F. Bruce** — *The Book of Acts*, *Paul: Apostle of the Heart Set Free*, *Commentary on Galatians*, *The Epistle to the Hebrews* (NICNT) | Acts, Pauline letters, Galatians, Hebrews | Solid evangelical; does not share the Adventist two-phase sanctuary reading |
| **Leon Morris** — *The Gospel According to John* (NICNT), *1 Corinthians* | John, 1 Corinthians | Reliable; no major issues |
| **John Stott** (Bible Speaks Today series) | Balanced pastoral-academic; all levels | Assumes eternal conscious torment; flag on judgment texts |
| **William Barclay's Daily Study Bible** | Greek word backgrounds, Greco-Roman cultural context | **Heavy flag:** Barclay holds universal salvation and rejects bodily resurrection in parts. Use ONLY for cultural/linguistic background. Never quote his theological conclusions as support. |
| **Word Biblical Commentary (WBC)** | Most thorough academic series in English | Technical; engage sanctuary/eschatology sections with Adventist caution |
| **Baker Exegetical (BECNT)** / **Pillar NT Commentary** | Technical NT exegesis with transliterated Greek | Evangelical defaults on anthropology and hell |

---

## Lexicons and Language Reference

Name the lexicon when a word study leans on it. "The Hebrew means" with no source behind it is an assertion, not a study.

| Tool | Scope | Notes |
|---|---|---|
| **BDB** (Brown-Driver-Briggs) | Hebrew/Aramaic | Free on Blue Letter Bible and STEP Bible. Note when BDB splits an entry into homonyms — that decision is often the whole interpretive question. |
| **HALOT** (Koehler-Baumgartner) | Hebrew/Aramaic | The current standard; usually paid. Compare against BDB where they differ. |
| **BDAG** | Koine Greek | The standard NT lexicon; paid. |
| **Thayer's** | Koine Greek | Free, dated, adequate for range-of-meaning work. |
| **Vine's Expository Dictionary** (OT and NT) | Word studies for preachers | Indexed in the EGW Writings API (refcodes `VED-OT` / `VED-NT`). Popular-level; verify against a real lexicon before building a point on it. |
| **James Barr**, *The Semantics of Biblical Language* (1961) | Method, not lexicon | The standard warning against the etymological/root fallacy. Any word study in this skill must be able to survive Barr. |

---

## Free Digital Tools

| Tool | URL | What it offers |
|---|---|---|
| **Blue Letter Bible** | blueletterbible.org | Interlinear, Strong's, Thayer's, BDB; Matthew Henry, JFB, Poole, Spurgeon |
| **Bible Hub** | biblehub.com | Interlinear, parallel translations, brief commentary excerpts |
| **STEP Bible** | stepbible.org | Original-language tools from Tyndale House |
| **EGW Writings** | egwwritings.org (API: `a.egwwritings.org`) | Ellen White corpus plus ABC, SDABC, Matthew Henry, Vine's. Use `egw-fetch.sh`; the public site 403s automated requests. |
| **BibleTools** | bibletools.info | SDABC full-text; scraped by `sdabc-fetch.sh` (first-paragraph extraction) |
| **Adventist Heritage** | adventistarchives.org | Pioneer Adventist primary documents |

---

## Why the tiers matter

See "Why the Multi-Commentary Tier Matters" at the end of the `bible-study-deep` SKILL.md. Short version: a single-source study risks missing the passage's texture, and doctrinally grounded is not the same as doctrinally isolated.
