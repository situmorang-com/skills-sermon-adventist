#!/usr/bin/env python3
"""Convert a Claude Code .jsonl transcript into a readable HTML conversation.

Usage:
    python3 scripts/jsonl-to-html.py path/to/session.jsonl [output.html]

If no output path is given, writes <session>.html next to the input.
"""
import sys, json, html, os, datetime

def esc(s):
    return html.escape(s or "")

def fmt_time(ts):
    if not ts:
        return ""
    try:
        return datetime.datetime.fromisoformat(ts.replace("Z", "+00:00")).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return ts

def render_blocks(content):
    """content is a str or a list of blocks. Returns list of (kind, html)."""
    out = []
    if isinstance(content, str):
        if content.strip():
            out.append(("text", esc(content).replace("\n", "<br>")))
        return out
    if not isinstance(content, list):
        return out
    for b in content:
        if not isinstance(b, dict):
            continue
        t = b.get("type")
        if t == "text":
            out.append(("text", esc(b.get("text", "")).replace("\n", "<br>")))
        elif t == "thinking":
            out.append(("thinking", esc(b.get("thinking", "")).replace("\n", "<br>")))
        elif t == "tool_use":
            name = b.get("name", "tool")
            inp = json.dumps(b.get("input", {}), indent=2, ensure_ascii=False)
            out.append(("tool", f"<b>⚙ {esc(name)}</b><pre>{esc(inp)}</pre>"))
        elif t == "tool_result":
            c = b.get("content", "")
            if isinstance(c, list):
                c = "\n".join(x.get("text", "") for x in c if isinstance(x, dict))
            out.append(("tool", f"<b>↳ result</b><pre>{esc(str(c))[:4000]}</pre>"))
    return out

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(src)[0] + ".html"

    rows = []
    title = os.path.basename(src)
    with open(src) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            if d.get("type") == "ai-title" and d.get("aiTitle"):
                title = d["aiTitle"]
            if d.get("type") not in ("user", "assistant"):
                continue
            msg = d.get("message", {})
            role = msg.get("role", d.get("type"))
            blocks = render_blocks(msg.get("content"))
            if not blocks:
                continue
            rows.append((role, fmt_time(d.get("timestamp")), blocks))

    parts = []
    for role, ts, blocks in rows:
        bubble = []
        for kind, h in blocks:
            if kind == "thinking":
                bubble.append(f'<details class="thinking"><summary>💭 thinking</summary><div>{h}</div></details>')
            elif kind == "tool":
                bubble.append(f'<details class="tool"><summary>{h.split("</b>")[0]}</b></summary><div>{h}</div></details>')
            else:
                bubble.append(f'<div class="text">{h}</div>')
        parts.append(
            f'<div class="msg {role}"><div class="meta">{esc(role)} · {esc(ts)}</div>'
            f'<div class="bubble">{"".join(bubble)}</div></div>'
        )

    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<title>{esc(title)}</title><style>
body{{font:15px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;background:#f4f6f8;margin:0;padding:24px;color:#1a2530}}
.wrap{{max-width:820px;margin:0 auto}}
h1{{font-size:20px;color:#0B2A4A}}
.msg{{margin:14px 0;display:flex;flex-direction:column}}
.msg.user{{align-items:flex-end}}
.meta{{font-size:11px;color:#8497a6;margin:0 6px 3px}}
.bubble{{max-width:90%;padding:12px 16px;border-radius:14px;box-shadow:0 1px 3px rgba(0,0,0,.07)}}
.user .bubble{{background:#1C7293;color:#fff;border-bottom-right-radius:4px}}
.assistant .bubble{{background:#fff;border-bottom-left-radius:4px}}
.text{{white-space:normal}}
pre{{background:#0d1b26;color:#cfe3ee;padding:10px;border-radius:8px;overflow:auto;font-size:12px;margin:6px 0}}
details{{margin:6px 0;font-size:13px}}
details.thinking summary{{color:#9b6b00;cursor:pointer}}
details.tool summary{{color:#2a6f97;cursor:pointer}}
summary{{user-select:none}}
</style></head><body><div class="wrap"><h1>{esc(title)}</h1>{"".join(parts)}</div></body></html>"""

    with open(dst, "w") as out:
        out.write(doc)
    print(f"Wrote {dst}  ({len(rows)} messages)")

if __name__ == "__main__":
    main()
