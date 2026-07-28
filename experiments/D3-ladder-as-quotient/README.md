# D3 — is the ladder a chart-invariance count? (result)

**Question ([D3](../../questions/UNKNOWN-LAWS.md)):** the register's oldest unworked
stone. D3 conjectured that a correspondence transfers **iff** it is chart-invariant,
and that the ladder is therefore not a scale of epistemic quality but *a count of
how many coordinate choices have been quotiented out*.

**Status: falsified, on its own registered falsifier.** The chart-free residue does
not distinguish the domains that transfer from the one that does not — its
distances are indistinguishable from sampling noise, and their *ordering* scrambles
across every sampling setting tried, while transfer skill spans a factor of 28 and
is stable to ±0.02 over 8 seeds. What does place the boundary is the **bare
exponent** 1/α — the magnitude that D7 calls gauge across domains. And that is not
a paradox: **the chart here is pinned**, so the magnitudes are facts.

Every registered prediction was met, including the primary one, which was written
to kill D3. **No tolerance was missed** — the first time in this arc, and the
registration says why it was set differently.

Run it: `python3 run.py` (numpy only, ~6 min, deterministic — seed 20260728).
Registered first and committed before this file existed:
[`PREREGISTRATION.md`](./PREREGISTRATION.md).

---

## The setup

The [ladder-vs-transfer harness](../ladder-vs-transfer/) holds the surface
phenomenon fixed — "a macroscopic quantity is the aggregate of n microscopic
contributions" — and varies how deeply domain A's Gaussian law applies in B. **The
chart is n**: it is the control the domain supplies, every observable varies along
it, and [D7](../D7-residue-projective/)/[D8](../D8-grassmannian-residue/) apply
directly. Six observables per domain — four quantile spreads and two dimensionless
shape ratios — and the residue is the projective class of their log-slope vector
against ln n.

**A note on what this stone could still use.** D3's own statement leans on the
transfer *cliff* — "the jump exactly at L2/L3", "a quotient is not a matter of
degree". [Paper 1](../../paper/transfer-cliff.md) retracted that step reading
(L1→L2 = +0.451 ≈ L2→L3 = +0.432). The registration recorded that the sharpness
argument was already dead and that this run does not get to use it.

## Results

### P1 — the scale exponents (AT RISK — passes)

| domain | scale slope d ln O/d ln n | seed sd | predicted | shape slopes |
|---|:--:|:--:|:--:|:--:|
| A (uniform) | **0.4960** | 0.0105 | 0.500 ± 0.03 | ≤0.003 |
| L4 (exponential) | **0.5013** | 0.0072 | 0.500 ± 0.03 | ≤0.002 |
| L3 (skewed mixture) | **0.5023** | 0.0160 | 0.500 ± 0.03 | ≤0.004 |
| L2 (t, ν = 1.5) | **0.6768** | 0.0308 | 0.667 ± 0.04 | ≤0.024 |
| L1 (not an aggregate) | **−0.0071** | 0.0124 | 0.000 ± 0.02 | ≤0.003 |

The finite-variance domains sit on ½ and the infinite-variance one on 1/α = ⅔, so
the observables are measuring the scaling structure the theory says is there.

### P2 — the residue does not separate the transfer boundary (AT RISK — the primary prediction, passes)

Projective classes, each normalized by its first component:

| domain | residue | distance from A |
|---|---|:--:|
| A | [1, 1.004, 1.006, 1.002, 0.004, 0.006] | — |
| L4 | [1, 0.998, 0.996, 0.988, −0.002, −0.004] | **0.0081** |
| L3 | [1, 0.992, 0.995, 1.010, −0.008, −0.005] | **0.0120** |
| L2 | [1, 0.982, 0.965, 0.943, −0.018, −0.035] | **0.0327** |
| L1 | **zero vector — no ray** | n/a |

Registered: all distances below 0.05 — **met**. Registered D3-saving criterion
(A–L2 exceeding both A–L3 and A–L4 by 3×) — **not met**: 0.0327 is 2.7× the L3
distance.

> **But that number ordered them, and my prediction said it would tie. So before
> counting this as a pass I checked what carries it.** The distances are all
> ~0.01–0.03, which is the same size as the seed-to-seed spread of the slopes
> themselves. Re-measuring on a different n-window at three sample sizes:
>
> | M | L4 | L3 | L2 | ordering |
> |:--:|:--:|:--:|:--:|---|
> | 800 | 0.0014 | 0.0294 | 0.0268 | L4 < L2 < L3 |
> | 3000 | 0.0310 | 0.0124 | 0.0202 | L3 < L2 < L4 |
> | 9000 | 0.0189 | 0.0135 | **0.0097** | **L2 < L3 < L4** |
>
> **The ordering scrambles completely, and at the best-estimated setting L2 — the
> domain that fails to transfer — is the *closest* to A.** Dropping the extreme
> q₉₉.₅−q₀.₅ observable, the worst-estimated one, changes nothing systematic. So
> the apparent ordering in the main run is one draw of a noise variable, and the
> residue carries **no** information about transfer. That is the registered
> prediction, reached more strongly than by a flat tie.

### P3 — the rank separates the wrong rung (AT RISK — passes)

| | A | L4 | L3 | L2 | L1 |
|---|:--:|:--:|:--:|:--:|:--:|
| rank r | 1 | 1 | 1 | 1 | **0** |
| count r(n−r) | 5 | 5 | 5 | 5 | **0** |

L1's aggregate does not depend on n at all, so its slope vector is zero and it has
no ray. Everything else has rank 1. **The "count" reading of D3 therefore takes two
distinct values across four rungs**, and it separates L1 from the rest — while
transfer separates L1–L2 from L3–L4. A two-valued quantity cannot be a four-valued
ladder, and the one boundary it does place is not the one that matters.

### P4 — which predictor places the transfer boundary (AT RISK — passes)

| rung | transfer skill | residue distance | bare exponent distance | rung label |
|---|:--:|:--:|:--:|:--:|
| L1 | 0.033 | n/a (rank 0) | **0.503** | 1 |
| L2 | 0.484 | 0.0327 | **0.181** | 2 |
| L3 | 0.916 | 0.0120 | **0.006** | 3 |
| L4 | 0.894 | 0.0081 | **0.005** | 4 |

**The bare exponent distance orders all four rungs exactly as transfer does** — L1
worst, L2 next, L3/L4 tied at the ceiling — with a 30× gap across the L2/L3
boundary. The residue does not place that boundary at all. *The chart-free part
predicts nothing and the gauge-looking magnitude predicts everything*, which is
D3's registered falsifier horn (i) in the sharpest available form: L2 is
chart-invariant to within noise and still fails to transfer.

*Disclosure:* the code operationalizes "places the boundary" with a separation
constant of 0.05 that the registration did not name. The conclusion does not depend
on it — every residue distance is ≤0.033 with a scrambling order, and every bare
exponent distance is separated by 30×.

### P5 — the chart is pinned, so the magnitudes are facts (AT RISK — passes)

D7's apparatus needs G_pow to be *available*, and it is not automatic.
[P-D](../PD-allometry-reduction/)'s leg F found that extensivity pins a chart to
G_diff. Aggregation composes the same way: n₁ contributions then n₂ is n₁ + n₂ of
them.

| a | 1.0 | 1.5 | 2.0 | 0.5 |
|---|:--:|:--:|:--:|:--:|
| additivity defect of n ↦ n^a | **0.0000** | **0.2929** | **0.5000** | **0.4142** |

Registered 0 at a = 1 and >20% otherwise: met, and the numbers are P-D's shape
exactly. **So G_pow was never available for n.** By
[D2](../../derivations/D2-gauge-of-the-tower.md)'s rule (i) the exponents are
facts here, and P4's verdict is not the paradox it first looks like: 1/α looks like
a gauge magnitude only if you may re-chart n, and you may not.

### P6 — reproducing the harness (CONSISTENCY CHECK)

Transfer skills 0.0329 / 0.4840 / 0.9156 / 0.8937 against the published 0.033 /
0.484 / 0.916 / 0.894 — max difference **0.0004**.

## What replaces D3

**The negative.** The ladder is not a chart-invariance count. On this harness the
chart-free residue is constant across three rungs that transfer at 0.48, 0.92 and
0.89, and the one thing it does separate — L1's rank 0 — is the boundary that
matters least.

**The positive, and it is smaller than D3 but it is measured.** What predicts
transfer here is **basin membership**, and basin membership is read off a
magnitude: the scale exponent 1/α. That fits what
[paper 1](../../paper/transfer-cliff.md) found and D3 could not explain — the real
structure is a **ceiling**, not a step. L2 saturates at ~0.54 no matter how much
data it gets, because more data cannot move an exponent to a different basin. A
quotient story predicts a step; a basin story predicts a ceiling; the ceiling is
what was measured.

**So the ladder's rungs are doing something D3 did not consider.** L3/L4 differ from
L2 by *which universality class the mechanism puts them in* — and a universality
class is exactly a statement about magnitudes being equal, not about ratios. D2 had
already recorded the relevant rule: **within a domain exponents are facts;
across domains only ratios, signs and counts are.** D3 assumed the ladder lives on
the second half of that sentence. On this harness it lives on the first, because
additivity pins the chart.

## Honest limits

- **One harness, one family.** Every domain here is "a sum of n contributions." A
  negative here is a counterexample to D3 as stated; it is **not** a proof that no
  chart-invariance reading of the ladder works. A family whose chart is *not*
  pinned would be the real test, and this experiment does not contain one.
- **Four rungs is n = 4.** No coefficient computed on four points can reach
  significance, as paper 1 already recorded for Spearman(level, skill). The
  argument rests on the *pattern of ties* — which boundary each predictor can and
  cannot place — and on the 30× versus scrambling-noise contrast, not on any
  correlation.
- **P6 is a consistency check**, declared in advance, and the transfer metric with
  its ~0.92 ceiling is inherited from the harness.
- **The residue's noise floor is not separately characterized.** The diagnostic
  shows the ordering is unstable across M and window; it does not establish the
  asymptotic residue distances are exactly zero, only that they are too small and
  too unstable to carry the transfer signal.
- **D3's own sharpness argument was retracted before this ran**, so its strongest
  motivation was gone at registration time. That is recorded in the registration
  and is not a post-hoc excuse.
