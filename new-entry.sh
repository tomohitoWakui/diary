#!/bin/bash
# 使い方: ./new-entry.sh [日付 例: 2026-06-11]
# 日付を省略すると今日の日付になる

DATE=${1:-$(date +%Y-%m-%d)}
ENTRY_FILE="entries/${DATE}.txt"

mkdir -p entries

if [ -f "$ENTRY_FILE" ]; then
  echo "⚠️  $ENTRY_FILE はすでに存在します。編集しますか？ (y/N)"
  read -r ans
  if [ "$ans" != "y" ] && [ "$ans" != "Y" ]; then
    exit 0
  fi
fi

# エディタで開く
${EDITOR:-vi} "$ENTRY_FILE"

# entries.json を更新
python3 update-entries.py

echo "✅ entries.json を更新しました"
echo ""
echo "次のコマンドでデプロイ:"
echo "  git add . && git commit -m '$DATE' && git push"
