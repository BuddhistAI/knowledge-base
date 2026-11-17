---
id: term-extraction
title: Term extraction
area: Translation
summary: "Propose glossary terms and their renderings from a source text and translation."
status: planned
related: [entity-extraction, translation-review]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Term extraction

Propose glossary terms and their renderings from a source text and translation.

## Definition

Picking out the technical terms of a text that need a consistent rendering, and, given a translation, how each was rendered. Building or checking against a project glossary is the main use.

## Input and output

- **Input:** A source text, and optionally its translation and an existing glossary.
- **Output:** A list of terms with their renderings and where they occur.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Terms with different meanings in different schools.
- Multi-word terms and abbreviations.
- Terms rendered inconsistently on purpose.

## Languages and traditions

- Any language pair; glossaries live in buddhist-skills shared/.

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

A translated text with its glossary, checked by the translator. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [entity-extraction](entity-extraction.md)
- [translation-review](translation-review.md)

<!-- used-in:start -->
## Found in workflows

- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
