---
title: "Journey: Get a skill or model measured"
id: get-measured
personas: [skill-builder]
version: 0.1.0
updated: 2026-11-18
---

# Journey: Get a skill or model measured

[← UX reviews](../README.md) · Persona: [Skill builder](../personas/skill-builder.md)

**Goal:** a builder gets their skill, prompt, model or tool scored on an open benchmark and listed on the leaderboard. This is the **Measure** step, and it can lead to **Release**.

**Done when:** a leaderboard row with the builder's solution is live, with its score, cost and credit.

## Steps today (2026-11-18)

| # | Where | What the person does |
| --- | --- | --- |
| 1 | [Homepage](https://buddhistai.github.io/) or [SUBMIT.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md) | Reads how to submit. Picks a task and its benchmark. |
| 2 | Their own machine | Runs the solution on the test data and scores it with the task's scorer, at least 3 times if it is not deterministic. |
| 3 | buddhist-benchmarks | Opens a pull request with `result.json`, outputs, `scores.json` and a `skills.json` line. Keeps a [provenance record](../../handbook/provenance.md) in their own repo. |
| 4 | Maintainer | Checks and merges. CI rebuilds the [leaderboard](https://buddhistai.github.io/buddhist-benchmarks/). |
| 5 | Release (if it leads) | The skill is promoted to buddhist-skills, and the new leader is announced. |

Planned: submit by pasting a repo link, scoring by a GitHub Action, and maintainer approval (team call 2026-11-17). Kalden's leaderboard app will change steps 1 to 4.

## Pages this journey touches

Homepage submit box, SUBMIT.md, `docs/results.md`, task `TASK.md` pages, the leaderboard site and app, the provenance handbook page, the workshop template repo.
