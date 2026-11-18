---
title: UX reviews
summary: How we design and review what users see, with user personas and Google's Elephant-Goldfish Model (EGM).
---

# UX reviews

BuddhistAI is one service with five user journeys. Before we change a page that users see, we write a short design and our **user personas** review it. We use Google's open-source [Elephant-Goldfish Model](https://github.com/google/elephant-goldfish-model) (EGM, Apache 2.0) for this.

- The **Elephant** is a Claude session that knows the project. It drafts the design.
- The **Goldfish** are fresh reviewers. They read only the design, not the conversation behind it. We add our personas as Goldfish, next to EGM's own reviewers.
- A **person** approves the design in a pull request before anything is built.

How to run a review, step by step: [Handbook: UX reviews with EGM](../handbook/ux.md).

## Personas

Drafts from what we know. Real feedback replaces guesses over time (each pain point needs a source).

| Persona | Audience |
| --- | --- |
| [Translator](personas/translator.md) | Buddhist project teams |
| [Project lead](personas/project-lead.md) | Buddhist project teams |
| [Funder](personas/funder.md) | Funders and coordinators |
| [Skill builder](personas/skill-builder.md) | People who build AI solutions |
| [Benchmark publisher](personas/benchmark-publisher.md) | People who build AI solutions |

## Journeys

| Journey | Personas |
| --- | --- |
| [Find and use a skill](journeys/find-and-use-a-skill.md) | Translator, Project lead |
| [Share know-how or a skill](journeys/share-know-how.md) | Translator, Skill builder |
| [Get a skill or model measured](journeys/get-measured.md) | Skill builder |
| [Share a benchmark](journeys/share-a-benchmark.md) | Benchmark publisher |
| [Understand the field](journeys/understand-the-field.md) | Funder |

## Standard

Every review checks the [UX journey standard](standards/journey-standard.md): the journey can be finished, plain words, trust, works on phones and in dark mode, and fits the whole service.

## Take part

You do not need to write code. Pick one:

1. **Tell us what was hard.** Open a [UX feedback](https://github.com/BuddhistAI/knowledge-base/issues/new?template=ux-feedback.yml) issue, or post in [Discussions](https://github.com/orgs/BuddhistAI/discussions). This is the most useful help of all: real feedback changes the personas.
2. **Review a design as a persona.** Designs waiting for review are pull requests with the label [`egm-review`](https://github.com/search?q=org%3ABuddhistAI+label%3Aegm-review+is%3Apr+is%3Aopen&type=pullrequests). Read the design as the persona closest to you, and comment: where would you stop, what is not clear, what would you not trust?
3. **Write a design.** Want to change a page? Copy [the design template](../docs/designs/TEMPLATE.md), describe the change step by step in a user's words, and open a pull request. Claude can draft it with you (`buddhistai-elephant` skill), but a person can write it alone too.
4. **Suggest a persona or fix one.** Is someone missing, for example a teacher, an artist or a monastery librarian? Or is a persona wrong about people like you? Edit its page or open a [UX feedback](https://github.com/BuddhistAI/knowledge-base/issues/new?template=ux-feedback.yml) issue. A new persona needs a real reason (feedback, a talk with users), not a guess.

Credit: you are named in the design, the persona's "Known pain points" or the `contributors` of the page you changed.

## The flow

```
feedback and walkthroughs → personas and journeys → design → Goldfish review → a person approves → build
         ↑                                                                                             |
         └─────────────────────────────────────────────────────────────────────────────────────────────┘
```

Small changes (a text or bug fix you can describe in two sentences) skip the design.

## Give feedback

Something on our sites was hard to use? Tell us in the [Website and development](https://github.com/orgs/BuddhistAI/discussions) category of Discussions, or open a [UX feedback](https://github.com/BuddhistAI/knowledge-base/issues/new?template=ux-feedback.yml) issue. Each piece of feedback updates a persona or a journey.
