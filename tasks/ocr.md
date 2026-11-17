---
id: ocr
title: OCR
area: Texts
summary: "Turn an image of a page (print, woodblock or manuscript) into Unicode text."
status: measured
related: [text-cleanup, spell-check]
benchmarks: [bdrc-tibetan-ocr (external, BDRC)]
leaderboard: https://huggingface.co/spaces/BDRC/tibetan-ocr-leaderboard
skills: []
contributors: []
---

# OCR

Turn an image of a page (print, woodblock or manuscript) into Unicode text.

## Definition

Reading the text on a page image and writing it out as Unicode, line by line, without correcting the author. Layout (which block is main text, which is a note or page number) is part of the task when the output keeps it.

## Input and output

- **Input:** One page image (scan or photo).
- **Output:** The text of the page in Unicode, in reading order, with line breaks.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Woodblock prints with worn or broken letters.
- Cursive (dbu med) manuscripts and abbreviations (bskungs yig).
- Interlinear notes in smaller script, marginalia, page numbers in the margin.
- Pages that mix scripts, such as Tibetan with Sanskrit in Lantsa.

## Languages and traditions

- Tibetan (bo): measured on the BDRC Tibetan OCR benchmark.
- Other languages: no benchmark listed yet.

## How it is measured

Tibetan OCR is ranked by BDRC on its own open leaderboard, which BuddhistAI lists but does not score: [Tibetan OCR leaderboard](https://huggingface.co/spaces/BDRC/tibetan-ocr-leaderboard), metric mean character error rate.

## Help wanted

Benchmarks for other scripts and languages (Pali in Burmese, Sinhala or Thai script; Classical Chinese; Sanskrit manuscripts), each with page images and checked transcriptions. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [text-cleanup](text-cleanup.md)
- [spell-check](spell-check.md)

<!-- used-in:start -->
## Found in workflows

- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
