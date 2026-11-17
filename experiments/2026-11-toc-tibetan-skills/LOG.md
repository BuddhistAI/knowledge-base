# Log: Tibetan TOC skill ranking

Reconstructed on 2026-11-13 from the workshop repo and its history. Newest last.

## 2026-11-02

- GEPA run produces gepa-v1 from the seed prompt (task model Haiku 4.5, reflection Sonnet 4.5), tuned on 48 passages of *A Lamp Illuminating the Intent of Vasubandhu*.

## 2026-11-05

- First comparison on Haiku 4.5, same-book set: gepa-v1 89.2, the colleague's sabcad-outliner 55.0 ([`results/history/`](https://github.com/BuddhistAI/toc-extraction-tibetan/tree/9576ad2/results/history)).

## 2026-11-13

- Benchmark 1.0.0 built: two books, 138 passages, evaluation sets of 76 (same book) and 9 (held-out book).
- Wrote sabcad-outliner-toc 1.0.0: sabcad-outliner plus a TOC task section and gepa-v1's rendering section, scripts and .docx spec removed, so it can ship as a TOC skill.
- Ran all five conditions, 3 runs each, on Haiku 5.5 and Sonnet 5.5 (commit [`3253458`](https://github.com/BuddhistAI/toc-extraction-tibetan/commit/3253458)).
- **Surprise:** on Haiku 5.5 the colleague's skill ties gepa-v1; the 2026-11-05 gap is gone. Model changes can reverse rankings.
- **Surprise:** every variant predicts ~1.5× the reference headings on *The Jewel Garland*, with recall near 1.0. Spot checks show ~12 missed positions are real sa-bcad headings (the EPUB tagged only some levels as `Tibetan-Sabche`). The held-out references are incomplete.
- Exported to buddhist-benchmarks `toc-extraction/bo` 1.0.0; scorer reproduces the lab numbers. Leaderboard created.
- Promoted sabcad-outliner-toc 1.0.0 to buddhist-skills on the headline metric (0.893 vs gepa-v1 0.886), noted as a near-tie (commit [`9576ad2`](https://github.com/BuddhistAI/toc-extraction-tibetan/commit/9576ad2)).
- Open: fix *Jewel Garland* references (benchmark 1.0.1) and re-run the top two.
