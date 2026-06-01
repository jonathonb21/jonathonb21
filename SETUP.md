# GitHub Profile README — Setup

This folder is a ready-to-publish **GitHub profile README** repository.

## How it works

GitHub shows a README on your profile when **all** of these are true ([docs](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)):

1. Repository name **exactly matches** your GitHub username (e.g. `jonathonb21/jonathonb21`)
2. Repository is **public**
3. Root contains `README.md` with content

## Publish steps

### Option A — GitHub website

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `jonathonb21` *(must match your username)*
3. Visibility: **Public**
4. Check **Add a README file** → Create repository
5. Replace the generated README with the contents of `README.md` in this folder
6. Commit `.github/workflows/snake.yml` for the contribution snake animation

### Option B — Git CLI

```bash
cd "github/jonathonb21"
git init
git add README.md .github/workflows/snake.yml
git commit -m "Add profile README"
git branch -M main
git remote add origin https://github.com/jonathonb21/jonathonb21.git
git push -u origin main
```

## After publishing

- **Stats cards** pull from [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) — they populate once the repo is live.
- **Snake animation** runs nightly via GitHub Actions. Trigger manually: **Actions → Generate Snake → Run workflow**. First run creates the `output` branch with SVG assets.
- **Profile view counter** ([komarev](https://github.com/antonkomarev/github-profile-views-counter)) starts counting after the README is on your profile.

## Customize

| Section | What to edit |
|---------|----------------|
| Typing lines | `readme-typing-svg.demolab.com` URL in README |
| Banner colors | `capsule-render.vercel.app` query params |
| Highlights table | Your proudest 4 bullets — keep it scannable |
| Tech badges | Add/remove shields in the **Tech Stack** section |
