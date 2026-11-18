---
title: UX journey standard
name: buddhistai-journey-standard
description: The quality bar for any BuddhistAI design or page that a user sees. Used by persona Goldfish reviewers in EGM reviews.
license: MIT
version: 0.1.0
updated: 2026-11-18
---

# UX journey standard

[← UX reviews](../README.md)

A design passes when every persona it touches can finish their journey without help, understands every word, and trusts what they see. Reviewers check the six points below. Each point that fails is a finding.

## 0. Context

- The design names the journeys it changes (`ux/journeys/<id>.md`) and the pages it touches. If a reviewer cannot tell which journey or which page, the review stops with a Blocker.

## 1. The journey can be finished

- The persona reaches the "Done when" of the journey.
- Every step says what happens next. No dead ends. A planned feature says that it is planned.
- No step needs a tool the persona does not have (for example a terminal for a translator).

## 2. Plain words

- Short, literal sentences for readers whose first language is not English. No idioms.
- Every project word (benchmark, skill, provenance, Share → Measure → Release) is explained or linked the first time.
- Our words: "Buddhist tasks", "Top performance", "Best value", "best skill".

## 3. Trust

- Every score and cost has a unit, a date or data version, and a link to its source. Nothing is invented.
- Credits are neutral: BuddhistAI belongs to everyone who takes part. WeBuddhist is one contributor among others.
- It is clear what happens to a person's data, files and name.

## 4. Works everywhere

- The page works at 360px wide and in dark mode, and uses the design system (`buddhistai.css`, tokens).
- Text and controls pass WCAG AA contrast. Images have alt text.

## 5. Fits the whole service

- The change keeps the five journeys and the [rules](../../handbook/README.md#rules-we-never-break) intact. It does not break a link or a step in another journey.
- If the change alters a journey's steps, the design updates `ux/journeys/<id>.md` too.
