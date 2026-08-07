#!/bin/bash

# Build dist/ packages for cross-LLM use
# Generates Claude Project, ChatGPT, and system-prompt packages from SKILL.md sources

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="$REPO_ROOT/dist"

echo "🔨 Building cross-LLM distribution packages..."
echo "Repository root: $REPO_ROOT"
echo "Dist directory: $DIST_DIR"
echo ""

# Function to copy references to dist knowledge folder
copy_references() {
    local skill=$1
    local dist_type=$2

    if [ -d "$REPO_ROOT/$skill/references" ]; then
        mkdir -p "$DIST_DIR/$dist_type/knowledge"
        # .md knowledge files plus .html assets (e.g. the bible-study page template)
        cp -v "$REPO_ROOT/$skill/references"/*.md "$DIST_DIR/$dist_type/knowledge/" 2>/dev/null || true
        cp -v "$REPO_ROOT/$skill/references"/*.html "$DIST_DIR/$dist_type/knowledge/" 2>/dev/null || true
    fi
}

# Function to check file size
check_size() {
    local file=$1
    local limit=$2
    local size=$(wc -c < "$file")

    if [ "$size" -gt "$limit" ]; then
        echo "⚠️  $file is $(($size / 1024))K (limit: $(($limit / 1024))K)"
        return 1
    else
        echo "✅ $file is $(($size / 1024))K (limit: $(($limit / 1024))K)"
        return 0
    fi
}

# Same check, but never aborts the build under `set -e` — oversize is a warning,
# not a failure (ChatGPT users split long instructions into knowledge files).
check_size_warn() {
    check_size "$1" "$2" || true
}

# ---

# 1. ADVENTIST-FOUNDATION (shared, needed by all)
echo "📦 Building adventist-foundation packages..."

# Claude Project (full)
cp -v "$REPO_ROOT/adventist-foundation/SKILL.md" "$DIST_DIR/claude-project/adventist-foundation-instructions.md"

# ChatGPT (same - foundation is usually OK size-wise)
cp -v "$REPO_ROOT/adventist-foundation/SKILL.md" "$DIST_DIR/chatgpt-gpt/adventist-foundation-instructions.md"

# System prompt (API)
cp -v "$REPO_ROOT/adventist-foundation/SKILL.md" "$DIST_DIR/system-prompt/adventist-foundation.txt"

echo "✅ adventist-foundation built"
echo ""

# ---

# 2. SERMON-ADVENTIST
echo "📦 Building sermon-adventist packages..."

# Claude Project (full SKILL.md)
cp -v "$REPO_ROOT/sermon-adventist/SKILL.md" "$DIST_DIR/claude-project/sermon-adventist-instructions.md"
copy_references "sermon-adventist" "claude-project"

# ChatGPT (full SKILL.md, let GPT read references on demand)
cp -v "$REPO_ROOT/sermon-adventist/SKILL.md" "$DIST_DIR/chatgpt-gpt/sermon-adventist-instructions.md"
copy_references "sermon-adventist" "chatgpt-gpt"

# System prompt (API)
cp -v "$REPO_ROOT/sermon-adventist/SKILL.md" "$DIST_DIR/system-prompt/sermon-adventist.txt"

echo "✅ sermon-adventist built"
echo ""

# ---

# 3. BIBLE-STUDY-DEEP
echo "📦 Building bible-study-deep packages..."

# Claude Project (full)
cp -v "$REPO_ROOT/bible-study-deep/SKILL.md" "$DIST_DIR/claude-project/bible-study-deep-instructions.md"
copy_references "bible-study-deep" "claude-project"

# ChatGPT (full)
cp -v "$REPO_ROOT/bible-study-deep/SKILL.md" "$DIST_DIR/chatgpt-gpt/bible-study-deep-instructions.md"
copy_references "bible-study-deep" "chatgpt-gpt"

# System prompt (API)
cp -v "$REPO_ROOT/bible-study-deep/SKILL.md" "$DIST_DIR/system-prompt/bible-study-deep.txt"

echo "✅ bible-study-deep built"
echo ""

# ---

# 4. SERMON-ILLUSTRATIONS
echo "📦 Building sermon-illustrations packages..."

# Claude Project (full)
cp -v "$REPO_ROOT/sermon-illustrations/SKILL.md" "$DIST_DIR/claude-project/sermon-illustrations-instructions.md"
copy_references "sermon-illustrations" "claude-project"

# ChatGPT (full)
cp -v "$REPO_ROOT/sermon-illustrations/SKILL.md" "$DIST_DIR/chatgpt-gpt/sermon-illustrations-instructions.md"
copy_references "sermon-illustrations" "chatgpt-gpt"

# System prompt (API)
cp -v "$REPO_ROOT/sermon-illustrations/SKILL.md" "$DIST_DIR/system-prompt/sermon-illustrations.txt"

echo "✅ sermon-illustrations built"
echo ""

# ---

# 5. SABBATH-SCHOOL-LESSON
echo "📦 Building sabbath-school-lesson packages..."

# Claude Project (full)
cp -v "$REPO_ROOT/sabbath-school-lesson/SKILL.md" "$DIST_DIR/claude-project/sabbath-school-lesson-instructions.md"
copy_references "sabbath-school-lesson" "claude-project"

# ChatGPT (full)
cp -v "$REPO_ROOT/sabbath-school-lesson/SKILL.md" "$DIST_DIR/chatgpt-gpt/sabbath-school-lesson-instructions.md"
copy_references "sabbath-school-lesson" "chatgpt-gpt"

# System prompt (API)
cp -v "$REPO_ROOT/sabbath-school-lesson/SKILL.md" "$DIST_DIR/system-prompt/sabbath-school-lesson.txt"

echo "✅ sabbath-school-lesson built"
echo ""

# ---

# 6. SIZE CHECKS
echo "📏 Checking file sizes for ChatGPT 8K instruction limit..."
check_size_warn "$DIST_DIR/chatgpt-gpt/adventist-foundation-instructions.md" 8000
check_size_warn "$DIST_DIR/chatgpt-gpt/sermon-adventist-instructions.md" 8000
check_size_warn "$DIST_DIR/chatgpt-gpt/bible-study-deep-instructions.md" 8000
check_size_warn "$DIST_DIR/chatgpt-gpt/sermon-illustrations-instructions.md" 8000
check_size_warn "$DIST_DIR/chatgpt-gpt/sabbath-school-lesson-instructions.md" 8000

echo ""
echo "📂 Generated files:"
find "$DIST_DIR" -type f | sort
echo ""
echo "✨ Build complete!"
echo ""
echo "📖 Next: See INSTALL.md for how to load into Claude.ai, ChatGPT, or API"
