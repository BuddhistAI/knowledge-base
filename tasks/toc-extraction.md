---
id: toc-extraction
title: Table-of-contents extraction
area: Texts
summary: "List the titles, levels and locations of a text's sections."
status: measured
related: [segmentation, text-commentary-alignment]
benchmarks: [toc-extraction/bo@2.0.0]
leaderboard: https://buddhistai.github.io/buddhist-benchmarks/
skills: [toc-extraction-tibetan]
contributors: []
---

# Table-of-contents extraction

List the titles, levels and locations of a text's sections.

## Definition

Recovering the outline of a work: every section heading, how deeply it is nested, and where it starts. In Tibetan commentaries the outline (sa bcad) is usually embedded in the running text rather than set as headings, so the task includes recognizing it.

## Input and output

- **Input:** The full text of a work.
- **Output:** A list of entries in reading order, each with its title as written, its level, and its start position or page.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Outlines announced in the text ("this has two parts") whose parts appear pages later.
- Headings that look like ordinary sentences.
- Texts with both chapter titles and a sa bcad outline.

## Languages and traditions

- Tibetan (bo): measured; see the benchmark below.

## How it is measured

Benchmark: [toc-extraction, Tibetan, version 2.0.0](https://github.com/BuddhistAI/buddhist-benchmarks/tree/main/tasks/toc-extraction), scored by structure F1. [Leaderboard](https://buddhistai.github.io/buddhist-benchmarks/). Best skill: [toc-extraction-tibetan](https://github.com/BuddhistAI/buddhist-skills/tree/main/skills/toc-extraction-tibetan).

## Help wanted

Benchmarks in other languages, and more Tibetan genres (sutras, collected works, histories). A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [segmentation](segmentation.md)
- [text-commentary-alignment](text-commentary-alignment.md)

<!-- used-in:start -->
## Found in workflows

- [Preparing a digital edition from a template repo](../workflows/digital-edition-pipeline.md) (Sitar)
- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
