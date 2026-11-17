---
id: translation
title: Translation
area: Translation
summary: "Produce a draft translation."
status: planned
related: [translation-review, term-extraction, segmentation]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Translation

Produce a draft translation.

## Definition

Rendering a source text into a target language, following a stated approach (literal or meaning-led), audience and glossary. A draft for a human translator to revise is the realistic goal today.

## Input and output

- **Input:** A source text segment, plus optional glossary, style guide and context (surrounding text, commentary).
- **Output:** A translation of the segment.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Verse.
- Technical terms that the glossary fixes.
- Passages whose meaning depends on the commentary.
- Mantras and names, which are usually transliterated.

## Languages and traditions

- Each source and target pair is its own task variant, e.g. Tibetan to English, Pali to Thai.

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

Source passages with reference translations by experienced translators, and a way to score them that translators trust. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Further reading

- [Subtracting the Typological Baseline](../papers/subtracting-the-typological-baseline/README.md) (Drupchen, 2026, Tibetan → French): how to prompt an AI for better drafts: a context checklist, a drafting pipeline where the French is written without the Tibetan in view, and correction examples.
- [Two strategies for improving machine translation from Tibetan](../papers/two-strategies-for-machine-translation-from-tibetan/README.md) (Drupchen, 2026): the practical guide.

## Related tasks

- [translation-review](translation-review.md)
- [term-extraction](term-extraction.md)
- [segmentation](segmentation.md)

<!-- used-in:start -->
## Found in workflows

- [Preparing a digital edition from a template repo](../workflows/digital-edition-pipeline.md) (Sitar)
- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
