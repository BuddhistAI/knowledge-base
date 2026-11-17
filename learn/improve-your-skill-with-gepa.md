---
title: Improve your skill with GEPA
summary: "Tutorial 5: let GEPA rewrite your skill's instructions to raise its score."
---

# Tutorial 5: Improve your skill with GEPA

[← Learn by building](README.md)

**GEPA** is an optimizer in [DSPy](https://dspy.ai/): a strong model reads your skill's mistakes and rewrites its instructions, again and again, keeping what scores best.

**Real example:** Tibetan TOC extraction. On Claude Haiku 5.5, the plain prompt scores 0.741. The GEPA version scores 0.824. It is today's **Best value** on the [leaderboard](https://buddhistai.github.io/buddhist-benchmarks/tasks/toc-extraction/bo/) (0.886 averaged over Haiku and Sonnet).

**You need:** Python 3, an Anthropic API key, and a scorer that gives feedback (Tutorials [1](run-the-scorer.md) and [3](write-your-first-skill.md)).

## Cost warning

GEPA calls models hundreds of times. **Always set a limit** (`--auto light` or `--max-calls`). Use a **small but varied** training set (about 24 + 24 items). **Never** train on the test set.

## Steps

```bash
# 1. Get the code
git clone https://github.com/BuddhistAI/toc-extraction-tibetan.git && cd toc-extraction-tibetan
python -m venv .venv && .venv/bin/pip install -r benchmark/requirements.txt
export ANTHROPIC_API_KEY=...

# 2. Check the metric (free, no model calls)
.venv/bin/python benchmark/gepa_toc.py selftest

# 3. Score the starting prompt
.venv/bin/python benchmark/gepa_toc.py baseline --task-model anthropic/claude-haiku-5-5

# 4. Optimize, with a hard limit
.venv/bin/python benchmark/gepa_toc.py optimize --task-model anthropic/claude-haiku-5-5 \
  --reflection-model anthropic/claude-sonnet-5-5 --max-calls 300 --out out/

# 5. Score the result on the real benchmark (3 runs)
.venv/bin/python benchmark/bench_skills.py --model anthropic/claude-haiku-5-5 --temperature 1.0 \
  --conds skill:out/skills/extract-tibetan-toc --out results/<date>-haiku-5-5-run1.json
```

Step 4 writes `out/program.json` and `out/skills/extract-tibetan-toc/SKILL.md`. Step 5 runs it on the official benchmark. Then share it ([Tutorial 3, step 4](write-your-first-skill.md#4-share-it)).

## For your own task

Copy `benchmark/gepa_toc.py` and change three things: the task (the `Signature`), the data loader, and the metric. The metric must return a score **and a short text saying what went wrong**. GEPA learns from that text.

## Check before you share

Read the new instructions. GEPA can write rules that only fit the training texts (our GEPA skill quotes "the first example"). Test on held-out material, as the leaderboard does.
