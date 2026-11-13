# BuddhistAI research

The lab notebook of [BuddhistAI](https://github.com/BuddhistAI): what we tried, why, and what we found. Each experiment has its own folder with a plan written before it ran, a dated log, and a report ready to post on the WeBuddhist forum.

Code, data and scores live in the other repos. This repo holds the reasoning and links to them.

| Repo | Holds |
| --- | --- |
| [buddhist-skills](https://github.com/BuddhistAI/buddhist-skills) | The promoted skills users install |
| [buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks) | Test sets, scorers and leaderboards for skills |
| [buddhist-bench](https://github.com/BuddhistAI/buddhist-bench) | BuddhistBench: Q&A benchmark ranking models on Buddhist knowledge |
| Workshop repos, e.g. [toc-extraction-tibetan](https://github.com/BuddhistAI/toc-extraction-tibetan) | Skill variants, runs and ranking reports for one skill |

## Experiments

| Experiment | Status | Question |
| --- | --- | --- |
| [2026-11-toc-tibetan-skills](experiments/2026-11-toc-tibetan-skills/) | Concluded, re-run pending | Which skill finds the sa-bcad outline of a Tibetan commentary best? |
| [2026-11-ai-intervention-study](experiments/2026-11-ai-intervention-study/) | Planned | Does publishing reliable information about a text change what AI models answer about it, and how fast? |

Status is one of: **Planned** (plan written, not started), **Running**, **Concluded**, **Abandoned** (with a note on why). Keep this table current when an experiment changes status.

## How an experiment works

1. **Open an issue** with the "Idea" template. Discuss there until it is worth running.
2. **Make the folder** `experiments/<yyyy-mm>-<slug>/`, named by the month it starts. Copy the three files from [templates/](templates/).
3. **Write `PLAN.md` before running anything.** State the question, the hypothesis, the method, the metric and what result would count against the hypothesis. Commit it. Once the experiment starts, don't edit the plan: record changes in `LOG.md` as deviations, with the reason. Git history is the proof that the goalposts didn't move. This matters most for experiments that try to change the world and then measure it, like the intervention study.
4. **Optionally post the plan on the forum** to invite feedback before starting.
5. **Keep `LOG.md` as you go:** dated entries, newest last. Note runs, interventions, surprises, and anything you changed.
6. **Write `REPORT.md` when it concludes.** It should stand alone so it can be pasted into the forum: result first, then what was measured, the numbers, the known problems and next steps. Link to data and results in the other repos at exact commits or versions.
7. **Post the report on the forum** and add its link to the report's header.
8. **Open issues for follow-ups** ("To-do" or "Re-run" templates), each linking back to the folder.

## Issues and the board

Issues track work; folders hold knowledge. Every issue names its experiment folder, so the reasoning is always one click away. Labels: `idea`, `todo`, `re-run`, plus one `exp:<slug>` label per experiment.

The [BuddhistAI research board](https://github.com/orgs/BuddhistAI/projects) shows the pipeline: Ideas, Planned, Running, Writing up, Done.

## Rules

- Link, don't copy. Data, code and long designs stay in their own repos; refer to them by commit or version so a link still shows what we used.
- Numbers in a report come from a results file you can link to.
- A re-run after a benchmark version change is a new LOG entry and, if it changes the conclusion, a new report section. Don't overwrite old numbers.
- Write for the forum: plain language, result first, short sentences.

## License

MIT. BuddhistAI was founded and is maintained by [WeBuddhist](https://webuddhist.com).
