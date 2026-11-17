---
title: Provenance records
summary: The standard provenance record ("bill of materials") for every score, kept in the skill's own repo.
---

# Provenance records

[← Handbook](README.md)

Every score on a BuddhistAI leaderboard must be easy to check and to repeat. For each leaderboard row, the repo where the skill is built keeps a **provenance record**: a short JSON file that says exactly what made the score. Some projects call this a "bill of materials".

## Where it lives

- **In the skill's own repo** (the workshop repo, for example [toc-extraction-tibetan](https://github.com/BuddhistAI/toc-extraction-tibetan/tree/main/provenance)), in a folder `provenance/`, one file per leaderboard row: `provenance/<run-id>.json`. The `<run-id>` is the same as the run folder name in buddhist-benchmarks.
- **Not in buddhist-benchmarks.** buddhist-benchmarks stays clean: it keeps only the short `result.json` of each row, its outputs and `scores.json`. The `skill_ref` in `result.json` (`owner/repo@commit:path`) leads to the skill repo, where the full record is.
- Run files and logs stay in the skill repo too (for example `results/`). The record points at them and stores their hashes.

## Format: `buddhistai/provenance@1`

One JSON object. Required keys are in **bold**.

| Key | What it holds |
| --- | --- |
| **`schema`** | Always `"buddhistai/provenance@1"`. |
| **`run_id`** | Same as the run folder in buddhist-benchmarks and the file name. |
| **`date`**, **`by`** | Date of the run (YYYY-MM-DD) and who ran it (person or organization). |
| **`task`**, **`language`** | Task ID from `tasks/index.json` and language code from `languages.json`. |
| **`skill`** | `name`, `variant`, `version` (semver), `ref` (`owner/repo@commit:path`), and `files`: every file of the skill folder with its git blob hash at that commit. |
| **`model`** | `id` (as in buddhist-benchmarks `models.json`), `provider`, `api` (how it was called, for example "Anthropic API through LiteLLM" or "OpenRouter"), and `settings` (temperature, max tokens, any other option). |
| **`prompt`** | `how` the prompt is built (one or two sentences) and `files`: the files whose text is sent to the model. If a system prompt or template is not in a file, put its full text in `text`. |
| **`benchmark`** | `repo`, `tag` (for example `toc-extraction/bo@2.0.0`), `path` of the data file, `data_version`, `scorer_version`, `data_sha256` (SHA-256 of the data file at that tag) and `items`. |
| **`harness`** | The code that ran the skill: `repo`, `commit`, `script`, `libraries` (with versions), `python`, and the exact `command`. If the command was not saved at run time, set `command_recorded: false` and say how it was rebuilt in `command_note`. |
| **`runs`** | One entry per repeat: `output` and `log` paths in the skill repo, each with its `sha256`. |
| `repeats` | Number of runs averaged. |
| **`usage`** | Input and output tokens per pass over the test set. `estimated: true` and a `method` if they are not from the API. |
| **`cost`** | `usd_per_pass`, `estimated`, and the `price` used (per million tokens, with date and source). |
| **`scores`** | The `headline` metric, the mean of each metric per split, and the standard deviation (`std`) of the headline. |
| **`links`** | The `result.json` in buddhist-benchmarks, the stored outputs, the report and the leaderboard page. |
| `notes` | Anything a reader should know (for example "measured on 1.0.0, same items as 2.0.0"). |

Never put an API key, a private path or personal data in a record.

## Example

[2026-11-13 gepa-v1 on Claude Haiku 5.5](https://github.com/BuddhistAI/toc-extraction-tibetan/blob/main/provenance/2026-11-13-toc-extraction-tibetan-gepa-v1-1.0.0-3253458-haiku-5-5.json) in toc-extraction-tibetan. The table of all records is in its [provenance/README.md](https://github.com/BuddhistAI/toc-extraction-tibetan/blob/main/provenance/README.md).

## How to make the records

In toc-extraction-tibetan (copy this pattern for a new skill repo):

```bash
python benchmark/bench_skills.py ... --out results/<date>-<model>-run1.json   # also saves results/...-run1.meta.json
python scripts/to_result_json.py --date <date> --commit <short-commit> --benchmarks ../buddhist-benchmarks
python scripts/provenance.py --benchmarks ../buddhist-benchmarks               # writes provenance/*.json + README.md
python scripts/provenance.py --check                                           # hashes still match
```

The run script saves the exact command, the Python and library versions and the repo commit at run time (`<out>.meta.json`), so new records have `command_recorded: true`.

For a new skill repo, start from the [workshop repo template](https://github.com/BuddhistAI/buddhist-skills/tree/main/templates/workshop) in buddhist-skills. Any script may write the records, as long as the keys above are there.

## Rules

1. A leaderboard row is only accepted when its skill repo has a provenance record (from 2026-11-17 on). For an external submission, the author adds the record to their own repo, or, for a closed tool, puts it in the pull request description.
2. Never edit a record by hand after a run. If something was wrong, re-run, or add a line in `notes` and say what changed in the commit message.
3. Never change a run file or log after its record was made. `provenance.py --check` fails if a hash differs.
4. Costs in a record are a snapshot. The leaderboard recomputes cost from `models.json` prices, so the two can differ after a price change.
