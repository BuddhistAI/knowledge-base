---
id: translation-review
title: Translation review
area: Translation
summary: "Check a translation against its source, the glossary and the style guide."
status: planned
related: [translation, text-translation-alignment, term-extraction]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Translation review

Check a translation against its source, the glossary and the style guide.

## Definition

Finding errors in a translation: mistranslations, omissions, additions, glossary violations and style problems, with the location and a suggested fix for each. It is the editor's and reviewer's step, not a new translation.

## Input and output

- **Input:** A source text, its translation, and optionally a glossary and style guide.
- **Output:** A list of issues, each with location, type, explanation and suggested fix.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Deliberate interpretive choices that are not errors.
- Omissions of a single particle that change the meaning.
- Style issues that depend on the audience.

## Languages and traditions

- Each source and target pair is its own task variant.

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

Translations with reviewers' real comments, so a benchmark can test whether a model finds the same issues. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Further reading

- [Subtracting the Typological Baseline](../papers/subtracting-the-typological-baseline/README.md) (Drupchen, 2026, Tibetan → French): why word-by-word comparison flags good translations, and a four-step review procedure that counts a loss only when the source made a real choice and the target language had a way to say it.
- [Two strategies for improving machine translation from Tibetan](../papers/two-strategies-for-machine-translation-from-tibetan/README.md) (Drupchen, 2026): the practical guide.

## Related tasks

- [translation](translation.md)
- [text-translation-alignment](text-translation-alignment.md)
- [term-extraction](term-extraction.md)

<!-- used-in:start -->
## Found in workflows

- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
