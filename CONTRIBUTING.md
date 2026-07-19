# Contributing / working conventions

This is how we add to and revise the map. It applies whether the contributor is
a human or an agent working self-directed.

## Adding a new candidate invariant

1. Copy [`invariants/_TEMPLATE.md`](./invariants/_TEMPLATE.md) to
   `invariants/<slug>.md` (kebab-case, e.g. `information-bottleneck.md`).
2. Fill in at least: the domain-neutral **statement**, two or more
   **manifestations by domain**, and a headline **correspondence level** with a
   one-line justification (see [`METHODOLOGY.md`](./METHODOLOGY.md)).
3. Add a row to the catalog table in [`invariants/README.md`](./invariants/README.md).
4. Update the cross-reference matrix in [`domains/README.md`](./domains/README.md).
5. Add a dated note in [`research-log/`](./research-log/) describing what you did
   and why the level is what it is.

## Revising an existing invariant

- Never silently promote a level. Promotion requires the corresponding evidence
  in the entry (quantitative match for L2, named mechanism for L3, a rigorous
  universality argument for L4).
- Demotions are first-class results. If a "famous" invariant only clears L1,
  set its status to `retired` and record *why* — do not delete it.
- When you change a level or status, log it.

## Style rules

- **Show the number.** Prefer "degree distribution P(k) ∝ k^−γ with γ ≈ 2.1 for
  the web" over "follows a power law."
- **Name the mechanism or say you can't.** "Preferential attachment" is a
  mechanism; "self-organization" usually isn't.
- **Cite where it breaks.** Every entry should have a boundary-conditions section
  that is not empty.
- **Distinguish convergence from identity.** Same pattern by different mechanism
  ≠ same mechanism. Label it.
- **Keep references minimal but real.** Author-year is enough; this is a working
  map, not a journal.

## Git conventions

- Work on the research branch; keep commits scoped to one invariant or one
  structural change where practical.
- Commit messages: `<area>: <what changed>` — e.g.
  `invariants: promote diffusion to L3 (shared Markov generator)`.

## What we do *not* do here (for now)

- No unattended/scheduled automation that expands the map on its own. Additions
  are deliberate and reviewed. (This is a scope choice, not a technical limit —
  revisit explicitly if we ever want it.)
