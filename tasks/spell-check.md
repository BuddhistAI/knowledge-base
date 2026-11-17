---
id: spell-check
title: Spell check
area: Texts
summary: "Flag and correct misspelled words in a source text or a translation."
status: planned
related: [text-cleanup, ocr]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Spell check

Flag and correct misspelled words in a source text or a translation.

## Definition

Finding words that are misspelled for the language and period of the text, and proposing the correct form. Unlike text cleanup, the input is assumed to be already readable; unlike edition collation, a variant reading attested in an edition is not a spelling error.

## Input and output

- **Input:** A text.
- **Output:** The positions of misspelled words and a suggested correction for each.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Archaic spellings and attested variants that are correct for the period.
- Names and Sanskrit loan words transcribed in Tibetan or Chinese.
- Mantras, which follow their own conventions.

## Languages and traditions

- Tibetan (bo): a Tibetan spell-check skill is in progress (team call, 2026-11-17).

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

Tibetan texts with marked spelling errors and their corrections, checked by a second reader. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [text-cleanup](text-cleanup.md)
- [ocr](ocr.md)

<!-- used-in:start -->
## Found in workflows

- [Preparing a digital edition from a template repo](../workflows/digital-edition-pipeline.md) (Sitar)
- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
