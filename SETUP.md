# Setup guide

This repo is a **GitHub profile README** — it only renders on your profile if the repo is
named *exactly* `aashma-yadav` (same as your username) and is **public**.

## 1. Create/upload the repo
```bash
# if you don't already have the special profile repo:
# create a new PUBLIC repo on GitHub named exactly: aashma-yadav

git init
git remote add origin https://github.com/aashma-yadav/aashma-yadav.git
git add .
git commit -m "init: cyberpunk profile"
git branch -M main
git push -u origin main
```

## 2. Turn on Actions
`Settings → Actions → General → Allow all actions and reusable workflows`

## 3. Snake animation (works out of the box)
`.github/workflows/snake.yml` uses the built-in `GITHUB_TOKEN`, no setup needed beyond
step 2. It writes to an `output` branch automatically. Run it once manually:
`Actions → Generate Snake Animation → Run workflow`.
After the first run, `assets` folder isn't touched — the SVG/GIF live on the `output`
branch and the README already points at
`https://raw.githubusercontent.com/aashma-yadav/aashma-yadav/output/snake.svg`.

## 4. Metrics (isometric calendar + achievements) — needs one secret
The `lowlighter/metrics` action needs a **Personal Access Token** (the default
`GITHUB_TOKEN` doesn't have enough scope to read full account stats):

1. GitHub → **Settings → Developer settings → Personal access tokens → Tokens (classic)**
2. Generate one with scopes: `repo`, `read:user`, `read:org` (optional)
3. In the `aashma-yadav/aashma-yadav` repo: **Settings → Secrets and variables → Actions
   → New repository secret**
4. Name it `METRICS_TOKEN`, paste the token
5. `Actions → Generate Metrics → Run workflow`

This commits `metrics.isocalendar.svg` and `metrics.achievements.svg` to `main`, which
the README already embeds.

## 5. Fill in the placeholders
- **Washify card** (`assets/card-washify.svg`) — I didn't have details on this project
  from your resume, so it's a placeholder. Send me a one-line description + 3 key
  features + tech stack and I'll regenerate it to match the others exactly.
- **Project links** — every card in the "Featured builds" section currently links to
  `https://github.com/aashma-yadav`. Point each `<a href="...">` at the actual repo.
- **LeetCode handle** — the LeetCode card assumes your LeetCode username is
  `aashma-yadav`. If it's different, edit the URL in the `## LeetCode` section.

## 6. Optional: regenerate project cards
All seven cards are generated from one script (`gen_cards.py`, included at repo root —
not required for the site to work, just kept for future edits). Edit the `CARDS` list
and rerun `python3 gen_cards.py` to update copy, bullets, or accent colors without
touching raw SVG by hand.

## Notes on the "auto light/dark mode"
GitHub reads `prefers-color-scheme` on `<picture>` tags in READMEs. The banner and
activity graph both ship dark + light variants and switch automatically with the
viewer's OS/browser theme — no action needed.
