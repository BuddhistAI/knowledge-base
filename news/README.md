---
title: News
summary: Announcements from BuddhistAI. New best skills, new benchmarks, releases and new contributors.
permalink: /news/
---

# News

Announcements from BuddhistAI: new best skills and leaders, new benchmarks, releases, and new contributors and supporters. Newest first.

Follow updates on X: [@buddhist_ai](https://x.com/buddhist_ai). You can also watch the [BuddhistAI repos on GitHub](https://github.com/BuddhistAI) or the [Discussions](https://github.com/orgs/BuddhistAI/discussions). Maintainers: how to post is in the [handbook](../handbook/how-to.md#post-news).

<!-- Add new posts at the top. Format: ## <date> · <title>, then 2 to 5 plain sentences with links. -->

## 17 November 2026 · Provenance for every score, tutorials and a governance page

Every score of the Tibetan table-of-contents skill now has a [provenance record](https://github.com/BuddhistAI/toc-extraction-tibetan/tree/main/provenance): the exact skill files, model, settings, prompt, data version, code, logs, tokens and cost. The [standard](../handbook/provenance.md) applies to all new results. New in this knowledge base: four [hands-on tutorials](../learn/README.md), a [Governance](../governance.md) page, a [FAQ](../faq.md) and a [Glossary](../glossary.md). The [Directory](../directory/README.md) now marks which datasets are open and which accept contributions. Organizations can now offer [API credits or compute](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=donate-compute.yml), and experts can [review a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=expert-review.yml).

## 17 November 2026 · Languages pages

The knowledge base now has a page for each of 21 Buddhist languages: the data that exists, who builds AI for it, and how well AI translates into it, with an overview of Buddhist countries. See [Languages](../languages/README.md).

## 17 November 2026 · Directory of Buddhist AI projects and datasets

A [Directory](../directory/README.md) of Buddhist AI projects and datasets from all traditions and languages. [Add yours](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml) by pasting a link.

## 13 November 2026 · First best skill: Tibetan table-of-contents extraction

The first task leaderboard went live: [Tibetan table-of-contents extraction](https://buddhistai.github.io/buddhist-benchmarks/tasks/toc-extraction/bo/), on an 85-item benchmark from two Tibetan commentaries. Five skill variants were measured on Claude Haiku 5.5 and Claude Sonnet 5.5. The sa-bcad method skill, adapted from a colleague's outliner skill, was released as [`toc-extraction-tibetan`](https://github.com/BuddhistAI/buddhist-skills/tree/main/skills/toc-extraction-tibetan). It is close to the GEPA-optimized variant, which is the Best value on Haiku.
