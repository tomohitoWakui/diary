# diary

GitHub Pages で動く日記サイト。

## セットアップ

```bash
# リポジトリ作成後
git init
git add .
git commit -m "init"
git remote add origin https://github.com/あなたのユーザー名/diary.git
git push -u origin main
```

GitHub の Settings → Pages → Source を `main` ブランチのルートに設定する。

---

## 日記の書き方

### 1. テキストファイルを作る

```
entries/2026-06-11.txt
```

中身はそのまま文章を書くだけ。段落は空行で区切る。

```
今日は雨だった。

夕方に散歩した。
```

### 2. 画像を入れたい場合

```
images/2026-06-11-1.jpg
images/2026-06-11-2.jpg
```

のように `日付-連番.拡張子` で置く。

### 3. entries.json を更新する

```bash
python3 update-entries.py
```

### 4. デプロイ

```bash
git add .
git commit -m "2026-06-11"
git push
```

---

## スクリプト（Mac/Linux）

```bash
chmod +x new-entry.sh
./new-entry.sh          # 今日の日付でエディタが開く
./new-entry.sh 2026-06-10  # 指定日付
```

エディタを保存して閉じると自動で `entries.json` が更新される。あとは `git push` するだけ。

---

## ファイル構成

```
index.html          # 日付一覧
entry.html          # 各エントリーページ
entries.json        # 全エントリーデータ（自動生成）
entries/            # 日記テキスト置き場
  2026-06-11.txt
images/             # 画像置き場
  2026-06-11-1.jpg
update-entries.py   # entries.json 再生成スクリプト
new-entry.sh        # 新エントリー作成ヘルパー（任意）
```
