---
id: entity-extraction
title: Entity extraction
area: Texts
summary: "Find people, places, texts, deities, dates and other named entities."
status: planned
related: [citation-mapping, term-extraction]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Entity extraction

Find people, places, texts, deities, dates and other named entities.

## Definition

Finding named entities in a text and classifying them (person, place, text, deity, monastery, date), ideally linking each to an authority record such as a BDRC or other database ID.

## Input and output

- **Input:** A text.
- **Output:** A list of entity mentions with type, position and, where possible, an authority ID.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- The same person under many names and titles.
- Dates in the Tibetan calendar or coded as words.
- Deity names that are also ordinary words.
- Author names in colophons.

## Languages and traditions

- Tibetan (bo): one team has an author-name detection skill and benchmark set (team call, 2026-11-17).

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

Texts with entities marked and linked by a human reader. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [citation-mapping](citation-mapping.md)
- [term-extraction](term-extraction.md)

<!-- used-in:start -->
## Found in workflows

- [Preparing a digital edition from a template repo](../workflows/digital-edition-pipeline.md) (Sitar)
- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
