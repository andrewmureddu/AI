# D3 — the ladder is *not* a chart-invariance count (result)

**Works** [D3](../../questions/UNKNOWN-LAWS.md#d3--the-ladder-is-a-chart-invariance-count).
**Pre-registered** in [`PREREGISTRATION.md`](./PREREGISTRATION.md), before any
measurement, including the disclosure that the forward direction could not score
above N1 and that P4 was expected to fire.

**Status: the biconditional is falsified; one direction survives at N0–N1, and the
by-product is the sharpest thing here — a measured statement about
[the residue](../../invariants/FLOORS.md#4-what-refused-the-tower--and-the-shape-it-makes).**

> **The one-line version.** A one-parameter family of domains that is
> chart-invariant against A to **m = 0.012** at every setting, whose transfer skill
> sweeps **0.935 → 0.875 → 0.640 → 0.003 → 0.000**. Chart-invariance in a ratio is
> **necessary and not sufficient**, and transfer is continuous where D3 predicted a
> quotient.

Run: `python3 run.py` (pure numpy, deterministic, ~50 s) →
[`verdict.json`](./verdict.json), [`summary.csv`](./summary.csv).

---

## 1. The measurement D3 asked for

D3's registered test was to add a chart-invariance measurement to each rung of
[`ladder-vs-transfer`](../ladder-vs-transfer/) and see whether it beats the rung
label at predicting transfer. The measurement is the **aggregation chart order**

```
        H(D)  =  d ln s(n) / d ln n ,        s(n) = IQR of the n-aggregate
```

log-response over log-rescaling — [`FLOORS.md`](../../invariants/FLOORS.md) §4's
signature — computed **inside one domain, with no reference to any other domain's
samples**. That blindness is what makes it a test rather than a restatement of the
transfer score. By [D2](../D2-gauge-group/)'s rule the bare H is gauge and the
**ratio** is the invariant: r = H_B/H_A, mismatch m = |r − 1|.

**P1 — the chart orders (identity; estimator check).** All within the registered
tolerances.

| Rung | H (3 seeds) | r | m | transfer skill |
|:--:|:--:|:--:|:--:|:--:|
| **A** uniform increments | **0.5006** ± 0.0038 | 1.0000 | 0 | — |
| **L4** exponential increments | **0.5037** ± 0.0046 | 1.0063 | **0.006** | 0.894 |
| **L3** skewed finite-var mixture | **0.4974** ± 0.0020 | 0.9935 | **0.007** | 0.902 |
| **L2** Student-t, ν = 1.5 | **0.6985** ± 0.0010 | 1.3953 | **0.395** | 0.537 |
| **L1** single heavy draw | **−0.0011** ± 0.0020 | −0.0021 | **1.002** | 0.062 |

Ceiling (A against an independent draw of A) = **0.931**, consistent with paper 1's
0.920 ± 0.023. L2's H sits at 0.6985 rather than the asymptotic 2/3 = 0.6667 — a
finite-n effect, since the α = 1.5 stable limit is approached slowly and n ≤ 4096
here. Within the ±0.05 registered for that rung, and flagged rather than smoothed.

**P2 — H is gauge, the ratio is the invariant.** Under φ_a(x) = sign(x)|x|^a:

| a | 0.5 | 1.0 | 1.5 | 2.0 | 3.0 |
|---|---|---|---|---|---|
| H_A | 0.2503 | 0.5006 | 0.7509 | 1.0012 | 1.5018 |
| **H_A / a** | **0.5006** | **0.5006** | **0.5006** | **0.5006** | **0.5006** |
| r = H_L2/H_A | 1.39540 | 1.39533 | 1.39526 | 1.39519 | 1.39504 |

Bare H spans **6.0×**; the ratio is constant to **3.6e-4** relative. D2's rule
reproduced in a system with **no singularity and no Φ** — which is what makes it
worth recording, since D2 derived it for floor-3 germs and P-D's leg F measured it
on a branching scheme.

> **⚠ Pre-registration error on record.** P2's registered threshold was *"r
> invariant to < 1e-6 relative,"* and the measurement is 3.6e-4 — so the
> verdict file reports `P2_holds: false`. The threshold was wrong, not the claim: it
> was computed as if s(n) were an exact power law, whereas the finite-n correction
> that pushes L2's H off 2/3 also makes the re-charted fit reweight the n grid
> slightly. A correct threshold would have been ~1e-3. Recorded rather than
> revised, per house style; the substantive statement (invariant to 4 digits while
> the gauge part moves 6×) is unaffected.

**P3 — m beats the rung label, and gets the tie the label cannot (confirmatory).**

| Predictor | R² against measured skill |
|---|:--:|
| mismatch m | **0.998** |
| ordinal rung label | 0.869 |

The rung label predicts L4 > L3; the measured skill difference is **−0.008** (a
tie). m gives L3 and L4 the same value, 0.006 vs 0.007. Disclosed in advance as
confirmatory: the transfer numbers were already known when this was registered.

**So D3's own test passes.** If the experiment had stopped where D3 asked it to
stop, this would read as a promotion.

---

## 2. P4 — the leg D3 did not ask for, and it fires

The registered attack. Domain **B★**: increments X_i = U·z_i with z_i ~ N(0,1)
i.i.d. and U > 0 a lognormal common factor of coefficient of variation c, drawn once
per aggregate. Finite variance at every c; **not independent**, since the whole row
shares U. Level assigned *before* measuring, by the harness's own criteria: same
surface phenomenon, same finite variance, **different mechanism** (A's mechanism is
i.i.d. aggregation) ⇒ **L2**.

The common factor multiplies the sum, so it cannot touch how the sum's scale grows
with n. H stays at ½ by construction — and therefore m stays at 0:

| c (mixing strength) | 0.0 | 0.25 | 0.5 | 1.0 | 2.0 |
|---|:--:|:--:|:--:|:--:|:--:|
| H | 0.4946 | 0.4951 | 0.4950 | 0.4936 | 0.4923 |
| **m** | **0.012** | **0.011** | **0.011** | **0.014** | **0.017** |
| **transfer skill** | **0.935** | **0.875** | **0.640** | **0.003** | **0.000** |
| shape distance d | 0.014 | 0.027 | 0.077 | 0.227 | 0.542 |
| shape: n=64 vs n=1024 | 0.010 | 0.006 | 0.008 | 0.013 | 0.025 |
| shape vs Gaussian (n=1024) | 0.004 | 0.019 | 0.075 | 0.228 | 0.551 |

**Three things happen at once, and the third is the one that matters.**

1. **The invariant is held fixed.** m ∈ [0.011, 0.017] across the sweep — tighter
   than the L4 rung's own 0.006 ± estimator noise, and 23–90× smaller than L2's
   0.395.
2. **Transfer is destroyed anyway, continuously.** From the ceiling (0.935 at c = 0,
   which is the i.i.d. limit and should be at the ceiling) through 0.640 to **below
   the L1 rung** by c = 1.0. No cliff, no step: a smooth sweep in a parameter the
   invariant cannot see.
3. **Each c is a genuine fixed point of the aggregation map, not slow convergence
   to A's.** Shape distance between the n = 64 and n = 1024 aggregates is
   0.006–0.025 — the same order as the L4 rung's own 0.015 and the L2 rung's 0.021,
   i.e. at the sampling floor — while the distance *to A's Gaussian* is unchanged
   between n = 64 and n = 1024 (0.073 → 0.075 at c = 0.5; 0.224 → 0.228 at c = 1.0).
   The shapes have converged; they have converged **somewhere else**.

Compare the archival rungs under the same diagnostic:

| | self-distance n=64 vs n=1024 | distance to Gaussian at n=1024 |
|---|:--:|:--:|
| L4 | 0.015 | 0.007 |
| L3 | 0.015 | 0.005 |
| L2 | 0.021 | 0.097 |
| B★ (c = 1.0) | 0.013 | **0.228** |

**What P4 measures, stated precisely: the aggregation map has a one-parameter
continuum of fixed points, all with the same eigenvalue H = ½.** The Gaussian is
c = 0. The exponent labels the *eigenvalue* of the description map; it does not
label the *fixed point*. Two domains can agree on every invariant this experiment
can form from H and still be attracted to different laws.

**Consequences, in order of how much they cost.**

- **D3's biconditional is false.** Chart-invariance in a ratio is **necessary, not
  sufficient**, for transfer.
- **D3's explanation of the cliff's sharpness is false.** D3 argued the L2/L3 jump
  is sharp *because* a quotient is not a matter of degree. Here the quotient is
  fixed and transfer is continuous — so quotient structure does not imply
  sharpness. (Independently, [paper 1](../../paper/transfer-cliff.md) had already
  retracted the "cliff" in favour of a ceiling; the two retractions agree.)
- **The ladder's mechanism criterion survives the reduction attempt, and is
  vindicated by it.** B★ shares the surface form *and* the scaling exponent with A
  and still fails to transfer. The only criterion in the repo that catches it is the
  L2/L3 one — "is it the same mechanism?" — because what B★ breaks is
  **independence**, which is part of A's mechanism and is not a coordinate choice.
  The ladder is not reducible to an invariance count *because mechanisms carry
  content that no exponent does*.

---

## 3. P5 — forcing the mismatch, and the metric's own gauge freedom

**B-only re-charting (registered, holds).** Re-chart the L4 rung's macro observable
by φ_a and leave A alone: m becomes |a − 1| and transfer collapses.

| a | 0.5 | 1.0 | 1.5 | 2.0 | 3.0 |
|---|:--:|:--:|:--:|:--:|:--:|
| skill, B re-charted only | **0.239** | 0.894 | **0.091** | **0.000** | **0.000** |
| skill, common a | 0.342 | 0.894 | 0.924 | 0.949 | 0.977 |

So the **forward direction is real and is interventional, not observational**:
manufacturing a chart mismatch in a correspondence that otherwise transfers
perfectly destroys it, at every a tested. This is D3's surviving half — and it is
N0–N1 by the pre-registration's own prior-art note, since "an estimator generalizes
iff it depends only on invariant structure" is IRM's thesis.

**Common-a re-charting (registered threshold FAILED).** Registered: skill within
0.05 of its a = 1 value. Measured deviation: **0.551**. Reported as a failure in
`verdict.json` (`P5_holds: false`).

**P5b (post-hoc, not registered) — the diagnosis is a measurement, not a defence.**
Skill is 1 − d/d_ref, and d_ref is the distance from A's shape to a reference heavy
law **read in the same chart**. That normalizer is chart-dependent, so skill is not
a chart-invariant number. Re-normalizing every distance by the *same chart's*
sampling floor (A against an independent draw of A, re-charted identically):

| a | 0.5 | 1.0 | 1.5 | 2.0 | 3.0 |
|---|:--:|:--:|:--:|:--:|:--:|
| sampling floor in that chart | 0.0483 | 0.0148 | 0.0244 | 0.0425 | 0.1262 |
| **d(common a) / floor** | **1.80** | **1.54** | **1.86** | **1.88** | **1.88** |
| d(B only) / floor | 3.37 | 1.54 | 8.02 | 10.85 | 11.48 |

**Common-a is preserved: 1.54–1.88, a 1.22× spread over a 6× span of a**, against
3.4–11.5× when only one domain is re-charted. So D2's common-a commitment holds
outside physics, and P5's registered failure was measuring the metric.

The criterion here is the **spread across charts, not the absolute level**, and that
choice needs stating because it was made after seeing the numbers: the a = 1 baseline
is already 1.54 rather than 1.00, because the L4 rung is genuinely not Gaussian at
n = 200 (finite-n skew), so "preserved" can only mean *does not move with the chart*.
A first version of this leg tested the absolute level against 1.6 and reported a
failure for a quantity that is flat to 22% — recorded because the mistake is the same
species as P2's mis-set threshold, and it was caught only because the boolean
disagreed with the table above it.

**But the metric fact is itself worth keeping**, because it is a caveat on every
transfer number in this repo: *the same preserved correspondence reads skill 0.34,
0.89, 0.92, 0.95 or 0.98 depending only on the chart the reference law is read in.*
"How well does it transfer" is not chart-invariant unless the normalizer is
chart-internal. Paper 1's numbers are all in the a = 1 chart and should be read as
chart-relative.

---

## 4. What this does to the map

**D3 is retired as stated.** It graduates nothing. What it leaves:

1. **Necessary, not sufficient** (§3, interventional) — worth keeping as a cheap
   screening test: a chart mismatch predicts transfer failure, and the mismatch is
   measurable in each domain separately, before any joint modelling.
2. **The residue is not exhausted by ratios** (§2) — the first measured
   counterexample, and the reason it matters is below.
3. **Transfer skill has a gauge freedom of its own** (§3).

**On [`FLOORS.md`](../../invariants/FLOORS.md) §4's live question — what the
residue's general form is.** Three routes had found a ratio: D2's codimension
p − 2, [D6](../D6-support-singularities/)'s q1/q2,
[P-D](../PD-allometry-reduction/)'s θ. This experiment adds a fourth ratio
(H_B/H_A, in a system with no singularity and no Φ) and then breaks the pattern the
other three suggested:

> **The residue is the fixed point of the description map. The ratio is only its
> eigenvalue.** Where the fixed-point set is a discrete list, the eigenvalue
> suffices to label it and the residue *looks* like an integer or a ratio — which is
> exactly the situation at a floor-3 germ, where normal-form theory supplies the
> discrete list (the A_k series) that D2 and D6 were reading. Where the fixed-point
> set is a **continuum**, as it is here, no finite collection of ratios can
> classify, and the residue is a *shape* — a function, not a number.

That statement explains why three independent routes all found ratios (all three
sat at singularities with discrete normal forms) without claiming ratios are the
general answer. **It also makes a prediction, which this experiment does not
test:** a floor-3 object whose fixed-point set is a continuum should have a residue
that is *not* an integer, and the codimension count should fail there. That is now
the cheapest next probe of the residue question — logged, not claimed.

## 5. Honest hedging

- **One invariant family** (CLT/stable limits), inherited from the harness. Nothing
  here settles the ladder in general, and §2's fourth bullet is a defence of the
  L2/L3 criterion in one family, not a proof of it.
- **H is one chart-invariant, not the chart-free content.** The experiment shows a
  single ratio is insufficient; it cannot enumerate what would suffice. The
  fixed-point statement in §4 is an interpretation of the measurement, and is
  labelled a prediction where it goes beyond it.
- **Synthetic**, like the harness it extends.
- **The probability content is textbook** — normal variance mixtures are the
  standard counterexample to "finite variance ⇒ CLT," recorded in the
  pre-registration's prior-art note before the run. The novelty claim is about this
  repo's residue, not about probability.
- **P4's level assignment for B★ is arguable** (someone could call it L1 on the
  grounds that dependence breaks the analogy outright). The leg does not depend on
  it: the force of P4 is that m is pinned at 0.012 while skill sweeps 0.94 → 0.00,
  which holds whatever the rung is called.
- **The n = 64 vs n = 1024 fixed-point check uses one seed** (M = 20000 aggregates).
  The distances are ~0.01 against sampling floors of the same order, so it
  establishes "converged, and not to A's law" and not the finer shape of the
  convergence.

## 6. Bookkeeping correction to paper 1

Recomputing the L2 rung's skill with 32 seeds instead of 8 gives **0.515 ± 0.050**,
against the archival **0.484**. The archival value is a low-side 8-seed estimate;
the difference is sampling noise in a heavy-tailed metric, not a bug (this run's
independent-stream 8-seed value was 0.537). Two consequences for
[`paper/transfer-cliff.md`](../../paper/transfer-cliff.md):

- The quoted **"L2 max 0.538 across 8 seeds"** is seed-limited; at 32 seeds the
  per-seed maximum is **0.629**. The zero-overlap claim against L3 (min 0.886)
  survives comfortably, but the specific max should not be quoted as a bound.
- The paper's load-bearing claim — L2 is **capped far below the 0.93 ceiling** — is
  unaffected, and 0.515 is if anything a cleaner "half the attainable skill."
