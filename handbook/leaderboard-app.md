---
title: Building the leaderboard app and arena
summary: Notes for the FastAPI + React leaderboard app and the arena: data to read, design files, the submission flow, and what the homepage already promises.
---

# Building the leaderboard app and arena

[← Handbook](README.md)

Kalden is building a leaderboard web app (FastAPI + React), with a first version due 2026-11-18, and then the arena. This page collects what that work needs. Nothing here is a final decision about the app's own design: these are the parts that already exist and the rules the app must follow.

## What the app is for

NT's target (2026-11-17) is a site in the style of [AI Hero](https://www.aihero.dev/) with three parts:

1. **Skills page.** For each task and language: the **Top performance** skill and the **Best value** skill, with how to install each.
2. **Leaderboard.** All tasks on one board, two views (Top performance and Best value). Models are ranked with no skill ("No skill (plain prompt)") and with each skill, with filters (model, open weights or commercial, skills only). The leaderboard decides which skill goes into buddhist-skills.
3. **Arena**, in the style of [arena.ai](https://arena.ai/): readers vote blind between two answers; votes become an Elo-style rating per task and language. For tasks with no single right answer, such as translation.

The current homepage (https://buddhistai.github.io/) is the approved design for all of this. Read it first: every section there (task picker, skills by task, leaderboard tabs, model table, arena example, request form, benchmark maturity ladder, workflows, paste-a-link contribute flow, people) is a part the app may take over. The static leaderboard (https://buddhistai.github.io/buddhist-benchmarks/) shows what the data supports today.

## Keep GitHub as the source of truth

Scores must stay traceable to files in git: every row cites an exact skill commit, model and data version. So the app should **read the existing JSON files**, not become a second place where results are typed in. If the app needs a database (arena votes, submissions in progress), keep results out of it, or copy them in from git on each build.

Files to read (all in public repos; raw URL pattern `https://raw.githubusercontent.com/BuddhistAI/<repo>/main/<path>`):

| File | Repo | What it gives you |
| --- | --- | --- |
| `tasks/index.json` | buddhist-benchmarks | Every task: id, title, summary, `active` or `planned`. |
| `tasks/<task>/TASK.md` | buddhist-benchmarks | Task description, headline metric. |
| `tasks/<task>/data/<code>/v<N>/README.md` | buddhist-benchmarks | Benchmark card: version, item count, source, license (YAML front matter). |
| `tasks/<task>/results/<code>/runs/*/result.json` | buddhist-benchmarks | One leaderboard row each: scores per split (mean, std, runs), usage, model, skill ref, date, by. |
| `tasks/<task>/results/<code>/skills.json` | buddhist-benchmarks | Display name, status (`promoted`, `challenger`, `baseline`, `reference`), approach, made by, `hidden`, `baseline`. |
| `models.json` | buddhist-benchmarks | Model names, provider, price tier, list prices with date and source. |
| `external.json` | buddhist-benchmarks | Leaderboards run by others (BDRC Tibetan OCR), shown as link-out cards. |
| `STATE.md` | buddhist-benchmarks | Summary for funders (generated). |
| `tracks/index.json`, `tracks/*/results/*/runs/*/{run.json,scores.json}` | buddhist-bench | BuddhistBench tracks and model runs (skip `dry_run` and the `example` split). |
| `SKILLS.md`, `.claude-plugin/marketplace.json`, `skills/*/SKILL.md` | buddhist-skills | Released skills with metadata, plugins per language. |
| `*/*/CARD.md` (not `templates/`) | buddhist-prompts | Shared, unmeasured entries (`kind`, authors, license). |
| `languages.json` | buddhist-skills | Language names and codes. |
| `tasks/*.md` front matter | knowledge-base | Task area, summary, related tasks, contributors; link "Learn more" to `https://buddhistai.github.io/knowledge-base/tasks/<id>.html`. |

There is also a flat results table on Hugging Face: [`BuddhistAI/buddhist-benchmarks-results`](https://huggingface.co/datasets/BuddhistAI/buddhist-benchmarks-results), one row per `result.json`.

**Reuse the logic, do not reinvent it.** buddhist-benchmarks `scripts/build_leaderboards.py` already does: the cost per 100 pages (1 page = 1,500 input characters; tokens × `models.json` prices), the Top performance and Best value picks (Best value = top score among shippable options costing at most 20% of the top performance), gain over the no-skill row, ranking only within one data version and model, hiding `hidden` skills, showing `reference` and `baseline` rows unranked. The rules are written down in [docs/results.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/docs/results.md). Port them to Python in the FastAPI app, or import that module, so both sites always agree.

## Design

Use the BuddhistAI design system ([repo](https://github.com/BuddhistAI/design), [style guide](https://buddhistai.github.io/design/)):

```js
// tailwind.config.js
module.exports = { presets: [require('./tailwind.preset.js')], content: ['./src/**/*.{ts,tsx}'] };
```

```tsx
import './buddhistai.css';   // tokens + components; dark mode follows the system
<div className="pick top"><span className="lab">Top performance</span>…</div>
```

- Copy `buddhistai.css` and `tailwind.preset.js` (or `tokens.js` without Tailwind) from the design repo into the app. Add the app to the "copy into each site" list in the design README.
- Use the existing parts and class names: header, footer, buttons, chips, cards, Top performance / Best value picks, badges, status labels, tables, maturity ladder, paste-a-repo box.
- No new hex colors. Lapis = Top performance and links; saffron = Best value and contribute; green = measured and new leader; red = losses only.
- Tibetan text gets `lang="bo"`. Layout must work at 360px wide. Words follow [VOICE.md](https://github.com/BuddhistAI/design/blob/main/VOICE.md).

## Submission flow

Decided at the 2026-11-17 call; not built yet. Model it on BDRC's OCR leaderboard:

1. The contributor pastes a GitHub repo link (skill, model or benchmark data). There must be a clear Submit button (an earlier email-based flow was too hard to use).
2. The app (or a GitHub Action) reads the repo: finds each `SKILL.md`, guesses task and language from the name, and asks the contributor to confirm.
3. The entry is listed at once under Community (unmeasured).
4. A GitHub Action runs it on every benchmark for its task, on the standard models, using a **sponsor key** (Dave offered inference keys). Set a spending limit and an iteration limit.
5. A maintainer checks and approves. The `result.json` is committed to buddhist-benchmarks (so the score stays in git).
6. If it becomes Top performance or Best value, it is promoted to buddhist-skills and the author is announced on LinkedIn and X ([how-to](how-to.md#announce-a-new-leader)).

Contributors may not come back to update their entries, so the flow should work from the link alone. Today the homepage's paste box only opens a prefilled buddhist-skills issue (`request.yml` or `share.yml`), and a maintainer does the rest by hand.

The homepage lists the promised steps for each kind of link (skill, model, benchmark). Keep the app's flow and those texts in step.

## Arena

Planned. What the homepage already shows:

- A source text and two answers (A and B), from a model alone or a model with a skill. The voter picks "A is better", "Tie" or "B is better". Entries are revealed only after the vote.
- One rating table per task and language (entry, rating, votes).
- First use: translation, Tibetan to English (example: *The Thirty-Seven Practices of Bodhisattvas*, verse 1). The homepage example is marked "Example layout. No votes yet." Never show invented votes.

Open points to settle with NT: who may vote (any visitor, signed-in GitHub users, or registered language readers; decisions should favor active translators), how votes are stored and published (an open votes file in git would match the rest of the project), and abuse protection.

## Hosting and domain

Not decided. Today all sites are GitHub Pages under `buddhistai.github.io`. NT bought `buddhistai.org` on Cloudflare (2026-11-17); DNS is not set up. A FastAPI app needs a server (the static pages can stay on GitHub Pages). Agree with NT where it runs and which subdomain it gets before pointing DNS. When the domain moves, update every link in the org profile, the homepage, the READMEs and this handbook.

## Checklist before launch

- Every number on the page comes from a file in git; nothing typed by hand.
- Rows from different data versions are never ranked together.
- "Top performance" and "Best value" (not "best overall"), "Buddhist tasks", plain English.
- Models are ranked too, with a "No skill" row; BuddhistBench is one Q&A benchmark among others.
- Planned features (arena, automatic scoring, MCP) are labelled as planned.
- Credits are neutral: contributors listed alphabetically, no lead organization.
- Footer links: GitHub org, Discussions, knowledge base, Directory, license (MIT).

## UX reviews for the app

The app is the biggest change users will see, so it uses the [UX reviews with EGM](ux.md) process from the start:

- Before each screen or flow (task page, compare view, submit, arena), write a short design in the app repo's `docs/designs/` and run the `buddhistai-ux-review` skill. The journeys that matter most are [Find and use a skill](../ux/journeys/find-and-use-a-skill.md) and [Get a skill or model measured](../ux/journeys/get-measured.md).
- Copy `.claude/settings.json`, `.claude/skills/buddhistai-*` and `.github/workflows/egm.yml` from buddhistai.github.io into the app repo, and set its user-facing paths (for example `frontend/`).
- After each release, update the journey files in knowledge-base `ux/journeys/` if steps changed.

