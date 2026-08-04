# D11 — the residue reconciled (result)

**Question ([D11](../../questions/UNKNOWN-LAWS.md)):** three independently
produced accounts of "what the tower's invariant residue is in general" —
[D7/D8](../D7-residue-projective/) (a projective ray / Grassmannian point),
[D10](../D10-composition-lens/) (the invariant content of the largest group a
composition law fails to pin), and
[D3-ladder-invariance](../D3-ladder-invariance/) ("the fixed point of the
description map; a ratio is only its eigenvalue") — were flagged in
[`SYNTHESIS.md`](../../SYNTHESIS.md) §7.0(iii) as never checked against each
other. Do they reconcile?

**Status: yes, in the setting they share — and all four registered predictions
pass, three of them to near machine precision.** Tests
[`derivations/D11-residue-reconciliation.md`](../../derivations/D11-residue-reconciliation.md).

Run it: `python3 run.py` (numpy + scipy, deterministic — every quantity is a
closed-form root-find, no random sampling, ~1 s). Registered first:
[`PREREGISTRATION.md`](./PREREGISTRATION.md).

---

## The claim

D7/D8's residue is the projectivized **eigenvalue data** of a description
map's linearization at a fixed point. D10's pinning criterion determines which
variables carry that structure at all. D3's "fixed point" language is the
literature's own name (renormalization-group theory) for what D7/D8 compute
the eigenvalues *of*. The derivation proves this identification for an
explicit description map — the dyadic renormalized-sum operator that is also
literally the central limit theorem's own RG (Jona-Lasinio 2001;
Calvo–Cuchí–Esteve–Falceto 2010) — and proves a consequence none of the three
stated: **the residue is exactly blind to directions tangent to the
fixed-point set**, which is why D3's counterexample exists and is not a fluke.

## Results

### P1/P2 — the exact eigenvalue, and the degenerate ray (AT RISK — pass to machine precision)

For a scale mixture X = U·Z (U > 0 independent of Z ~ N(0,1)), the sum of n
shared-U draws S_n satisfies S_n =_d √n·X *exactly*, for every n and every law
of U (proved in the derivation). Five two-point mixture configurations,
spanning near-Gaussian to strongly leptokurtic:

| config | u₁ | u₂ | p | H (IQR) | H (10–90 range) | ray gap |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| gaussian | 1 | 1 | 1.0 | 0.500000000 | 0.500000000 | 5.6e-17 |
| mild | 1 | 2 | 0.5 | 0.500000000 | 0.500000000 | 0.0 |
| strong | 1 | 5 | 0.5 | 0.500000000 | 0.500000000 | 5.6e-17 |
| rare extreme | 1 | 10 | 0.9 | 0.500000000 | 0.500000000 | 1.7e-16 |
| asymmetric | 0.5 | 3 | 0.3 | 0.500000000 | 0.500000000 | 1.1e-16 |

Registered: |H − 0.5| < 1e-6 for all 10 measurements (2 observables × 5
configs), R² > 1 − 1e-10. **Measured: every deviation is at the machine-epsilon
floor** (≤ 1.7e-16), not merely inside tolerance — the log-log regression
estimator this arc has used since D1 recovers an eigenvalue known exactly, to
the precision double floats allow, once the noise source (finite Monte Carlo
sampling) is removed. The ray [H_IQR : H_1090] is the same point of ℝP¹, [1:1],
for every configuration — the residue this arc's machinery extracts is
identical across the whole family.

**Context for the earlier, noisier measurement.** D3-ladder-invariance
measured H ∈ [0.4923, 0.4951] for the same construction via Monte Carlo
sampling (finite aggregates, one seed). This run's exact values are 0.5 to
16 digits — consistent with the earlier spread being sampling noise around
the true value this derivation predicts exactly, not evidence of a different
one.

### P3/P4 — the shape ratio: varies substantially, and is exactly invariant along the family (AT RISK — pass)

SR(n) = (Q₉₇.₅(n) − Q₂.₅(n)) / (Q₇₅(n) − Q₂₅(n)), a scale-invariant (hence,
by construction, H ≡ 0) kurtosis-like ratio:

| config | SR(n=10) | SR(n=100) | SR(n=10000) | \|SR(10)−SR(10⁴)\| |
|---|:--:|:--:|:--:|:--:|
| gaussian | 2.905846952 | 2.905846952 | 2.905846952 | 4.4e-16 |
| mild | 3.572406289 | 3.572406289 | 3.572406289 | 4.4e-16 |
| strong | 6.440140790 | 6.440140790 | 6.440140790 | 9.8e-15 |
| rare extreme | 8.950813048 | 8.950813048 | 8.950813048 | 1.8e-15 |
| asymmetric | 4.753156124 | 4.753156124 | 4.753156124 | 1.1e-14 |

Registered: spread (max/min − 1) ≥ 0.15 across configs, while H stays flat.
**Measured: spread = 2.08** (208%, the "gaussian" row's 2.9058 is the textbook
normal quantile ratio, an independent sanity check) — far past the registered
bar — while SR is n-invariant to the same machine-epsilon floor as P1/P2's H.
**This is the falsifiable core, targeted in advance rather than found post
hoc:** the direction the residue construction cannot see (a scale-invariant
shape statistic, which is by definition tangent to the fixed-point set —
constant along the whole approach) is exactly the direction that actually
varies across the family, and by a lot.

### D10, checked on a variable it had not been applied to (not registered — a boundary noted honestly)

The control here is an aggregate count n, additive under concatenating two
samples. By D10's C3 this pins the chart to G_diff, so H = 1/2 is a *fact*
here, not gauge — matching
[D3-ladder-as-quotient](../D3-ladder-as-quotient/)'s independent finding that
this harness's chart is pinned by additive aggregation. The value axis carries
no composition meaning, so its chart is free — already measured in
D3-ladder-invariance's P2/P5 (H moves by exactly a factor of a under
x ↦ sign(x)|x|^a). Not re-tested here; cited as the reason D10 is a
precondition for this construction rather than a competing account of it.

## Honest limits

- **Checked in one setting.** A single control (n), an explicit *linear*
  description map (renormalized convolution) with an exactly-solvable
  fixed-point set. D8's m > 1 Grassmannian case, and a description map with
  genuine nonlinear dynamics (where the fixed-point set's tangent directions
  are not available in closed form), are both untested — named as the obvious
  next probes in the derivation, not run here.
- **The construction is elementary, not RG-in-the-strict-sense.** No
  supersymmetric protection, no nonlinear RG flow — just the self-similarity
  of the Gaussian under convolution. The two named physics analogues (lines of
  fixed points from a marginal operator; CFT conformal manifolds) are the
  nearest known matches, not identical constructions — recorded in the
  pre-registration's prior-art note before any code was written.
- **Novelty is graded N1**, per the pre-registration: a recombination of
  already-known results (RG-eigenvalue exponents; CLT as an RG fixed point),
  correctly composed across four of this repo's own independently-produced
  results. The one derived consequence beyond restating the three — the
  residue's blindness to fixed-point-tangent directions is *provable* in
  closed form, not observed once by accident — is the only part that could be
  new, and the pre-registration's nearest-miss test names exactly what would
  make even that N0.
- **Five mixture configurations, one family (two-point scale mixtures of
  Gaussians).** Chosen to span a wide shape range and confirmed to do so
  (SR spread 208%), but the claim that *every* fixed-point set with tangent
  directions behaves this way is a generalization from one explicit, if
  representative, example.
- **P1/P2's two observables (IQR, 10–90 range) are both quantile spreads —
  the same scaling *type*, hence trivially the same eigenvalue (1/2) even
  before any measurement.** This experiment does not test a genuinely
  *nontrivial* eigenvalue ratio the way D2's β/k, D6's q1/q2 or P-D's θ did;
  it tests whether the estimator recovers a *known, exact* value once Monte
  Carlo noise is removed, and whether a scale-invariant (hence zero-exponent)
  direction is correctly invisible. C1's identification of the ray with
  eigenvalue *ratios* in general rests on the already-tested nontrivial cases
  (D2, D6, P-D, D7, D8), not on anything newly measured here.
