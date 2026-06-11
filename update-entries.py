#!/usr/bin/env python3
"""
entries/ フォルダのテキストファイルから entries.json を再生成する。

ファイル構成:
  entries/2026-06-11.txt        → 本文テキスト
  images/2026-06-11-1.jpg      → 画像（複数可、番号を連番にする）
  images/2026-06-11-2.jpg
"""

import json
import os
import re
import glob

entries_dir = "entries"
images_dir = "images"

entries = []

txt_files = glob.glob(os.path.join(entries_dir, "*.txt"))

for path in txt_files:
    filename = os.path.basename(path)
    date = filename.replace(".txt", "")

    # 日付フォーマットチェック（YYYY-MM-DD）
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        print(f"スキップ: {filename}（日付フォーマット不正）")
        continue

    with open(path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    # 画像を探す（images/YYYY-MM-DD-*.* の形式）
    image_patterns = [
        os.path.join(images_dir, f"{date}-*.jpg"),
        os.path.join(images_dir, f"{date}-*.jpeg"),
        os.path.join(images_dir, f"{date}-*.png"),
        os.path.join(images_dir, f"{date}-*.gif"),
        os.path.join(images_dir, f"{date}-*.webp"),
    ]
    images = []
    for pattern in image_patterns:
        images.extend(sorted(glob.glob(pattern)))
    # パスをウェブ用に変換（バックスラッシュ対策）
    images = [p.replace("\\", "/") for p in images]

    entries.append({
        "date": date,
        "text": text,
        "images": images
    })

# 新しい順にソート
entries.sort(key=lambda e: e["date"], reverse=True)

with open("entries.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

print(f"✅ {len(entries)} 件のエントリーを entries.json に書き込みました")
