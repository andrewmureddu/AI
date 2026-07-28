# D9 — chart-invariance and transfer on an *unpinned* chart (result)

**Question ([D9](../../questions/UNKNOWN-LAWS.md)):** the half
[D3](../D3-ladder-as-quotient/) could not reach. D3 falsified "the ladder is a
chart-invariance count" on a harness whose chart is a **count**, pinned by
additivity — so G_pow was never available there. Does chart-invariance predict
transfer where the control is a genuine distance-to-threshold?

**Status: INCONCLUSIVE, and the fault is in the design rather than in the
measurements.** The residue legs pass cleanly and the bare-exponent contrast with D3
is exactly as predicted. **But the transfer leg — the whole point — fails on its
registered thresholds, because the harness has almost no dynamic range in transfer.**
Crossing the class boundary from p = 4 to p = 6 changes the fluctuation law by
almost nothing, so the four rungs are not four rungs, and a test of "does the
residue predict transfer" cannot be run on a harness where transfer barely varies.
**D3's open half stays open.**

The by-product is worth more than the intended result: **the degeneracy order
classifies the scaling structure but is nearly invisible in the fluctuation shape.**

Run it: `python3 run.py` (numpy only, ~2 min, deterministic, quadrature — no
sampling). Registered first and committed before this file existed:
[`PREREGISTRATION.md`](./PREREGISTRATION.md).

---

## Results

### P1 — residue distances (AT RISK — passes)

Subspace sine between each domain's log-slope vector and A's, with every domain
reading its own coordinate δ (ε = δ^c):

| pair | measured | registered |
|---|:--:|:--:|
| A–L4 — same p = 4, coefficients differing up to 18×, chart c = 2.0 | **0.0009** | < 0.05 |
| A–L3 — same p = 4, chart c = 0.6 | **0.0020** | < 0.05 |
| A–L2 — **p = 6**, chart c = 1.3 | **0.2606** | 0.214 ± 0.06, and > 0.15 |
| A–L1 — no singularity | **undefined** — Φ‴ ≡ 0 | rank 0 |

Stable to the fourth decimal across three ε-windows and two quadrature resolutions.
The residue does exactly what D7 says: same class ⇒ same chart-free content, despite
different coefficients *and* different coordinates.

**L1 is sharper than registered.** I predicted a zero ray; what happens is that one
observable is *identically* zero — an ordinary quadratic well has no third
derivative — so the residue is not small, it is **undefined**. That is a stronger
separation than any distance, and the first version of the code reported it as a
`nan`. Fixed to report the degeneracy explicitly.

### P2 — transfer, and whether the residue orders it (AT RISK — **FAILS**)

| rung | transfer skill | registered |
|---|:--:|:--:|
| L4 | 0.988 | > 0.80 ✓ |
| L3 | 0.984 | > 0.80 ✓ |
| L2 | **0.938** | **< 0.40 ✗** |
| L1 | **0.664** | **< 0.40 ✗** |

The ordering clause passes (L4, L3 closer than L2, stable across all six settings)
and so does the stability clause that was registered as the real bar. **Neither is
worth anything, because the quantity being ordered spans 0.938 to 0.988 among the
rungs that matter.** A predictor that orders a range of 0.05 is not shown to predict
transfer; D3's contrast had a 28× spread to work with.

### P3 — the contrast with D3 (AT RISK — passes on its own terms, uninformative in context)

| | D3 (pinned chart) | D9 (unpinned chart) |
|---|:--:|:--:|
| bare exponent across same-class domains | 0.4960 / 0.5013 / 0.5023 — **1.013×** | 0.667 / 1.333 / 0.401 — **3.33×** |
| bare exponent orders transfer | **yes**, 30× gap | **no** |
| residue ordering stable under re-sampling | **no**, scrambles | **yes**, to 4 decimals |

Every number is as registered, and the mechanism is real: on an unpinned chart the
bare exponent is not shared even between domains of the same class, because each
domain's coordinate choice multiplies it. **But "does not order transfer" is nearly
vacuous when transfer does not vary.** The contrast is suggestive and it is not
evidence.

### P4 — re-charting invariance (DECLARED, not evidence — tolerance missed)

Residue shift under δ ↦ δ^a for a ∈ {0.5, 1, 2, 3}: **0.0159** against a registered
< 0.01, while bare k spans **5.91×** against the predicted 6×. The miss is the
finite-ε budget — re-charting moves the physical window, exactly as in
[D7](../D7-residue-projective/)'s P2 — and this leg was declared not to be evidence
in either direction.

## Why it failed, measured rather than asserted

The registered thresholds were unreachable, so either the claim is wrong or the
readout has no range. Excess kurtosis settles it — it is the standardized shape in
one number:

| | A (p=4) | L4 (p=4) | L3 (p=4) | L2 (**p=6**) | L1 (Gaussian) | reference (Laplace) |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| excess kurtosis | −0.900 | −0.936 | −0.862 | **−1.036** | 0.000 | **+2.961** |
| raw shape distance from A | — | 0.0020 | 0.0027 | **0.0104** | 0.0561 | 0.167 |

**Crossing the class boundary moves the shape by 0.14 in kurtosis; the metric's
reference is 2.96 away.** So every singular rung normalizes to a skill near 1. A
far-tail readout does not rescue it either — the q₉₉.₅/q₇₅ ratio separates p = 4 from
p = 6 by 0.154 against a within-p = 4 spread of 0.076, a ratio of 2:1 where the
residue's is 130:1.

**So the design error is structural, not a bad choice of statistic.** The CLT harness
D3 used works because crossing *its* class boundary changes the law utterly — a
Gaussian shape versus a stable one. Here the two classes have nearly the same law.
**I built a harness whose rungs differ in the residue but not in the law**, and that
cannot test whether one predicts the other. The registration checked that transfer
and residue were read from *different quantities*, which they are; it did not check
that the readout had any range across the rungs, which is the failure mode that
actually occurred.

## What this does establish

**A substantive by-product, and it slightly complicates the arc.** The degeneracy
order *p* — which [D1](../D1-chart-invariance/), D7 and
[D8](../D8-grassmannian-residue/) establish as the classifier of floor-3
singularities — is **nearly invisible in the shape of the fluctuations**. It
classifies the scaling structure and almost nothing else that an observer sees
directly. That also explains something about [D6](../D6-support-singularities/):
its kurtosis estimator worked because it spanned q = 0.5 to 8 (+22.2 to −1.08), and
the discrimination is strong at small q and weak between adjacent large ones. Anyone
reusing that estimator between neighbouring degeneracies should expect it to be
blunt.

## Honest limits

- **The claim D9 set out to make is not established.** Whether chart-invariance
  predicts transfer on an unpinned chart is open, exactly as D3 left it.
- **P2 failed, P4 missed its tolerance, and P3 is uninformative given P2.** Only P1
  carries weight, and P1 is a re-measurement of D7 in a new coordinate arrangement
  rather than a new result.
- **Two code faults on record.** L1's residue came out `nan` because one observable
  is identically zero; fixed to report the degeneracy. And a patch script broke on a
  docstring containing a triple quote — harmless, but it is the second scripting
  self-injury this session after the `pkill` incident.
- The registration's guard against tuning held: **the models were not changed after
  the numbers were seen.** Fixing this experiment means building a *different*
  harness, and doing that here would have made the registration meaningless.

## The concrete fix, for whoever takes the next pass

Rungs whose **laws** differ, not just whose residues do. D6 has the material:
q₁ = 1 versus q₁ = 2 gives excess kurtosis **+3.0000 versus 0.0000**, a separation
20× larger than p = 4 versus p = 6. A harness built on the support-type/degeneracy
boundary — with each domain still supplying its own coordinate, which is the part
D9 got right — would have both the dynamic range D9 lacks and the unpinned chart D3
lacks. That is the experiment that answers the question, and it is not this one.
