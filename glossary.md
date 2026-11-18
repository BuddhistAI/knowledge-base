---
title: Glossary
summary: The words we use in BuddhistAI, in plain English.
---

# Glossary

The words we use on our sites and in our repos, in plain English. Missing a word? Click "Edit this page" and add it, or ask in [Discussions](https://github.com/orgs/BuddhistAI/discussions).

## The basics

**Buddhist task**
: One job that people in Buddhist projects do and that AI can help with: OCR, translation, translation review, finding the outline of a text, answering questions on the teachings, describing an image, preparing a course. Each task has a page in this knowledge base. We speak of Buddhist *tasks*, not only Buddhist *texts*.

**Task ID**
: The short name of a task, such as `toc-extraction` or `translation-review`. It is the same in every repo.

**Workflow**
: How a real project does its work from start to finish, step by step (for example translating a text). Each step maps to a task. Workflows show which tasks matter. See [Workflows](README.md#workflows).

**AI model**
: The AI system itself, such as Claude, GPT, Gemini, Llama or Qwen. We rank models as well as skills.

**Skill**
: A folder with a `SKILL.md` file: written instructions (and sometimes scripts or glossaries) that help a model do one task in one language. Its name is `<task>-<language>`, for example `toc-extraction-tibetan`.

**Prompt**
: The text sent to a model. A skill is a carefully written, tested and versioned prompt, with its extras.

**Prompt library**
: The repo [buddhist-prompt-library](https://github.com/BuddhistAI/buddhist-prompt-library), where people share files they give to AI for Buddhist work (Claude files, project instructions, style guides, glossaries, prompts) and skills that have no score yet. Nothing in it is measured.

**Community entry**
: An entry in the prompt library. Until 2026-11-18 these were in the `community/` folder of buddhist-skills.

**Personal AI setup**
: The files, projects and instructions one person uses with an AI assistant day to day (for example their Claude files). Can be shared in the prompt library.

## Measuring

**Benchmark**
: Test material with correct answers for one task and one language, and a way to score results. Also called a test set or data set.

**Item**
: One question or example in a benchmark: an `input`, the correct `target`, and `metadata`.

**Reference** (or **target**, or **answer key**)
: The correct answer of an item, written or checked by a person who knows the material.

**Scorer**
: The program that compares a model's answers with the references and gives a score. One scorer per task, used for every language.

**Headline score**
: The one number a leaderboard ranks by, for example `structure_f1` for table-of-contents extraction.

**Run**
: One pass of one skill and one model over a benchmark. We usually do 3 runs and show the mean, because models give slightly different answers each time.

**Baseline** ("No skill")
: The same model with a plain prompt and no skill. It shows how much a skill really adds (the **gain**).

**Data version**
: The version number of a benchmark, such as `2.0.0`. Patch (2.0.1) = fixed answers; minor (2.1.0) = new items; major (3.0.0) = new format or scorer. Scores are only compared within one version.

**Maturity level**
: How much you can trust a benchmark. 1 **Example**: format check only. 2 **Draft**: real items, one author. 3 **Reviewed**: a second reader from the tradition checked the answers. 4 **Stable**: held out and used in practice.

**Held-out**
: Material that a skill or model was not trained or tuned on. Scores on held-out material show how well it works on new work.

**Provenance record**
: A file that says exactly what made a score: skill files, model, settings, prompt, data version, code, logs, tokens, cost and date. Some projects call it a "bill of materials". See [Provenance records](handbook/provenance.md).

**Contamination**
: When a model may have seen the test items during training (for example because they are public on the web). Such scores can be too high. Public sets are marked `contamination: public`.

## Results

**Leaderboard**
: The ranked table of models and skills for one task and language, with score and cost. [Leaderboard](https://buddhistai.github.io/buddhist-benchmarks/).

**Top performance**
: The option with the highest score for a task and language.

**Best value**
: The option with the highest score among those that cost at most a fifth (20%) of the Top performance. Often a smaller model with a good skill.

**Cost**
: What one pass over the benchmark costs, from the tokens used and the model's list price. Shown per 100 pages where possible.

**Tokens**
: The units AI models count text in. Price is per million tokens, for input (what you send) and output (what the model writes).

**Challenger**
: A skill that is measured on the leaderboard but is not the current best skill.

**Best skill** (or **released skill**)
: The skill in buddhist-skills for a task and language, because it is the Top performance or the Best value on the leaderboard. Maintainers call this step "promotion".

**Arena** (planned)
: A page where people read two answers to the same request, without knowing which model made them, and pick the better one. Votes rank tasks that are hard to score with a program, such as translation.

## Taking part

**Share → Measure → Release**
: The three steps from a shared idea to a best skill. See [Governance](governance.md#how-a-skill-becomes-the-best-skill).

**Contributor**
: Anyone who shares, fixes, reviews or tests something. Credited by name.

**Backer**
: An organization that supports the project, for example with funds, API credits or compute. Listed under "Supported by".

**Expert review**
: A check of a benchmark's items and answers by someone who knows the material well. It can move a benchmark up a maturity level.

**Language reader**
: A volunteer who reads a language well enough to check answers in it.

**Maintainer**
: A member of the Maintainers team, who reviews and merges changes in the core repos. See [Governance](governance.md#roles).

**Partner organization**
: A group that contributes regularly and has its own GitHub team with access to its own task repos.

**Workshop repo** (or **task repo**)
: The repo where one skill is built: all its variants, runs, reports and provenance records. Example: [toc-extraction-tibetan](https://github.com/BuddhistAI/toc-extraction-tibetan).
