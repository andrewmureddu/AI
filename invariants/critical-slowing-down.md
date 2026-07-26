# Critical slowing down & early-warning signals

> **One-line claim:** Rising autocorrelation and variance as a system nears a
> tipping point is an established early-warning signal in ecology — and may be a
> domain-neutral predictor of *any* impending transition, including computational.
> **Headline correspondence level:** L3–L4 candidate (a real physics phenomenon;
> reach is the open part). *(seed — speculative)*
> **Status:** seed
> **Floor:** **3** (Φ-singular) — tested ([S7](../experiments/S7-critical-slowing/)): the Hessian going soft, i.e. the approach to the singular set

## Statement

Near a bifurcation/critical point the dominant eigenvalue → 0, so perturbations
relax ever more slowly: lag-1 autocorrelation → 1 and variance diverges.
Domain-neutral object: these leading-indicator statistics as transition precursors.

## Manifestations by domain (seed)

- Physics: critical slowing down at continuous transitions. anchor.
- Ecology/climate: early-warning signals before regime shifts (Scheffer). L3.
- Neuroscience: rising autocorrelation before epileptic seizures. L3.
- Finance: variance/autocorrelation build-up before crashes (contested). L2.
- CS: critical slowing down = the hardness peak at the SAT transition (S6). L3.

## Boundary found (2026-07-26) — τ·λ = 1 is a *single-basin* law

[S7](../experiments/S7-critical-slowing/) established τ·λ_min = 0.94±0.13 across
saddle-node, mean-field Ising and GD at the MP edge. All three legs are
single-basin, and [P-A](../experiments/PA-spectral-gap/) found where that matters:
in a double well the spectral gap falls **3540×** while the local potential
curvature U″(±1) *rises* **6×**, so the product τ·λ_min runs from 3.5e1 to 7.5e5
instead of staying at 1. Where relaxation is **barrier crossing** rather than
relaxation within a basin, the local curvature is the wrong object; the law is
restored by taking λ from the trajectory free energy (Λ''·gap stays O(1),
converging to 2). So: τ·λ = 1 holds where the slow mode *is* a local curvature.

## Why it's here / to develop

Speculative question **S7**. Sharpest test: apply the same statistics to ML
training-loss curves before collapse/grokking. Falsifier: a known tipping point
with no rise in autocorrelation/variance. Cross-links
`criticality-phase-transitions.md`. Refs: Scheffer et al. 2009; Wissel 1984.
