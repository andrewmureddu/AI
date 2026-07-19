# The map: invariant × domain cross-reference

This is the actual "map" — which candidate invariants surface in which domains, and
at what correspondence level *within that domain*. Rows are invariants, columns are
domains. A cell shows the best-supported level (see
[`../METHODOLOGY.md`](../METHODOLOGY.md)); blank = not (yet) claimed there.

Levels: **L4** universality · **L3** shared mechanism · **L2** shared math ·
**L1** structural analogy · *blank* = none/unexamined. Parentheses mark
contested/soft claims.

## Matrix

| Invariant \ Domain | Physics | Chemistry | Biology | Neuro | Economics | CS / ML | Ecology | Ling./Social |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| [Power laws](../invariants/power-laws.md) | L3 | | L3 | L3 | L2 | L3 | L2 | L2 |
| [Conservation/Noether](../invariants/conservation-noether.md) | **L4** | L3 | L3 | | (L1) | L3 | L3 | |
| [Entropy/information](../invariants/entropy-information.md) | **L4** | L3 | | (L2) | (L2) | L2 | L2 | |
| [Diffusion/random walk](../invariants/diffusion-random-walks.md) | **L4** | L3 | L3 | L2 | L3 | L3 | L2 | (L2) |
| [Criticality/universality](../invariants/criticality-phase-transitions.md) | **L4** | | (L3) | (L2) | (L1) | (L2) | | |
| [Feedback/control](../invariants/feedback-control.md) | L3 | L2 | L3 | L3 | L2 | L3 | L2 | (L1) |
| [Optimization/variational](../invariants/optimization-variational.md) | **L4** | L2 | (L1) | (L2) | L2 | L3 | | (L1) |
| [Networks/percolation](../invariants/networks-percolation.md) | L3 | L2 | L3 | L2 | L2 | L3 | L2 | L2 |
| [Scaling/allometry](../invariants/scaling-allometry.md) | L2 | | L3 | | L2 | L2 | L2 | |
| [Symmetry breaking](../invariants/symmetry-breaking.md) | **L4** | L3 | L2 | | | | | (L1) |
| [Fractals/self-similarity](../invariants/self-similarity-fractals.md) | L3 | L2 | L3 | L2 | L2 | L2 | L2 | |
| [Selection/replicator](../invariants/selection-replicator.md) | | L2 | **anchor** | | L3 | L3 | L2 | (L2) |
| [Emergence/renormalization](../invariants/emergence-renormalization.md) | **L4** | L3 | (L1) | (L1) | (L1) | (L2) | | (L1) |
| [Trade-offs/Pareto](../invariants/tradeoffs-pareto.md) | L2 | | L2 | L2 | L2 | L2 | L2 | |
| [Duality/conjugates](../invariants/duality.md) | L3 | L2 | | | L2 | L3 | | |
| [Information bottleneck](../invariants/information-bottleneck.md) | | | | L3 | | L2 | | (L2) |

*(Cell levels are seed estimates for the un-worked invariants; treat anything in
a `seed`-status entry as a hypothesis to be checked, not a finding.)*

## What the map is telling us (early reads)

- **Physics is the anchor column.** Most L4 cells are physics; the honest question
  for every other column is whether the invariant is *inherited* from physics
  (e.g., ecology's conservation is just physical conservation) or genuinely native.
- **The dense rows** — diffusion, networks, feedback, power laws — are the
  strongest cross-domain travelers. They also tend to be the ones with a *theorem*
  behind them (CLT, percolation transition).
- **The contested cells** (parentheses) cluster in neuro/economics/social columns
  for criticality, optimization, and emergence. That is exactly where
  "universality inflation" happens, and where the research value is highest.

## Per-domain notes

Add a `domains/<domain>.md` file when a domain accumulates enough
domain-specific caveats to warrant one (e.g., how "value" behaves in economics,
why biological scaling exponents are contested). None yet — seed stage.
