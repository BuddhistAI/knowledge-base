---
title: How-to guides
summary: Step-by-step guides for the regular maintainer jobs in BuddhistAI.
---

# How-to guides

[← Handbook](README.md)

Each guide lists the repo, the steps and the check to run. In every repo: run `python3 scripts/build.py` (where it exists), then `python3 scripts/check.py`, before you push. CI runs the same check.

- [Run an evaluation](#run-an-evaluation)
- [Add a result and update the leaderboard](#add-a-result-and-update-the-leaderboard)
- [Promote a winner to buddhist-skills](#promote-a-winner-to-buddhist-skills)
- [Handle a submission](#handle-a-submission)
- [Announce a new leader](#announce-a-new-leader)
- [Turn a Share issue into a community entry](#turn-a-share-issue-into-a-community-entry)
- [Add a benchmark](#add-a-benchmark)
- [Add a task, a language or a model](#add-a-task-a-language-or-a-model)
- [Add an external leaderboard](#add-an-external-leaderboard)
- [Release a BuddhistBench version](#release-a-buddhistbench-version)
- [Knowledge base: pages, Directory, experiments](#knowledge-base-pages-directory-languages-experiments)
- [Change the design](#change-the-design)
- [Add a contributor or a backer](#add-a-contributor-or-a-backer)

## Run an evaluation

Today a maintainer runs every evaluation on their own machine with their own API key. Automatic scoring is planned ([Status](status.md)).

**Generic steps (any task):**

1. Read the task's `TASK.md` in buddhist-benchmarks for the input, the output format and the headline metric.
2. Run the skill (or the plain model, for the "No skill" row) on every item's `input` in `tasks/<task>/data/<code>/v<major>/test.jsonl`. Save `predictions.jsonl`, one line per item: `{"id": ..., "output": ...}`.
3. **Log real token counts** from the API (input and output, every call, retries and tool calls too). Cost on the leaderboard comes from these.
4. Score it:

   ```bash
   python3 tasks/<task>/scorer/score.py --language <code> \
     --data tasks/<task>/data/<code>/v<major>/test.jsonl \
     --predictions predictions.jsonl > scores.json
   ```

5. Repeat at least 3 times when the model is not deterministic (Claude 5.5 models only accept temperature 1.0).
6. Never tune a skill on the test set. Use separate training data (for example toc-extraction-tibetan `benchmark/data/train.jsonl`).
7. Run the same model with no skill too, so the leaderboard can show the gain.

**Worked example: Tibetan TOC** ([toc-extraction-tibetan](https://github.com/BuddhistAI/toc-extraction-tibetan)):

```bash
python -m venv .venv && .venv/bin/pip install -r benchmark/requirements.txt
export ANTHROPIC_API_KEY=...
python benchmark/bench_skills.py --model anthropic/claude-haiku-5-5 --temperature 1.0 \
  --conds ours,colleague,colleague+tool,seed,skill:variants/sabcad-outliner-toc \
  --out results/<date>-haiku-5-5-run1.json      # run 3 times: run1, run2, run3
python scripts/summarize.py results/<date>-*-run*.json
python scripts/to_result_json.py --date <date> --commit <short-commit> --benchmarks ../buddhist-benchmarks
```

`ours` is the GEPA variant, `colleague` the sa-bcad outliner, `seed` the no-skill prompt; `skill:<folder>` runs any variant folder. `to_result_json.py` writes the `result.json` files straight into a buddhist-benchmarks checkout. The benchmark version is pinned in `benchmark/benchmark.json` and downloaded on first use. GEPA optimization (`benchmark/gepa_toc.py`) burns many tokens: always set an iteration limit.

## Add a result and update the leaderboard

Repo: buddhist-benchmarks. Format: [docs/results.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/docs/results.md).

1. Make `tasks/<task>/results/<code>/runs/<run-id>/` with `result.json` (required), plus `scores.json` and the outputs so anyone can re-score. `<run-id>` = `<date>-<skill>-<variant>-<version>-<short-commit>-<model-slug>`.
2. `result.json` must cite `skill_ref` (`owner/repo@commit:path`), `model` (must be in `models.json`), `data_version`, `scorer_version`, `repeats` and `usage` (real tokens, `estimated: false`).
3. Add the variant to that language's `skills.json` if it is new: `status` (`promoted`, `challenger`, `baseline` or `reference`), `name`, `approach` (two sentences), `made_by`, `source`.
4. Run `python3 scripts/build_leaderboards.py` and `python3 scripts/check.py`. Commit and push to `main` (or open a PR and merge it).
5. CI rebuilds `LEADERBOARD.md`, the README table, `STATE.md` and the site, and publishes the results table to Hugging Face.
6. **Update the homepage by hand:** the leaderboard preview on https://buddhistai.github.io/ is a `rows` array in buddhistai.github.io `index.html` (search for `const rows=`). Copy the new numbers there. (Planned: read them from the leaderboard data instead.)

Top performance = highest headline score among shippable skills on the latest data version. Best value = highest score among options that cost at most 20% of the top performance. The script picks both.

## Promote a winner to buddhist-skills

Repo: buddhist-skills. Full steps in its [CONTRIBUTING.md](https://github.com/BuddhistAI/buddhist-skills/blob/main/CONTRIBUTING.md#from-challenger-to-promoted-skill).

1. Check the leaderboard: the new skill beats the current one on the same data version, by more than the run-to-run noise (compare the ± values).
2. Copy the skill into `skills/<task>-<language>/` with metadata: `task`, `language`, `language-code`, `benchmark` (`<task>/<code>@<version>`), `score`, `version`, `source` (`owner/repo@commit:path`), `promoted` (date), `authors`.
3. Run `python3 scripts/build.py` (regenerates `SKILLS.md` and `.claude-plugin/marketplace.json`) and `python3 scripts/check.py`.
4. Add an entry at the top of `CHANGELOG.md`.
5. If this is the first skill for this task in any language, add the task to `skills/ask-buddhistai/SKILL.md`.
6. In buddhist-benchmarks `skills.json`, set the new variant to `promoted` and the old one to `challenger`, and set `promoted`. Rebuild the leaderboards.
7. Update the task page here (`skills:` in the front matter), run `python3 scripts/build.py`.
8. [Announce the new leader](#announce-a-new-leader).

Never edit a released `SKILL.md` directly. Improvements start as a challenger in `drafts/` and come back through promotion.

## Handle a submission

**Today (manual):**

1. A submission arrives as a pull request to buddhist-benchmarks (following [SUBMIT.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md)), a Share issue, a homepage "paste your repo" link (opens a prefilled buddhist-skills issue), or a post in Discussions.
2. Check: the result cites an exact commit, the right data version, real token counts, and includes outputs. The skill follows the one-language rule. The author is named.
3. If only a skill was submitted (no run), run the evaluation yourself ([above](#run-an-evaluation)) on the standard models (today Claude Haiku 5.5 and Claude Sonnet 5.5).
4. Merge. Move the item on the [Skills board](https://github.com/orgs/BuddhistAI/projects/1) to "Being measured", then "Released" if it is promoted.
5. Thank the author on the issue or PR.

**Planned (decided at the 2026-11-17 call):** submit by linking a GitHub repo; a GitHub Action reads the repo, guesses task and language, runs the benchmark on a sponsor key, and posts the score; a maintainer approves (like BDRC's OCR leaderboard). See [Building the leaderboard app](leaderboard-app.md#submission-flow).

## Announce a new leader

When a submission becomes the Top performance or Best value pick for a task and language, or a new benchmark goes live:

1. Congratulate the author on the issue or PR.
2. Post on LinkedIn and X, crediting the person and their organization, with a link to the leaderboard row. Who owns the social accounts is not decided yet ([Status](status.md#open-questions)); until then, ask NT.
3. Keep posts plain and neutral: what the task is, the score and cost, who made it, how to install it.

Example: "New Best value for Tibetan TOC extraction: [skill] by [author, org] scores 0.82 on Claude Haiku 5.5 at about $0.05 per 100 pages. Install it from buddhist-skills. Leaderboard: [link]"

## Turn a Share issue into a community entry

Repo: buddhist-skills.

1. Create `community/<task>-<language>/<author>-<name>/` with `CARD.md` (from `templates/CARD.md`) and the content as `SKILL.md`, `WORKFLOW.md`, `PROMPT.md` or, for a personal setup, its own file name with `kind: personal`.
2. Credit the author in `authors`. Keep one language per entry. Use a task ID from `tasks/index.json` when one fits.
3. Run `python3 scripts/build.py` and `python3 scripts/check.py`. Link the commit on the issue and close it. Move the card on the Skills board to "Shared".

## Add a benchmark

Repo: buddhist-benchmarks (see its [CONTRIBUTING.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/CONTRIBUTING.md)).

1. Agree on it in a [Propose a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=propose-benchmark.yml) issue. Prefer real data already in use. Favor what active translators need.
2. Add `tasks/<task>/data/<code>/v1/test.jsonl` and `README.md` (dataset card; template: `toc-extraction/data/bo/v2`). Add `tasks/<task>/results/<code>/skills.json`.
3. New task: also `TASK.md`, `scorer/score.py`, the entry in `tasks/index.json` (set `active`), `CHANGELOG.md`.
4. Have the answer key checked by a reader of that language and tradition.
5. Run `python3 scripts/check.py`, merge. CI tags `<task>/<code>@1.0.0` and publishes `BuddhistAI/<task>-<language>` on Hugging Face.
6. Run the current skills and plain models on it. Update the task page here (`benchmarks:`, `leaderboard:`, `status: measured`).

When two groups have different benchmarks for the same task, keep both and score new skills on both.

## Add a task, a language or a model

- **Task:** a page `tasks/<id>.md` here (copy `templates/task.md`) and a `planned` entry in buddhist-benchmarks `tasks/index.json`. Run `python3 scripts/build.py` here.
- **Language:** add it to buddhist-skills `languages.json` and buddhist-bench `taxonomy/languages.json`.
- **Model:** add it to buddhist-benchmarks `models.json` with its display name, provider, price tier and list prices (`input_per_mtok`, `output_per_mtok`, `date`, `source`) before adding its first result. When a provider changes prices, update them there: every cost follows.

## Add an external leaderboard

Add an entry to buddhist-benchmarks `external.json`. The overview shows it as a card that links out. To show its live top rows, add a parser in `build_leaderboards.py` (`--fetch-external`). Nothing external is scored by us.

## Release a BuddhistBench version

Repo: buddhist-bench. Bump `VERSION` and each changed `track.json`, add a `CHANGELOG.md` entry, run `python3 scripts/check.py`, push to `main`. `hf-sync` tags `vX.Y.Z` and publishes. Real items need human authors and two human reviewers (same tradition and another tradition). Never commit `test.jsonl`, permission letters or private papers. Never publish an intervention that is not accurate, sourced and reviewed.

## Knowledge base: pages, Directory, Languages, experiments

Repo: knowledge-base.

- **Task or workflow page:** copy from `templates/`. Run `python3 scripts/build.py` (index tables, "Found in workflows", Directory tables), then `python3 scripts/check.py`.
- **Directory entry:** add to `directory/projects.yml` or `directory/datasets.yml`, never to `directory/README.md`. Verify the link first.
- **Language page:** `languages/<id>.md`, copied from `templates/language.md`. Keep every frontmatter key and section. `directory_names` must match the language names used in the Directory YAML: the "In the Directory" block on each page and the counts in `languages/README.md` are generated from them by `scripts/build.py`. Countries live in `languages/countries.yml` (each with a source link). The speakers chart on `languages/README.md` is drawn by `scripts/charts.py` from `speakers_n`, `speakers_year`, `speakers_source` (and optional `speakers_basis`, `short_title`) in each page; the map uses `iso` and `buddhists_n` in `countries.yml` and is drawn in the browser by `assets/buddhist-map.js` (d3 and world-atlas from jsdelivr). Leave a number out rather than guess it. Every fact needs a numbered source; write "not verified" when you cannot check a fact. Re-check the pages about every six months, because AI support changes fast.
- **Experiment:** folder `experiments/<yyyy-mm>-<slug>/` from `templates/experiment/`. Write `PLAN.md` before running and never edit it after the start; record changes in `LOG.md`. Numbers in `REPORT.md` link to results at an exact commit or version. Update the table in `experiments/README.md`.
- **This handbook:** update it in the same PR as any change it describes.

## Change the design

Repo: design.

1. Edit `tokens.json` or `css/*.css`.
2. `python3 scripts/build.py`, then `python3 scripts/check.py` (WCAG AA in light and dark).
3. Bump `version` in `tokens.json`, add a `CHANGELOG.md` line. Never rename a class without a major bump.
4. Copy `buddhistai.css` into buddhist-benchmarks `site/` and knowledge-base `assets/` (and the leaderboard app, when it exists).

## Add a contributor or a backer

1. Edit both the org profile (BuddhistAI/.github `profile/README.md`, "Contributors" and "Supported by") and the homepage (buddhistai.github.io `index.html`, section `#people`). Alphabetical order.
2. Contributors get avatar cards (GitHub avatar, name, "Person" or "Organization"). Backers get text cards (name + website).
3. Only add a backer after NT confirms it. No logos without permission. WeBuddhist stays one card among others.
