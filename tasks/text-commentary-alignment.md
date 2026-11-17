---
id: text-commentary-alignment
title: Text-commentary alignment
area: Texts
summary: "Link each root text passage to the commentary passages that explain it."
status: planned
related: [toc-extraction, citation-mapping, annotation-detection]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Text-commentary alignment

Link each root text passage to the commentary passages that explain it.

## Definition

Separating root text from commentary and pairing each root passage with the commentary that explains it. Works whether the commentary quotes the root text in full, quotes only its first words, or does not quote it.

## Input and output

- **Input:** A root text and a commentary, or a commentary with the root text embedded.
- **Output:** Pairs of root passage and commentary span.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Commentaries that quote only a few syllables of each verse.
- Several commentaries on one root text.
- Commentaries that skip or reorder passages.

## Languages and traditions

- Tibetan (bo): a root text and commentary pipeline is in use in one team.

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

A root text with one commentary aligned by hand. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [toc-extraction](toc-extraction.md)
- [citation-mapping](citation-mapping.md)
- [annotation-detection](annotation-detection.md)

<!-- used-in:start -->
## Found in workflows

- [Preparing a digital edition from a template repo](../workflows/digital-edition-pipeline.md) (Sitar)
- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
