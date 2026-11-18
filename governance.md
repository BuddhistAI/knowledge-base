---
title: Governance
summary: Who decides what in BuddhistAI, how a skill becomes the best skill, how people and organizations join, and how we stay neutral.
---

# Governance

This page says who decides what in BuddhistAI, and how. It is short on purpose. If something is not covered here, ask in [Discussions](https://github.com/orgs/BuddhistAI/discussions), and we will add the answer.

## What BuddhistAI is

BuddhistAI is an open, shared project. It helps anyone working on a Buddhist project find the best-performing and best-value AI solution for their task, and it helps anyone who builds AI solutions share theirs and take part in the evaluations. Everything is public on [GitHub](https://github.com/BuddhistAI): skills, benchmarks, scores, decisions and the reasons for them. Code and our own data are MIT licensed. Imported data keeps its own license.

## Principles

1. **Scores decide, not people.** A skill becomes the best skill for a task because it scores best on an open benchmark, not because of who made it. Maintainers check that a result is correct; they do not choose winners.
2. **Everything can be checked.** Every score cites the exact skill version, model, data version and cost, and has a [provenance record](handbook/provenance.md). Anyone can re-run it.
3. **Neutral.** BuddhistAI belongs to everyone who takes part, from every tradition and language. No organization is the brand or the lead. Contributors and backers are listed in alphabetical order and never ranked by size or money.
4. **Practitioners first.** When we must choose, we favor what active translators, teachers and project teams need in their real work.
5. **Competing views are kept.** If two groups make different benchmarks for the same task, we keep both and score new skills on all of them.
6. **Never invent.** No made-up data, scores, votes or links. Anything planned is labeled as planned.

## Roles

| Role | Who | What they can do |
| --- | --- | --- |
| **Contributor** | Anyone | Share a skill, model, prompt, workflow or test set; report a problem; edit a page by pull request; review a benchmark; vote in the arena (when it opens). No account rights needed. |
| **Partner organization** | A group that contributes regularly (for example a translation team) | Everything a contributor can do, plus write access to **its own** task repos, through a GitHub team named after it. See [Adding people and organizations](#adding-people-and-organizations). |
| **Language or workflow owner** | A named expert per language or workflow | Reviews changes to the data, skills and pages for their language or workflow (listed in each repo's `CODEOWNERS`). |
| **Maintainer** | Members of the Maintainers team | Write access to the core repos. Review and merge pull requests, run evaluations, update leaderboards, release best skills, publish news. |
| **Project lead** | NT ([@ngawangtrinley](https://github.com/ngawangtrinley)) | Owner of the GitHub org, the domain, the Hugging Face org and the secrets. Final say when maintainers cannot agree. Confirms new backers. |

Today the project lead is also the only maintainer. More maintainers will be added from active contributors.

## How decisions are made

- **Day-to-day changes** (a fix, a new page, a new directory entry, a new result) are made by pull request. One maintainer or code owner reviews and merges.
- **Bigger changes** (a new rule, a new repo, a change to how scores or cost are computed, a scorer change) start as a post in [Discussions](https://github.com/orgs/BuddhistAI/discussions) or an issue. We wait at least a week for comments. Maintainers then decide, aiming for agreement. If they do not agree, the project lead decides and writes down why.
- **Changes to what users see** (a page, a form, install steps, the leaderboard app) start with a short design that our user personas review, and a person approves it in the pull request before it is built. Small text or bug fixes skip this. See [UX reviews](ux/README.md).
- **Team calls** may make decisions. The decisions and open questions are written in the [handbook status page](handbook/status.md) the same day.
- Every decision that changes how a repo, site or rule works is written in the [handbook](handbook/README.md).

## How a skill becomes the best skill

1. **Share.** Anyone shares a skill, or any file they give to AI. It is listed in the [prompt library](https://github.com/BuddhistAI/buddhist-prompt-library), unmeasured. A skill for a task with a benchmark is also added as a variant to the task's workshop repo.
2. **Measure.** It is run on the task's benchmark with the standard models. The run gets a `result.json` in buddhist-benchmarks and a provenance record in the skill's repo.
3. **Release.** If it is the **Top performance** (highest score) or the **Best value** (high score for at most a fifth of the top cost) on the latest data version, and it beats the current skill by more than the run-to-run noise, a maintainer copies it into buddhist-skills. The previous skill stays on the leaderboard as a challenger.

Only maintainers release skills into buddhist-skills, and only through the leaderboard. Nobody edits a released skill directly: improvements start as a new challenger and go through the same three steps. Details: [Promote a winner](handbook/how-to.md#promote-a-winner-to-buddhist-skills).

## Benchmarks

- Anyone may propose a benchmark. Material in real use (exam papers, reviewed translations) is preferred.
- A benchmark moves up four maturity levels: 1 Example, 2 Draft, 3 Reviewed (a second reader from the tradition checked the answers), 4 Stable (held out and used in practice).
- Every change to items or answers gets a new version. Scores are compared only within one version.
- Exam papers and other private material need a written permission record before they are published.

## Adding people and organizations

Anyone can contribute **without any access rights**: by a pull request from their own fork, or through the forms (Share, Request, Propose a benchmark, Review a benchmark, Donate compute). Access rights are only for people and groups who contribute often.

### Who can change what

| Repos | Who has write access | Everyone else |
| --- | --- | --- |
| **Core repos:** `buddhist-skills`, `buddhist-benchmarks`, `buddhistai.github.io` (the homepage), `design`, `knowledge-base`, `.github` (org profile) | Maintainers team only | Pull request, reviewed by the code owner |
| **A partner's task repos** (for example `translation-tibetan-to-english`) | Maintainers + that partner's team | Pull request |
| **A partner's own repo** (outside BuddhistAI) | The partner | Linked from our pages and leaderboard |

Partner teams **cannot** edit the homepage or buddhist-skills. This keeps the released skills tied to the leaderboard, and the main site neutral. A partner's skill reaches buddhist-skills only by winning on the leaderboard.

### Steps: add a partner organization

Done by an org owner or maintainer, in the GitHub web UI.

1. **Agree first.** Talk with the group in an issue or in Discussions: what they will contribute, which task and language, who their contact person is. Make sure they have read the [Code of Conduct](https://github.com/BuddhistAI/.github/blob/main/CODE_OF_CONDUCT.md).
2. **Invite the members.** Org page → People → Invite member. Give them the role **Member** (never Owner). The org's base permission for members must stay **Read** (Settings → Member privileges).
3. **Create their team.** Org page → Teams → New team. Name it after the group, for example `<org>-team`. Visibility: visible. Add their members. Make their contact person a team maintainer.
4. **Give access only to their repos.** For each of their task repos: repo Settings → Collaborators and teams → Add teams → their team → role **Write** (or **Maintain** if they manage the repo). If they keep their work in their own GitHub account, skip this step and link their repo instead.
5. **Optional: help with issues.** To let them sort issues on the Skills or Benchmarks board, give their team **Triage** on buddhist-skills or buddhist-benchmarks. Triage cannot change files.
6. **Make them reviewers for their area.** In the core repo's `.github/CODEOWNERS`, add their team on the lines for their language or workflow (for example `/skills/*-tibetan/ @BuddhistAI/<org>-team`). They then review pull requests in their area, but a maintainer still merges.
7. **Credit them.** Add the organization to the Contributors list on the org profile and the homepage (`#people`), in alphabetical order ([how-to](handbook/how-to.md#add-a-contributor-or-a-backer)), and post a short welcome in [News](news/README.md).

### Steps: add a person

- **One-time contributor:** nothing to do. Merge their pull request and credit them (`authors`, `contributors` or `made_by`).
- **Regular contributor:** invite as a Member with no extra rights, or add them to their organization's team.
- **New maintainer:** a maintainer proposes them after sustained, careful contributions; the other maintainers agree; the project lead adds them to the **Maintainers** team.

### Protection of the core repos

The org has a **Maintainers** team (`@BuddhistAI/maintainers`) since 17 November 2026; repo permissions for it are not set yet. Planned when the first partner team joins: on each core repo, a branch rule on `main` that requires a pull request with one approving review from a code owner, and the Maintainers team as the only team with write access. Until then, the project lead and Claude sessions working for the project push to `main` directly. See the [handbook](handbook/architecture.md#permissions) for the current state.

## Money, compute and credit

- Evaluations run on API keys or compute donated by supporters. A donor never gets a better score or a better place in any list.
- Backers are listed under "Supported by" in alphabetical order, only after the project lead confirms them. Donors of compute or API credits can be listed there too, if they wish. See [Contribute](CONTRIBUTING.md).
- Everyone who contributes is credited by name, including reviewers and language readers.

## Code of conduct

Everyone follows the [Code of Conduct](https://github.com/BuddhistAI/.github/blob/main/CODE_OF_CONDUCT.md). Report problems to the project lead.

## Changing this page

This page changes like any big decision: a proposal in Discussions, at least a week for comments, then a pull request.
