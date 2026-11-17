---
id: digital-edition-pipeline
title: Preparing a digital edition from a template repo
area: Texts
owner: Sitar
contributors: []
mode: hosted
source:
source_version:
languages: [bo]
tasks: [text-cleanup, block-id-assignment, segmentation, annotation-detection, toc-extraction, text-commentary-alignment, entity-extraction, spell-check, translation]
status: draft
version: 0.1.0
updated: 2026-11-17
---

# Preparing a digital edition from a template repo

**Owner:** Sitar. Written from Sitar's description in the BuddhistAI team call of 2026-11-17; Sitar has not yet reviewed this page.

## Who it is for

Teams that turn many Tibetan texts into structured digital editions and want every new text project to start with the same skills, scripts, formats and rules.

## How the project is set up

Each text gets its own git repo made from a shared template with a standard layout:

- `inbox/`: raw material as it arrives (scans, e-texts, exports);
- `source/`: the cleaned source text;
- `transformation/`: structured outputs built from the source;
- `skills/` and `scripts/`: the AI skills plus linters and parsers that check each output.

Skills are made generic before they go into the template, so every new repo inherits them. Fixes for one text's edge cases (for example, block IDs that follow an Abhidharma text's own numbering) stay in that text's repo.

## Steps

| # | Step | What happens | Task | AI today |
| --- | --- | --- | --- | --- |
| 1 | Bring in the text | Put the raw e-text in `inbox/`, clean it into `source/`. | [text-cleanup](../tasks/text-cleanup.md), [spell-check](../tasks/spell-check.md) | skills, unmeasured |
| 2 | Give blocks IDs | Assign stable IDs to each block, following the source's numbering when it has one. | [block-id-assignment](../tasks/block-id-assignment.md) | skills, unmeasured |
| 3 | Segment | Split blocks into sentences or translation units. | [segmentation](../tasks/segmentation.md) | skills, unmeasured |
| 4 | Find annotations | Detect interlinear notes and annotations and separate them from the main text. | [annotation-detection](../tasks/annotation-detection.md) | skills, unmeasured |
| 5 | Outline | Extract the table of contents (sa bcad). | [toc-extraction](../tasks/toc-extraction.md) | measured |
| 6 | Root text and commentary | Separate root text from commentary and link each passage to its explanation. | [text-commentary-alignment](../tasks/text-commentary-alignment.md) | skills, unmeasured |
| 7 | Names | Detect author names and other entities. | [entity-extraction](../tasks/entity-extraction.md) | skills, unmeasured |
| 8 | Translate | Draft a translation of each unit. | [translation](../tasks/translation.md) | skills, unmeasured |
| 9 | Check | Run linters and parsers over every output. | — | scripts |

## Notes

- Open question from the call: how should an edge-case fix made in one text's repo flow back to the template without breaking the generic skill? One idea is a skill that scans repos built from the template and proposes template improvements.
- Sitar's team has benchmark sets for Tibetan annotation detection and author-name detection that could seed those tasks' benchmarks.
