---
id: edition-collation
title: Edition collation
area: Texts
summary: "Compare editions of a text and record where and how they differ."
status: planned
related: [text-cleanup, text-translation-alignment]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Edition collation

Compare editions of a text and record where and how they differ.

## Definition

Aligning two or more editions of the same text and listing each variant: its location, the reading in each edition, and the kind of difference. Choosing the best reading (making a critical edition) is a separate, later judgement.

## Input and output

- **Input:** Two or more e-texts of the same work.
- **Output:** A list of variants, or a variorum edition with the variants marked.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Large omissions or additions, and passages in a different order.
- Differences in spelling or punctuation only, which some projects ignore.
- Editions that silently correct each other.

## Languages and traditions

- Tibetan (bo): Kangyur and Tengyur editions (Derge, Peking, Narthang and others).
- Classical Chinese (lzh): Taishō apparatus and other canons.
- Pali (pi): Burmese, Sinhalese and Thai editions.

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

A short text with several editions and a human-made list of variants. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [text-cleanup](text-cleanup.md)
- [text-translation-alignment](text-translation-alignment.md)

<!-- used-in:start -->
## Found in workflows

- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
