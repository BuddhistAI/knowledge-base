# Which skill best finds the outline of a Tibetan commentary?

_2026-11-13 · Benchmark toc-extraction/bo 1.0.0 · Claude Haiku 5.5 and Sonnet 5.5, 3 runs each · Forum post: (add link)_

## Result

We promoted **sabcad-outliner-toc 1.0.0**, a colleague's hand-written sa-bcad outliner packaged as a TOC skill, as `toc-extraction-tibetan` in BuddhistAI's skills. It scored 0.893 on our headline metric against 0.886 for a prompt optimised with GEPA.

That is a near-tie, not a win. The gap is within run-to-run noise, and the GEPA prompt does better on the book no skill was tuned on. That book's answer key is incomplete, so we will fix it and run both again before calling it settled.

## What we measured

Given a passage of Tibetan commentary with all formatting removed, the model must list every sa-bcad (ས་བཅད) heading in order, with its depth and its first 40 characters. We used two public-domain books: 76 passages of Jamyang Loter Wangpo's *A Lamp Illuminating the Intent of Vasubandhu* and all 9 passages of Chenga Chökyi Gyalpo's *The Jewel Garland*. The headline metric, structure_f1, counts a heading as right only if both its position and its depth match.

## Results

| Skill | Haiku 5.5 | Sonnet 5.5 | Mean | Held-out book |
| --- | --- | --- | --- | --- |
| **sabcad-outliner-toc 1.0.0** (promoted) | 0.823 | 0.962 | **0.893** | 83.8 |
| gepa-v1 1.0.0 | 0.824 | 0.949 | 0.886 | **87.8** |
| seed 0.1.0 (one-paragraph prompt) | 0.741 | 0.951 | 0.846 | 79.4 |

Two more rows, the colleague's original .docx skill run through an adapter, scored 0.903 and 0.899 but can't ship as a TOC skill as they are. The full tables are in the [workshop report](https://github.com/BuddhistAI/toc-extraction-tibetan/blob/9576ad2/REPORT.md) and on the [leaderboard](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/tasks/toc-extraction/results/bo/LEADERBOARD.md).

## What the numbers say

1. **Skills matter a lot on the small model and little on the medium one.** On Haiku 5.5 a good skill lifts the score from 0.74 to 0.82. On Sonnet 5.5 the one-paragraph prompt already scores 0.95.
2. **Hand-written expertise held up.** The colleague's skill was never tuned on this data, yet it matches the optimised prompt on the book that prompt was tuned on.
3. **The unseen book separates them.** gepa-v1 does best on *The Jewel Garland*, which no skill saw.
4. **Rankings don't survive model upgrades.** On Haiku 4.5 a week earlier, the GEPA prompt led 89.2 to 55.0. On Haiku 5.5 they are tied. We'll re-rank whenever default models change.

## Known problems

- ***The Jewel Garland*'s answer key misses about 12 real headings.** The source EPUB tagged only some outline levels. Every skill is penalised, possibly unevenly. A Tibetan reader needs to check these 9 passages.
- The held-out set is small: 9 passages, 25 headings.
- Depths are rebuilt from the outline grammar, not checked by hand.

## Next steps

1. Fix *The Jewel Garland* references (benchmark 1.0.1) and re-run sabcad-outliner-toc and gepa-v1. Tracked in issue #1.
2. Add passages from at least two more books (benchmark 1.1.0).
3. Re-run GEPA on Haiku 5.5 seeded with the colleague's rules; combining them is the likeliest way to beat both.

## Links

- Plan: [PLAN.md](./PLAN.md) · Log: [LOG.md](./LOG.md)
- Workshop repo (variants, harness, raw results): [toc-extraction-tibetan@9576ad2](https://github.com/BuddhistAI/toc-extraction-tibetan/tree/9576ad2)
- Benchmark data and scorer: [buddhist-benchmarks toc-extraction](https://github.com/BuddhistAI/buddhist-benchmarks/tree/main/tasks/toc-extraction)
- Promoted skill: [buddhist-skills toc-extraction-tibetan](https://github.com/BuddhistAI/buddhist-skills/tree/main/skills/toc-extraction-tibetan)
