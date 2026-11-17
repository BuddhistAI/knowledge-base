# BuddhistAI Knowledge base

> BuddhistAI helps anyone working on a Buddhist project find the best-performing and best-value AI solution for their task, and helps anyone building AI solutions share theirs and take part in the evaluations. **This knowledge base is the shared place to learn about those tasks: what each task is, how projects do their work, and what our experiments found.**

Read and edit it on the web: **https://buddhistai.github.io/knowledge-base/** (every page has an "Edit this page" link).

The knowledge base has four sections:

- **Task pages** are the core. A task is one job that a model or skill can be asked to do and measured on, such as segmentation, OCR or translation review. Its page defines it: what goes in, what should come out, worked examples, edge cases, how it differs across languages and traditions, and how it is measured. It links the task's benchmark and leaderboard and names the current best skills, or says that no benchmark exists yet so you can help build one.
- **Workflow pages** describe how real projects work from start to finish: translating a text, preparing a digital edition, building a course, running a center. They are where tasks are found. Each step is mapped to a task, and a step with no task yet is a candidate for a new one. Workflows are owned by the people who do the work, and a workflow kept elsewhere (a Google Doc, a website) stays there: we link to it and credit its owner.

- **[Experiments](experiments/README.md)** record what we tried and what we learned: a plan written before each experiment, a dated log, and a report. Ideas for new experiments start as an [Idea issue](https://github.com/BuddhistAI/knowledge-base/issues/new?template=idea.yml).
- **[Directory](directory/README.md)** lists Buddhist AI projects and datasets from all traditions and languages: who makes them, what they do, and how open they are. The entries live in [`directory/projects.yml`](directory/projects.yml) and [`directory/datasets.yml`](directory/datasets.yml). [Add a project or dataset](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml) by pasting a link.

```
workflows  →  tasks  →  benchmarks + leaderboards  →  best skills
   (knowledge base)     (buddhist-benchmarks)         (buddhist-skills)
```

This is about **Buddhist tasks**, not only texts: translation and study, but also teaching, art and visual work, practice support, personal AI setups and the running of centers and projects.

## Contribute

You do not need git. Pick whichever is easiest:

1. **Edit a page.** Click "Edit this page" (or the pencil icon on GitHub), change it, and propose the change. Add an example, an edge case, a language note, a link.
2. **Paste a link.** [Add a project or dataset](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml) to the directory, [share a workflow](https://github.com/BuddhistAI/knowledge-base/issues/new?template=share-workflow.yml) by linking your document, or [suggest a task](https://github.com/BuddhistAI/knowledge-base/issues/new?template=suggest-task.yml) in a few sentences. A maintainer writes the page and credits you.
3. **Write a page.** Copy [`templates/task.md`](https://github.com/BuddhistAI/knowledge-base/blob/main/templates/task.md) or [`templates/workflow.md`](https://github.com/BuddhistAI/knowledge-base/blob/main/templates/workflow.md) and open a pull request.
4. **Discuss.** Ask or propose in [Discussions](https://github.com/orgs/BuddhistAI/discussions).

See [CONTRIBUTING.md](./CONTRIBUTING.md) for ownership, credit and review.

<!-- index:start -->
## Tasks

| Task | Area | Benchmark | Best skills | Found in |
| --- | --- | --- | --- | --- |
| [Annotation detection](tasks/annotation-detection.md) | Texts | none yet, help build one | none yet | 1 workflow |
| [Block ID assignment](tasks/block-id-assignment.md) | Texts | none yet, help build one | none yet | 1 workflow |
| [Buddhist knowledge Q&A](tasks/buddhist-knowledge-qa.md) | Study and teaching | yes | none yet | 0 workflows |
| [Citation mapping](tasks/citation-mapping.md) | Texts | none yet, help build one | none yet | 1 workflow |
| [Edition collation](tasks/edition-collation.md) | Texts | none yet, help build one | none yet | 1 workflow |
| [Entity extraction](tasks/entity-extraction.md) | Texts | none yet, help build one | none yet | 2 workflows |
| [OCR](tasks/ocr.md) | Texts | yes | none yet | 1 workflow |
| [Segmentation](tasks/segmentation.md) | Texts | none yet, help build one | none yet | 2 workflows |
| [Spell check](tasks/spell-check.md) | Texts | none yet, help build one | none yet | 2 workflows |
| [Table-of-contents extraction](tasks/toc-extraction.md) | Texts | yes | toc-extraction-tibetan | 2 workflows |
| [Term extraction](tasks/term-extraction.md) | Translation | none yet, help build one | none yet | 1 workflow |
| [Text cleanup](tasks/text-cleanup.md) | Texts | none yet, help build one | none yet | 2 workflows |
| [Text-commentary alignment](tasks/text-commentary-alignment.md) | Texts | none yet, help build one | none yet | 2 workflows |
| [Text-translation alignment](tasks/text-translation-alignment.md) | Translation | none yet, help build one | none yet | 1 workflow |
| [Translation](tasks/translation.md) | Translation | none yet, help build one | none yet | 2 workflows |
| [Translation review](tasks/translation-review.md) | Translation | none yet, help build one | none yet | 1 workflow |

## Workflows

| Workflow | Area | Owner | Kept | Status | Steps with a benchmark |
| --- | --- | --- | --- | --- | --- |
| [Preparing a digital edition from a template repo](workflows/digital-edition-pipeline.md) | Texts | Sitar | here | draft | 1 of 9 tasks |
| [Translating a Buddhist text](workflows/translation.md) | Translation | Kurt Keutzer | linked (owner's document) | draft | 2 of 13 tasks |
<!-- index:end -->

## Wanted

We have no workflows or tasks yet for these areas. If your project does this work, [share how you do it](https://github.com/BuddhistAI/knowledge-base/issues/new?template=share-workflow.yml):

- Teaching: building a course, preparing a talk, answering students' questions.
- Study: preparing for monastic exams, reading a text with its commentaries.
- Art and visual work: iconography checks, thangka and image description, archive cataloguing.
- Practice support: practice texts, schedules, retreat material.
- Centers and projects: newsletters, event planning, volunteer coordination, grant writing.
- Personal AI setups: the Claude or ChatGPT files, projects and instructions you use day to day.

## For maintainers

The **[Project handbook](handbook/README.md)** has everything needed to keep building BuddhistAI: mission and rules, every repo and site, conventions, how-to guides (run an evaluation, update the leaderboard, promote a winner), notes for the leaderboard app and arena, and the current status, decisions and roadmap.

## Related repos

- [buddhist-benchmarks](https://github.com/BuddhistAI/buddhist-benchmarks): tasks, test data, scorers and the [leaderboard](https://buddhistai.github.io/buddhist-benchmarks/) for models and skills.
- [buddhist-skills](https://github.com/BuddhistAI/buddhist-skills): the best skill per task and language, ready to install, plus community skills not yet measured.

## Contributors

Owners and contributors are credited on each page. Kurt Keutzer's model translation workflow was the first workflow linked here. The Experiments section was the separate `research` repo until 2026-11-17; its full history is kept here. Pages are maintained by BuddhistAI contributors, including the WeBuddhist team.

MIT licensed (see [LICENSE](https://github.com/BuddhistAI/knowledge-base/blob/main/LICENSE)). A linked document keeps its own owner and terms; we only link to it and summarize it in our own words.
