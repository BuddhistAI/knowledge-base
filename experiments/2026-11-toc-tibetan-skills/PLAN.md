# Plan: Tibetan TOC skill ranking

_Written retrospectively on 2026-11-13, after the runs, from the workshop repo at [`9576ad2`](https://github.com/BuddhistAI/toc-extraction-tibetan/tree/9576ad2). It records the plan the runs followed; it is not a preregistration. Status: Concluded._

## Question

Which skill variant gives the best sa-bcad outline (headings, depth, position) of a Tibetan commentary, on current Claude models, and which one should ship as `toc-extraction-tibetan` in buddhist-skills?

## Hypothesis

The GEPA-optimised prompt (gepa-v1) beats a colleague's hand-written outliner skill (sabcad-outliner), because on 2026-11-05 with Haiku 4.5 it scored 89.2 against 55.0 on the same-book set.

## What would count against it

sabcad-outliner, or its shippable form sabcad-outliner-toc, matching or beating gepa-v1 on the headline metric averaged over both models.

## Method

- **Data:** toc-extraction-tibetan benchmark 1.0.0, also exported as buddhist-benchmarks `toc-extraction/bo` 1.0.0. Two public-domain books cut into ~6,000-character passages at heading boundaries:
  - same book: 76 passages of Jamyang Loter Wangpo's *A Lamp Illuminating the Intent of Vasubandhu* that GEPA never saw (it was tuned on 48 other passages of this book);
  - held-out book: all 9 passages of Chenga Chökyi Gyalpo's *The Jewel Garland*, which no variant was tuned on.
- **Systems:** seed 0.1.0, gepa-v1 1.0.0, sabcad-outliner 1.0.0 (through a benchmark adapter, with and without its `extract_sabcad.py` script) and sabcad-outliner-toc 1.0.0. All at workshop commit `3253458`.
- **Models:** Claude Haiku 5.5 and Claude Sonnet 5.5.
- **Procedure:** DSPy 3.5.0 `ChainOfThought` with typed output (`benchmark/bench_skills.py`), temperature 1.0, 3 runs per variant and model.
- **Metric:** headline `structure_f1` (micro F1 over all 394 headings, matching position within 3 characters and depth), averaged over the two models. Secondary: the per-passage lab score (0.3 × position F1 + 0.7 × position-and-depth F1) and the held-out book score.
- **Promotion rule:** the best headline score among variants that can ship as a TOC skill.

## Not in scope

Other languages, other outline formats (.docx output), and non-Claude models.

## Links

- Harness and variants: [toc-extraction-tibetan](https://github.com/BuddhistAI/toc-extraction-tibetan)
- Scorer and data: [buddhist-benchmarks toc-extraction](https://github.com/BuddhistAI/buddhist-benchmarks/tree/main/tasks/toc-extraction)
