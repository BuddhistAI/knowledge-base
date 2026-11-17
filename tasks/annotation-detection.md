---
id: annotation-detection
title: Annotation detection
area: Texts
summary: "Find interlinear notes, glosses and other annotations and separate them from the main text."
status: planned
related: [ocr, text-cleanup, text-commentary-alignment]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Annotation detection

Find interlinear notes, glosses and other annotations and separate them from the main text.

## Definition

Marking which parts of a text are annotations (interlinear notes, glosses, marginal remarks, editorial notes) rather than the main text, and where each attaches.

## Input and output

- **Input:** A text, or a page image.
- **Output:** The main text and the annotations, each annotation with its position.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Annotations written in the same size and script as the main text.
- Notes by later hands.
- Annotation commentaries (mchan ’grel) where notes are woven into the root text.

## Languages and traditions

- Tibetan (bo): benchmark sets exist in one team and could seed a public benchmark (team call, 2026-11-17).

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

Texts with annotations marked by a human reader. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [ocr](ocr.md)
- [text-cleanup](text-cleanup.md)
- [text-commentary-alignment](text-commentary-alignment.md)

<!-- used-in:start -->
## Found in workflows

- [Preparing a digital edition from a template repo](../workflows/digital-edition-pipeline.md) (Sitar)
<!-- used-in:end -->
