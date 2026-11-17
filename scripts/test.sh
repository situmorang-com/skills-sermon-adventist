#!/bin/bash
# test.sh — the repo's checks.
#
#   scripts/test.sh          # fast, offline: syntax, the tools' core paths, stale dist/ (the pre-commit hook)
#   scripts/test.sh --net    # also the API fallbacks and the live sources (needs the internet)
set -uo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
fail=0
ok()   { echo "  ok    $1"; }
bad()  { echo "  FAIL  $1"; fail=1; }
warn() { echo "  warn  $1"; }
run()  { # run "<label>" <command...>   passes when the command exits 0
  local label="$1"; shift
  if "$@" >"$TMP/out" 2>&1; then ok "$label"; else bad "$label"; sed 's/^/        /' "$TMP/out" | head -8; fi
}
has()  { # has "<label>" "<text>" <command...>   passes when the output contains the text
  local label="$1" text="$2"; shift 2
  # Captured first: with pipefail, grep -q closing the pipe early fails a command with long output.
  local out; out="$("$@" 2>&1)"
  if grep -qF -- "$text" <<<"$out"; then ok "$label"; else bad "$label (expected: $text)"; fi
}

echo "Syntax"
for f in scripts/*.py; do run "python  $f" python3 -c 'import ast,sys; ast.parse(open(sys.argv[1]).read(), sys.argv[1])' "$f"; done
for f in scripts/*.sh scripts/hooks/pre-commit; do run "bash    $f" bash -n "$f"; done
for f in scripts/sermon-deck/build.js sabbath-school-lesson/references/teaching-deck-generator.js; do
  run "node    $f" node --check "$f"
done
for f in */SKILL.md; do
  has "front matter  $f" "name:" head -5 "$f"
done

for f in bible-study-deep/references/html-template.html sabbath-school-lesson/references/teachers-guide-template.html sabbath-school-lesson/examples/bilingual-guide.html; do
  # Without width:100% the article grows to its widest table and the page scrolls sideways on a phone.
  has "phone width  $f" "article{width:100%;min-width:0" cat "$f"
done
for f in */chatgpt-instructions.md; do
  if [ "$(wc -c < "$f")" -le 8000 ]; then ok "ChatGPT limit  $f"; else bad "ChatGPT limit  $f is over 8000 characters"; fi
done

echo "Tools"
export SERMON_OUTPUT="$TMP/out-root"
has "sermon-out dir"   "2026-01-03-a-test-title" python3 scripts/sermon-out.py dir 2026-01-03 "A Test: Title!"
D="$SERMON_OUTPUT/2026-01-03-a-test-title"
printf '# Bible Study: John 3:16\n\n## A Test\n\n*Prepared for: a test*\n*Translation: KJV*\n\n## 1. Passage Context\n\n> For God so loved the world, that he gave his only begotten Son\n> — John 3:16 (KJV)\n\n## Verification Ledger\n\nsecret para_id 1.2\n' > "$D/bible-study.md"
printf '> For God so loved the planet\n> — John 3:16 (KJV)\n' > "$D/wrong.md"
printf '> "For all have sinned, and come short of the glory of God" (Romans 3:23, KJV)\n' > "$D/inline.md"
if [ -f "${BIBLE_DATA:-$HOME/DEV/bible-data}/bible.db" ]; then
  has "bible.py pack (local)" "only begotten Son" python3 scripts/bible.py pack "John 3:16" --brief
  has "bible.py Indonesian book name" "new song" python3 scripts/bible.py verse "Wahyu 14:3" --t eng_kjv
  run "check-quotes passes a true quotation" python3 scripts/check-quotes.py "$D/bible-study.md"
  has "check-quotes reads a citation in brackets" "1 match" python3 scripts/check-quotes.py "$D/inline.md"
  if python3 scripts/check-quotes.py "$D/wrong.md" >/dev/null 2>&1; then bad "check-quotes catches a wrong quotation"; else ok "check-quotes catches a wrong quotation"; fi
else
  warn "no local Bible database; local-mode checks skipped (run bible.py sync)"
fi
run "render-study writes the page" python3 scripts/render-study.py "$D/bible-study.md"
if grep -q "para_id" "$D/bible-study.html"; then bad "render-study keeps the ledger out"; else ok "render-study keeps the ledger out"; fi
rm -f "$D/wrong.md" "$D/inline.md"
has "sermon-out tidy files the study" "bible-study.md -> study/" python3 scripts/sermon-out.py tidy "$D"
if [ -d scripts/sermon-deck/node_modules/pptxgenjs ]; then
  node scripts/sermon-deck/build.js --example > "$TMP/deck.json"
  run "sermon-deck builds the example" node scripts/sermon-deck/build.js "$TMP/deck.json" "$TMP/deck.pptx"
else
  warn "deck dependencies not installed; run scripts/install.sh"
fi

echo "Packages"
stale=""
for f in */SKILL.md; do
  # The system-prompt package is a straight copy of each SKILL.md, so a difference means dist/ was not rebuilt.
  cmp -s "$f" "dist/system-prompt/$(dirname "$f").txt" || stale="$stale $(dirname "$f")"
done
if [ -n "$stale" ]; then
  warn "dist/ is behind:$stale. Rebuild with scripts/build-dist.sh"
else
  ok "dist/ is current"
fi

if [ "${1:-}" = "--net" ]; then
  echo "Network"
  export BIBLE_DATA="$TMP/no-data"
  has "bible.py pack (fallback)" "fallback" python3 scripts/bible.py pack "John 3:16"
  has "bible.py strongs (fallback)" "love" python3 scripts/bible.py strongs G25
  has "helloao commentary" "Matthew Henry" python3 scripts/helloao-fetch.py commentary "John 3:16"
  printf '> Karena begitu besar kasih Allah akan dunia ini\n> — Yohanes 3:16 (TB)\n' > "$TMP/tb.md"
  run "check-quotes reads the Terjemahan Baru" python3 scripts/check-quotes.py "$TMP/tb.md"
fi

[ $fail -eq 0 ] && echo "All checks passed." || echo "Some checks FAILED."
exit $fail
