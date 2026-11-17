---
id: citation-mapping
title: Citation mapping
area: Texts
summary: "Find quotations and references and link them to their source texts."
status: planned
related: [entity-extraction, text-commentary-alignment]
benchmarks: []
leaderboard: 
skills: []
contributors: []
---

# Citation mapping

Find quotations and references and link them to their source texts.

## Definition

Detecting where a text quotes or refers to another work, identifying the source work, and locating the quoted passage in it. Checking whether the quote is accurate is part of the task.

## Input and output

- **Input:** A text.
- **Output:** A list of quotations or references, each with its span, the source work and the location in the source.

## Examples

None yet. Add a short real example with its correct answer, and say where it comes from.

## Edge cases

- Quotes introduced only by "a sutra says".
- Paraphrases and partial quotes.
- Quotes of a Sanskrit work through its Tibetan or Chinese translation.

## Languages and traditions

- All languages; cross-language search tools such as Dharmamitra help.

## How it is measured

**No benchmark yet: help build one.** See below.

## Help wanted

Passages with quotations identified and located by a scholar. A first benchmark can be small: twenty to fifty items. See [how to submit a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md).

## Related tasks

- [entity-extraction](entity-extraction.md)
- [text-commentary-alignment](text-commentary-alignment.md)

<!-- used-in:start -->
## Found in workflows

- [Translating a Buddhist text](../workflows/translation.md) (Kurt Keutzer)
<!-- used-in:end -->
