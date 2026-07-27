# D7 — what the invariant residue is (result)

**Question ([D7](../../questions/UNKNOWN-LAWS.md)):** the successor to the map's
P0. [D2](../../derivations/D2-gauge-of-the-tower.md), [D6](../D6-support-singularities/)
and [P-D](../PD-allometry-reduction/) each reached "the chart-free residue" by a
different route and produced three objects that cannot state each other — a
codimension, a ratio of leading exponents, and an allometric exponent in a system
with no potential at all. Is there a general statement, or are the scheme layer's
invariants heterogeneous?

**Status: one statement, and the three members are it, computed on three different
slope vectors.** The residue is the log-slope vector modulo the **diagonal** ℝ⁺ —
equivalently, the slopes of observables against *other* observables. All five
at-risk legs pass on their substance. **Three registered tolerances were missed**,
all three by the same mechanism and all three because I set the number tighter than
the error budget I had written down one section earlier; that is logged in §4 as a
registration error rather than smoothed over.

Run it: `python3 run.py` (numpy only, ~4 min, deterministic — seed 20260727).
Registered first and committed before this file existed:
[`PREREGISTRATION.md`](./PREREGISTRATION.md). Derivation:
[`derivations/D7-the-residue.md`](../../derivations/D7-the-residue.md).

---

## The claim

Observables O₁,…,O_n vary along one control family carried by a chart ε; their
log-slopes are y_i = d ln O_i/d ln ε. G_pow relabels the family, ε ↦ ε^a, and acts
on the *whole* slope vector by one common scalar:

```
        y  ↦  a·y          ⇒        residue  =  [y] ∈ RP^{n-1}
                           ⇒        the invariants are  d ln O_i / d ln O_j
```

Four consequences, three of which correct statements the map currently carries:
weight 1 for every observable; **n − 1** independent invariants; the residue is
**not** intrinsically discrete; and common-*a* is the group rather than a caveat.

## Results

### P1 — estimator on exact powers (IDENTITY, declared)

Slopes recovered to **6.2e-15**, ratios invariant to the same, against a registered
1e-10. Declared in advance as algebra. It establishes only that the estimator is
sound across the slope range used below.

### P2 — weight 1 on an all-orders model (AT RISK — passes at p = 4, tolerance missed at p = 6)

Five observables of the full germ Φ = y^p/p + 0.2y^{p+1} + 0.05y^{p+2} − εy, each
read off the model with every order present, slopes measured over a window **fixed
in the new chart** so that each *a* interrogates a different physical window.

| p | w(y\*) | w(λ) | w(Var) | w(ΔΦ) | w(Φ‴) | max \|w − 1\| |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 4 | 1.0105 | 0.9900 | 0.9900 | 1.0021 | 0.9525 | **0.0475** |
| 6 | 1.0245 | 0.9890 | 0.9890 | 1.0035 | 0.9685 | **0.0315** |

Registered ±0.05 — met for both, but at p = 4 with almost no margin, and the
margin is consumed entirely by Φ‴ at the shallowest window.

The ratio λ-slope / y\*-slope, which D7 says is the invariant and D2 says is p − 2:

| a | 0.5 | 0.75 | 1.0 | 1.5 | 2.0 | 3.0 | bare slope span |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| p = 4 → 2 | 2.0866 | 2.0241 | 2.0066 | 2.0005 | 2.0000 | 2.0000 | **5.88×** |
| p = 6 → 4 | 4.2691 | 4.1357 | 4.0649 | 4.0139 | 4.0029 | 4.0001 | **5.88×** |

The bare slopes move by the full factor the group demands — λ's slope runs 0.3403 →
2.0000 at p = 4 — while the ratio sits on p − 2. **p = 4 meets the registered ±5%
(4.33%); p = 6 does not (6.73%).** Both deviations are monotone in *a* and vanish
as the window deepens, which is the registered error budget and is diagnosed in §4.

### P2b — the chart-derivative exception (AT RISK — passes, and more sharply than registered)

The derivation says χ = dy\*/dε is *not* an observable and must transform affinely,
y_χ(a) = a·y_χ(1) + (a − 1). Measured against that formula, with no free parameter:

| p | max err vs **affine** | max err vs pure weight | ratios formed with χ |
|:--:|:--:|:--:|:--:|
| 4 | **6.4e-3** | 2.003 | range **2.57×** the a=1 value |
| 6 | **1.26e-2** | 2.013 | range **2.17×** |

Registered ±0.05 on the affine law, ≥0.1 separation from a pure weight, ≥20% motion
in the ratios: all met, the middle one by a factor of 20.

**The cleanest form of this was not the registered statistic.** The affine law
predicts y_χ vanishes at a = 1/(1 − k). At p = 4, k measures 0.6678, so the
prediction is a = 3.010 — and the measured y_χ(3) is **−0.0000**. A homogeneous
quantity of weight 1 cannot change sign as the chart is relabelled; this one does,
exactly where predicted. At p = 6 the zero sits at a = 5.11, outside the range, and
no sign change occurs. The registered "fitted weight ≠ 1" number is reported in
`verdict.json` but is a degenerate statistic precisely because of that zero, and
should be read as the sign change rather than as a weight.

### P3 — the count is n − 1 (AT RISK — passes)

Six slope vectors (one per *a*) in ℝ⁵, stacked:

| p | σ₁ | σ₂ | **σ₂/σ₁** | invariants |
|:--:|:--:|:--:|:--:|:--:|
| 4 | 7.0222 | 0.0208 | **2.96e-3** | 5 − 1 = **4** |
| 6 | 7.3012 | 0.0252 | **3.45e-3** | 5 − 1 = **4** |

Registered < 0.05; met with a factor of 15 to spare. The five measured slope
vectors span a **line**, so the quotient is ℝP⁴ and the count is 4. **This is the
first measurement of the residue at n > 2** — every previously known member (p − 2,
q1/q2, θ) has n = 2 and therefore exactly one invariant, which is why each looked
like *the* residue rather than like one coordinate among several.

### P4 — independent re-charting kills the ratios (CONTROL, declared)

Three anisotropic directions (p = 4, 6, 8), six observables, re-charted with a
different exponent per direction:

| | σ₂/σ₁ | ratio λ₂/λ₁ span | signs |
|---|:--:|:--:|:--:|
| independent charts, (ℝ⁺)³ | **0.227** | **4.24×** | unchanged |
| common *a*, diagonal ℝ⁺ | **2.19e-3** | — | unchanged |

Registered > 0.2 and ≥ 1.5×: met. Declared in advance as a control and not counted
as evidence — its job is to show that P2/P3's invariance is a property of the group
and not something the estimator manufactures, which is the check
[D6's P2](../D6-support-singularities/) was missing. The 100× gap between the two
rows is the content: **the same observables, the same estimator, invariance present
under the diagonal and absent under the product group.** This is the measured form
of D2's common-*a* caveat, which the derivation gets as the statement that the
orbits of (ℝ⁺)ⁿ on the orthant are the orthant, leaving only signs — and the signs
are indeed unchanged in every case.

### P5 — one estimator, three classes (AT RISK — passes; the N2 leg)

One function, `residue(O_a, O_b) = d ln O_a / d ln O_b`, applied unmodified:

| leg | system | quantities | measured | predicted | source it must reproduce |
|---|---|---|:--:|:--:|---|
| P5a | smooth germ, p = 4 | y\* vs λ | **0.4996** | 0.5000 | D2's 0.5000 |
| P5a | smooth germ, p = 6 | y\* vs λ | **0.2483** | 0.2500 | D2's 0.2503 |
| P5b | Φ = A\|y\|²+\|y\|⁴ | A_c vs D | **0.5000** | 0.5000 | D6 |
| P5b | Φ = A\|y\|+\|y\|² | A_c vs D | **0.5000** | 0.5000 | D6 |
| P5b | Φ = A\|y\|²+\|y\|⁶ | A_c vs D | **0.6667** | 0.6667 | D6 |
| P5b | Φ = A\|y\|+\|y\|³ | A_c vs D | **0.6667** | 0.6667 | D6 |
| P5c | branching scheme, n = 2…10 | B vs V | **0.7495–0.7500** | 0.7500 | P-D's 3/4 |

Nothing is fitted and no formula is inserted; each row is the same two-line
estimator handed a different pair of measured quantities. **The third block is the
one that decides the claim**, because allometry has no singularity, no Φ, no
continuous chart and no thermodynamic limit — and the estimator that produced D2's
codimension and D6's ratio returns P-D's 3/4 there without modification.

Coarse-graining the scheme by *a* levels: θ spread **1.96e-6** across a = 1…8 while
the per-level slope ln n moves by **8.0×**. Registered 1e-10 — **missed**, see §4;
the effect is finite-N and the spread falls to 1.9e-12 one window deeper.

### P6 — the residue is not discrete (IDENTITY, declared; decisive against a map claim)

| system | measured | predicted |
|---|:--:|:--:|
| Φ = A\|y\|² + \|y\|^{2π} | **0.68169** | 1 − 1/π = 0.68169 |
| smooth germ, p = 2 + √2 | **0.70698** | 1/√2 = 0.70711 |

The algebra is forced and was declared an identity in advance. Its weight is
entirely in what it refutes: `FLOORS.md` and `SYNTHESIS.md` §7.0 both read D2's
result as "the chart-free residue is **one integer**, the codimension p − 2." A
projective space has no distinguished rational points, and a singularity with
incommensurable leading exponents has an irrational residue. **D2's integer is
inherited from Taylor orders being integers in the smooth case, not from the
residue.**

### P7 — the kink is a projective wall (AT RISK — passes)

P-D's θ = min(1, ln n/−ln(β²γ)) is non-analytic at nβ²γ = 1, and the D2/P-D
reconciliation explicitly left open whether that kink is a floor-3 degeneracy read
in a scheme variable or something with no floor-3 counterpart.

| quantity | measured | registered |
|---|:--:|:--:|
| RMS of θ(x) against min(1, ·), away from the wall | **5.6e-9** | ±0.01 |
| θ for x > 1 | **1.000000** | 1 |
| located wall x_c | **1.00012** | 1.000 ± 0.005 |
| x_c spread under coarse-graining, a = 1…8 | **4.7e-6** | 1e-6 (**missed**) |
| per-level slope motion over the same a | **8.0×** | — |

**The min is not imposed — it emerges from the exact finite sum**, which is what
put this leg at risk. And the wall is where the two log-slopes are *equal*: the
point [1 : 1] of ℝP¹. So the answer to the reconciliation's open item is that the
kink is a wall in the residue's own space, at a distinguished point of the
projective line, chart-invariant, with no Φ anywhere in its statement.

## 4. Three missed tolerances, and one code bug

**All three misses are the same mechanism, and it is the one §5 of the registration
named.** G_pow is the *asymptotic* group; over a finite window the measured slopes
carry corrections to scaling, and over a finite level count the exact sum carries
x^N. I wrote that down and then set three tolerances tighter than it. Post-hoc
diagnostics, run to separate "the claim failed" from "the budget was under-quoted",
since the second makes a prediction the first does not:

| miss | registered | measured | diagnostic |
|---|:--:|:--:|---|
| P2 ratio, p = 6 | ±5% | 6.73% | deviation ∝ window depth: **3.78% → 1.62% → 0.67% → 0.27% → 0.11%** as y\*_max falls 1.5e-1 → 4.0e-3 |
| P5c coarse-graining | 1e-10 | 1.96e-6 | spread tracks x^N: **2.0e-6 → 1.9e-12 → 4.8e-15** at N = 20 → 50 → 100 |
| P7 x_c spread | 1e-6 | 4.7e-6 | x_c → 1 under refinement: **1.00012 → 1.00002 → 1.00000** |

The p = 4 window series is the same shape (1.49% → 0.33% → 0.07% → 0.02% → 0.00%),
and in both cases the deviation falls in proportion to y\* at the top of the window
— i.e. in proportion to the correction-to-scaling term C₃·y\*, which is where it
must come from if the group statement is exact. **The diagnostics are post-hoc,
are not counted as passes, and are marked as such in `verdict.json`.** The
registered numbers stand as missed.

> **Registration error on record, and it is a new kind.** The register has logged
> three slips, all of them the same one — misclassifying a consequence of my own
> construction as a test of it ([D1's P5](../D1-chart-invariance/PREREGISTRATION.md),
> [D2's resampling no-op](../D2-gauge-group/README.md),
> [D6's P2](../D6-support-singularities/)). This is a fourth slip of a *different*
> kind: **the identity/risk split was right and the tolerances were wrong** — set
> from what I expected the answer to be rather than from the error budget I had
> just finished writing. It is the more dangerous of the two, because a tolerance
> set from expectation converts a passing claim into a failing one or the reverse
> without touching the reasoning. The fix that would have worked is mechanical:
> derive each tolerance from the scope section, in the scope section.

> **A code bug, found by disbelieving a diagnostic.** The kink locator's parabolic
> refinement was reading an off-centre triple of the curvature array — the argmax
> index had already been shifted to match the ln x grid, and the three points fed
> to the parabola were shifted with it. The registered P7 first read
> x_c = 0.99220, a miss; the refinement series read 0.99219, 0.99439, **1.10974**,
> 1.00153. The 1.11 is what exposed it: a locator that is merely grid-limited does
> not get *worse* by a factor of 40 when the grid is refined. With the triple
> centred the same code gives 1.00012 and a monotone refinement series. Recorded
> because the wrong number was the *registered* one, and because the thing that
> caught it was an out-of-pattern value in a diagnostic rather than any check I had
> planned.

## 5. What survives, and what does not

**Survives.** The residue has a general form: it is the log-slope vector modulo the
diagonal ℝ⁺, i.e. slopes of observables against observables. The three known
members are that invariant computed on three slope vectors, established by one
estimator across a smooth germ, a support-type singularity and a branching scheme
with no Φ. The count is n − 1 and is now measured at n = 5. Common-*a* is the
group, with the product group's sign-only residue exhibited alongside it.

**Does not survive.** "The chart-free residue is one integer, the codimension
p − 2", as `FLOORS.md` §4 and `SYNTHESIS.md` §7.0 both currently put it. The
integrality is the smooth case's, not the residue's.

**Honest limits.**

- Every model here is one-dimensional or separable, and the anisotropic germ in P4
  is separable by construction — the multi-dimensional case with genuinely coupled
  directions is untested.
- P1 and P6 are identities, P4 is a control, and P5b reproduces D6's numbers with
  D6's own estimator, so it is a consistency check on the unification and not
  independent evidence for the ratio.
- The mathematics is old in every component and the register entry says so: the
  N2 claim is the cross-domain identification and the consequences, not the
  projective quotient.
- **Essential singularities remain outside**, exactly as after D6. No leading power,
  no finite log-slope, nothing here applies. The remainder does not narrow.
- Whether the residue's coordinates obey any *arithmetic* across composed
  singularities is [D5](../../questions/UNKNOWN-LAWS.md)'s question, was registered
  as untouched, and remains untouched.
