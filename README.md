# Cross-Domain Invariants

A research repository for **mapping cross-domain invariants** — the patterns,
structures, and laws that recur across otherwise-unrelated fields (physics,
biology, economics, computer science, linguistics, ecology, …) — and, crucially,
for **telling the real ones apart from seductive analogies**.

The goal is not to collect metaphors. It is to build a vetted map where every
claimed correspondence is placed on an explicit ladder of rigor, backed by a
quantitative signature and, where possible, a shared mechanism.

## The core question

When two domains seem to "obey the same law," which of these is actually true?

1. They share only a **word** (metaphor).
2. They share a **relational structure** (analogy).
3. They share a **mathematical form** — the same equation or distribution.
4. They share a **generative mechanism** — the same process produces the pattern.
5. They belong to the same **universality class** — a rigorous argument proves a
   whole family of microscopically different systems *must* behave alike.

Most cross-domain claims in popular writing live at levels 1–2 while being sold
as levels 4–5. This repo exists to do the demotion/promotion work honestly. The
ladder is defined in [`METHODOLOGY.md`](./METHODOLOGY.md).

## How the repository is organized

| Path | What lives there |
|------|------------------|
| [`METHODOLOGY.md`](./METHODOLOGY.md) | The correspondence ladder, evidence standards, anti-patterns, and the expansion⇄restraint rhythm. Read this first. |
| [`PREDICTION-FIELD.md`](./PREDICTION-FIELD.md) | The organizing frame: the environment we map *is* a prediction field; invariants are its measurement-invariant structure. |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | Conventions for adding or revising an invariant or a domain. How "we" work. |
| [`invariants/`](./invariants/) | One file per candidate invariant. [`invariants/README.md`](./invariants/README.md) is the master catalog. |
| [`domains/`](./domains/) | The invariant × domain cross-reference matrix — the actual "map." |
| [`questions/`](./questions/) | The agenda in two tiers: [`OPEN-QUESTIONS.md`](./questions/OPEN-QUESTIONS.md) (rigorous) and [`SPECULATIVE.md`](./questions/SPECULATIVE.md) (AI-native leaps, tagged & falsifiable). |
| [`experiments/`](./experiments/) | Runnable tests of specific questions. First: [`S3-fisher-geometry`](./experiments/S3-fisher-geometry/). |
| [`research-log/`](./research-log/) | Dated entries recording what we investigated, decided, and changed. |

## How to navigate

- Want the **big-picture map**? → [`domains/README.md`](./domains/README.md)
- Want the **list of candidates and their status**? → [`invariants/README.md`](./invariants/README.md)
- Want to know **what to work on next**? → [`questions/OPEN-QUESTIONS.md`](./questions/OPEN-QUESTIONS.md)
- Want to **add something**? → [`CONTRIBUTING.md`](./CONTRIBUTING.md) and copy [`invariants/_TEMPLATE.md`](./invariants/_TEMPLATE.md)

## Status

Seeded 2026-07-19 with an initial taxonomy of candidate invariants and an
open-questions agenda. Everything here is provisional; contested and retired
candidates are kept, not deleted, because knowing *why* a tempting
correspondence fails is part of the map.
