---
title: Conventions
summary: Names, data format, versions, licenses, design system and writing style used across BuddhistAI.
---

# Conventions

[← Handbook](README.md)

## Tasks and languages

- **Task IDs** live in one place: buddhist-benchmarks [`tasks/index.json`](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/tasks/index.json) (status `active` or `planned`). Each task also has a page here in `tasks/<task-id>.md`. A new task needs both.
- **Language names and codes** live in buddhist-skills [`languages.json`](https://github.com/BuddhistAI/buddhist-skills/blob/main/languages.json): full English name for folder names (`tibetan`, `classical-chinese`), ISO code for data folders and metadata (`bo`, `lzh`). buddhist-bench keeps a copy in `taxonomy/languages.json`; keep the two in sync. Add a language there before its first skill or data set.

## Skills

- **One skill = one task in one language.** Never mix languages in one skill. Language specialists own their language.
- **Flat names:** `skills/<task>-<language>/`, for example `toc-extraction-tibetan`. A task that produces another language adds `-to-<language>`: `translation-tibetan-to-english`. Language-neutral skills (the router `ask-buddhistai`) have no suffix.
- **Three places in buddhist-skills:** `skills/` (released, only changed by promotion), `drafts/<task>-<language>/<org>-<variant>/` (challengers), `community/<task>-<language>/<author>-<name>/` (shared, unmeasured: `CARD.md` plus `SKILL.md`, `WORKFLOW.md` or `PROMPT.md`).
- **One plugin per language:** `scripts/build.py` writes `.claude-plugin/marketplace.json` with `buddhist-skills-<language>` per language plus the all-in-one `buddhist-skills`. Marketplace name: `buddhistai`. Install: `claude plugin marketplace add BuddhistAI/buddhist-skills`, then `claude plugin install buddhist-skills-tibetan@buddhistai`. Community entries are never in a plugin.
- **The router** `skills/ask-buddhistai/SKILL.md` must list every task that has a skill. Update it when a task is added or removed.
- **Shared resources** (glossaries, transliteration tables, style guides) live only in buddhist-skills `shared/`.
- Full design rationale: buddhist-skills [docs/design.md](https://github.com/BuddhistAI/buddhist-skills/blob/main/docs/design.md).

## Benchmark data format

One standard for every task benchmark, so each loads with Hugging Face `datasets`:

```
tasks/<task>/data/<lang-code>/v<major>/
  test.jsonl     one item per line: {"id": ..., "input": ..., "target": ..., "metadata": {...}}
  README.md      Hugging Face dataset card: YAML front matter (license, language, configs → test.jsonl),
                 then version, purpose, item count, source and license of the texts,
                 who made the answers, and a worked example
```

- Template: [toc-extraction/data/bo/v2](https://github.com/BuddhistAI/buddhist-benchmarks/tree/main/tasks/toc-extraction/data/bo/v2).
- `metadata.subset` splits the score (for example `same-book` and `held-out-book`).
- An `example` folder holds format examples only. They never go on a leaderboard.
- **One scorer per task**, shared by every language: `tasks/<task>/scorer/score.py`. Language-specific normalization goes inside it, keyed by language code.
- Prefer real data that people already use (real OCR, real editions, real exam papers). About 30 items is a good first set. Small but diverse is better than large.
- Results format (`result.json`, `skills.json`, cost): buddhist-benchmarks [docs/results.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/docs/results.md).

BuddhistBench uses its own item schema (`tracks/<track>/data/<lang>/<split>.jsonl`, [docs/schema.md](https://github.com/BuddhistAI/buddhist-bench/blob/main/docs/schema.md)) because it is a Q&A set with traditions, reviewers and permissions. Its `test.jsonl` is private and never committed.

## Versions

Everything that is scored has a semantic version (`MAJOR.MINOR.PATCH`).

| Thing | Where the version is | Patch | Minor | Major |
| --- | --- | --- | --- | --- |
| Benchmark data set | Dataset card `README.md` + task `CHANGELOG.md`; tag `<task>/<lang>@X.Y.Z` (made by CI) | Fixed references | New items | Scorer or format change: new `v<major>/` folder |
| Scorer | `SCORER_VERSION` in `score.py` and `TASK.md` | — | — | Any change that moves scores; bump every data set's major too |
| Skill or variant | `metadata.version` in `SKILL.md` | Wording fix | New behaviour | Changed output |
| BuddhistBench | `VERSION` + each `track.json` + `CHANGELOG.md`; tag `vX.Y.Z` | Gold fixes | New items, tracks, languages | Format, scorer or judge change |
| Workflow page | `version` in its front matter (`source_version` is the owner's own version) | Small fix | New step or task | Restructure |
| Design system | `version` in `tokens.json` + `CHANGELOG.md` | Changed value | New token or part | Renamed or removed class |

- Never change items or references without bumping the version.
- Leaderboard rows cite the exact data version. **Never compare rows across data versions.**
- Every result cites the exact skill commit: `owner/repo@commit:path`.
- Rules in full: buddhist-benchmarks [VERSIONING.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/VERSIONING.md).

## Licenses and imports

- Everything we write is **MIT**.
- Imported data keeps its own license, and that license must be compatible with MIT (for example the Thai exam set is Apache-2.0). Non-commercial licenses (such as CC-BY-NC-SA) cannot be imported; link to the set instead.
- **Copy, do not use submodules.** Add a `SOURCE.md` next to the copy with the source URL, the pinned revision, the license and the date. Mark published sets `contamination: public` (they may be in model training data).
- A linked workflow stays in its owner's document. Summarize it in our own words and link to it; never copy it.
- Language pages: every fact has a source; mark evidence as benchmark, vendor claim or anecdotal; give the year of each test; never compare chrF++ or BLEU scores across languages.
- Directory entries: verify every link, never invent one, describe without ranking, and write "license not stated" when you cannot find the license.

## Design system

One look for every site. Source: [BuddhistAI/design](https://github.com/BuddhistAI/design), style guide at https://buddhistai.github.io/design/.

- `tokens.json` is the source of truth. `scripts/build.py` writes `css/tokens.css`, `buddhistai.css`, `tailwind.preset.js` and `tokens.js`. `scripts/check.py` checks WCAG AA contrast in light and dark mode. Never add a hex color anywhere else.
- **Sites copy `buddhistai.css`** (they do not link to it across sites). Today: buddhist-benchmarks `site/buddhistai.css` and knowledge-base `assets/buddhistai.css`. After a design change, copy the new file into each site. The homepage still has its own inline CSS from the same design.
- React apps use `buddhistai.css` + `tailwind.preset.js` (or `tokens.js` without Tailwind). See [Building the leaderboard app](leaderboard-app.md#design).
- Colors mean one thing each: **lapis** = links, primary action, Top performance. **Saffron** = contribute, Best value. **Green** = measured, new leader, gains. **Red** = losses and errors only.
- Fonts: Bricolage Grotesque (headings), Inter (text), JetBrains Mono (code, numbers), Noto Serif Tibetan (`lang="bo"`).
- Layout works at 360px wide. Dark mode follows the system.
- Logo: a caliper measuring an eight-spoke wheel with "AI" at the hub. Files in design `assets/`. Emoji mark: ☸📊.

## Writing

- Plain English for non-native readers. Short, literal sentences. No idioms. See [VOICE.md](https://github.com/BuddhistAI/design/blob/main/VOICE.md).
- "Buddhist tasks", "Top performance", "Best value", "Share → Measure → Release", "best skill".
- Unicode for Tibetan, Sanskrit, Pali and Chinese; say which transliteration scheme you use.
- Commit messages: a short sentence saying what changed, in the imperative ("Add …", "Fix …").

## Credit

- Credit every author by name: `authors` in a community `CARD.md`, `metadata.authors` in a `SKILL.md`, `made_by` in `skills.json`, `contributors` on task and workflow pages. Reviewers and language readers too.
- **Contributors** (organizations and people who build things) are shown as avatar cards on the org profile and the homepage `#people` section: today WeBuddhist and ngawangtrinley. Add new contributors to both places, in alphabetical order.
- **Backers** ("Supported by") are organizations that support the project, shown as text cards in alphabetical order on both pages: today Buddha Educational Foundation, OpenPecha, Unione Buddhista Italiana. Only list a backer after NT confirms it. Never rank or size them by amount.
- WeBuddhist is one contributor among others. Never put it at the top or call it the lead.
