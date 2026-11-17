---
title: Project handbook
permalink: /handbook/
summary: Everything a maintainer or developer needs to keep building BuddhistAI.
---

# Project handbook

This handbook is for the people who maintain and build BuddhistAI. Read it and you should be able to keep the project going without asking anyone. If something here is wrong or missing, fix it in the same pull request as the change that made it wrong.

Last full review: 2026-11-17.

## Read in this order

1. **This page**: mission, audiences, and the rules we never break.
2. **[Architecture](architecture.md)**: every repo, site, board, form, CI workflow and secret, and how data flows between them.
3. **[Conventions](conventions.md)**: names, data format, versions, licenses, design system, writing style.
4. **[How-to guides](how-to.md)**: run an evaluation, update the leaderboard, promote a winner, add a benchmark, handle a submission, announce a new leader.
5. **[Building the leaderboard app and arena](leaderboard-app.md)**: notes for the FastAPI + React site: which files to read, which design files to use, what the homepage already promises.
6. **[Provenance records](provenance.md)**: the standard record of what made each score (skill files, model, prompt, data, code, logs, cost), kept in the skill's own repo.
7. **[Status, decisions and roadmap](status.md)**: what is real today, what is still a mock or a plan, decisions and open questions from the team call of 2026-11-17, and the next steps.

## Mission

BuddhistAI helps **anyone who works on a Buddhist project** find the best AI solution for each task: the one with the best results (**Top performance**) and the one with the best results for its cost (**Best value**). It also helps **anyone who builds AI solutions** share them and take part in the evaluations.

It is a community hub, not one organization's set of tools. Everything is open source and built together.

## Audiences

The homepage and the org profile give each audience its own door near the top.

| Audience | What they want | Where they go |
| --- | --- | --- |
| Buddhist project teams: translators, teachers, editors, centers | The best tool for their task and language, and a way to ask for one when nothing exists | [Leaderboard](https://buddhistai.github.io/buddhist-benchmarks/), [buddhist-skills](https://github.com/BuddhistAI/buddhist-skills) (install), [Request an AI solution](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=request.yml) |
| People and organizations who build AI solutions | Have their model, skill, prompt or workflow measured and ranked | [SUBMIT.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md), [Share form](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=share.yml), [Propose a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=propose-benchmark.yml) |
| Funders and coordinators (for example Khyentse Foundation, the Italian Buddhist Union) | The state of AI for Buddhist tasks, and the gaps | [STATE.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/STATE.md) |

## Rules we never break

These come from NT, the project lead. Every page, site, commit message and social post follows them.

1. **Buddhist tasks, not Buddhist texts.** Texts are one area. The project also covers translation, teaching, study, art and visual work, practice support, the running of centers, and personal AI setups (for example someone's Claude files). Tagline: "Open Buddhist AI benchmarks and skills".
2. **Plain English.** Many readers are not native English speakers. Write short, literal sentences. No idioms ("in the open", "ship it", "side by side", "lab notebook"). See [VOICE.md](https://github.com/BuddhistAI/design/blob/main/VOICE.md).
3. **Our words.** "Top performance" and "Best value" (never "best overall" or Michelin-style names). The contributor path is **Share → Measure → Release**. Say "best skill", not "promoted", to users.
4. **Neutral branding.** BuddhistAI belongs to everyone who takes part. WeBuddhist is credited as one contributor among others, never as the lead or the brand. No "Maintained by WeBuddhist" or "founded by" lines.
5. **We rank models as well as skills.** Every task leaderboard has a "No skill (plain prompt)" row per model, and models are compared directly.
6. **BuddhistBench is one Q&A benchmark among others.** It is not a special pillar and is never featured above the other benchmarks.
7. **Never invent data.** No made-up benchmark items, scores, votes, users or links. Example items are marked as examples. A mock feature on a site says that it is planned.
8. **Never edit generated files by hand.** Leaderboards, `STATE.md`, `SKILLS.md`, the plugin marketplace, index tables and design CSS are all built by scripts. Each repo's `CLAUDE.md` (also `AGENTS.md`) says which.
9. **Version everything that is scored.** Skills, data sets, scorers and workflow pages use semver ([Conventions](conventions.md#versions)).

## People

| Who | Role |
| --- | --- |
| NT ([@ngawangtrinley](https://github.com/ngawangtrinley)) | Project lead. Default reviewer in every repo (CODEOWNERS). Owns the org, the domain and the secrets. |
| Kalden | Developer. Builds the leaderboard web app (FastAPI + React), then the arena. |
| Sitar | Builds skills (segmentation, annotation detection, Tibetan spell check) and gathers benchmark data. Owner of the [digital edition workflow](../workflows/digital-edition-pipeline.md). |
| Evan | Helps document Buddhist data workflows (structure not decided). |
| Dave | Offered inference keys for evaluation runs. |
| Kurt Keutzer | Owner of the [translation workflow](../workflows/translation.md) (his own document; we only link to it). |

Who decides what, and how people and partner organizations get access, is on the public [Governance](../governance.md) page. Newcomers learn the basics in [Learn by building](../learn/README.md), the [Glossary](../glossary.md) and the [FAQ](../faq.md).

Team work is tracked on the [Development board](https://github.com/orgs/BuddhistAI/projects/3), for team members (private for now).

Ask NT for: membership or owner role in the [BuddhistAI GitHub org](https://github.com/BuddhistAI), the [Hugging Face org](https://huggingface.co/BuddhistAI), repo secrets, and the `buddhistai.org` domain on Cloudflare.

## Working with Claude

Much of this project was built with Claude (Claude Code). Every repo has a `CLAUDE.md` and an `AGENTS.md` with the rules an agent must follow in that repo. Keep them short and current; an agent reads them before it changes anything. When you add a rule a person would need to know, put it in this handbook too.
