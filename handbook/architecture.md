---
title: Architecture
summary: Every BuddhistAI repo, site, board, form, CI workflow and secret, and how data flows between them.
---

# Architecture

[← Handbook](README.md)

## The flow

```
workflows → tasks → benchmarks → results → leaderboards → best skills
(knowledge base)    (buddhist-benchmarks, buddhist-bench)     (buddhist-skills)
                         ↑
     workshop repos (one per skill, e.g. toc-extraction-tibetan): variants, runs, reports
```

1. A **workflow** page describes how a real project works. Each step maps to a **task**.
2. A **task** has a definition page here and an entry in buddhist-benchmarks `tasks/index.json`.
3. A **benchmark** (test data + scorer) measures the task for one language.
4. Skills and models are run on the benchmark. Each run adds a `result.json`.
5. Scripts build the **leaderboards** from the result files. Nothing on a leaderboard is typed by hand.
6. The best skill per task and language is **released** to buddhist-skills, where people install it.

## Repos

All repos are in the [BuddhistAI GitHub org](https://github.com/BuddhistAI), public, MIT licensed. Each has a `README.md` and a `CLAUDE.md` / `AGENTS.md` that starts with the same "Start here" block (read this handbook, check the Development board, the core rules) followed by the repo's own rules. The main repos also have a `scripts/check.py` that CI runs. The homepage and toc-extraction-tibetan have no CI.

| Repo | Role | Site |
| --- | --- | --- |
| [.github](https://github.com/BuddhistAI/.github) | Org profile (`profile/README.md`, banners in `profile/assets/`), org-wide `CODE_OF_CONDUCT.md`. | [github.com/BuddhistAI](https://github.com/BuddhistAI) |
| [template-skill-repo](https://github.com/BuddhistAI/template-skill-repo), [template-benchmark](https://github.com/BuddhistAI/template-benchmark) | GitHub template repos for new skill repos and new benchmark repos ([how-to](how-to.md#create-a-new-repo)). Created 2026-11-18. | — |
| [buddhistai.github.io](https://github.com/BuddhistAI/buddhistai.github.io) | The homepage. One self-contained `index.html` (inline CSS and JS). Scores on it are copied by hand from the leaderboard. | https://buddhistai.github.io/ |
| [design](https://github.com/BuddhistAI/design) | Design system: `tokens.json` (source of truth), generated `buddhistai.css`, `tailwind.preset.js`, `tokens.js`, logos, banners, `VOICE.md`. | https://buddhistai.github.io/design/ |
| [knowledge-base](https://github.com/BuddhistAI/knowledge-base) | This site: task definitions, workflows, experiments, the Directory, the Languages pages (AI resources per Buddhist language and a country overview), and this handbook. Jekyll on GitHub Pages. Was called `wiki`; the old `research` repo was merged in. | https://buddhistai.github.io/knowledge-base/ |
| [buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks) | Hub for task benchmarks: `tasks/index.json`, per task `TASK.md`, scorer, data, results; `models.json` (prices); `external.json` (other groups' leaderboards); `STATE.md`; `SUBMIT.md`. Builds the leaderboard site. | https://buddhistai.github.io/buddhist-benchmarks/ |
| [buddhist-bench](https://github.com/BuddhistAI/buddhist-bench) | BuddhistBench: a Q&A benchmark of Buddhist knowledge (tracks by tradition, text and exam; language as an axis). Also the OpenRouter runner and the intervention study. Version 0.4.0, examples plus one imported set. | Shown on the leaderboard site |
| [buddhist-skills](https://github.com/BuddhistAI/buddhist-skills) | The shelf: only released (promoted) skills in `skills/`, challengers in `drafts/`, unmeasured shared entries in `community/`, shared glossaries in `shared/`. Builds the Claude plugin marketplace. | Installed as a plugin |
| [toc-extraction-tibetan](https://github.com/BuddhistAI/toc-extraction-tibetan) | The first workshop repo: every variant of the Tibetan TOC skill, the runs, and `REPORT.md`. Pins the benchmark; holds no test data. | — |
| [research](https://github.com/BuddhistAI/research) | **Archived.** Now the [Experiments](../experiments/README.md) section of this site. | — |

Old names still redirect: `BuddhistAI/skills` → buddhist-skills, `BuddhistAI/wiki` → knowledge-base. Always use the new names.

Hugging Face: org [BuddhistAI](https://huggingface.co/BuddhistAI). Data sets there are copies made by CI ([below](#github-to-hugging-face)). Never edit them on Hugging Face.

### Target layout (decided, not built yet)

The team decided on 2026-11-17 that each benchmark gets **its own repo** with maturity information, and buddhist-benchmarks becomes a list of all benchmarks per task. Today the only task benchmark (`toc-extraction/bo`) still lives inside buddhist-benchmarks. Likewise each task gets a workshop repo with all submitted versions, and buddhist-skills holds per task both the **Top performance** and the **Best value** skill (today it holds one released skill per task and language). See [Status](status.md#roadmap).

## Sites

| Site | Built from | How it deploys |
| --- | --- | --- |
| https://buddhistai.github.io/ | buddhistai.github.io `index.html` | GitHub Pages from `main`, root. No build step. |
| https://buddhistai.github.io/buddhist-benchmarks/ | buddhist-benchmarks `scripts/build_leaderboards.py --site` + `site/` (CSS, JS) | `leaderboards` workflow (`.github/workflows/pages.yml`) on push to `main` and daily at 03:17 UTC. Pages source: GitHub Actions. |
| https://buddhistai.github.io/knowledge-base/ | knowledge-base Markdown, `_layouts/default.html`, `assets/` | GitHub Pages from `main`, root (Jekyll, plugins in `_config.yml`). |
| https://buddhistai.github.io/design/ | design `index.html` | GitHub Pages from `main`. |
| `buddhistai.org` | — | Domain bought by NT on Cloudflare (2026-11-17). DNS is not set up yet. |

## GitHub Projects boards

The Skills and Benchmarks boards are public, for contributors. The Development board is for team work. Columns, fields and automations are set only in the GitHub web UI (Settings of each project).

| Board | Columns | Filled by |
| --- | --- | --- |
| [Skills board](https://github.com/orgs/BuddhistAI/projects/1) | Requested → Shared → In progress → Being measured → Released | Auto-adds open buddhist-skills issues labeled `request` or `community-share`. |
| [Benchmarks board](https://github.com/orgs/BuddhistAI/projects/2) | Proposed → Needs test data → In progress → Being reviewed → Live | Auto-adds open buddhist-benchmarks issues labeled `benchmark`. |
| [Development board](https://github.com/orgs/BuddhistAI/projects/3), for team members | To do → In progress → In review → Done; fields Owner and Area; views Board and Table | Team tasks, added by hand. **Private** for now (only org members can open it) until NT decides whether it should be public. |

## Issue forms and labels

| Repo | Form | Label | What a maintainer does |
| --- | --- | --- | --- |
| buddhist-skills | [Request an AI solution for a task](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=request.yml) | `request` | Find or define the task; add a task page here if needed. |
| buddhist-skills | [Share a skill](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=share.yml) (a link or uploaded files) | `community-share` | Turn it into a `community/` entry and credit the author ([how-to](how-to.md#turn-a-share-issue-into-a-community-entry)). |
| buddhist-skills | [Volunteer as a language reader](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=reader.yml) | `language-reader` | Match them with data that needs a reader (see [Status](status.md#waiting-on-a-reader)). |
| buddhist-skills | [Report a problem](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=problem.yml) | `bug` | Fix or route. |
| buddhist-benchmarks | [Propose a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=propose-benchmark.yml) | `benchmark` | Discuss, then add the task and data ([how-to](how-to.md#add-a-benchmark)). |
| buddhist-benchmarks | [Review a benchmark as an expert](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=expert-review.yml) | `expert-review` | Agree on the scope, share the items, record the review ([how-to](how-to.md#handle-an-expert-review)). |
| buddhist-benchmarks | [Donate compute or API credits](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=donate-compute.yml) | `compute` | NT replies; set up the key as a secret; credit the donor ([how-to](how-to.md#handle-a-compute-or-api-credit-donation)). |
| knowledge-base | Add to the Directory | `directory` | Verify the link, add a YAML entry (with `access` and `collaborative` for datasets). |
| knowledge-base | Update a language page | (edit link) | Edit `languages/<id>.md`; each fact needs a source. |
| knowledge-base | Share a workflow | `workflow` | Write a workflow page, credit the owner. |
| knowledge-base | Suggest a task | `task` | Write a task page and a `planned` entry in `tasks/index.json`. |
| knowledge-base | Idea (experiment) | `idea` | Discuss; if it goes ahead, write `PLAN.md`. |
| knowledge-base | Re-run, To-do | `re-run`, `todo` | Track work. |
| buddhist-bench | Propose items, Propose a track, Dispute an answer (Markdown templates) | — | Follow buddhist-bench `CONTRIBUTING.md`: real items need human authors and two reviewers. |

Pull request templates: buddhist-skills and knowledge-base. 

## Community: GitHub Discussions

NT chose GitHub Discussions as the community home (2026-11-17): https://github.com/orgs/BuddhistAI/discussions. Start with the [welcome post](https://github.com/orgs/BuddhistAI/discussions/1) (pinned).

Categories: Announcements (maintainers only), Introductions, Find the best AI (Q&A), Requests and ideas, Skills, Models and evaluations, Benchmarks and test data, Tasks and workflows, Languages (put the language in the title), Arena and judging, Website and development, Polls.

- Point people to the matching category when they ask "where do I ask?". Bugs and concrete requests still go to the issue forms above.
- Maintainers post leaderboard news and new leaders in **Announcements**.
- To get notified: watch the BuddhistAI/.github repo, choose Custom, then Discussions.
- A chat channel (Discord or WhatsApp) may come later. Not decided.

## CI workflows

| Repo | Workflow | When | What |
| --- | --- | --- | --- |
| design, knowledge-base, buddhist-benchmarks, buddhist-bench, buddhist-skills | `check` | Push to `main`, pull requests | Runs `check.py`. A failing check means a generated file is stale or a rule is broken. |
| buddhist-benchmarks | `leaderboards` (`pages.yml`) | Push to `main`, daily 03:17 UTC, manual | Rebuilds `LEADERBOARD.md` files, the README table and `STATE.md` and commits them (`[skip ci]`); creates missing data release tags `<task>/<lang>@X.Y.Z`; builds and deploys the site (reads buddhist-bench results and live top rows of `external.json` boards). |
| buddhist-benchmarks | `hf-sync` | After `leaderboards`, on tag push, manual | Publishes each data release to Hugging Face and the results table to `BuddhistAI/buddhist-benchmarks-results`. |
| buddhist-bench | `hf-sync` | `VERSION` changes on `main`, `v*` tag, manual | Checks, tags `vX.Y.Z`, publishes public splits to `BuddhistAI/buddhist-bench`. |
| buddhist-bench | `daily` | Daily 03:00 UTC | Intervention-study runs on OpenRouter. Skips cleanly without keys. |
| buddhist-bench | `import-nak-tham` | Manual | Imports the Thai exam set from Hugging Face (Actions can reach Hugging Face when a container cannot). |
| knowledge-base | `agent-notes` | Mondays 04:23 UTC, manual | Opens a pull request adding the standard `CLAUDE.md` and `AGENTS.md` (from `scripts/agent-notes/CLAUDE.md`) to every org repo that has none. Needs `ORG_REPOS_TOKEN`. |

Tags pushed by `GITHUB_TOKEN` do not start other workflows. That is why `hf-sync` runs on `workflow_run` after `leaderboards`.

## GitHub to Hugging Face

GitHub is the source of truth. Hugging Face holds copies made by CI.

- A data release tag `<task>/<lang>@X.Y.Z` in buddhist-benchmarks becomes the dataset `BuddhistAI/<task>-<language name>` (for example [BuddhistAI/toc-extraction-tibetan](https://huggingface.co/datasets/BuddhistAI/toc-extraction-tibetan)) with Hugging Face tag `vX.Y.Z`. `main` there is the newest release. It ships the data folder, `TASK.md`, the CHANGELOG, the scorer and the license.
- All result files become one table: `BuddhistAI/buddhist-benchmarks-results`.
- buddhist-bench publishes `BuddhistAI/buddhist-bench` (public `dev` and `example` splits only; never `test`, never held-out exam papers).
- Details: buddhist-benchmarks [docs/huggingface.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/docs/huggingface.md) and buddhist-bench [docs/huggingface.md](https://github.com/BuddhistAI/buddhist-bench/blob/main/docs/huggingface.md).
- Live since 2026-11-17. Both workflows do a dry run and skip publishing when `HF_TOKEN` is missing.

## Secrets

Never commit a key. Repo or org secrets are set by NT in GitHub Settings → Secrets and variables → Actions.

| Secret | Used by | Status (2026-11-17) |
| --- | --- | --- |
| `ORG_REPOS_TOKEN` | `agent-notes` in knowledge-base (opens PRs in other org repos); set it as a repo secret of BuddhistAI/knowledge-base | **Not set.** Fine-grained token, resource owner BuddhistAI, all repositories, permissions Contents: read and write, Pull requests: read and write. Without it the workflow only lists the repos that need notes. |
| `HF_TOKEN` | `hf-sync` in buddhist-benchmarks and buddhist-bench | Set. Write token of the BuddhistAI Hugging Face org. |
| `OPENROUTER_API_KEY` | buddhist-bench runner and `daily` workflow | **Not set.** Needed for live model runs. Dave offered sponsor keys. |
| `BRAVE_API_KEY` | buddhist-bench `logged-search` mode | **Not set.** |
| `ANTHROPIC_API_KEY` | Workshop runs on your own machine (toc-extraction-tibetan `bench_skills.py`) | Local only, never in a repo. |

Automatic scoring of submissions (planned) will need an inference key as a secret too. Use a sponsor key, and put a spending limit on it.

## Permissions

- NT has given standing permission to merge PRs, push to `main`, and create repos in the org without asking first.
- CODEOWNERS: NT reviews everything until language and workflow owners exist. A hosted workflow's owner is added on the line for their page.
- **Access model** (written 2026-11-17, see [Governance](../governance.md#adding-people-and-organizations)): anyone contributes by fork and pull request or the forms. A partner organization gets a team `@BuddhistAI/<org>-team` with Write only on its own task repos (optional Triage on buddhist-skills and buddhist-benchmarks, and CODEOWNERS lines for its language). Only a **Maintainers** team has write access to the core repos (buddhist-skills, buddhist-benchmarks, buddhistai.github.io, design, knowledge-base, .github). Releases into buddhist-skills happen only through the leaderboard.
- **Teams (2026-11-17):** `Maintainers` (`@BuddhistAI/maintainers`) and `WeBuddhist` (`@BuddhistAI/webuddhist`) exist; NT is in both; no repo permissions given to either yet.
- **Not set up yet** (NT decided on 2026-11-17 to document now and set up when the first partner team joins): Maintainers access on the core repos, member base permission check (must be Read), and a branch rule on `main` of each core repo requiring a pull request with one code-owner review. Today nobody outside NT and Claude sessions has write access, and they push to `main` directly.
- Creating a new repo needs an org owner (NT) in the GitHub UI. Always start from a template ([how-to](how-to.md#create-a-new-repo)).
