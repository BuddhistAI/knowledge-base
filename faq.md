---
title: FAQ
summary: Short answers to common questions about BuddhistAI.
---

# Frequently asked questions

Short answers. Words in **bold** are explained in the [Glossary](glossary.md). Your question is not here? Ask in [Discussions](https://github.com/orgs/BuddhistAI/discussions).

## About the project

**What is BuddhistAI?**
An open project that tests AI models and skills on real Buddhist tasks and shares all results for free. For each task you see the **Top performance** and the **Best value**. People who build AI solutions can send theirs to be tested.

**Who runs it?**
It is a shared project. Many people and organizations contribute; none of them owns the brand. How decisions are made is on the [Governance](governance.md) page. Contributors and supporters are listed on the [homepage](https://buddhistai.github.io/#people).

**Is it only about texts?**
No. Texts are one area. We cover Buddhist tasks in general: translation and study, teaching, art and images, practice support, running centers and projects, and personal AI setups.

**Which traditions and languages?**
All of them. Today most benchmarks are Tibetan and Thai, because that is where people started. See [Languages](languages/README.md) for what exists in each language.

**Is it free?**
Yes. Everything is public and MIT licensed (imported data keeps its own license). Evaluations are paid for by supporters, so testing your solution is free too.

## Using the results

**Which AI should I use for my task?**
Open the [leaderboard](https://buddhistai.github.io/buddhist-benchmarks/), find your task and language, and choose the Top performance (best quality) or the Best value (good quality, much cheaper). For translation into a Buddhist language, see [Languages](languages/README.md).

**How do I install a skill?**
Skills are in [buddhist-skills](https://github.com/BuddhistAI/buddhist-skills). In Claude Code: `claude plugin marketplace add BuddhistAI/buddhist-skills`, then `claude plugin install buddhist-skills-<language>@buddhistai` (for example `buddhist-skills-tibetan`). You can also copy the `SKILL.md` file into any assistant that reads skills, or paste it as instructions.

**Can I trust the scores?**
Each score says which skill version, model and data version it comes from, and has a [provenance record](handbook/provenance.md) with the exact prompt, settings, logs and cost. Anyone can re-score the stored answers ([Tutorial 1](learn/run-the-scorer.md)). Also check the benchmark's maturity level: a Draft benchmark is less certain than a Reviewed one.

**Why is there no benchmark for my task?**
Nobody has built one yet. You can [propose one](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=propose-benchmark.yml), or [request an AI solution](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=request.yml) for your task.

**Why do costs say "estimated"?**
Some early runs did not log token counts, so they were estimated from the text length. New runs use the real counts from the API.

## Contributing

**I am not a programmer. Can I help?**
Yes. You can share how your project works (a workflow), check answers in your language, review a benchmark as an expert, suggest a task, add a project to the [Directory](directory/README.md), or fix a page. Most of this is a form or the "Edit this page" link. See [Contribute](CONTRIBUTING.md).

**How do I submit my model or skill?**
Paste a link on the [homepage](https://buddhistai.github.io/#submit). For a skill or any file you give to AI, you can also use the [Share your files](https://github.com/BuddhistAI/buddhist-prompt-library/issues/new?template=share.yml) form. A maintainer runs it on the benchmark. To learn the steps yourself, follow the [tutorials](learn/README.md).

**Can my organization donate API credits or compute?**
Yes, please. Use the [Donate compute or API credits form](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=donate-compute.yml). Donations pay for evaluations of everyone's submissions. They never change a score or a ranking.

**Our team wants to contribute regularly. Do we get access?**
Yes. Your organization can get its own GitHub team with write access to your own task repos. The steps are in [Governance](governance.md#adding-people-and-organizations).

**Can I submit a closed or commercial tool?**
Yes. Include its outputs on the benchmark and say in your submission how others can get the tool. It appears on the leaderboard like any other entry.

**Who owns what I contribute?**
You keep your copyright. Contributions to our repos are published under the MIT license (data under the license you choose and state). You are credited by name.

**My skill won. What happens?**
It becomes the best skill for its task and language in buddhist-skills, we congratulate you, and we announce it in [News](news/README.md), crediting you and your organization.
