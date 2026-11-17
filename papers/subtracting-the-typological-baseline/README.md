---
title: "Subtracting the Typological Baseline"
authors: Drupchen
github: drupchen
license: CC-BY-4.0
date: 2026-11-17
tasks: [translation-review, translation]
language: tibetan
target-language: french
---

# Subtracting the Typological Baseline

*Discourse Organisation and the Assessment of Fidelity in a Tibetan–French Translation*, by Drupchen ([@drupchen](https://github.com/drupchen)), 2026-11-17. 44 pages.

- **Read it:** [full text in Markdown](paper.md) · [the author's PDF](subtracting-the-typological-baseline.pdf)
- **License:** CC BY 4.0, chosen by the author.

## What it is about, in short

When people (or an AI) check a translation from Tibetan into French, they often count something as "lost" when the French simply says it in the normal French way. Tibetan puts the verb at the end, chains clauses, and uses repetition for "more and more". French does these things with other tools. If you compare the two texts word by word, a good translation looks worse than a literal one.

The paper shows this on one short oral meditation instruction and its French translation:

1. Each text is first described alone, without looking at the other.
2. A normal comparison, against the Tibetan form, finds the translation a failure.
3. The Tibetan features are then sorted: features of the language, features of the genre, and real choices by the speaker. Only real choices count.
4. A second comparison, by function, withdraws almost all the "losses". An audit of 26 meaning units finds one real loss.

A second study on about 20 minutes of teaching confirms the main findings. The paper proposes a four-step procedure: a source choice counts as lost only if it was a real choice and French had a way to say it.

## Why it matters for BuddhistAI

- **Translation review:** an AI reviewer that compares word by word will flag good translations. The paper says what an AI can check reliably (countable things) and what it cannot (whether French sounds natural).
- **Benchmarks:** scores like BLEU or chrF reward literal translations. The paper and its companion guide suggest another way to score: meaning-unit coverage, with a field that says whether a unit is in the text, moved to the layout, or correctly left out. Colophons are proposed as a first test set.
- **Corpora:** a training set made mostly of literal published translations teaches the same bias.

## How it was made

The author says the analysis and the text were produced with Claude in a long dialogue. The author made the key corrections and is the only author. Details are in the "Contributions" section at the end of the paper.

## Related

- Practical guide by the same author: [Two strategies for improving machine translation from Tibetan](../two-strategies-for-machine-translation-from-tibetan/README.md) (in Papers).
- Tasks: [Translation review](../../tasks/translation-review.md), [Translation](../../tasks/translation.md).

## Source

The PDF is the author's, unchanged. The Markdown was converted from it: page headers and footers were removed, and the Tibetan was checked by script against the PDF text. If anything looks wrong, the PDF is the reference. Shared 2026-11-17 by NT, with the author's agreement, including the quoted Tibetan teaching and French draft.
