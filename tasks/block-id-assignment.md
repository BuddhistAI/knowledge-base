---
id: block-id-assignment
title: Block ID assignment
area: Texts
summary: "Give every block of a text (paragraph, verse, section) a stable ID."
status: planned
related: [segmentation, toc-extraction]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Block ID assignment

Give every block of a text (paragraph, verse, section) a stable ID.

## Definition

Assigning each block of a text an identifier that stays the same across versions, so translations, notes and alignments can point at it. When the source has its own numbering (verse numbers, Abhidharma paragraph numbers) the IDs follow it.

## Input and output

- **Input:** A text, possibly already segmented.
- **Output:** The text with an ID on each block, in a stated scheme.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Sources with their own numbering, including gaps and sub-numbers.
- Blocks split or merged in a later edition.
- Commentaries that quote the root text block by block.

## Languages and traditions

- Tibetan (bo): used in template-based digital edition projects (see the workflow below).

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

A written ID convention and a few texts with IDs assigned by hand. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [segmentation](segmentation.md)
- [toc-extraction](toc-extraction.md)

<!-- used-in:start -->
## Found in workflows

- [Preparing a digital edition from a template repo](../workflows/digital-edition-pipeline.md) (Sitar)
<!-- used-in:end -->
