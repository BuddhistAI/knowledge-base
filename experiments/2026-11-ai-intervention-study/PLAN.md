# Plan: AI-intervention study

_Draft, 2026-11-13 · Status: Planned, not frozen · Owner: NT_

> **Preregistration.** This plan becomes binding when it is marked _Frozen_ with a date and commit, before the first intervention is published. After that, changes go in [LOG.md](./LOG.md) as dated deviations with reasons. The point is that nobody can say we chose the metric after seeing the results.

The benchmark format, the OpenRouter runner, the search-call logging and the intervention log are designed in [buddhist-bench](https://github.com/BuddhistAI/buddhist-bench) ([docs/intervention-study.md](https://github.com/BuddhistAI/buddhist-bench/blob/c8fb3d9/docs/intervention-study.md) at `c8fb3d9`). This plan does not repeat that design. It fixes the questions, hypotheses and analysis that the design will be used for.

## Question

When reliable information about a specific Buddhist text, as taught by specific traditions, is newly published on the open web:

1. Do models' answers about that text improve?
2. How long after publication does any change appear, per model?
3. Which models call web search for these questions, and when do they find and cite the new pages?
4. Which kinds of intervention (site, language, format) move answers most?

## Hypotheses

- **H1 (search models move first).** Models that call web search will improve on the target items within days to weeks of an intervention being indexed, and will cite the new pages.
- **H2 (no-search models don't move in the study window).** Models answering without tools will show no change beyond baseline noise, because the new pages can only reach them through retraining.
- **H3 (asking for sources triggers search).** Questions that ask for reliable or sourced answers trigger search more often than plain questions, on the models that support it.
- **H4 (specific beats general).** Target items, whose answers the interventions directly publish, improve more than control items about the same text that no intervention addresses.

## What would count against them

- H1: no improvement on target items for search-enabled models beyond the baseline band after the planned window, or improvement without the new pages ever being retrieved.
- H2: no-search models improving on target items, which would point at something other than retrieval (a model update, or contamination).
- H4: target and control items improving equally, which would mean the change is not caused by our interventions.

## Method (outline; details in the buddhist-bench design)

- **Text and items.** First text: *The Thirty-seven Practices of Bodhisattvas* (Gyalsé Tokmé Zangpo). Questions drawn from its commentaries, each attributed to a tradition and source, split into **target** items (an intervention will publish the answer) and **control** items (no intervention). The split is fixed and recorded before baseline.
- **Models.** A fixed list of models through OpenRouter, recorded with exact model IDs at freeze time. Each in the modes defined by the runner (at least: no tools, and web search available).
- **Baseline.** Daily runs for at least 14 days before the first intervention, to measure day-to-day noise for each model.
- **Interventions.** Each published page is logged with URL, site, language, date, content hash and which items it addresses (intervention log in buddhist-bench). Interventions are staggered, not all on one day, so their effects can be told apart.
- **Follow-up.** The same daily runs after each intervention, for a window fixed at freeze time (proposed: 90 days).
- **Logged per answer.** Score, whether search was called, the queries, the URLs retrieved and cited, and whether any intervention URL appears.

## Metrics (headline fixed at freeze)

- **Headline:** per model and mode, the change in target-item accuracy from baseline to the end of the window, minus the change in control-item accuracy.
- **Time to effect:** days from an intervention's publication to the first day its target items stay above the baseline band for 3 consecutive runs.
- **Search rate:** share of answers with a search call, per model and question type.
- **Retrieval rate:** share of search-enabled answers that retrieve or cite an intervention URL.

## Not in scope

- Whether models answer "through a Buddhist lens"; this is knowledge and attribution only.
- Effects on training data of future models, beyond noting model version changes when they happen.

## Risks and ethics

- **Wikipedia and other sites have their own rules.** Edits must be accurate, sourced, neutral and follow each site's policies on conflicts of interest. Content is published because it is true and useful, not just to move a score.
- **Model updates during the window.** OpenRouter model IDs can change underneath us. Log every change in the model list and flag affected days.
- **Contamination.** Once the target answers are public, the items are public too. Keep a held-back set of control items that is never published.
- **Search non-determinism.** Search results vary by day and region. Run at a fixed time and log the region.

## Open decisions before freezing

- [ ] Final model list and modes
- [ ] Item set, target/control split, and tradition coverage
- [ ] Baseline length and follow-up window
- [ ] First interventions: which sites and languages, in what order
- [ ] Re-pin the buddhist-bench design links to the commit current at freeze time

## Links

- Design: [docs/intervention-study.md](https://github.com/BuddhistAI/buddhist-bench/blob/c8fb3d9/docs/intervention-study.md); results format: [docs/results.md](https://github.com/BuddhistAI/buddhist-bench/blob/c8fb3d9/docs/results.md)
- Intervention log: `studies/<study-id>/interventions.jsonl` ([schema](https://github.com/BuddhistAI/buddhist-bench/blob/c8fb3d9/schema/intervention.schema.json)); study design: [study.schema.json](https://github.com/BuddhistAI/buddhist-bench/blob/c8fb3d9/schema/study.schema.json); example: [studies/example-37-practices/](https://github.com/BuddhistAI/buddhist-bench/tree/c8fb3d9/studies/example-37-practices)
- Scripts: [openrouter_run.py](https://github.com/BuddhistAI/buddhist-bench/blob/c8fb3d9/scripts/openrouter_run.py) (runner), [analyze_study.py](https://github.com/BuddhistAI/buddhist-bench/blob/c8fb3d9/scripts/analyze_study.py) (analysis), [check_interventions.py](https://github.com/BuddhistAI/buddhist-bench/blob/c8fb3d9/scripts/check_interventions.py) (liveness checks)
- Related: [BuddhistBench design](https://github.com/BuddhistAI/buddhist-bench/blob/main/docs/design.md)
