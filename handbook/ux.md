---
title: UX reviews with EGM
summary: How every change that users see is designed, reviewed by user personas with Google's Elephant-Goldfish Model, approved and checked after release.
---

# UX reviews with EGM

[← Handbook](README.md)

NT decided on 2026-11-18: BuddhistAI is one service, and every change that users see goes through an EGM review with our user personas. Public summary for contributors: [UX reviews](../ux/README.md).

## What EGM is

The [Elephant-Goldfish Model](https://github.com/google/elephant-goldfish-model) is a free, open-source plugin from Google (Apache 2.0, October 2026). It is a method plus Markdown skills and reviewer prompts. It runs in Claude Code, Codex and Antigravity.

- **Elephant:** a session with the full project context. It drafts a design document and writes no code.
- **Goldfish:** fresh subagents that read only the design and the files it links. They find gaps the Elephant cannot see.
- **A person** approves the design before anything is built.

EGM's own reviewers (design critic, comprehension, zoom-out, structural, readiness) review software designs. EGM does not have user personas. We add ours as custom Goldfish: `egm-review-loop` accepts any file path as a reviewer.

## What needs a review

| Needs a design and a review | Skips it |
| --- | --- |
| A new page or section, a changed journey step, a new or changed form, install steps, the leaderboard app and the arena, homepage sections, words on buttons and headings, the design system's look | A text or bug fix you can describe in two sentences (EGM's own advice), content pages (a task, a language, a directory entry), data, scores, scripts that users do not see |

## Where things live

| What | Where |
| --- | --- |
| Personas, journeys, the UX standard | knowledge-base [`ux/`](../ux/README.md) (source of truth for every repo) |
| Design documents | `docs/designs/<yyyy-mm-dd>-<slug>.md` in the repo that changes; template in knowledge-base [`docs/designs/TEMPLATE.md`](../docs/designs/TEMPLATE.md); `SITEMAP.md` lists them |
| Claude skills | `.claude/skills/buddhistai-elephant` (load context, draft) and `.claude/skills/buddhistai-ux-review` (run the review). Source: knowledge-base; copies in buddhistai.github.io, buddhist-benchmarks, buddhist-skills and design must match. |
| EGM plugin | Offered by each repo's `.claude/settings.json` (marketplace `google/elephant-goldfish-model`, plugin `egm@egm`). Each repo's `CLAUDE.md` has `EGM artifact directory: docs/designs`. |
| CI | `egm` workflow in each repo with pages; it calls the reusable `egm-gate` and `egm-goldfish` workflows in knowledge-base. Monthly `ux-walkthrough` in knowledge-base. |

## How to run a review

1. Install EGM once: `claude plugin marketplace add google/elephant-goldfish-model`, then `claude plugin install egm@egm`. (Claude Code offers it when you open a BuddhistAI repo.) Needs Claude Code 2.1.271 or later.
2. In the repo you change, ask Claude to use the **buddhistai-elephant** skill and draft the design (`/egm:egm-draft`). It saves `docs/designs/<date>-<slug>.md`.
3. Ask Claude to use the **buddhistai-ux-review** skill. It runs EGM's `egm-review-loop` with EGM's reviewers plus the personas of the journeys the design names. The loop asks you before each new round. It stops after two clean rounds in a row (no open Blocker or Major finding) or after 5 rounds.
4. Fix what you agree with. Fill in the "Goldfish review" section. Open a pull request with the design (and later the code). In the description, link the design under "EGM review".
5. A maintainer approves. Then build. If the build changes a journey's steps, update `ux/journeys/<id>.md` in the same pull request.

Every repo's `CLAUDE.md` (section "Changes users see: follow EGM") tells Claude to do steps 2 to 5 by itself, so a developer who codes with Claude follows EGM by default. The review runs in the developer's own Claude session: no API key and no CI are needed. The `egm-review` label in CI is an optional extra.

EGM by itself asks the developer a lot: one question at a time, approval of each drafted section, and a decision on each finding. Our rule overrides that. Claude answers gaps from the code, the knowledge base and the personas, resolves findings itself, and asks the developer only the product decisions that no source settles, in one short list with a recommendation for each.

Humans can do every step without Claude: write the design from the template, and ask people to review it as personas.

## CI: the egm workflows

- **egm-gate** (free, every pull request): if a pull request changes user-facing paths, it fails unless the pull request adds or links a design in `docs/designs/`, or ticks "Small change" in the description. Each repo sets its user-facing paths in `.github/workflows/egm.yml`. It is not a required check: a maintainer can still merge.
- **egm-goldfish** (paid, on request): add the label `egm-review` to a pull request. One review round runs in CI (`anthropics/claude-code-action` with the EGM plugin) and posts the findings as a comment. It never edits files. It needs the secret `ANTHROPIC_API_KEY`; without it, it skips.
- **ux-walkthrough** (paid, monthly on the 1st at 05:41 UTC, or manual): Claude reads the live sites as each persona, tries each journey and opens an issue labeled `ux-walkthrough`. It reads page text only: a simulated walkthrough, never proof. Needs `ANTHROPIC_API_KEY`.

## Feedback loop

- Real feedback comes from the [UX feedback form](https://github.com/BuddhistAI/knowledge-base/issues/new?template=ux-feedback.yml) (label `ux-feedback`), Discussions (Website and development), team calls and talks with users.
- Once a week, a maintainer sorts new `ux-feedback` and `ux-walkthrough` issues: a problem becomes a card on the Development board; a fact about users goes into the persona's "Known pain points" with its source, and into project memory. A changed persona gets a version bump.
- Never add a pain point, a persona trait or a number without a source. Walkthrough findings are guesses until a real user confirms them.

## Board

Board fields and automations can only be set in the GitHub web UI. **Not set up yet (2026-11-18), NT to do:**

1. Development board → Settings → Status field: add **Design review** after To do. Use it for cards whose design waits for a Goldfish review or approval.
2. Development board → Workflows → Auto-add to project: repository knowledge-base, filter `is:issue label:ux-feedback,ux-walkthrough`. Turn it on.
3. In each repo with an `egm` workflow, create the labels `egm-review` (and in knowledge-base `ux-feedback`, `ux-walkthrough`). The first use of a label in a form or workflow also creates it.
