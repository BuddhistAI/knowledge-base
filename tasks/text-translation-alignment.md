---
id: text-translation-alignment
title: Text-translation alignment
area: Translation
summary: "Align a source text with its translation, segment by segment."
status: planned
related: [segmentation, translation-review, edition-collation]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Text-translation alignment

Align a source text with its translation, segment by segment.

## Definition

Pairing each segment of a source text with the segment of a translation that renders it. The source and translation can be in different languages, or be two translations of one original (for example a Sanskrit text and its Tibetan and Chinese translations).

## Input and output

- **Input:** A source text and a translation.
- **Output:** Pairs of aligned segments, including one-to-many and unaligned segments.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Free translations that merge or reorder sentences.
- Translator additions in brackets.
- Verse rendered as prose.

## Languages and traditions

- Any source and target pair; note the pair on each item.

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

Published translations aligned sentence by sentence by a translator. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [segmentation](segmentation.md)
- [translation-review](translation-review.md)
- [edition-collation](edition-collation.md)

<!-- used-in:start -->
## Found in workflows

- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
