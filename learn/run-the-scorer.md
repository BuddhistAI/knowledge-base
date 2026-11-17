---
title: Run the scorer on your computer
summary: "Tutorial 1: download a Buddhist benchmark, score stored results with the official scorer, and read the numbers."
---

# Tutorial 1: Run the scorer on your computer

[← Learn by building](README.md)

**You will:** download the Tibetan table-of-contents benchmark, score answers that a model already gave, and understand what the numbers mean.
**You need:** Python 3.9 or newer and git. No API key, no cost. About 15 minutes.

## 1. Get the benchmark

```bash
git clone https://github.com/BuddhistAI/buddhist-benchmarks.git
cd buddhist-benchmarks
```

Look at one item of the data set:

```bash
head -c 600 tasks/toc-extraction/data/bo/v2/test.jsonl
```

Each line is one **item**: an `id`, the `input` (a passage of a Tibetan commentary), the `target` (the correct outline headings: title, level and position) and `metadata` (which book it comes from). There are 85 items. The task is explained in [TASK.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/tasks/toc-extraction/TASK.md).

## 2. Score perfect answers

First, check that the scorer works. Make a file of "predictions" that are simply the correct answers:

```bash
python3 -c "
import json
with open('perfect.jsonl', 'w', encoding='utf-8') as out:
    for line in open('tasks/toc-extraction/data/bo/v2/test.jsonl', encoding='utf-8'):
        item = json.loads(line)
        out.write(json.dumps({'id': item['id'], 'output': item['target']}, ensure_ascii=False) + '\n')
"
python3 tasks/toc-extraction/scorer/score.py --language bo \
  --data tasks/toc-extraction/data/bo/v2/test.jsonl --predictions perfect.jsonl
```

You should see `"structure_f1": 1.0`. A perfect answer scores 1.0, an empty answer scores 0.0.

## 3. Score a real model's answers

The leaderboard keeps the answers of every run. Score the answers that Claude Haiku 5.5 gave with the GEPA skill:

```bash
RUN=tasks/toc-extraction/results/bo/runs/2026-11-13-toc-extraction-tibetan-gepa-v1-1.0.0-3253458-haiku-5-5
python3 tasks/toc-extraction/scorer/score.py --language bo \
  --data tasks/toc-extraction/data/bo/v2/test.jsonl --predictions $RUN/outputs > my-scores.json
head -8 my-scores.json
```

You should see `"structure_f1": 0.8386`. Compare it with `$RUN/scores.json`: the numbers are the same. This is how anyone can check a score on the leaderboard.

## 4. Read the numbers

- **`structure_f1`** is the **headline score**. A heading counts as found only if it is in the right place and at the right level. 1.0 is perfect.
- **`title_f1`** counts headings in the right place, at any level.
- **`level_accuracy`** is the share of found headings that also have the right level.
- **`by_subset`** splits the score by book. `held-out-book` is a book that no skill was trained on, so it shows how well a skill works on new material.

Why is the leaderboard number (0.824) different from 0.8386? The leaderboard shows the **mean of three runs**, because a model gives slightly different answers each time. The stored outputs are from run 2. The full record of each run (model, settings, prompt, files, cost) is in the skill's [provenance records](https://github.com/BuddhistAI/toc-extraction-tibetan/tree/main/provenance).

## Next

[Tutorial 2: Evaluate your first model on a Buddhist task](evaluate-your-first-model.md).
