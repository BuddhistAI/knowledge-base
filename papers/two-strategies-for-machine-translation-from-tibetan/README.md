---
title: "Two strategies for improving machine translation from Tibetan"
authors: Drupchen
github: drupchen
license: CC-BY-4.0
date: 2026-11-17
tasks: [translation, translation-review]
language: tibetan
target-language: french
---

# Two strategies for improving machine translation from Tibetan

A method note by Drupchen ([@drupchen](https://github.com/drupchen)), 2026-11-17. 15 pages.

- **Read it:** [full text in Markdown](paper.md) · [the author's PDF](two-strategies-for-improving-machine-translation-from-tibetan.pdf)
- **License:** CC BY 4.0, chosen by the author.

## What it is about, in short

How to get better drafts from an AI when you translate spoken Tibetan teachings into French. There are two strategies:

1. **In context (today):** answer five context questions first (pivot language, reader and register, how the source was delivered, target format, who decides terms). Then draft in four steps, and write the French in a separate turn where the Tibetan is not visible. Tell the AI which Tibetan features *not* to copy. Give it 5 to 10 correction examples (source, AI draft, correction). Give it a fixed list of places to flag.
2. **Training (later):** fine-tune only on correction examples, never on published literal translations, and only after an evaluation harness exists.

The note says the AI can be trusted for countable checks (term consistency, repetition, missing meaning units), but not for judging whether French sounds natural.

## Why it matters for BuddhistAI

- It is the source of two draft skills, `translation-tibetan-to-french` variants `drupchen-method-units-v1` (meaning units first, then French without the Tibetan in view) and `drupchen-method-onepass-v1`, credited to Drupchen as the source of the method. See the [experiment plan](../../experiments/2026-11-tibetan-french-translation/PLAN.md).
- Its §9 describes a way to score translations without BLEU: meaning-unit coverage, countable checks and blind preference. Its §9.3 proposes **colophons** as a first test set. This is the plan for a Tibetan colophon translation benchmark.

## How it was made

The author says Claude wrote this note from a long conversation with him, at his request. It is theory: the author applies it in his own translation system, which uses private data and is not shared.

## Related

- Companion paper by the same author: [Subtracting the Typological Baseline](../subtracting-the-typological-baseline/README.md).
- Tasks: [Translation](../../tasks/translation.md), [Translation review](../../tasks/translation-review.md).

## Source

The PDF is the author's, unchanged. The Markdown was converted from it: page headers and footers were removed, tables were joined across pages, and the Tibetan was checked by script against the PDF text. If anything looks wrong, the PDF is the reference. Shared 2026-11-17 by NT, with the author's agreement.
