---
id: translation
title: Translating a Buddhist text
area: Translation
owner: Kurt Keutzer
contributors: []
mode: linked
source: https://docs.google.com/document/d/1r_ICSUPoyTY6DwR1cafCKVFkZvWzYDk_mQ3Bb4SjqOk/edit
source_version: "2.2 (minor revision 2026-06-01)"
languages: [any]
tasks: [ocr, text-cleanup, spell-check, edition-collation, toc-extraction, segmentation, citation-mapping, term-extraction, entity-extraction, text-commentary-alignment, text-translation-alignment, translation, translation-review]
status: draft
version: 0.1.0
updated: 2026-11-17
---

# Translating a Buddhist text

**Owner:** Kurt Keutzer. **Read the full workflow:** [A Model of the Human Translation Workflow, v2.2](https://docs.google.com/document/d/1r_ICSUPoyTY6DwR1cafCKVFkZvWzYDk_mQ3Bb4SjqOk/edit) (Google Doc). That document is Kurt's and stays the reference; it credits the translators and editors who shaped it. This page only summarizes it in our own words and maps its steps to tasks. Kurt has not yet reviewed this page.

## Who it is for

Translators of classical Buddhist texts (Tibetan, Sanskrit and others) and their editors. The model is deliberately inclusive, so any one project will use a subset of it.

## Steps

Numbers follow the source document.

| # | Step | What happens | Task | AI today |
| --- | --- | --- | --- | --- |
| 1a–1b | Gather the texts | Find the editions of the root text and its main commentaries in every source language. | new task? (finding editions) | none yet |
| 1c1 | Make e-texts | Turn each edition into clean Unicode text: OCR a scan, or transcribe. | [ocr](../tasks/ocr.md), [text-cleanup](../tasks/text-cleanup.md), [spell-check](../tasks/spell-check.md) | measured (OCR, Tibetan) |
| 1c2 | Compare editions | Build a variorum edition that records where editions differ; most variants are settled later. | [edition-collation](../tasks/edition-collation.md) | none yet |
| 1d, 2c | Outline the text | Divide the text into chapters, sections and down to the basic unit of translation, so editions and commentaries can be lined up. | [toc-extraction](../tasks/toc-extraction.md), [segmentation](../tasks/segmentation.md) | measured (TOC, Tibetan) |
| 1e | Gather secondary literature | Collect earlier translations and scholarly studies. | new task? (literature search) | none yet |
| 2a–2b | Decide the approach | Genre, voice and audience of the original; target audience; literal or meaning-led; how many notes; whether to show source terms. | — | human only |
| 3a | Chunk the text | Break the text into translation units. | [segmentation](../tasks/segmentation.md) | none yet |
| 3b1 | Identify each unit | Is it a scriptural quote (find it, check it), an objection in a debate, an instruction, verse or prose? | [citation-mapping](../tasks/citation-mapping.md) | none yet |
| 3b2 | Work through each sentence | Parse grammar and implied subjects; check key terms against the glossary; spot mantras, names, places, texts and dates; flag hard words and look them up. | [term-extraction](../tasks/term-extraction.md), [entity-extraction](../tasks/entity-extraction.md), new task? (dictionary lookup) | none yet |
| 3b2b–3b2d | Use parallels and commentaries | Check the original if the text is itself a translation, compare parallel versions, read commentaries, resolve variants. | [text-translation-alignment](../tasks/text-translation-alignment.md), [text-commentary-alignment](../tasks/text-commentary-alignment.md), [edition-collation](../tasks/edition-collation.md) | none yet |
| 3b2e, 3a3 | Render and reread | Write the sentence, then reread the whole unit for flow. | [translation](../tasks/translation.md) | none yet |
| 4 | Build the apparatus | Notes on quote sources, people, places, texts, term choices and parallel passages. | [citation-mapping](../tasks/citation-mapping.md), [entity-extraction](../tasks/entity-extraction.md) | none yet |
| 5 | Refine | Revisit the approach with editors, revise each unit, simplify, polish wording, check notes and references. | [translation-review](../tasks/translation-review.md) | none yet |
| 6 | Independent editing | Copy editing, clarity, house style, and alternative renderings from an editor. | [translation-review](../tasks/translation-review.md), [spell-check](../tasks/spell-check.md) | none yet |
| 7–9 | Publish | Choose print or electronic, mono- or bilingual, then typeset and proofread. | new task? (typesetting, proofing) | none yet |

## Notes

- The source document cites Gregory Forgues' terminology for the steps of translation and Douglas Robinson's *Becoming a Translator*.
- Steps 2a–2b and the editor's judgement in 5–6 are where the translator's choices live. AI can support them (by surfacing how a term was rendered before, for example) but they are listed as human only.
