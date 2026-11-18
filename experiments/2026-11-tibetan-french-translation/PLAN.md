# Plan: does Drupchen's method improve Tibetan → French translation?

_Written 2026-11-18, before any run. Status: Planned. Do not edit after the first run; record changes in [LOG.md](LOG.md)._

## Question

Do skills built from Drupchen's method ([Two strategies](../../papers/two-strategies-for-machine-translation-from-tibetan/README.md) and [Subtracting the Typological Baseline](../../papers/subtracting-the-typological-baseline/README.md), CC BY 4.0) give better French from Tibetan than plain Claude? And how much of the gain comes from writing the French from a list of meaning units, with the Tibetan not in view?

## Hypothesis

1. Both skill variants beat plain Claude on `unit_coverage` and on the colophon measures.
2. The two-stage variant (`units`) beats the one-pass variant (`onepass`). The papers say the sealed composition step carries most of the gain.

## What would count against it

- A skill variant that does not beat plain Claude by more than the run-to-run spread (± one standard deviation over 3 repeats) on `unit_coverage`.
- `units` not beating `onepass` by more than that spread. Then the extra calls are not worth their cost.

## Method

- **Data:** buddhist-benchmarks `translation/bo-fr` v1: 30 real Tibetan colophons, meaning units written by a reader of Tibetan and checked by a human ([authoring rules](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/tasks/translation/data/bo-fr/AUTHORING.md)). **The data set does not exist yet; this plan waits for it.** The exact data version and commit go in LOG.md at the start.
- **Systems** (buddhist-skills `drafts/translation-tibetan-to-french/`):
  - `no-skill`: the model alone, with the item's context sheet ("Translate this Tibetan text into French").
  - `onepass`: `drupchen-method-onepass-v1` 0.1.0, one call.
  - `units`: `drupchen-method-units-v1` 0.1.0, three calls: meaning units and flags from the Tibetan; French from the units in a new conversation, with all Tibetan text removed; audit.
- **Models:** Claude Sonnet 5.5 and Claude Opus 5.5, default settings (no temperature setting; these models do not accept one).
- **Procedure:** buddhist-benchmarks `tasks/translation/harness/run.py`, 3 repeats per system and model, real token counts logged per call.
- **Scoring:** `tasks/translation/scorer/judge.py` (judge `claude-opus-5-5`, effort medium, judge 0.1.0) then `scorer/score.py` (0.1.0). The judge sees the source, the meaning units and one translation, never a reference translation, and never which system produced it.
- **Metric:** headline `unit_coverage`, mean over the two models. Secondary: `matrix_verb_early`, `epithet_as_slot`, `target_order`, `unlicensed_connectives`. Cost in dollars per 100 pages from logged tokens.
- **Human check:** Drupchen (or another reader of Tibetan and French) checks the judge's labels on a sample of 20 translations, without knowing which system made them. If the judge disagrees with the human on more than 1 in 5 labels, the scores are reported as unreliable and the judge prompt is revised in a new version.

## Cost estimate (list prices, 2026-11)

Per item: plain about $0.03 (Opus) and $0.015 (Sonnet); one pass about $0.09 and $0.05; three-stage about $0.16 and $0.08; judging about $0.03 per translation.

For 30 items × 3 repeats × 3 systems × 2 models: about **$38 for the runs ($25 Opus, $13 Sonnet) and $16 for judging 540 translations, so about $55 in total**. Opus only: about $33. Sonnet only: about $21. A first check on 5 items with one repeat costs about $2. A maintainer runs it only after NT approves the spend.

## Not in scope

Correction examples (source, AI draft, correction): the papers' highest-leverage item. They must come from real corrections, so they are a later variant. Other target languages. Spoken teaching transcripts (a later data set).
