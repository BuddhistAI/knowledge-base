---
title: Evaluate your first model on a Buddhist task
summary: "Tutorial 2: run an AI model on a real Buddhist benchmark, score it, and compare it with the leaderboard."
---

# Tutorial 2: Evaluate your first model on a Buddhist task

[← Learn by building](README.md)

**You will:** run an AI model of your choice on the Tibetan table-of-contents benchmark, score its answers, and compare the result with the leaderboard.
**You need:** [Tutorial 1](run-the-scorer.md) done, and an [OpenRouter](https://openrouter.ai/) API key with a little credit. OpenRouter gives one key for many models (Claude, GPT, Gemini, Llama, Qwen and others). About 30 minutes.
**Cost:** 5 items cost about one cent on a small model. All 85 items cost from a few cents (small models) to a few dollars (large models).

Never put your API key in a file that you commit, and never paste it into an issue or a chat.

## 1. Get the example script

From the `buddhist-benchmarks` folder of Tutorial 1:

```bash
curl -O https://raw.githubusercontent.com/BuddhistAI/knowledge-base/main/learn/examples/run_model.py
```

[`run_model.py`](examples/run_model.py) is short and uses only the Python standard library. Read it before you run it. For each item, it sends one prompt with the passage to the model, reads the JSON answer, and writes one line to `predictions.jsonl`.

## 2. Start small

Make a small test file with the first 5 items, and check that everything works without calling the API:

```bash
head -5 tasks/toc-extraction/data/bo/v2/test.jsonl > small.jsonl
python3 run_model.py --data small.jsonl --dry-run --out predictions.jsonl
```

Now run a real model. Copy a model id from [openrouter.ai/models](https://openrouter.ai/models) (a cheap one first):

```bash
export OPENROUTER_API_KEY=...            # your key, only in this terminal
python3 run_model.py --data small.jsonl --model <model-id> --out predictions.jsonl
python3 tasks/toc-extraction/scorer/score.py --language bo --data small.jsonl --predictions predictions.jsonl
```

Score against `small.jsonl`, not the full file: items without an answer count as wrong.

## 3. Run the full benchmark

```bash
python3 run_model.py --data tasks/toc-extraction/data/bo/v2/test.jsonl --model <model-id> --out predictions.jsonl
python3 tasks/toc-extraction/scorer/score.py --language bo \
  --data tasks/toc-extraction/data/bo/v2/test.jsonl --predictions predictions.jsonl > scores.json
```

The script prints the tokens it used. Write them down: the leaderboard needs them to compute cost.

## 4. Compare with the leaderboard

Open the [Tibetan TOC leaderboard](https://buddhistai.github.io/buddhist-benchmarks/tasks/toc-extraction/bo/). The "No skill" rows use a plain prompt, like this script. Is your model better or worse? Is it cheaper?

Run it **3 times** before you trust the number. Most models give slightly different answers each time.

## 5. Make it count

Two ways to put your model on the leaderboard:

- **Easy:** paste your model's link on the [homepage](https://buddhistai.github.io/#submit) (choose "Model"), and add the model id, your `scores.json` and the token counts. A maintainer re-runs it and adds it.
- **Full:** follow [SUBMIT.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md): a pull request with `result.json`, your outputs and `scores.json`, and a [provenance record](../handbook/provenance.md) in your own repo that says exactly how you ran it.

## Try next

- Change `PROMPT` in the script and see if the score goes up. When it does, you have the start of a skill: [Tutorial 3](write-your-first-skill.md).
- Try other models. Which one gives the **Best value** (a high score for much less money)?
