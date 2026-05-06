# ChatGPT Setup Instructions

These skills are too large for ChatGPT's 8K custom instruction limit. **Solution:** Load the loader instruction + knowledge files.

## Steps

### 1. Create a Custom GPT
Go to chatgpt.com → "Create a GPT" → "Create"

### 2. Add the Loader Instruction
- Click **"Configure"** (gear icon)
- Under **"Instructions"**, paste the content from the **loader-instructions.md** file for the skill you want
- Leave the rest at defaults for now

### 3. Upload Knowledge Files
- Under **"Knowledge"**, upload all `.md` files from the `knowledge/` folder:
  - `adventist-themes.md`
  - `commentary-sources.md`
  - `research-notes-template.md`
  - `structures.md`
  - `illustration-sources.md` (if sermon-illustrations)
- (ChatGPT will read these when you prompt it)

### 4. Save & Test
- Name the GPT: "Sermon Adventist", "Bible Study Deep", etc.
- Send a test prompt to verify it works
- Share the GPT link with your team

---

## Why This Structure?

ChatGPT's **custom instructions** are limited to 8,000 characters. The full skill SKILL.md files are much longer. By splitting:
- **Loader instructions** (~1,500 chars): Tells ChatGPT what to do and how to use the knowledge files
- **Knowledge files** (uploaded separately): Full reference material ChatGPT reads on demand

This gives you the full capability without hitting the limit.

---

## What to Do With Each Skill

| Skill | Files to Upload | Loader |
|---|---|---|
| **Sermon Adventist** | adventist-foundation-instructions.md (full), then sermon-adventist-instructions.md, structures.md, research-notes-template.md, commentary-sources.md, adventist-themes.md | `loader-sermon-adventist.txt` |
| **Bible Study Deep** | adventist-foundation-instructions.md (full), then bible-study-deep-instructions.md, commentary-sources.md, adventist-themes.md | `loader-bible-study-deep.txt` |
| **Sermon Illustrations** | sermon-illustrations-instructions.md, illustration-sources.md | `loader-sermon-illustrations.txt` |

---

**Need help?** Check `INSTALL.md` in the repo root for more detailed instructions.
