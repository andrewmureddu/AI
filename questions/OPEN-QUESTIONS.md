# Open questions — the research agenda

Concrete, falsifiable questions, roughly prioritized. Each should resolve to a
promotion, a demotion, or a sharper boundary condition on some invariant. When you
work one, record the outcome in [`../research-log/`](../research-log/) and update
the relevant entry.

Priority key: **P0** high-value & tractable · **P1** high-value, harder ·
**P2** worthwhile, open-ended.

---

### Q1 (P0) — Do our claimed power laws survive a proper model comparison?
For each power-law instance in [`power-laws.md`](../invariants/power-laws.md), run
the Clauset–Shalizi–Newman procedure (MLE exponent + goodness-of-fit + likelihood
ratio vs. lognormal / stretched-exponential). **Outcome:** demote any that don't
clear it; keep only the survivors as L2+. This is the single highest-leverage
cleanup — power laws are the most over-claimed invariant.

### Q2 (P1) — Is self-organized criticality one universality class or several?
Sandpiles, neuronal avalanches, earthquakes, forest fires all report avalanche
power laws. Do their exponents (size τ, duration, and the scaling *function*)
collapse onto one class, or are these convergent-but-distinct mechanisms?
**Outcome:** decides whether SOC is an L4 cross-domain invariant or a bundle of L2
look-alikes. See [`criticality-phase-transitions.md`](../invariants/criticality-phase-transitions.md).

### Q3 (P0) — Where does MaxEnt/thermo↔information *predict* vs. *re-describe*?
Build two explicit lists for [`entropy-information.md`](../invariants/entropy-information.md):
(a) cases where MaxEnt derives a distribution later confirmed (Boltzmann, Gaussian
under variance constraint, Landauer cost); (b) cases where "entropy" is a borrowed
formula with no new prediction (ecological indices, "social entropy"). **Outcome:**
a crisp L3-vs-L2 boundary for the whole entropy family.

### Q4 (P1) — Are ML neural scaling laws a criticality/universality phenomenon?
Loss ∝ compute^(−α) with small, seemingly universal exponents. Is this (i) a
statistical-physics critical phenomenon (L4-style universality), (ii) an
approximation-theoretic / data-manifold-dimension effect, or (iii) coincidental
L2 power-law shape? **Outcome:** places neural scaling on the ladder and connects
[`scaling-allometry.md`](../invariants/scaling-allometry.md) ↔
[`criticality-phase-transitions.md`](../invariants/criticality-phase-transitions.md).

### Q5 (P2) — Are there genuine symmetry→conservation pairs outside physics?
Is the "gauge theory of economics" (Malaney–Weinstein) an L2 formalism, or does it
yield a *testable* conserved current? Do Markov-process Noether theorems (Baez–Fong)
give non-trivial conserved quantities in biology/CS? **Outcome:** decides whether
[`conservation-noether.md`](../invariants/conservation-noether.md) has any L3+ reach
beyond inherited physics.

### Q6 (P1) — Urban scaling vs. biological allometry: shared mechanism or shared shape?
Biological metabolism scales as M^(3/4); urban infrastructure as N^~0.85,
socioeconomic output as N^~1.15. Does the West–Brown–Enquist fractal-transport
mechanism actually apply to cities (→ L3), or do they merely share power-law form
with unrelated mechanisms (→ L2)? Also test the standing critique that even the
biological 3/4 exponent isn't universal. See
[`scaling-allometry.md`](../invariants/scaling-allometry.md).

### Q7 (P2) — Is "replicator dynamics ≡ multiplicative-weights ≡ Bayesian update" a real L3 identity?
Formalize the claim that evolutionary replicator dynamics, exponential-weights /
multiplicative-weights learning, and (a form of) Bayesian updating are the *same*
update rule. If it holds, it's one of the cleanest L3 unifications in the catalog
(biology ↔ ML ↔ inference). See
[`selection-replicator.md`](../invariants/selection-replicator.md).

### Q8 (P2) — Does the Legendre transform genuinely unify thermodynamics and convex optimization?
Thermodynamic potentials and convex conjugates are related by the *same* Legendre
transform. Is this an L3 structural identity that transfers technique (e.g., duality
gaps ↔ phase coexistence), or a superficial L2 coincidence? See
[`duality.md`](../invariants/duality.md).

---

## Method reminders for working a question

- State the level *before* and *after*; a question that doesn't move a level or a
  boundary condition wasn't sharp enough.
- Prefer a quantitative test (exponents, data collapse, model comparison) over a
  verbal argument.
- Convergence (same pattern, different mechanism) is a valid and publishable
  answer — just label it as such, don't inflate it to L3/L4.
