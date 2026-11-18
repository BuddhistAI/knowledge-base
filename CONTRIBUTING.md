# Contributing

This knowledge base is the shared place to learn about Buddhist tasks: what each task is, how it is measured, the workflows it comes from, and what our experiments found. Everyone who does Buddhist work is welcome here: translators, teachers, editors, artists, librarians, center staff, developers. You do not need to write code or use git. Please follow the [code of conduct](https://github.com/BuddhistAI/.github/blob/main/CODE_OF_CONDUCT.md).

## Ways to take part

| You can give | How | Credit |
| --- | --- | --- |
| A skill, prompt, model or personal AI setup | [Share form](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=share.yml) or paste a link on the [homepage](https://buddhistai.github.io/#submit) | `authors` on the entry; leaderboard row |
| Test material (exam papers, checked translations, corrected OCR) | [Propose a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=propose-benchmark.yml) | Dataset card; benchmark page |
| **An expert review of a benchmark** | [Review a benchmark](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=expert-review.yml): check items and answers in a field you know | Named as reviewer in the dataset card |
| Reading in your language | [Volunteer as a language reader](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=reader.yml) | Named as reader |
| **Compute or API credits** | [Donate compute or API credits](https://github.com/BuddhistAI/buddhist-benchmarks/issues/new?template=donate-compute.yml): pays for evaluations of everyone's submissions | "Supported by" on the homepage and org profile, if you wish |
| How your project works | [Share a workflow](https://github.com/BuddhistAI/knowledge-base/issues/new?template=share-workflow.yml) | Owner of the workflow page |
| A project or dataset we do not list | [Add to the Directory](https://github.com/BuddhistAI/knowledge-base/issues/new?template=add-to-directory.yml) | — |
| A fix or a new page | "Edit this page" on any page | `contributors` on the page |
| **Feedback on our sites, or a review of a design** | [UX reviews](ux/README.md#take-part): tell us what was hard, review a design as a persona, write a design, or suggest a persona | Named in the design or the persona |

New to this? The [tutorials](learn/README.md) teach the steps by doing them. Organizations that contribute often can get their own GitHub team: see [Governance](governance.md#adding-people-and-organizations).

## Improve a task page

Task pages belong to everyone. Click "Edit this page" on the site (or the pencil icon on GitHub) and propose a change. The most useful additions are:

- a real **example** with its correct answer, and where it comes from;
- an **edge case**: a hard case where people or models often make mistakes;
- a **language or tradition note**: how the task differs in Pali, Classical Chinese, Tibetan and so on;
- a sharper **definition**, especially where two tasks overlap;
- a link to a tool, data set, paper or benchmark.

Add your name to `contributors` in the page's frontmatter. A maintainer reviews the change; a disagreement about a definition goes to the page's discussion (an issue or a Discussions thread linked from the page) and both views can be recorded on the page until it is settled.

## Who owns a workflow page

Every workflow has an **owner**: the person or organization whose practice it describes. Choose one of two modes.

| Mode | Where the document lives | What lives here | Who can change it |
| --- | --- | --- | --- |
| `linked` | Your own place (Google Doc, website, PDF) | A short page in our own words: summary, credit, a link to your version, and a map from your steps to tasks | You change your document whenever you like. Our page follows it; we update the version and the step map. |
| `hosted` | This repo | The full workflow | You review every change to your page (listed in `.github/CODEOWNERS`). Others suggest edits by pull request. |

Rules for both modes:

- We never copy a linked document wholesale. We summarize it and link to it.
- The owner is credited at the top of the page and in the frontmatter (`owner`, `contributors`). Name the people who helped you in `contributors`.
- A page records the owner's own version number (`source_version`) so readers know which version the step map describes.
- An owner may ask us to remove or change their page at any time.

## Share a workflow

1. **Easiest:** [open a "Share a workflow" issue](https://github.com/BuddhistAI/knowledge-base/issues/new?template=share-workflow.yml) and paste a link. A maintainer writes the `linked` page, maps your steps to tasks and asks you to check it.
2. **By pull request:** copy [`templates/workflow.md`](https://github.com/BuddhistAI/knowledge-base/blob/main/templates/workflow.md) to `workflows/<id>.md`, fill it in, run `python3 scripts/build.py` and `python3 scripts/check.py`, and open a pull request.

Good workflow pages:

- Describe what people really do, including the steps no AI does today. A step with no task is useful information: it shows what is missing.
- Map each step to a task ID from [`tasks/`](https://github.com/BuddhistAI/knowledge-base/tree/main/tasks) where one fits. If none fits, write `new task?` in the table and say what the step needs; a maintainer will propose a task.
- Stay one workflow per page. A variant (another language, another tradition, another team's order of steps) gets its own page that names the one it adapts.

## Propose a task

A task is one step that a model or skill can be measured on, such as segmentation or translation review. [Open a "Suggest a task" issue](https://github.com/BuddhistAI/knowledge-base/issues/new?template=suggest-task.yml), or copy [`templates/task.md`](https://github.com/BuddhistAI/knowledge-base/blob/main/templates/task.md). Task IDs are shared with [buddhist-benchmarks `tasks/index.json`](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/tasks/index.json) and skill names in buddhist-skills (`<task>-<language>`), so a new task gets added there too.

## Help a task get a benchmark

Most tasks have no benchmark yet. A benchmark starts small: twenty to fifty real items from work you already do, with the answer a careful human would give. See [buddhist-benchmarks SUBMIT.md](https://github.com/BuddhistAI/buddhist-benchmarks/blob/main/SUBMIT.md) and the task page's "Help wanted" section.

## Propose or run an experiment

Start with an [Idea issue](https://github.com/BuddhistAI/knowledge-base/issues/new?template=idea.yml). How an experiment is planned, logged and reported is described in [experiments/README.md](experiments/README.md).

## For maintainers

- Frontmatter fields are checked by `scripts/check.py`. The index tables in `README.md`, the "Found in workflows" lists on task pages and the directory tables in `directory/README.md` are generated by `scripts/build.py`; never edit them by hand. Directory entries are edited in `directory/projects.yml` and `directory/datasets.yml` (the field list is at the top of each file).
- When a benchmark or a best skill changes, update the task page's `benchmarks`, `leaderboard` and `skills` fields.
- Version pages with semver in `version`: a new step or task mapping is minor, a wording fix is patch, a restructure is major. `source_version` is the owner's own version and is separate.
