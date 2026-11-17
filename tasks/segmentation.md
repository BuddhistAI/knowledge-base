---
id: segmentation
title: Segmentation
area: Texts
summary: "Split a text into sentences or translation units."
status: planned
related: [block-id-assignment, text-translation-alignment]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Segmentation

Split a text into sentences or translation units.

## Definition

Dividing a text into units small enough to translate, align or cite, at boundaries a careful reader would accept. The unit (sentence, verse line, couplet, paragraph) is set by the project and should be stated.

## Input and output

- **Input:** A text.
- **Output:** The same text split into units, each unit a span of the original with nothing added or removed.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Verse, where a sentence runs across lines or stanzas.
- Long Tibetan sentences joined by connective particles.
- Quotations embedded mid-sentence.
- Unpunctuated Classical Chinese.

## Languages and traditions

- Tibetan (bo): shad is not a reliable sentence boundary.
- Classical Chinese (lzh): sentence breaking (句读) is itself an interpretive task.

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

Texts segmented by translators in real projects, with the unit stated. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [block-id-assignment](block-id-assignment.md)
- [text-translation-alignment](text-translation-alignment.md)

<!-- used-in:start -->
## Found in workflows

- [Preparing a digital edition from a template repo](../workflows/digital-edition-pipeline.md) (Sitar)
- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
