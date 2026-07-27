# D6 pre-registration — written before any measurement

Works [D6](../../questions/UNKNOWN-LAWS.md), the remainder
[D2](../../derivations/D2-gauge-of-the-tower.md) left open: floor 3's classifier
was established for **degeneracy-type** singularities, where Φ has a Taylor
expansion and the first non-vanishing anharmonic term defines *p*. Support-type
singularities (S5's type S) have no *p*. Are they a separate class, is p = ∞ the
right label, or is the classifier more general than D1 stated?

Per [`UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6: prior-art note,
identity/risk split, then numbers.

---

## 0. Prior-art note (written first)

**Old.** Generalized-Gaussian (exponential-power) densities exp(−c|y|^q) and their
moments are standard. That the LASSO's soft threshold becomes invisible once the
noise exceeds it is elementary and known in every form. Crossover scaling between
two competing terms in a potential is the same balancing argument as the Ginzburg
criterion, already flagged in [D1](../D1-chart-invariance/)'s prior-art note as
covering that experiment's formula. M/M/1's geometric stationary law is 1950s
queueing theory.

**Not covered.** The claim that these are **one classifier**: that the exponent
governing the crossover at *any* floor-3 singularity — degeneracy-type or
support-type — is a function of the **ratio** of the two leading exponents of Φ,
and that D1's *p* is the special case where smoothness pins the first of them to 2.
The cross-domain reading (a queue, a penalized estimator and a Landau potential
classified by one number) is the N2 claim; the scaling algebra is not.

**Nearest miss, recorded so it cannot be relabelled.** If the two-exponent form is
standard in the crossover-scaling or multicritical literature — which is plausible,
since competing-term crossovers are exactly what crossover exponents describe —
D6's formula is **N0–N1** and only the "one classifier across floor 3, and it is a
ratio" reading survives at N2.

---

## 1. The claim

Near a floor-3 singularity write the effective potential's two leading terms as

```
        Phi(y)  =  A |y|^q1  +  B |y|^q2  + (higher),     q1 < q2
```

with **A → 0** the control. Rescaling y = (D/A)^{1/q1}·ŷ gives
Φ/D = ŷ^{q1} + u·ŷ^{q2} with u = B·D^{q2/q1 − 1}·A^{−q2/q1}, so every shape
statistic depends on **u alone** and the crossover locus is

```
        A_c  ~  D^{(q2 - q1)/q2}   =   D^{1 - q1/q2}
```

**D1 is the case q1 = 2**, where smoothness forces a quadratic leading term:
(p−2)/p with q2 = p. **Support loss is the case q1 = 1** — a kink or a boundary
rather than a degeneracy — where D1's formula is not merely wrong but *undefined*,
since there is no quadratic term to expand.

**Observable.** Shape, not the rounding ratio D1 used: for a single-term
Φ = A|y|^q the standardized moments depend on q alone, independent of A and D. So
excess kurtosis reads q off directly, and it works for q = 1 (Laplace, +3.0000)
and q = 2 (Gaussian, 0.0000) alike, where D1's R = Var·λ/D needs a curvature λ
that a kink does not have. Limiting values, computed in advance from
Γ(5/q)Γ(1/q)/Γ(3/q)² − 3:

| q | 0.5 | 1 | 2 | 3 | 4 | 6 | 8 |
|---|---|---|---|---|---|---|---|
| excess kurtosis | +22.2000 | +3.0000 | 0.0000 | −0.5816 | −0.8116 | −1.0000 | −1.0766 |

A_c(D) is located where the measured kurtosis crosses the **midpoint** of its two
limiting values.

## 2. Identity vs. risk — the required disclosure

**Analytic identities. These cannot come out wrong; they are the functional form,
not evidence for it:**

- **A_c ~ D^{1−q1/q2} for the exact two-term model.** Forced by the u-rescaling
  above, exactly as D1's §4 declared for its own formula. The synthetic grid in P1
  verifies the algebra and the estimator; it is not evidence.
- The limiting kurtosis values in the table.

**Genuinely at risk:**

- **P2 — a real model with all orders and q1 = 1.** L1-penalized logistic
  regression: the smooth part carries y², y³, y⁴, … and the u-argument does not
  apply to it.
- **P3 — M/M/1, where the prediction is that no crossover exists at all.** A
  discrete state space could induce one; if it does, the "no second term ⇒ no
  crossover" reading fails.
- **P4 — the q2 → ∞ corner (finite buffer).** Predicts exponent 1; nothing
  guarantees the hard-wall limit is continuous in q2.
- **P5 — the ratio discriminator.** The structural claim, and the one that
  separates D6 from D1 rather than extending it.

---

## 3. Registered predictions

**P1 — the functional form (identity; estimator check).** Fitted crossover
exponents for the synthetic two-term models, each within **±0.04 absolute**:

| (q1, q2) | q1/q2 | predicted exponent |
|---|:--:|:--:|
| (2, 4) | 0.500 | **0.5000** |
| (1, 2) | 0.500 | **0.5000** |
| (2, 6) | 0.333 | **0.6667** |
| (1, 3) | 0.333 | **0.6667** |
| (1, 4) | 0.250 | **0.7500** |
| (0.5, 2) | 0.250 | **0.7500** |
| (2, 8) | 0.250 | **0.7500** |
| (3, 4) | 0.750 | **0.2500** |
| (1, 6) | 0.167 | **0.8333** |

**P2 — the ratio is the classifier, not either exponent (AT RISK, structural).**
Registered as the sharp separation from D1, and stated so it can fail:

- The three pairs (1,4), (0.5,2), (2,8) share **no** exponent value in common —
  q1 ∈ {1, 0.5, 2} and q2 ∈ {4, 2, 8} — yet share the ratio 0.25. Predict their
  measured crossover exponents agree with each other within **0.04**.
- (2,4) and (1,2) likewise, and (2,6) and (1,3) likewise.
- Meanwhile pairs sharing q2 but not the ratio — (2,4) vs (1,4), both q2 = 4 —
  must **differ** by at least 0.20.

**P3 — a real all-orders model with q1 = 1 (AT RISK).** L1-penalized logistic
regression on balanced data, Φ(β) = ℓ(β) + τ|β| with ℓ smooth and carrying every
order. Control A = τ, so q1 = 1, q2 = 2. Predict **τ_c ~ D^{0.500} within
±0.04**.

**P4 — M/M/1 has no crossover (AT RISK).** With an infinite buffer the stationary
law is geometric at every ρ, i.e. the q1 = 1 shape with **no second term**. Predict
the excess kurtosis of the scaled queue length stays at the exponential value
**6.0 ± 0.3** across ρ → 1 (spanning ≥3 decades in 1 − ρ) and that **no crossover
locus exists to fit**. This is the registered sense in which support-type
singularities are *not* p = ∞: they are q1 = 1 with q2 absent.

**P5 — the hard-wall corner (AT RISK).** M/M/1/K, finite buffer K, exact
distribution P(n) ∝ ρⁿ on 0..K. The wall is q2 → ∞, so the predicted exponent
(q2−q1)/q2 → **1**. With 1/K playing the role of D, predict the crossover locus
A_c ∝ K^{−1} with fitted exponent **1.00 ± 0.10**, where A = ln(1/ρ).

---

## 4. What would kill D6

- **P2 fails** — pairs with equal q1/q2 and different (q1, q2) give different
  exponents. Then the classifier is not the ratio and floor 3 needs more than one
  number per singularity.
- **P3 fails** — the formula governs two-term toys only, so it says nothing about
  real support-type singularities and D1's restriction to degeneracies stands.
- **P4 fails** (a crossover appears in M/M/1) — then "q2 absent" is not a coherent
  category and support loss may indeed be p = ∞ after all, which would *simplify*
  the answer and refute this framing.
- **P5 fails** — the hard-wall limit is not the q2 → ∞ limit, so boundaries are a
  separate class rather than a corner of the same one.

## 5. Scope, registered

- One-dimensional, additive noise, one control parameter — inherited from D1.
- **Essential singularities remain outside.** If Φ has no leading power at all
  (Φ ~ exp(−1/y)), no q1 exists and nothing here applies. That is the genuinely
  unclassified remainder after this experiment, and it is *narrower* than the
  remainder D2 left, which was all of support-type.
- The **logarithmic corner q1 → 0** — where exp(−Φ/D) becomes a power law, i.e.
  the catalog's heavy-tail entry — is a consequence of the formula that is
  **noted, not tested here**. Recorded so that a later claim to have predicted it
  cannot be backdated.
- P4 and P5 use exact stationary distributions, not simulation, so they test the
  claim and not a sampler.
