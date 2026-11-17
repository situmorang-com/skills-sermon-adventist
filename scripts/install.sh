#!/bin/bash
# install.sh — make the tools callable by name from any folder, and switch on the pre-commit check.
#
#   scripts/install.sh            # link into ~/.local/bin, install deck dependencies, set the git hook
#
# The skills name the tools bare (bible.py, sermon-out.py, egw-fetch.sh ...), because a skill
# runs from whatever folder the user is in. Run this once per computer after cloning.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BIN="${SERMON_BIN:-$HOME/.local/bin}"
mkdir -p "$BIN"

link() {  # link <target> <name>
  if [ -e "$1" ]; then
    ln -sfn "$1" "$BIN/$2"
    echo "  $2 -> $1"
  else
    echo "  (skipped $2: $1 is not on this computer)"
  fi
}

echo "Linking into $BIN"
for f in bible.py helloao-fetch.py bri-fetch.py sermon-out.py check-quotes.py render-study.py; do
  chmod +x "$REPO/scripts/$f"
  link "$REPO/scripts/$f" "$f"
done
chmod +x "$REPO/scripts/sermon-deck/build.js"
link "$REPO/scripts/sermon-deck/build.js" sermon-deck
# Helpers kept outside this repo. They find their credentials beside themselves, so they
# get a wrapper that runs them in place; a symlink would make them look in $BIN.
wrap() {  # wrap <target> <name>
  if [ -e "$1" ]; then
    rm -f "$BIN/$2"
    printf '#!/bin/bash\nexec "%s" "$@"\n' "$1" > "$BIN/$2"
    chmod +x "$BIN/$2"
    echo "  $2 => runs $1"
  else
    echo "  (skipped $2: $1 is not on this computer)"
  fi
}
wrap "$HOME/.config/scripts/egw-fetch.sh" egw-fetch.sh
wrap "$HOME/.config/scripts/sdabc-fetch.sh" sdabc-fetch.sh

case ":$PATH:" in
  *":$BIN:"*) ;;
  *) echo "NOTE: $BIN is not on your PATH. Add it in your shell profile." ;;
esac

if command -v npm >/dev/null 2>&1; then
  if [ ! -d "$REPO/scripts/sermon-deck/node_modules/pptxgenjs" ]; then
    echo "Installing the deck builder's dependencies"
    npm install --silent --prefix "$REPO/scripts/sermon-deck"
  fi
else
  echo "NOTE: npm not found; sermon-deck needs Node.js and 'npm install' in scripts/sermon-deck."
fi

git -C "$REPO" config core.hooksPath scripts/hooks
chmod +x "$REPO/scripts/hooks/pre-commit" "$REPO/scripts/test.sh"
echo "Pre-commit check on (scripts/hooks/pre-commit)."
echo "Output goes to: $("$REPO/scripts/sermon-out.py" root 2>&1 | tr '\n' ' ')"
