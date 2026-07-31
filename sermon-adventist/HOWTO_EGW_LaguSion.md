HOWTO: Fetch EGW quotations (Tier-1) and lookup Lagu Sion / SDA hymn numbers

Purpose
- Centralize local operational steps used by this project: (A) retrieving verified Ellen G. White quotations via the official EGW Writings API helper, and (B) querying the local Lagu Sion → SDA Hymnal mapping database.

A. EGW — using the local helper (Tier-1, a.egwwritings.org)
Paths referenced in the project:
- Helper script: ~/.config/scripts/egw-fetch.sh
- Credentials: ~/.config/scripts/.egw-credentials.env (or macOS Keychain item used by the helper)

Common commands
- Search for relevant paragraphs (returns para_id and refcodes):
  ~/.config/scripts/egw-fetch.sh search "your phrase"

- Fetch verbatim text by paragraph id (count = number of paragraphs):
  ~/.config/scripts/egw-fetch.sh para <para_id> <count>

Notes & troubleshooting
- If you see "EGW_CLIENT_ID / EGW_CLIENT_SECRET not set" the helper could not read credentials. Confirm ~/.config/scripts/.egw-credentials.env exists and is readable, or unlock Keychain if credentials are stored there.
- The public egwwritings.org site blocks automated fetches (HTTP 403); use the helper which calls the official API a.egwwritings.org with OAuth.
- If the helper needs to access Keychain, run it from the interactive shell or grant appropriate permissions. In some cases elevated permissions are required (see project docs).

B. Lagu Sion + SDA Hymnal (local DB)
Repo path: /Users/edmundsitumorang/DEV/lagu-sion-sda-hymnal
Files of interest: lagu_sion.db, lagu_sion.json, search.js, server.js

Quick sqlite lookup (example):
- Find by title or English title:
  sqlite3 -csv /path/to/lagu_sion.db "SELECT number,title,english_title,sda_hymnal_num,sda_hymnal_title FROM songs WHERE lower(title) LIKE '%great is thy faithfulness%' OR lower(english_title) LIKE '%great is thy faithfulness%';"

Node CLI (fast):
- Install deps: npm install
- Search by text: node search.js "Great Is Thy Faithfulness"
- Start web UI: npm start  → open http://localhost:3000

Mapping notes
- The scraper records LSEL (Edisi Baru) numbers and correlates to SDA Hymnal, LS Edisi Lama and Toba editions. Use the sda_hymnal_num and sda_hymnal_title columns for SDA equivalents.

C. Where this is referenced in the project
- sermon-adventist README and dist/system prompts reference the helper and the Lagu Sion repo.
- See: sermon-adventist/dist/chatgpt-gpt/adventist-foundation-instructions.md and README.md for policy notes.

D. Safety and policy
- EGW quotations fetched via the helper are Tier-1 and safe to quote verbatim with page numbers in sermon materials. Paraphrases must be labeled when Tier-1 fetch is not performed.
- Do not publish credentials or Keychain exports. Keep ~/.config/scripts/.egw-credentials.env private.

If you want, I can: (1) add brief examples into sermon files where EGW quotes were used, (2) run the helper to fetch additional passages, or (3) add a short shell wrapper in the repo to run common queries. Which of these should I do next?