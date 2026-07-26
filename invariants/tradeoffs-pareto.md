# Trade-offs & Pareto frontiers

> **One-line claim:** Systems that can't optimize everything at once are pushed to a
> Pareto frontier; the same accuracy/cost, robustness/efficiency, and
> exploration/exploitation tensions recur everywhere.
> **Headline correspondence level:** L1–L2; often a consequence of constrained
> optimization rather than an independent law. *(provisional — seed)*
> **Status:** seed
> **Floor:** **2** (Φ-regular), partial — a frontier with a real exchange rate *is* a Legendre transform; without one it is not an invariant. ▸facet

## Statement

Given competing objectives that cannot be jointly maximized, achievable states are
bounded by a Pareto frontier; improvement in one objective costs another.
Domain-neutral object: the Pareto front of a constrained multi-objective problem,
and specific named trade-offs (bias–variance, speed–accuracy, robustness–fragility).

## Manifestations by domain (seed)

- ML: bias–variance; exploration–exploitation; no-free-lunch — L2.
- Biology: r/K selection; metabolic trade-offs; robustness–evolvability — L2.
- Engineering/economics: cost–performance; efficiency–resilience — L2.
- Control/perception: speed–accuracy trade-off — L2.

## To develop

Ask whether these are one invariant or many instances of "constrained optimization
has a frontier" (in which case the real invariant is `optimization-variational.md`).
Where a trade-off has a *quantitative* exchange rate that recurs (e.g., rate–
distortion), that's stronger. Cross-link `optimization-variational.md`.
