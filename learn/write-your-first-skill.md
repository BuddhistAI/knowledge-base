---
title: Write your first skill
summary: "Tutorial 3: write a SKILL.md for a Buddhist task, try it with an AI assistant, share it, and have it measured."
---

# Tutorial 3: Write your first skill

[← Learn by building](README.md)

**You will:** write a skill for one Buddhist task, test it by hand, share it with the community, and (if the task has a benchmark) have it measured.
**You need:** a text editor and a GitHub account. An AI assistant that reads skills (for example Claude) helps you test. About 45 minutes.

## What a skill is

A **skill** is a folder with a file called `SKILL.md`. The file has a short header and then written instructions: how to do the task, the rules, the output format and an example. An AI assistant reads it when the task comes up. A good skill makes a model do the task better, or makes a cheaper model do it as well as an expensive one.

One skill is for **one task in one language**. Its name is `<task>-<language>`, for example `toc-extraction-tibetan` or `translation-pali-to-english`. Task names are in the [task list](../README.md#tasks).

## 1. Copy the template

Copy [`templates/skill/SKILL.md`](https://github.com/BuddhistAI/buddhist-skills/blob/main/templates/skill/SKILL.md) from buddhist-skills into a new folder named after your task and language. Fill in:

- `name`: `<task>-<language>`.
- `description`: one sentence saying what the skill does and when to use it. The assistant reads this to decide whether to use your skill, so be concrete.
- `metadata.version`: start at `0.1.0`. Raise it every time you change the skill.

## 2. Write the instructions

Write as if you explain the job to a careful new assistant who knows the language but not your project:

1. **Steps**: what to do first, next and last.
2. **Rules**: the things your team checks by hand. Which glossary, which transliteration, what never to change.
3. **Output format**: exactly what the answer looks like. If the task has a benchmark, use the format in its `TASK.md`.
4. **Example**: one short real input and the correct output.

Keep it short. Long skills cost more tokens on every call, and the leaderboard shows cost.

## 3. Test it by hand

Give your skill and three or four real inputs to your assistant. In Claude, add the folder as a skill, or paste `SKILL.md` into the chat and then the input. Check the answers yourself. Fix the instructions where the model goes wrong, and raise the version.

For a task with a benchmark, you can test on the real items: put the text of your skill into `PROMPT` in the script from [Tutorial 2](evaluate-your-first-model.md) and score it.

## 4. Share it

Open the [Share your files](https://github.com/BuddhistAI/buddhist-prompt-library/issues/new?template=share.yml) form and paste a link to your folder (or attach the file). A maintainer adds it to the [prompt library](https://github.com/BuddhistAI/buddhist-prompt-library) with your name in `authors`. You do not need to know git, but you need a free GitHub account. The form is public.

## 5. Have it measured

If the task has a benchmark, a maintainer runs your skill on it with the standard models, or you submit a run yourself ([SUBMIT.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md)). The run gets a [provenance record](../handbook/provenance.md), so anyone can see exactly which version of your skill made the score. If your skill becomes the **Top performance** or **Best value** for its task, it is released in buddhist-skills and we announce it, crediting you.

If the task has a benchmark, a maintainer also adds your skill as a variant in the task's workshop repo. If the task has no benchmark yet, your skill stays in the prompt library until there is one. You can help build it: [Tutorial 4](add-a-benchmark.md).

## Good to know

- Never mix languages in one skill. A Tibetan and a Pali version are two skills.
- Credit the glossaries, editions and other people's work your skill uses, with their licenses.
- Skills are MIT licensed when they are added to buddhist-skills.
