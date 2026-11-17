---
title: Add a benchmark
summary: "Tutorial 4: turn material your team already checks by hand into an open benchmark for a Buddhist task."
---

# Tutorial 4: Add a benchmark

[← Learn by building](README.md)

**You will:** turn real material your team already uses (exam papers, corrected OCR, a reviewed translation) into a small benchmark, so that AI models and skills can be measured on it.
**You need:** some real examples with correct answers, and the right to share them. No code is needed for the first step. About one hour for a first draft.

## What makes a good benchmark

- **Real work.** Material from real projects is better than invented examples.
- **Small but varied.** 30 to 100 items is a good start, if they cover the hard cases.
- **Checked answers.** Every correct answer is checked by someone who knows the material. A second reader from the tradition makes it more trusted.
- **Open.** Anyone can download it and check a score. If you cannot share the material openly, say so: some sets can stay private and be used only for scoring.

Benchmarks move up four **maturity levels**: 1 Example (format check only), 2 Draft (real items, one author), 3 Reviewed (checked by a second reader), 4 Stable (held-out set, used in practice).

## 1. Propose it (no code)

Open a [Propose a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=propose-benchmark.yml) issue. Say which task, which language, what material, who owns it, who can check the answers, and how results should be scored. It goes on the [Benchmarks board](https://github.com/orgs/BuddhistAI/projects/2), and a maintainer replies.

Not sure which task it fits? Read the [task pages](../README.md#tasks), or describe it in your own words.

## 2. Make 5 items by hand

Write 5 items in the standard format, one per line in a file `test.jsonl`:

```json
{"id": "my-set-001", "input": "the text or question", "target": "the correct answer", "metadata": {"source": "where it comes from"}}
```

- `id` never changes once published.
- `input` is exactly what the model sees.
- `target` is the correct answer, in the format the task's scorer reads (see the task's `TASK.md`).
- `metadata` holds facts for breaking down scores (book, level, year). The model never sees it.

Attach the file to your issue. A maintainer checks it with the scorer (as in [Tutorial 1](run-the-scorer.md)) and tells you if anything is missing.

## 3. Grow it and write the card

Add the rest of the items. Then write a short `README.md` (the dataset card): what the set is for, how many items, where the material comes from and its license, who wrote and who checked the answers, and one worked example. The template is [toc-extraction/bo/v2](https://github.com/BuddhistAI/buddhist-benchmarks/tree/main/tasks/toc-extraction/data/bo/v2).

## 4. Publish

A maintainer (or you, with a pull request) adds it to buddhist-benchmarks following its [CONTRIBUTING.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/CONTRIBUTING.md). It gets a version (`1.0.0`), a git tag and a copy on Hugging Face. Every skill for the task is then scored on it, and we announce the new benchmark, crediting you and your team.

## 5. Keep it alive

- Found a wrong answer? Fix it and the version goes up (1.0.1). Scores are only compared within one version.
- Found a new hard case? Add it (1.1.0).
- Ask an expert to [review the benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=expert-review.yml). Their review moves it up a maturity level.

Groups may publish competing benchmarks for the same task. We keep both, and new skills are scored on all of them.
