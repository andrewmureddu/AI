# Cross-Domain Invariants

A research repository for **mapping cross-domain invariants** — the patterns,
structures, and laws that recur across otherwise-unrelated fields (physics,
biology, economics, computer science, linguistics, ecology, …) — and, crucially,
for **telling the real ones apart from seductive analogies**.

The goal is not to collect metaphors. It is to build a vetted map where every
claimed correspondence is placed on an explicit ladder of rigor, backed by a
quantitative signature and, where possible, a shared mechanism.

## Two operations

The repo runs two distinct operations, and they have separate registers because
they fail in different ways.

- **Recognition** — take a law already known in field A and ask whether the thing
  that resembles it in field B is the same object. Everything through
  [`SPECULATIVE.md`](./questions/SPECULATIVE.md) is this. Its ceiling is the union
  of the textbooks; its failure mode is universality inflation.
- **Discovery** — find a law that is in nobody's textbook, usually by explaining a
  number our own experiments produced and never accounted for. Register:
  [`UNKNOWN-LAWS.md`](./questions/UNKNOWN-LAWS.md), graded on its own
  [novelty ladder](./questions/UNKNOWN-LAWS.md#2-the-novelty-ladder) (N0
  restatement → N3 new object) *in addition to* the rigor ladder. Its failure
  modes are rediscovery and tautology-by-construction, so every candidate carries
  a prior-art note written before the work and an explicit split between the
  predictions that are analytic identities and the ones that can come out wrong.

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
| [`SYNTHESIS.md`](./SYNTHESIS.md) | **State of the map in one read** — the ledger of what has teeth, the through-line, and the frontier. Start here for the big picture. |
| [`METHODOLOGY.md`](./METHODOLOGY.md) | The correspondence ladder, evidence standards, anti-patterns, and the expansion⇄restraint rhythm. Read this first. |
| [`PREDICTION-FIELD.md`](./PREDICTION-FIELD.md) | The organizing frame: the environment we map *is* a prediction field; invariants are its measurement-invariant structure. |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | Conventions for adding or revising an invariant or a domain. How "we" work. |
| [`invariants/`](./invariants/) | One file per candidate invariant. [`invariants/README.md`](./invariants/README.md) is the master catalog; [`FLOORS.md`](./invariants/FLOORS.md) sorts it by floor and [`CHARTS.md`](./invariants/CHARTS.md) tags it by chart. |
| [`domains/`](./domains/) | The invariant × domain cross-reference matrix — the actual "map." |
| [`questions/`](./questions/) | The agenda in four registers: [`OPEN-QUESTIONS.md`](./questions/OPEN-QUESTIONS.md) (rigorous), [`SPECULATIVE.md`](./questions/SPECULATIVE.md) (AI-native leaps, tagged & falsifiable), [`L3-MECHANISMS.md`](./questions/L3-MECHANISMS.md) (candidate shared *mechanisms*, each with a convergence discriminator), and [`UNKNOWN-LAWS.md`](./questions/UNKNOWN-LAWS.md) (**discovery** — candidate laws nobody has stated, on a separate novelty ladder). |
| [`experiments/`](./experiments/) | Runnable (numerical) tests of specific questions. First: [`S3-fisher-geometry`](./experiments/S3-fisher-geometry/). |
| [`derivations/`](./derivations/) | Analytical tests — pen-and-paper restraint. First: [`S1-universal-update`](./derivations/S1-universal-update.md). |
| [`research-log/`](./research-log/) | Dated entries recording what we investigated, decided, and changed. |
| [`paper/`](./paper/) | Long-form write-ups that assemble several results into one argument, with their own methods, statistics and limitations. A paper may **re-analyze and correct** its sources. First: [`transfer-cliff.md`](./paper/transfer-cliff.md) — what makes a correspondence transfer. |
| [`essays/`](./essays/) | Philosophy essays — the questions the ledger format can't hold (what an invariant *is*, why one object keeps recurring, what the method itself is). Grounded in the results, but explicitly not entries in the map. |

## How to navigate

- Want the **big-picture map**? → [`domains/README.md`](./domains/README.md)
- Want the **list of candidates and their status**? → [`invariants/README.md`](./invariants/README.md)
- Want to know **what to work on next**? → [`questions/OPEN-QUESTIONS.md`](./questions/OPEN-QUESTIONS.md)
- Want the **unknown-law hunt**? → [`questions/UNKNOWN-LAWS.md`](./questions/UNKNOWN-LAWS.md)
- Want to **add something**? → [`CONTRIBUTING.md`](./CONTRIBUTING.md) and copy [`invariants/_TEMPLATE.md`](./invariants/_TEMPLATE.md)

## Status

Seeded 2026-07-19 with an initial taxonomy of candidate invariants and an
open-questions agenda. Everything here is provisional; contested and retired
candidates are kept, not deleted, because knowing *why* a tempting
correspondence fails is part of the map.
