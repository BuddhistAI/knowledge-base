---
title: "Journey: Find and use a skill"
id: find-and-use-a-skill
personas: [translator, project-lead]
version: 0.1.0
updated: 2026-11-18
---

# Journey: Find and use a skill

[← UX reviews](../README.md) · Personas: [Translator](../personas/translator.md), [Project lead](../personas/project-lead.md)

**Goal:** a person finds the best AI solution for their task and language, and uses it on their own work.

**Done when:** the person has used a skill or a model on their own text, or knows that none exists yet and has asked for one.

## Steps today (2026-11-18)

| # | Where | What the person does |
| --- | --- | --- |
| 1 | [Homepage](https://buddhistai.github.io/) | Reads what BuddhistAI is and picks their task in the task list. |
| 2 | [Leaderboard](https://buddhistai.github.io/buddhist-benchmarks/) | Opens the task and language. Compares the **Top performance** and **Best value** rows, the "No skill" baseline and the cost per 100 pages. |
| 3 | [buddhist-skills](https://github.com/BuddhistAI/buddhist-skills) | Installs the best skills as a Claude plugin, or copies one skill's `SKILL.md`. |
| 4 | Their own AI tool | Uses the skill on their own text. |
| 5 (no tool yet) | [Request form](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=request.yml) | Asks for a solution for a task that is not covered. |

## Pages this journey touches

Homepage (task list, "Install the best skills"), leaderboard site, buddhist-skills README and install steps, the request form, the [Languages](../../languages/README.md) pages.

## Known problems

- Install needs Claude Code or a GitHub account for some steps (to be checked in a walkthrough).
