# S5 — is there only one threshold? (result)

**Question ([S5](../../questions/SPECULATIVE.md), Cluster C):** are Shannon's
channel capacity, Eigen's error catastrophe, and the quantum fault-tolerance
threshold *one* redundancy-vs-noise transition? **Stated falsifier:** the
redundancy-vs-(threshold − p) scaling exponents differ across the three.

**Status: falsifier fires — the exponents span 1.00 to 3.17. What replaces the
stone is sharper than the stone: the exponent is not a domain label but a
*degeneracy order*, and it is predicted by how the prediction field goes
singular at the threshold.**

Run it: `python3 run.py` (pure numpy, deterministic, ~5 min). Predictions were
registered in [`predictions.json`](./predictions.json) before the run.

## Design

One resource definition, applied identically in every leg:

```
   N(p) = minimum physical resource per protected bit needed to keep the
          information recoverable indefinitely, at noise level p

   N(p) ~ (p_c - p)^(-alpha)
```

- **A — coding theory** (4 channels). N = 1/C, with C computed by direct
  maximization of I(X;Y) over the input distribution (formulas used only as a
  cross-check; max relative error vs. closed form ≤ 3.8e-5).
- **B — biology.** Eigen's quasispecies, *exact* deterministic dynamics in the
  Hamming-class representation (exact for a single-peak landscape, since fitness
  depends only on the class). **B1** bare model. **B2** with a decoder: majority
  repair across r copies per functional site, r_min found from the same exact
  dynamics.
- **C — quantum fault tolerance.** Concatenated distance-(2t+1) codes: resource
  n₀^L per logical qubit against the level-L error recursion.

## Results

### The falsifier fires, cleanly

| Leg | System | α |
|-----|--------|--:|
| A | BSC (p→½) | **2.0000** |
| A | binary-input AWGN (a→0) | **1.9985** |
| B2 | quasispecies + majority repair (μ→½) | **2.035** (2.003 on the smallest half) |
| A | BEC (e→1) | **1.0000** |
| A | Z-channel (q→1) | **1.0000** |
| C | concatenated, n₀=23, t=3 | **2.2621** |
| C | concatenated, n₀=5, t=1 | **2.3223** |
| C | concatenated, n₀=7, t=1 | **2.8078** |
| C | concatenated, n₀=9, t=1 | **3.1704** |

Spread 2.17. There is no single exponent, and the variation is **not** by
domain: coding theory alone supplies both 1.00 and 2.00, and fault tolerance
supplies four different values depending only on which code you concatenate.

### Three mechanism classes, each with its exponent derived and measured

- **Type M — smooth merge (α = 2).** The two conditional output laws converge to
  each other. The first-order term of any divergence between them cancels
  identically (both are normalized), so the leading term is the **Fisher
  quadratic form** — quadratic is *forced*, not fitted. Members: BSC, BI-AWGN,
  and majority-repair quasispecies. Max deviation from 2: **0.035**.
  Bonus, unregistered: the type-M channels share the *constant* too —
  C/χ²_sym = **0.1803 = 1/(8 ln 2)** for both BSC and BI-AWGN.
- **Type S — support mismatch (α = 1).** The laws stay distinguishable where
  they overlap; what vanishes is the probability of the informative event. Mass
  is a *linear* functional, so the order is 1. Members: BEC, Z-channel. Max
  deviation from 1: **0.0000**.
- **Type R — decoder RG fixed point (α = ln n₀ / ln(t+1)).** The threshold is
  not a capacity zero at all: it is the unstable fixed point of the recursion
  p → A·p^(t+1). Linearizing in u = ln(p_th/p) gives eigenvalue (t+1) while
  resources multiply by n₀ per level, so α is a ratio of logs — an RG
  eigenvalue, i.e. a property of the *scheme*, not the domain. Verified against
  log_{t+1}(n₀) for four codes to **1.55e-4** relative.

### The discriminator: α = the order of vanishing of χ²_sym

The registered diagnostic ("infinite χ² ⇒ α = 1") turned out to be
**direction-dependent and therefore ill-posed**, which the Z-channel exposed:
χ²(P₀‖P₁) = 1e-4 (finite) but χ²(P₁‖P₀) = ∞. The registered *prediction* for
the Z-channel (α = 1, against the naive merge reading — its laws do merge, total
variation = 1e-4) was correct; the stated rule was not usable as written.

Replaced by a quantitative rule and then tested: **α equals the order of
vanishing of the symmetrized χ² between the two conditional laws.** Across all
four channels, |α − order(χ²_sym)| ≤ **0.0015**, and C/χ²_sym is constant in the
gap for each channel. So the exponent is readable off the *local geometry of the
two laws at the threshold* — no capacity computation needed.

### Eigen's threshold is the uncoded corner of Shannon's, and the gap is a constant

- **B1, bare quasispecies.** The classic condition is recovered from the exact
  dynamics: the master frequency vanishes transcritically at L·μ_c = ln σ, with
  relative error 0.0093 → 0.0023 as L: 50 → 400 (falling like 1/L), and matching
  the finite-L root 1 − σ^(−1/L) to 1.6e-2 → 3.2e-3. Tested at σ = 2 and 10.
- **Structural finding: the bare model has no redundancy knob.** Every site is
  functional (N per protected bit ≡ 1), so "required redundancy vs. gap" is
  *malformed* for this leg — and the threshold sits at ln σ/L, which moves with
  genome length rather than at a fixed p_c. The error catastrophe is the
  **zero-redundancy corner** of the coding picture, not a separate law.
- **B2, add a decoder and the threshold becomes Shannon's.** With majority repair
  the threshold moves from ln σ/L to μ = ½ (nothing rescues μ = ½: r_min is
  unbounded there), and r_min ∝ δ^(−2) with r_min·δ² = **1.32** constant to 0.5%
  over δ ∈ [0.0075, 0.063] (an 8× range of gaps), drifting only to 1.19 at
  δ = 0.25 — within 10% over the full 33× range, the expected log correction from
  the binomial prefactor. Robust to a 100× change in the
  survival criterion (α = 2.038 / 2.047 at master-frequency 0.001 / 0.1).
- **The coding gap is a constant, not an exponent.** r_min / (1/C_BSC) ≈ **3.8**,
  flat in δ. A repetition code is the crudest possible code and an optimal code
  is the best possible one; near the threshold they differ by a *factor*, because
  both are governed by the same Chernoff/KL quadratic. **Exponent = geometry;
  code quality = constant.**

## Verdict

- S5's "one threshold" reading: **retired to L1.** Three exponents, and the
  variation is within-domain, not across-domain.
- S5's replacement: **L2–L3 on-model, with a mechanism.** The thresholds are one
  *kind* of object — a place where the prediction field stops supporting
  prediction — differentiated by the *order* of the degeneracy: 2 for a smooth
  metric merge, 1 for support loss, ln n₀/ln(t+1) for a decoder's RG fixed
  point.
- **Fifth arrival at the ∇²Φ singular set**, and the first that measures its
  *order*. S3 found divergence, [S25](../../derivations/S27-control-split.md)
  found null spaces, the [symmetry sector](../../derivations/symmetry-sector.md)
  found Goldstone flat directions, [S7](../S7-critical-slowing/) found the slow
  mode. Here the capacity threshold is where the induced Fisher information
  about the message develops a **null direction**, and α counts how fast it
  vanishes. Both of S25's named singular faces show up — *null Fisher
  directions* (type M) and *supports* (type S) — and they carry **different
  exponents**, which is why the stone's single-exponent premise had to fail.
- The tower's floors are doing visible work: type M and S are Φ-singular facts,
  while type R is not a Φ fact at all — it is a property of a decoder's flow.
  A threshold can be an RG fixed point of a *scheme* rather than a singularity of
  the field, and the exponent tells you which you are looking at.

## Boundaries

- **Leg C is scheme-specific by construction.** Constant-overhead fault
  tolerance with good LDPC codes achieves O(1) overhead below threshold
  (Gottesman 2013), so α = ln n₀/ln(t+1) describes *concatenation*, not fault
  tolerance as such. This strengthens the reading (the exponent tracks the
  scheme) but means leg C is not a statement about the quantum capacity.
- Leg C is arithmetic on the standard recursion, not a simulation of a noisy
  circuit; A = 1/p_th is taken as given rather than counted from a gate set.
- Leg B2's decoder is a repetition code with majority repair — biologically
  motivated (gene conversion / polyploid repair) but the crudest code there is.
  k = 64 functional sites, single-peak landscape, deterministic (infinite
  population) dynamics: no drift, no epistasis, no recombination.
- μ > ½ is outside the quasispecies model (deterministic inversion is signal,
  not noise); the class dynamics degenerates to a 2-cycle there and the run
  guards against it rather than interpreting it.
- Type M's "α = 2 is forced" argument is a local-expansion argument. A family
  whose Fisher form *also* vanishes at the threshold would give α = 4; no such
  case is exhibited here, so the taxonomy is verified at orders 1 and 2 only.
- All four channels are binary-input and memoryless.
