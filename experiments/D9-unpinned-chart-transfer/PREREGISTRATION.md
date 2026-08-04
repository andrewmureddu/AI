# D9 pre-registration — written before any measurement

Works [D9](../../questions/UNKNOWN-LAWS.md), the half
[D3](../D3-ladder-as-quotient/) could not reach. D3 falsified "the ladder is a
chart-invariance count" on a harness whose chart is *n*, a **count**, which
aggregation composes additively — so G_pow was never available there, the chart was
pinned, and by [D2](../../derivations/D2-gauge-of-the-tower.md)'s rule (i) the bare
magnitudes were facts. That refutes D3 **as stated** and says nothing about the
regime the whole chart apparatus was built for.

**The question: on an unpinned chart — a genuine distance-to-threshold, where
G_pow *is* available — does chart-invariance predict transfer?**

Per [`UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6: prior-art note,
identity/risk split, then numbers.

---

## 0. Prior-art note (written first)

**Old.** That the stationary density of an overdamped gradient system is
∝ exp(−Φ/D), that exp(−a|y|^p/pD) is a generalized-Gaussian whose standardized
shape depends on p alone, and that catastrophe germs A_{p−1} classify
one-dimensional degeneracies, are all classical. Nothing about the *models* is new.

**Also old, and it is this repo's:** [D1](../D1-chart-invariance/) established that
bare exponents near a floor-3 singularity are chart artifacts and that *p*
classifies; [D7](../D7-residue-projective/) established that the chart-free content
is the log-slope vector modulo the diagonal. **D9 does not re-derive any of that and
must not be read as evidence for it.**

**What is new here is a comparison, not a law.** D3 measured, on a pinned chart,
that the residue predicts nothing and the bare exponent predicts everything. D9 asks
whether the *same two readouts, measured the same way*, swap roles when the chart is
unpinned. A single harness cannot establish that; the claim is the **contrast
between two harnesses**, with the pinning test saying in advance which regime each
one is in. If that contrast holds it is N1–N2 at best: the parts are D3's and D7's,
the composition is what would be new.

**Prior expectation, recorded:** this is the outcome D3's own analysis predicts, so
it is the *comfortable* result and deserves more suspicion than a surprise would.
§2 registers what would make it uninteresting even if the numbers come out right.

---

## 1. Design — deliberately parallel to the harness D3 used

Hold the surface phenomenon fixed — **"an observable's fluctuations grow as a
control approaches a threshold"** — learn the law in a reference domain A, and vary
how deeply it applies in B. Four rungs, matched to
[ladder-vs-transfer](../ladder-vs-transfer/)'s:

| rung | domain B | why that rung |
|:--:|---|---|
| **L4** | same degeneracy order p = 4, **completely different** potential coefficients, and its own chart | same class by theorem, nothing else shared |
| **L3** | p = 4, same mechanism, mildly different coefficients, its own chart | same mechanism |
| **L2** | **p = 6** — a different degeneracy class — same "softening" surface, its own chart | wrong universality class |
| **L1** | no singularity at all: λ does not vanish | shares only the word |

**Every domain supplies its own coordinate**, which is the whole point and the thing
D3's harness could not vary: domain B reports its control as δ with ε = δ^c for a
domain-specific c. That is exactly G_pow, and it is available here because a
distance-to-threshold has no canonical scale.

**The two readouts, measured from different quantities so the test is not circular:**

- **Transfer** — from the *distribution shape*. A's law is the standardized quantile
  curve of its fluctuations at the singularity; transfer is how well B's curve
  matches it, by the same robust-shape 1-D Wasserstein metric the existing harness
  uses.
- **Residue** — from the *scaling exponents*, the projective class of the log-slope
  vector, exactly as in D3.

Shape and residue are both functions of p in this family, as shape and 1/α were both
functions of the basin in D3's. **That structure is not the finding.** The finding is
which of the two chart-dependent readouts survives each domain supplying its own
coordinate.

## 2. Identity vs. risk — the required disclosure

**Declared, not evidence:**

- **P4 — re-charting invariance of the residue.** D7 established it and D1 measured
  it. Included only to confirm the estimator behaves here; a pass is not evidence
  for anything.
- **The fact that shape and residue both track p.** Structural in this family, as
  §1 says. Registered as *not* a result so it cannot be presented as one later.

**Genuinely at risk:**

- **P1 — the residue distances.** Same-p domains must come out close *despite*
  different coefficients and different charts, and the p = 6 domain far. Finite-ε
  corrections could blur it, and the higher-order coefficients differ by up to 4×.
- **P2 — THE LEG. Transfer, and whether the residue orders it stably.** D3's residue
  did produce an ordering in its main run, which dissolved when re-sampled. **The
  registered bar here is therefore stability, not ordering**: the ordering must hold
  across every sampling setting tried, or this is D3 again.
- **P3 — the contrast, and it is the claim.** The bare exponent must *fail* here,
  where it succeeded in D3.

**What would make this uninteresting even if the numbers are right** (registered per
§0): if the bare exponent fails only because I chose the charts to make it fail.
That is why P3 is stated as a *quantitative contrast with D3's measured numbers*
rather than as "the bare exponent does badly", and why the charts are set once, in
§3, and not tuned.

## 3. Models — fixed here, not tuned

Symmetric potential for the shape, one-sided with a control for the exponents:

```
    Phi(y) = a_p |y|^p / p  +  c3 |y|^{p+1}  +  c4 |y|^{p+2}      [shape, eps = 0]
    Phi(y) = a_p  y^p  / p  +  c3  y^{p+1}  +  c4  y^{p+2} - eps*y  [exponents]
```

| domain | p | a_p | c3 | c4 | chart exponent c (ε = δ^c) |
|---|:--:|:--:|:--:|:--:|:--:|
| A (reference) | 4 | 1.0 | 0.20 | 0.05 | 1.0 |
| L4 | 4 | 3.0 | −0.40 | 0.90 | **2.0** |
| L3 | 4 | 1.5 | 0.10 | 0.02 | **0.6** |
| L2 | 6 | 1.0 | 0.20 | 0.05 | **1.3** |
| L1 | — | quadratic well, λ bounded away from 0 | | | 1.0 |

Observables (n = 5): y\*, λ = Φ″(y\*), Var, ΔΦ, |Φ‴|. Densities and moments by
Gauss–Legendre quadrature of the exact density — no sampling anywhere, so "sampling
setting" below means the ε-window and the quadrature resolution.

## 4. Registered predictions

**P1 — residue distances (AT RISK).** Subspace sine between each domain's log-slope
vector and A's, computed as in D3 (never via arccos):

| pair | predicted | tolerance |
|---|:--:|:--:|
| A–L4 (same p, different coefficients **and** chart) | **< 0.05** | — |
| A–L3 (same p) | **< 0.05** | — |
| A–L2 (p = 6) | **≈ 0.214** | ±0.06, and **> 0.15** |
| A–L1 | **rank 0** — no ray | — |

The 0.214 is computed in advance from the asymptotic slope vectors
(1, 2, −2, 4, 1) for p = 4 and (1, 4, −4, 6, 3) for p = 6, normalized and compared.

**P2 — transfer, and stability (AT RISK; the leg).** Shape-transfer skill by the
harness's metric, with a Laplace reference shape:

- **L4 and L3 above 0.80**; **L2 and L1 below 0.40**.
- **The residue distance orders transfer** — A–L4 and A–L3 both smaller than A–L2 —
  **and that ordering is unchanged across all three ε-windows and both quadrature
  resolutions tried.** If the ordering moves under re-sampling the way D3's did,
  this leg fails regardless of the central values.

**P3 — the contrast with D3 (AT RISK; the claim).** Within the same-class group:

| | D3's harness (pinned chart) | D9 (unpinned chart), predicted |
|---|:--:|:--:|
| bare exponent, same-class domains | 0.4960 / 0.5013 / 0.5023 — spread **0.6%** | k differs by ≥ **2×** across A / L3 / L4 |
| does the bare exponent order transfer? | **yes**, 30× gap at the boundary | **no** |
| does the residue order transfer? | **no**, ordering scrambles | **yes**, stably |

Predicted bare k = (p−2)/(p−1) × c: **0.667** (A), **1.333** (L4), **0.400** (L3),
so a 3.3× spread among domains that all transfer.

**P4 — re-charting invariance (DECLARED, not evidence).** Under δ ↦ δ^a for
a ∈ {0.5, 1, 2, 3}, each domain's residue is unchanged to **< 0.01** while its bare
k moves by the full factor a.

## 5. What would kill D9

- **P1 fails** — same-p domains are not close in residue, so the residue is not
  measuring the class and nothing downstream means anything.
- **P2's stability clause fails** — the ordering moves under re-sampling. Then this
  is D3 with a different potential and the contrast is not real.
- **P3 fails in the direction of the bare exponent working** — then the chart is
  effectively pinned here too, and the pinned/unpinned distinction does not do the
  work the conclusion needs.
- **The comfortable-result check:** if P3 holds only because the chart exponents c
  were chosen adversarially, the result is an artifact. The charts are fixed in §3
  above and will not be changed; if they are changed for any reason, the run is void
  and the change is logged.

## 6. Scope, registered

- **One family again** — one-dimensional gradient systems. D3 tested one family and
  this tests one other; the *contrast* between them is the claim, and two families
  is not many.
- **This does not resurrect D3 as stated.** The most it can establish is that the
  chart reading holds where G_pow is available and fails where the chart is pinned,
  which is a *delimitation*, not a rehabilitation. Registered so the write-up cannot
  quietly upgrade it.
- Tolerances are set from the asymptotic values computed in §4 plus the finite-ε
  correction size the coefficients generate, per the budget discipline D7 and D8
  both failed and D3 got right. Estimator resolution pre-checked: subspace sines
  throughout, never arccos.
- **Essential singularities and marginal directions remain outside**, unchanged.
