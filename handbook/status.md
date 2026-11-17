---
title: Status, decisions and roadmap
summary: What is real today, what is still planned, decisions and open questions from the 2026-11-17 team call, and the next steps.
---

# Status, decisions and roadmap

[← Handbook](README.md)

Status as of 2026-11-17. Update this page when something here changes.

## What is real today

| Part | State |
| --- | --- |
| Homepage https://buddhistai.github.io/ | Live. One static page. All scores on it are real results, copied by hand from the leaderboard. A banner says the arena and automatic scoring are planned. |
| Leaderboard https://buddhistai.github.io/buddhist-benchmarks/ | Live. Generated from `result.json` files by CI. One task benchmark with results (Tibetan TOC), plus BuddhistBench and an external card (BDRC Tibetan OCR). |
| Knowledge base https://buddhistai.github.io/knowledge-base/ | Live. 16 task pages, 2 workflow pages (both drafts, not yet reviewed by their owners), 2 experiments, 2 community papers, a Directory of 87 projects and 73 datasets, Languages pages for 21 Buddhist languages with a country overview, and this handbook. |
| Design system https://buddhistai.github.io/design/ | Live, version 1.0.0. Used by the leaderboard and the knowledge base. |
| buddhist-skills | One released skill (`toc-extraction-tibetan` 1.0.0), the router `ask-buddhistai`, one community entry (a personal setup, `my-dharma.md`, CC0). Plugin marketplace works. |
| buddhist-benchmarks | 15 tasks in `tasks/index.json`; 1 active (`toc-extraction`), with data set `toc-extraction/bo` 2.0.0 (85 items). Published on Hugging Face. |
| buddhist-bench (BuddhistBench) | Version 0.4.0, a scaffold. Format examples only, plus the imported Thai Dhamma exam set (4,075 questions). No live model runs yet (no OpenRouter key). |
| GitHub → Hugging Face sync | Live since 2026-11-17. |
| Boards and forms | Skills board and Benchmarks board live (public), fed by issue forms. Development board for team members (private for now). |

### Current results: Tibetan TOC extraction

Benchmark `toc-extraction/bo` 2.0.0 (85 passages from two commentaries, one book held out). Headline metric: structure F1. Full table: [leaderboard](https://buddhistai.github.io/buddhist-benchmarks/tasks/toc-extraction/bo/); report: [REPORT.md](https://github.com/BuddhistAI/toc-extraction-tibetan/blob/main/REPORT.md); experiment: [2026-11-toc-tibetan-skills](../experiments/2026-11-toc-tibetan-skills/).

- **Top performance:** TOC extraction (sa-bcad method) 1.0.0 on Claude Sonnet 5.5: 0.962, about $1.20 per 100 pages. This is the released skill.
- **Best value:** TOC extraction (GEPA-optimized) 1.0.0 on Claude Haiku 5.5: 0.824, about $0.05 per 100 pages.
- The two skills are a near-tie within run-to-run noise. On Sonnet 5.5 the plain prompt already scores 0.951; the skills help most on Haiku 5.5 (+0.08).
- **Costs are estimates (≈):** the runs did not log tokens, so tokens were counted afterwards. A measured re-run (about $30) would replace them. Not decided yet.
- **Known problem:** the held-out book's answer key (*The Jewel Garland*) misses many real headings. A Tibetan reader must check those 9 passages. That gives benchmark 2.0.1 (patch), then re-run the top two skills ([issue knowledge-base#1](https://github.com/BuddhistAI/knowledge-base/issues/1)).

### Planned or mock (labelled on the sites)

- **Arena:** the homepage shows an example layout with no votes. Nothing is built.
- **Automatic scoring:** the homepage paste box only opens a prefilled GitHub issue; a maintainer runs every evaluation.
- **Repo auto-detection** (guessing task and language from a pasted repo): not built.
- **MCP server** serving the top skills to tools other than Claude: not built.
- **Workflow skills** (skills that chain other skills, with end-to-end leaderboards): documented only ([buddhist-skills#2](https://github.com/BuddhistAI/buddhist-skills/issues/2)).
- **One repo per benchmark** with a maturity level (Example → Draft → Reviewed → Stable): shown on the homepage, not built. Benchmarks still live inside buddhist-benchmarks.
- **Best value and Top performance both in buddhist-skills:** decided, not built. Today one skill per task and language.
- **Intervention study** (does publishing sourced information change AI answers?): designed in buddhist-bench, plan not frozen ([knowledge-base#2](https://github.com/BuddhistAI/knowledge-base/issues/2)), waiting for keys and real items.
- **Community parts not set up:** monthly digest, pinned help-wanted list. (The contributors list is generated daily, and includes community authors.)
- **Sharing without a GitHub account:** not possible yet. The Share form needs a free GitHub account.

### Waiting on NT

- **Secret `ORG_REPOS_TOKEN`** in BuddhistAI/knowledge-base, for the weekly `agent-notes` check ([Architecture](architecture.md#secrets)). Until then the check only lists repos that have no `CLAUDE.md`.
- The BuddhistAI/.github repo has no agent notes yet: the session that wrote them cannot push to it. The weekly check will open a pull request there once the token is set.

### Waiting on a reader

- **Tibetan:** check *The Jewel Garland* references in TOC benchmark (see above).
- **Thai:** confirm whether the imported Thai set is the monastic Nak Tham exam or the lay Dhamma Studies exam (its source groups suggest lay exams), and review it.
- **Workflow owners:** Kurt Keutzer and Sitar to review their workflow pages.

Readers volunteer with the [language reader form](https://github.com/BuddhistAI/buddhist-skills/issues/new?template=reader.yml).

## Team call, 2026-11-17

### Decisions

- **One common buddhist-skills repo** holds only the top-ranked skills per task. **Each task has its own repo** with all submitted versions. Users always get the best skill; contributors are motivated by ranking higher.
- **Two views on one leaderboard:** Top performance and Best value (cheaper models or fewer tokens). A skill that is good enough for less money matters to practical users. The group chose these names over Michelin-style names.
- **Benchmarks per task, in separate repos.** buddhist-benchmarks lists them and does not hold all the data (too heavy).
- **Conflicting benchmarks stay.** When groups' benchmarks differ, keep both and score new skills on both. Groups that do not want to merge (for example Kai's team) are welcome to link theirs.
- **Onboarding by linking a GitHub repo** (Evan's idea), with a clear Submit button. Contributors may not come back to update.
- **Submission like BDRC's OCR leaderboard:** GitHub issue, a GitHub Action computes the score, a maintainer approves.
- **Inference for evaluations runs on a sponsor's key** (Dave offered keys).
- **Qualitative evaluation through an Elo-style arena.**
- **Start benchmarks from real data already in use** (monastery exam papers were suggested); keep them open and public. Small but diverse.
- **Evaluations cover zero-shot models and skills together,** with filters.
- **Decisions on benchmarks favor active translators.**
- The buddhist-skills repo can be used as a plugin or an MCP server.

### Action items from the call

| Who | What | State |
| --- | --- | --- |
| Kalden | Leaderboard web app MVP (FastAPI + React) by 2026-11-18, then the arena. Then add Sitar's skills and invite other organizations; reply to the Italian group. | In progress. See [Building the leaderboard app](leaderboard-app.md). |
| Sitar | Segmentation, annotation detection and Tibetan spell-check skills; gather data sets that can serve as benchmarks for each. Sitar's team already has sets for Tibetan annotation detection and an author-name detection skill. | Open. Task pages exist here; no benchmarks yet. |
| Evan | Help document Buddhist data workflows (a place where organizations share theirs; structure to be worked out). Try Google's "elephantgoldfish" for shared project memory; talk to Monlam about feedback. | Open. Evan is the natural owner of the knowledge base Workflows section, not confirmed. |
| Owner not named | A skill in the Rails template repo that syncs updated skills from the template into repos built from it. | Open. |

### Open questions

- **Community channel:** answered 2026-11-17: [GitHub Discussions](https://github.com/orgs/BuddhistAI/discussions), with categories for each area of the project. A chat channel (WhatsApp, which translators prefer, or Discord) may come later.
- **Edge-case fixes back to the template:** fixes made in one repo's copy of a skill stay local because they can break the generic version. Idea: a skill that scans repos built from the template and improves the template skill.
- **Cheap evaluations:** evals and optimizers like GEPA burn many tokens. Always set an iteration limit; keep benchmarks small but diverse.
- **Who owns workflow documentation:** Kurt's translation workflow stays his own document. Evan and Kalden were asked and did not commit.
- **Who maintains benchmarks:** proposal: skill publishers also publish benchmarks, and others add edge cases. An agent that improves benchmarks was mentioned, not settled.
- **Who posts on LinkedIn and X** when there is a new leader. The X account [@buddhist_ai](https://x.com/buddhist_ai) exists (2026-11-17); LinkedIn is pending.
- **Hosting** of the FastAPI app and DNS for `buddhistai.org`.
- From buddhist-skills design notes: a shared runner for reproducible runs across models; human evaluation where metrics fall short; a minimum data size before a promotion counts.

## Roadmap

In rough order. Owners in brackets where known.

1. **Leaderboard app MVP** reading the existing JSON files and using the design tokens [Kalden]. Then the **arena** [Kalden].
2. **Domain:** point `buddhistai.org` (Cloudflare) at the sites; decide where the app runs; update links everywhere [NT, Kalden].
3. **Sponsor key and automatic scoring:** add `OPENROUTER_API_KEY` (and `BRAVE_API_KEY`) as secrets; a GitHub Action that scores a submitted repo; maintainer approval [NT, Kalden].
4. **First model runs:** run commercial and open-weight models through OpenRouter on the Thai exam set and the TOC benchmark, so the model table fills in.
5. **Fix the TOC answer key** with a Tibetan reader → benchmark 2.0.1 → re-run the top two with real token logging (replaces the estimated costs).
6. **New benchmarks from Sitar's team:** segmentation, annotation detection, Tibetan spell check. Then promote their skills through the leaderboard [Sitar].
7. **Split benchmarks into one repo each** with a maturity level, and make buddhist-benchmarks the list. Move the TOC data first and keep tags and Hugging Face names stable.
8. **buddhist-skills holds both picks** (Top performance and Best value) per task and language; decide the folder naming.
9. **Monastery exam papers** as benchmarks, with permission records. Plan: [buddhist-benchmarks#1](https://github.com/BuddhistAI/buddhist-benchmarks/issues/1) with sub-issues #2 to #11.
10. **Thai reader** for the imported set; **workflow owners** review their pages; more workflows from teaching, art and practice.
11. **Community:** Discussions is set up (2026-11-17). Still to do: a contributors list, a help-wanted list, decide who posts on LinkedIn and X; maybe a chat channel later.
12. **Homepage:** read scores from the leaderboard data instead of a hand-copied array (or replace the page with the app).
13. **Access for partner organizations:** before the first partner team gets access, give the Maintainers team (created 2026-11-17) access to the core repos, check member base permission is Read, and add branch rules (pull request + code-owner review) on the core repos ([Governance](../governance.md#adding-people-and-organizations)) [NT].

## Changes since the call

- 2026-11-17: first community translation material, by Drupchen (CC BY 4.0): the paper *Subtracting the Typological Baseline* in the new [Papers](../papers/README.md) section (linked from the Translation and Translation review tasks), and its practical guide *Two strategies for improving machine translation from Tibetan*, also in Papers (French added to buddhist-skills `languages.json`). The guide was first a buddhist-skills community entry, then moved: it is theory, not a skill. We write our own skills from it (style profile; Tibetan to French with a profile), credited to Drupchen, and a Tibetan colophon translation benchmark. Papers are not in the top menu (NT finds it too long); they are linked from the home page and the task pages.
- 2026-11-17: after a comparison with openwaldo.org, NT decided: (1) a **provenance record** per leaderboard row, kept in the skill's own repo, never in buddhist-benchmarks: standard [buddhistai/provenance@1](provenance.md), applied to all 10 toc-extraction-tibetan rows (costs still estimated); (2) no shared data commons for now, but the Directory marks each dataset **open** and **collaborative**; (3) four **tutorials** in [Learn by building](../learn/README.md); (4) two new contribution paths: **expert review of a benchmark** and **donate compute or API credits** (buddhist-benchmarks forms, CONTRIBUTING files, homepage); (5) [Governance](../governance.md) (with the access model for partner organizations), [FAQ](../faq.md), [Glossary](../glossary.md) and [News](../news/README.md) pages.
- 2026-11-17: access model written down; NT chose to set up the Maintainers team and branch rules later, when the first partner team joins.
- 2026-11-17: the knowledge base gained Languages: one page per Buddhist language (data, AI projects, translation quality, recommendation) and a country overview.
- 2026-11-17: this handbook was written; the knowledge base gained the Directory; GitHub → Hugging Face sync went live.
