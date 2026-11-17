---
id: text-cleanup
title: Text cleanup
area: Texts
summary: "Fix OCR and input errors and normalize a text without changing its content."
status: planned
related: [ocr, spell-check]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Text cleanup

Fix OCR and input errors and normalize a text without changing its content.

## Definition

Correcting errors introduced by OCR, typing or conversion, and normalizing encoding, punctuation and spacing to an agreed convention. It does not include choosing between readings of different editions (that is edition collation) or modernizing spelling unless the convention says so.

## Input and output

- **Input:** A raw e-text, possibly with OCR noise, mixed encodings or stray markup.
- **Output:** The same text, corrected and normalized, plus (ideally) a list of what was changed.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Errors that are also valid words.
- Archaic or variant spellings that must be kept.
- Non-Unicode legacy fonts and look-alike characters.
- Page headers, footers and folio numbers mixed into the text.

## Languages and traditions

- Tibetan (bo): tsheg and shad spacing, Unicode normalization of stacks, legacy fonts.
- Classical Chinese (lzh): variant characters (异体字) and punctuation added by modern editors.
- Pali and Sanskrit: diacritics and transliteration schemes (IAST, Velthuis, ASCII).

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

Pairs of raw and corrected text from real digitization work, with the normalization convention written down. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [ocr](ocr.md)
- [spell-check](spell-check.md)

<!-- used-in:start -->
## Found in workflows

- [Preparing a digital edition from a template repo](../workflows/digital-edition-pipeline.md) (Sitar)
- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
