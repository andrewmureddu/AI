# D3 pre-registration — written before any measurement

Works [D3](../../questions/UNKNOWN-LAWS.md), the register's oldest unworked stone:
**is the ladder a chart-invariance count?** D3 conjectured that a correspondence
transfers *iff* it is chart-invariant, and that the ladder is therefore not a scale
of epistemic quality but a count of how many coordinate choices have been
quotiented out.

Two things have changed since it was written, and both are why it is worth running
now rather than never.

1. **"Count" now has a referent.** When D3 was written the phrase was a metaphor.
   [D7](../D7-residue-projective/) made it n − 1 and
   [D8](../D8-grassmannian-residue/) made it r(n − r), with an estimator validated
   across three classes. D3 is now a measurement rather than a slogan.
2. **Its supporting evidence was retracted.** D3 leans on the transfer *cliff* —
   "the jump exactly at L2/L3" and "a quotient is not a matter of degree" — and
   [paper 1](../../paper/transfer-cliff.md) **retracted the step reading**
   (L1→L2 = +0.451 ≈ L2→L3 = +0.432). What survives is a **ceiling**: L3/L4 reach
   complete transfer (0.920 ± 0.023, indistinguishable from a law transferring to
   itself), L2 saturates at ~0.54 forever. **So the sharpness argument in D3's own
   statement is already dead, and this registration does not get to use it.**

Per [`UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6: prior-art note,
identity/risk split, then numbers.

---

## 0. Prior-art note (written first)

**Old.** That the CLT basin is a universality class, that infinite-variance sums
converge to α-stable laws instead, and that the scale of a sum grows as n^{1/α} are
1930s probability (Lévy, Gnedenko–Kolmogorov). Domain-of-attraction membership as
the thing that determines whether a Gaussian approximation is legitimate is the
content of those theorems and nothing here adds to it.

**Not covered, and it is a claim about *this repo*, not about probability.** D3 is a
claim about the **ladder** — the methodology's own instrument. Whether ladder level
is a chart-invariance count is a question about our classification scheme, so there
is no field that owns it and no literature that could contain it. That also means
the usual protection is absent: **no specialist will object**, so the burden falls
entirely on the pre-registration.

**The real risk here is not rediscovery, it is self-flattery.** D3 would, if it
survived, upgrade the repo's central instrument from a convention to a measured
structure. That is exactly the kind of result one should expect to be wrong, and
§2 is written accordingly: **the outcome I actually expect is registered as the
primary prediction, and it falsifies D3.**

---

## 1. The claim, and what would decide it

The [ladder-vs-transfer harness](../ladder-vs-transfer/) holds the surface
phenomenon fixed — "a macroscopic quantity is the aggregate of n microscopic
contributions" — and varies how deeply domain A's Gaussian law applies in domain B:

| rung | domain B | transfer skill (measured, existing) |
|---|---|:--:|
| L4 | exponential increments (finite variance) | 0.894 |
| L3 | skewed finite-variance mixture | 0.916 |
| L2 | Student-t, ν = 1.5 (**infinite** variance) | 0.484 |
| L1 | a single heavy draw (not an aggregate) | 0.033 |

**The chart is n.** It is the control the domain supplies, every observable varies
along it, and the harness already sweeps it. So D7/D8 apply directly: measure the
log-slope vector of each domain's observables against ln n, and the chart-free
residue is its projective class.

**D3 predicts** that the residue distance between A and B tracks transfer skill —
that L3/L4 share A's chart-free content and L1/L2 do not.

## 2. Identity vs. risk — the required disclosure

**Analytic identities and consistency checks. Not evidence:**

- **P6 — reproducing the harness's four transfer skills.** Same metric, same seeds.
  It exists so the correlations below are computed against numbers comparable to
  the published ones, and it is a check on my re-implementation.

**Genuinely at risk — and the primary prediction is the one that kills D3:**

- **P1 — the scale exponents.** Finite-n corrections are strong for α-stable
  convergence and could bias the fit enough to blur the two classes.
- **P2 — THE LEG. The residue is *degenerate across the transfer boundary*.**
  Registered as the outcome I expect, and it is D3's falsifier horn (i): an L2
  correspondence that is chart-invariant and still fails to transfer.
- **P3 — the rank separates the wrong rung.**
- **P4 — the predictive comparison**, which is the actual question D3 asks.
- **P5 — whether n is even a legitimate G_pow chart.**

## 3. Registered predictions

Observables at each n, from M aggregates: four scale-like quantile spreads
(q₇₅−q₂₅, q₉₀−q₁₀, q₉₈−q₀₂, q₉₉.₅−q₀.₅) and two dimensionless shape ratios
(the second and third divided by the first) — so n = 6, matching D8's germ setup.
n swept over 50…2000, four seeds.

**P1 — scale exponents (AT RISK).** Fitted d ln O/d ln n for the scale-like
observables:

| domain | predicted | tolerance |
|---|:--:|:--:|
| A (uniform), L3, L4 | **0.500** | ±0.03 |
| L2 (t, ν = 1.5) | **0.667** = 1/α | ±0.04 |
| L1 (not an aggregate) | **0.000** | ±0.02 |

The shape ratios are predicted to have slopes **|·| < 0.05** for every aggregating
domain, since each converges to *its own* limit law.

**P2 — the residue is degenerate across the transfer boundary (AT RISK; the
primary prediction, and it falsifies D3).** Normalizing each slope vector by its
first component, I predict the projective class is

```
        [1, 1, 1, 1, ~0, ~0]        for A, L2, L3 and L4 alike
```

with the **pairwise residue distance between A and each of L2, L3, L4 below 0.05**,
i.e. no larger for L2 than for L3/L4. Since transfer skill runs 0.484 vs 0.916
across that same boundary, **chart-invariance would then fail to predict transfer,
which is precisely D3's registered falsifier.**

*The outcome that would save D3, registered so it is not dismissible after the
fact:* if the A↔L2 residue distance exceeds the A↔L3 and A↔L4 distances by at
least a factor of 3, the residue does separate the transfer boundary and D3
survives this leg.

**P3 — rank separates L1, not L2 (AT RISK).** L1's aggregate does not depend on n
at all, so its slope vector is zero: rank **0**, count r(n−r) = **0**. Every other
domain has rank **1** and count n − 1 = **5**. So the "count" reading of D3 takes
only **two distinct values across four rungs** and cannot be a four-valued ladder.
Predicted rank vector across (A, L1, L2, L3, L4) = (1, 0, 1, 1, 1).

**P4 — the predictive comparison (AT RISK; the question D3 actually asks).** Rank
the four rungs by each candidate predictor and compare to the transfer ordering
L1 < L2 < L4 ≈ L3:

- **residue distance** — predicted to separate only L1, giving ties across
  L2/L3/L4 and therefore **failing to place the L2/L3 boundary**;
- **bare exponent distance** |1/α_A − 1/α_B| — predicted **0.000 / 0.167 / 0.000 /
  0.000** for L1(undefined→0.5)/L2/L3/L4, which *does* place the L2/L3 boundary;
- **rung label** — places it by construction.

Predicted verdict: **the chart-free part predicts the wrong boundary and the
gauge-looking magnitude predicts the right one.**

**P5 — is n a legitimate chart? (AT RISK).** D7's whole apparatus needs G_pow to be
available. It is not automatic: [P-D](../PD-allometry-reduction/)'s leg F found that
**extensivity pins a chart to G_diff**, where exponents are facts. n is a *count of
contributions*, and aggregation composes: n₁ then n₂ contributions is n₁ + n₂.
Under n ↦ n^a with a ≠ 1 that additivity breaks. Predict an additivity defect of
**0 at a = 1** and **> 20% at a = 1.5, 2 and 0.5**, exactly as P-D measured for
mass. If so, G_pow was never available here, the magnitudes are facts by D2's rule
(i), and P4's verdict is not a paradox but a consequence.

**P6 — reproduce the harness (CONSISTENCY CHECK).** Transfer skills within **±0.02**
of 0.033 / 0.484 / 0.916 / 0.894.

## 4. What would kill the *registration* (not just D3)

- **P1 fails** — the exponents do not come out at 1/2 and 2/3, so the observables
  are not measuring what I think and nothing downstream means anything.
- **P2 comes out the D3-saving way** — then D3 survives its own falsifier, the
  ladder *is* a chart-invariance count on this harness, and §0's warning about
  self-flattery was misplaced. Registered as a real possibility.
- **P5 fails** (additivity survives re-charting) — then n *is* a G_pow chart, the
  exponent magnitudes are gauge, and P4's verdict would mean transfer is predicted
  by something that is not a fact — which would be a much stranger result and would
  need explaining rather than reporting.

## 5. Scope, registered

- **One harness, one family.** Every domain here is "a sum of n contributions," so
  this tests D3 inside the CLT/stable family and nowhere else. A negative here is a
  counterexample to D3 as stated; it is **not** a proof that no chart-invariance
  reading of the ladder works.
- **Four rungs is n = 4.** No correlation computed on four points can reach
  significance, and the paper already recorded this for Spearman(level, skill). The
  argument therefore rests on the *pattern of ties* — which boundary each predictor
  can and cannot place — and not on any coefficient. Tolerances above are set from
  the seed-to-seed spread the harness already publishes, not from expectation;
  that is the specific slip [D7](../D7-residue-projective/) and
  [D8](../D8-grassmannian-residue/) both logged.
- **Estimator resolution checked in advance this time**, per D8's third-category
  slip: residue distances are computed as subspace sines, never as arccos of a
  principal cosine, which floors at √(machine eps).
- The transfer metric is the harness's, including its known ceiling of ~0.92; no
  claim is made about the ~0.08 shortfall, which paper 1 established is metric
  noise.
