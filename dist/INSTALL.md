# Installation Guide — Use These Skills in Any LLM

Four Adventist sermon-prep skills, ready for **Claude.ai**, **ChatGPT**, **API**, or any LLM.

---

## TL;DR — Quick Install

### Claude.ai (Fastest)
1. Copy the full SKILL.md content from `claude-project/[skill]-instructions.md`
2. Paste into a **Claude Project** → "Project instructions"
3. Upload all files from `claude-project/knowledge/` as project knowledge
4. Start chatting

### ChatGPT (Custom GPT)
1. Create a Custom GPT at chatgpt.com
2. Paste the **loader instruction** from `chatgpt-gpt/loader-[skill].txt`
3. Upload all `.md` files from `chatgpt-gpt/knowledge/` under "Knowledge"
4. Save & share

### Any API (OpenAI, Anthropic SDK, etc.)
1. Use the text from `system-prompt/[skill].txt` as your system prompt
2. Can also use with open-source LLMs (LLaMA, Mistral, etc.)

---

## Detailed Instructions by Platform

### 🔵 Claude.ai (Recommended for Best Experience)

**Why Claude:** Full skill-creator support, no instruction limits, generous file handling.

#### Step 1: Create a Project
- Go to **claude.ai**
- Click **"+ Projects"** (top left)
- Name it: "Adventist Sermon Prep"
- Set visibility (Private recommended)

#### Step 2: Load Adventist Foundation (Required First)
1. Click the project → **"Project instructions"** (gear icon)
2. Paste the full content of `dist/claude-project/adventist-foundation-instructions.md`
3. Click **"Save"**

#### Step 3: Load the Skill You Want
Choose one or more:

**For Sermon Prep:**
- Copy: `dist/claude-project/sermon-adventist-instructions.md`
- Paste in a NEW chat message: `@sermon-adventist [your prompt]`
- Or upload to project instructions (can have multiple)

**For Bible Study:**
- Copy: `dist/claude-project/bible-study-deep-instructions.md`
- Use in chat: `@bible-study-deep [passage]`

**For Illustrations:**
- Copy: `dist/claude-project/sermon-illustrations-instructions.md`
- Use in chat: `@sermon-illustrations [theme]`

#### Step 4: Upload Knowledge Files
1. In project → **"Project knowledge"** (right sidebar)
2. Upload all files from `dist/claude-project/knowledge/`:
   - `adventist-themes.md`
   - `commentary-sources.md`
   - `research-notes-template.md`
   - `structures.md`
   - `illustration-sources.md`
3. Claude will reference these automatically

#### Step 5: Start Using
```
You: I'm preaching Romans 8:1-11 this Sabbath. 30 minutes, mixed ages, 
expository structure. KJV, English.

Claude: [Uses sermon-adventist skill to generate all three documents]
```

---

### 🟠 ChatGPT Custom GPTs

**Why ChatGPT:** Easy sharing, familiar interface, works offline after initial setup.

**Note:** ChatGPT's custom instructions are limited to 8,000 characters, so we use "loader" instructions that reference knowledge files.

#### Step 1: Create a Custom GPT
1. Go to **chat.openai.com**
2. Click **"Create"** (top left)
3. Choose **"Create a GPT"**
4. Name it: "Adventist Sermon Prep", "Bible Study Deep", etc.
5. Click **"Configure"** (gear icon)

#### Step 2: Paste the Loader Instruction
⚠️ **Read `dist/chatgpt-gpt/README-CHATGPT-SETUP.md` first** — it explains the loader approach.

For **Sermon Adventist**:
1. Under **"Instructions"**, paste: `dist/chatgpt-gpt/loader-sermon-adventist.txt`
2. Leave other settings at defaults

For **Bible Study Deep**:
1. Paste: `dist/chatgpt-gpt/loader-bible-study-deep.txt`

For **Illustrations**:
1. Paste: `dist/chatgpt-gpt/loader-sermon-illustrations.txt`

#### Step 3: Upload Knowledge Files
1. Scroll down to **"Knowledge"**
2. Click **"Upload files"**
3. Upload all `.md` files from `dist/chatgpt-gpt/knowledge/`:
   - `adventist-foundation-instructions.md`
   - `sermon-adventist-instructions.md` (or the skill you're loading)
   - `adventist-themes.md`
   - `commentary-sources.md`
   - `research-notes-template.md`
   - `structures.md`
   - `illustration-sources.md`

#### Step 4: Save & Test
1. Click **"Save"** (top right)
2. In the chat, test: 
   ```
   I'm preaching Daniel 12:4 to an AY program. 40 minutes, Indonesian.
   ```
3. ChatGPT will read the knowledge files and respond

#### Step 5: Share
- Click **"Share"** (top right)
- Generate a public or private link
- Share with your church, team, or seminary

---

### 🔴 API / SDK (Any LLM)

**Why API:** Use with OpenAI, Anthropic, open-source models, or custom systems.

#### For OpenAI API (Python)
```python
import openai

with open("dist/system-prompt/sermon-adventist.txt") as f:
    system_prompt = f.read()

response = openai.ChatCompletion.create(
    model="gpt-4",
    system=system_prompt,
    messages=[
        {"role": "user", "content": "I'm preaching Romans 8 on Sabbath..."}
    ]
)

print(response.choices[0].message.content)
```

#### For Anthropic SDK
```python
import anthropic

with open("dist/system-prompt/sermon-adventist.txt") as f:
    system = f.read()

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-opus-4",
    max_tokens=4096,
    system=system,
    messages=[
        {"role": "user", "content": "I'm preaching Romans 8..."}
    ]
)

print(message.content[0].text)
```

#### For Open-Source LLMs (LLaMA, Mistral)
Use `dist/system-prompt/[skill].txt` as your system prompt in any framework:
- **LangChain:** Set as `system_message`
- **LlamaIndex:** Pass to LLM initialization
- **Ollama:** Use in prompt template
- **LocalAI:** Include in request

---

## File Structure Explained

```
dist/
├── claude-project/
│   ├── *-instructions.md          (Full SKILL.md for Claude Projects)
│   └── knowledge/                 (Reference files to upload)
│
├── chatgpt-gpt/
│   ├── loader-*.txt               (Compressed for 8K instruction limit)
│   ├── README-CHATGPT-SETUP.md    (ChatGPT-specific guide)
│   └── knowledge/                 (Upload these as GPT knowledge)
│
├── system-prompt/
│   ├── *.txt                      (Plain system prompts for any API)
│   └── (Use as-is in any LLM)
│
└── INSTALL.md                     (This file)
```

---

## Which Skill Do I Need?

| Use Case | Skill |
|---|---|
| **Writing a complete sermon** | `sermon-adventist` |
| **Deep Bible study or Sabbath School prep** | `bible-study-deep` |
| **Finding or creating illustrations** | `sermon-illustrations` |
| **All of the above** | Load all three + `adventist-foundation` |

---

## Troubleshooting

### "It doesn't know what to do"
- Make sure you've uploaded all knowledge files
- For ChatGPT, verify the loader instruction is present
- Try a specific prompt: "I'm preaching [passage]..."

### "It's making up quotes/hymn numbers"
- That's a bug — report it
- These skills are designed to never fabricate, so if it is, the skill's anti-fabrication rules aren't being followed

### "It's asking me questions but batching them"
- For sermon-adventist, it should ask **one question at a time**
- If it's batching, repeat: "One question at a time, please"

### "I want to use this locally"
- Use the `system-prompt/` files with any local LLM (LLaMA, Mistral, etc.)
- Example: `ollama run mistral --system-prompt "$(cat dist/system-prompt/sermon-adventist.txt)"`

---

## Support

- **Repository:** https://github.com/situmorang-com/skills-sermon-adventist
- **Issues:** Open an issue on GitHub
- **Questions:** Check README.md for overview

---

## What's Inside Each Skill

### Adventist Foundation (Load First)
- 28 Fundamental Beliefs guardrails
- 3-tier Ellen G. White citation policy  
- KJV/Indonesian defaults
- Anti-fabrication rules
- Adventist doctrinal infiltration list

### Sermon Adventist
- Complete sermon workflow (research → outline → manuscript)
- 6 choosable structures
- Interactive one-at-a-time brainstorm
- Mandatory bookend illustrations
- Service header block (hymns, responsive reading)
- Multi-commentary insights (Andrews, SDABC, Doukhan, LaRondelle, etc.)

### Bible Study Deep
- 8-section exegetical study
- 4-tier commentary framework
- Word studies (Hebrew/Greek + translation comparison)
- EGW live-fetched from egwwritings.org
- Application questions

### Sermon Illustrations
- Tier 1: Search famous/attributed illustrations first
- Tier 2: Create original illustrations labeled clearly
- Themed source lists by doctrine

---

**Ready to go.** Pick your platform and start above. 🎯
