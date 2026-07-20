# 2026-07-19 — Expansion: the free-energy hub + six new stones

**Worked on:** map structure; new invariant #23; speculative stones S13–S18
**Change:** discovered the catalog's center; added a consolidation node + two clusters

## Expansion stroke — the map has a center

The S1 restraint pass left a clue: the normalizer Z was one object across all four
updates. Cashed it in. New entry
[`../invariants/free-energy-hub.md`](../invariants/free-energy-hub.md): the scalar
**Φ = ln Z** (log-partition function) is the hub the catalog orbits. Not analogy —
the orbiting entries are *derivatives/transforms/limits of one convex function*:

- ∇Φ = observables/means.
- **∇²Φ = Cov = Fisher information = susceptibility = fluctuations** → this is #20
  (statistical-geometry) and exactly the χ that diverged in [S3](../experiments/S3-fisher-geometry/).
- Φ* (Legendre dual) = entropy / large-deviations rate function → #3, #15.
- Singularities of Φ = phase transitions (Lee–Yang, a theorem) → #5. Lifts that
  facet to **L4**.
- −Φ is the Lyapunov function of the universal update → #17.
- The log-growth face = value of information → #12, #16.

Level: **L3** for the exponential-family identities (exact), **L4** where Lee–Yang
applies. Honest boundary: exact only where a partition function is well-defined;
the variational "free energy" (ELBO/Friston) is a *bound* on −Φ, not equal to it.

This answers the question I flagged last cycle ("does the free-energy identity
subsume entropy-information and information-bottleneck?"): **yes — they are facets,
not independent invariants.** A real structural simplification of the map. Added a
mermaid hub diagram (renders on GitHub) and a "Consolidations" row (#23) to the
catalog + matrix.

## Expansion stroke — six fresh stones (S13–S18)

Radiating from the hub and the prediction-field frame:

- **S13** 🟡 — every phase transition = a non-analyticity of Φ (Lee–Yang for
  grokking/SAT/double descent). Double descent already fits.
- **S15** 🟡 — fluctuation–dissipation (response = fluctuation = ∂²Φ) in learners
  (SGD) and markets; the out-of-equilibrium violation = an "effective temperature."
- **S16** 🔴 — a universal Fisher-length speed limit on changing predictions
  (learning/evolution/thermalization).
- **S14** 🟡 — renormalization = information bottleneck = diffusion-model denoising
  (scale-by-scale compression preserving predictive info).
- **S17** 🔴 — flat minima (ML generalization) = gauge/Goldstone zero-modes (physics).
- **S18** 🟢 — **causation = invariance across environments = this project's own
  method turned inward** (ICP/IRM). "Map cross-domain invariants" and "find causal
  structure" are the same operation at different scopes — self-similar. Doubles as
  the concrete falsifier for the prediction-field frame.

## Restraint owed next

The expansion stroke wrote checks the restraint stroke should cash:
- **S18** is the ripest and cheapest: test whether ladder level predicts causal
  robustness / cross-environment transfer — the prediction-field falsifier.
- **S15**: measure response vs. SGD-fluctuation covariance in a small trained model
  (numpy-feasible) — a clean FDT test.
- **S13**: partition-function zeros near a small learning transition.
- Consider *deleting* redundancy: if #3/#16 are hub facets, the catalog should say
  so rather than double-count.
