# What Makes a Cross-Domain Correspondence Transfer

**Depth of correspondence predicts predictive transfer — and the operative
difference is a ceiling, not a step**

*Cross-Domain Invariants project · paper 1 · 2026-07-26*

---

## Abstract

Claims that two unrelated fields "obey the same law" are cheap to make and hard
to grade. This project maintains an explicit **correspondence ladder** — L0 shared
word, L1 shared structure, L2 shared mathematical form, L3 shared generative
mechanism, L4 provable universality — as hygiene against selling metaphors at
universality prices. The ladder was built as bookkeeping. This paper asks whether
it is also *predictive*: does a correspondence's level tell you how well a law
learned in one domain transfers to another?

We report three experiments. (1) In a controlled structural causal model, the
stability of a predictor's relationship across training environments ranks its
error on a held-out environment at Spearman ρ = 0.985, and the *most*
in-distribution-predictive feature is the *worst*-transferring (transfer MSE 7.71
vs 0.95). (2) Holding a surface phenomenon fixed ("a macroscopic quantity is the
aggregate of n microscopic contributions") and varying only the depth at which a
Gaussian limit law actually applies, transfer skill runs 0.033 / 0.484 / 0.916 /
0.894 across L1 / L2 / L3 / L4. (3) On data we did not construct, invariance
predicts transfer at ρ = 0.983 (permutation p = 6 × 10⁻⁵) on a real clinical
dataset with age-quartile environments, and Benford's law transfers across four
structurally unrelated generative processes (mean skill 0.97) while failing on
surface-matched controls (0.00).

We also report a **correction to this project's own headline reading**. The
previously stated result — a "cliff at the L2/L3 boundary," with transfer
"near-useless at L1–L2" — is not what the data show. The adjacent steps are
L1→L2 = 0.451 and L2→L3 = 0.432: statistically indistinguishable in size. What is
genuinely special about the L2/L3 boundary is not the size of the step but the
**ceiling**. Measuring the metric's own ceiling for the first time — by scoring a
domain against an independent draw of itself — gives 0.920 ± 0.023, and as
evidence grows (n = 2 → 1024) L3 and L4 climb to exactly that value while L2
saturates at ~0.54, bounded away from it permanently. L3 does not merely transfer
well; it transfers as well as the law transfers to itself. The honest claim is
therefore *not* "form buys nothing and mechanism buys everything," but **"more
evidence redeems a shared mechanism and never redeems a shared form."** L3 ≈ L4
throughout (step −0.022): a theorem transfers no better than the mechanism it
certifies.

---

## 1. The problem

Cross-domain correspondence is the most seductive move in science communication
and one of the most productive in science itself. Power laws in earthquakes and
in city sizes; criticality in magnets and in neural avalanches; "selection" in
biology, in markets, in ideas. Some of these are among the deepest results we
have. Others are puns.

The distinguishing question is rarely asked in a form that admits an answer.
"Is the analogy real?" has no operational content. This project's wager is that
the useful version is:

> **Does a prediction made in domain A survive the trip to domain B?**

That reframing is what makes the [correspondence
ladder](../METHODOLOGY.md) more than a taxonomy. If the ladder's levels are
degrees to which *a prediction transfers across a domain boundary*, then the
ladder makes a testable claim about itself: level should predict transfer. If it
doesn't, the ladder is decorative and should be demoted to a labeling
convention.

This paper tests that claim three times, at increasing distance from our own
design choices.

### 1.1 The ladder

| Level | Shared | Buys you | Typical failure |
|:-----:|--------|----------|-----------------|
| **L0** | a word | nothing predictive | "momentum" of a sales team |
| **L1** | a relational structure | hypothesis generation | mistaking map for territory |
| **L2** | a mathematical form — same distribution, same PDE | quantitative transfer of *technique* | same form, unrelated mechanism |
| **L3** | a generative mechanism — the same process produces the pattern | explanation + intervention | convergent-but-distinct mechanisms read as one |
| **L4** | a universality argument — RG, a CLT-type theorem, a symmetry principle | prediction of *new* systems | "universality inflation" |

Full definitions and evidence standards: [`METHODOLOGY.md`](../METHODOLOGY.md).
The key methodological rule is that a correspondence's headline level is the
highest level *actually defended*, and that convergent-but-distinct mechanisms
must be labeled as such rather than silently promoted to L3.

### 1.2 The frame

The ladder sits inside a broader organizing frame, developed in
[`PREDICTION-FIELD.md`](../PREDICTION-FIELD.md): what we map is not a catalog of
observed recurrences but the **measurement-invariant predictive structure** of a
system — the part of what-can-be-predicted that does not depend on which domain
you look through or how you measure. Under that frame, an invariant just *is* a
symmetry of the prediction field, and the ladder is a transfer-of-prediction
scale.

The frame is stated with explicit tiering, and this paper tests only its
operational tier — the reading on which "map the invariants" and "chart the
measurement-independent predictive structure" are the same task stated twice. The
frame's stronger metaphysical reading ("prediction is ontologically prior to
measurement") is held as scaffolding and is *not* under test here; a separate
experiment tested it directly and [declined to promote
it](../experiments/S25-channel-independence/).

---

## 2. Experiment 1 — invariance predicts transfer, and in-distribution fit anti-predicts it

**Source:** [`experiments/S18-invariance-transfer/`](../experiments/S18-invariance-transfer/)
· `run.py`, pure numpy, deterministic.

### 2.1 Design

A linear structural causal model with one invariant mechanism and one spurious
correlate, instantiated across environments indexed by `e`:

```
X_c ~ N(0, 1)                          # a genuine cause of Y
Y   = a·X_c + ε_y,   ε_y ~ N(0, 1)     # INVARIANT: coefficient a fixed across e
X_s = b_e·Y + ε_s,   ε_s ~ N(0, 0.3²)  # X_s is an EFFECT of Y; coupling b_e varies
```

Training environments use `b_e ∈ {0.8, 1.0, 1.2, 1.5}`; the held-out test
environment uses `b = −1.2` — outside the training range *and* sign-flipped.
Because `ε_s` is small, `X_s` is deliberately the stronger in-distribution
predictor, so empirical risk minimization is drawn to it.

We sweep a one-parameter predictor family `Z(α) = (1−α)·X_c + α·X_s` over
α ∈ [0, 1] on z-scored features, and measure two quantities from **disjoint
data**: *instability*, the normalized standard deviation of `Z(α)`'s fitted
slope across the four training environments; and *transfer error*, MSE on the
held-out environment for a model pooled-fit on training. Invariance never sees
the test environment; transfer error never sees the training spread. A
relationship between them is therefore an empirical finding rather than an
identity.

This is the ICP / IRM setting (Peters et al. 2016; Arjovsky et al. 2019),
used here as an instrument rather than as a contribution.

### 2.2 Results

| Quantity | Value |
|----------|:-----:|
| in-distribution MSE, spurious feature only | **0.160** |
| in-distribution MSE, causal feature only | 0.986 |
| transfer MSE, spurious only | **7.705** |
| transfer MSE, causal only | **0.952** |
| transfer MSE, ERM on both | 6.564 |
| Spearman(train instability, held-out error) | **0.985** |
| ICP-style stability selection picks | **X_c (causal)** |

Three findings. **The inversion:** as the predictor slides causal → spurious,
in-distribution error falls 6× while transfer error rises 8×. The best
in-distribution model is the worst-transferring one. **Invariance ranks
transfer:** instability measured only on training environments almost perfectly
orders held-out error. **Selection works blind:** choosing the most stable
feature recovers the causal one without ever touching the test environment.

Figure: [`s18_result.png`](../experiments/S18-invariance-transfer/s18_result.png).

### 2.3 What this does and does not establish

The decisive caveat is that **invariance, causation and transfer coincide by
construction here.** The SCM was built so the invariant mechanism is the causal
one, so the experiment validates the internal logic — that train-time invariance
is a usable, non-circular *estimator* of test-time transfer, and that ERM is
seduced by the spurious feature — without establishing anything about naturally
occurring correspondences. It is also linear and Gaussian, and invariance is
certified only over the environments sampled; a predictor invariant across the
environments you happened to see can still break outside their span. Here the
invariant one holds globally because the SCM guarantees it, which real data does
not.

The ρ = 0.985 is computed over 41 points of a swept one-parameter family, which
are strongly dependent. It should be read as *"the ordering is clean,"* not as a
statistic with 41 degrees of freedom. Section 4 supplies the leg where a
significance test is meaningful.

---

## 3. Experiment 2 — varying correspondence depth with the phenomenon held fixed

**Source:** [`experiments/ladder-vs-transfer/`](../experiments/ladder-vs-transfer/)
· `run.py`, `vary_n.py`, pure numpy, deterministic, 8 seeds.

### 3.1 Design

Experiment 1's weakness is that invariance and transfer were linked by our own
construction. This experiment removes that by making the transfer outcome a
consequence of **probability theory** rather than of our design.

We hold the *surface phenomenon* fixed across all conditions — "a macroscopic
quantity is the aggregate of n = 200 i.i.d. microscopic contributions" — and
learn the law in a reference domain A (uniform increments): *the normalized
aggregate is Gaussian.* We then vary only how deeply that Gaussian invariant
actually applies in domain B, which is exactly the correspondence level:

| Level | Domain B | Why that level | Theory predicts |
|:-----:|----------|----------------|-----------------|
| **L4** | exponential increments | finite variance ⇒ the CLT is a **theorem**, despite a completely different micro-law | Gaussian — transfers |
| **L3** | skewed finite-variance mixture (10% jump component) | **same mechanism** (CLT), mild finite-n skew | Gaussian — transfers |
| **L2** | Student-t increments, ν = 1.5 (**infinite variance**) | same "sum of many" *appearance*; converges to an α-stable law, a different universality class | not Gaussian — fails |
| **L1** | a single heavy draw — no aggregation at all | shares only the word "combine" | irrelevant — fails |

The level assignments are justified by real theory (finite vs infinite variance;
theorem vs none — Gnedenko & Kolmogorov 1954), not by the outcome, so a
level ⇒ transfer relationship is a consequence rather than a construction.

**Metric.** Robustly standardized shape distance: each sample is centered by its
median and scaled by its interquartile range, then compared to A's learned shape
by 1-D Wasserstein distance over the [0.02, 0.98] quantile band (97 grid points).
Skill = 1 − d / d_ref, where d_ref is the distance from a Gaussian to a
maximally-different heavy-tailed shape. Median/IQR standardization is required
because the L2 condition has no finite variance to standardize by.

### 3.2 Results at n = 200

Means over 8 seeds, with per-seed spread from
[`analysis/robustness.py`](./analysis/robustness.py):

| Level | transfer skill | sd | min–max | shape distance |
|:-----:|:--------------:|:--:|:-------:|:--------------:|
| L1 | **0.033** | 0.036 | 0.000–0.088 | 0.209 |
| L2 | **0.484** | 0.038 | 0.411–0.538 | 0.111 |
| L3 | **0.916** | 0.022 | 0.886–0.952 | 0.018 |
| L4 | **0.894** | 0.032 | 0.833–0.933 | 0.023 |

Spearman(level, skill) = 0.80. Seed-wise, the L2 and L3 distributions do not
overlap at all (L2 max 0.538 < L3 min 0.886), and L3 − L2 > 0 in every seed
(mean 0.432, sd 0.051, min 0.347).

Figure: [`ladder_transfer.png`](../experiments/ladder-vs-transfer/ladder_transfer.png).
The left panel shows it directly — the L3 and L4 quantile curves hug A's
Gaussian, while L2 and L1 peel away in the tails, which is where the heavy-tailed
universality class lives.

### 3.3 The shape of the relationship — a correction to our earlier reading

Earlier write-ups in this repository, including
[`METHODOLOGY.md`](../METHODOLOGY.md) and
[essay 1](../essays/01-the-ladder-is-an-epistemology.md), characterized this
result as a **cliff at the L2/L3 boundary**, with transfer "near-useless at
L1–L2" and jumping "to high at L3–L4." Computing the adjacent steps directly
does not support that characterization:

| Adjacent step | Δ skill | sd over seeds |
|---------------|:-------:|:-------------:|
| L1 → L2 | **+0.451** | 0.058 |
| L2 → L3 | **+0.432** | 0.051 |
| L3 → L4 | **−0.022** | 0.042 |

The L1→L2 step is *at least as large* as the L2→L3 step. Paired across the 8
seeds, their difference is 0.019 ± 0.098, **t(7) = 0.56** — nowhere near
distinguishable. At n = 200 the shape is
not "flat, cliff, flat" but **two comparable rises and a flat top**. And L2 at
0.484 is not "near-useless": it is roughly half of the attainable skill. The
original phrasing overstated the case, and we retract it here.

Two readings survive, and they are not equivalent.

**Reading A — L1 is a control, not a rung.** The L1 condition is not an
aggregation at all; it is a degenerate control that shares nothing but a word.
Among the three conditions that genuinely instantiate the surface phenomenon
(L2, L3, L4), there is exactly one step, and it is at L2/L3. On this reading the
original claim survives, restricted to correspondences that are actually
correspondences. This is defensible but weaker than it sounds, because it makes
the claim partly definitional: L1 was excluded by a judgment about what counts
as a rung.

**Reading B — the difference is a ceiling, not a step.** This is the one the
data support without adjudication, and it comes from the `vary_n` sweep below.

### 3.4 The ceiling result

Varying n, the number of contributions per aggregate, from 2 to 1024
([`vary_n_verdict.json`](../experiments/ladder-vs-transfer/vary_n_verdict.json)):

| n | L1 | L2 | L3 | L4 | L3 − L2 |
|---:|:--:|:--:|:--:|:--:|:--:|
| 2 | 0.028 | 0.123 | 0.355 | 0.302 | 0.232 |
| 8 | 0.038 | 0.312 | 0.749 | 0.669 | 0.437 |
| 32 | 0.045 | 0.368 | 0.862 | 0.804 | 0.494 |
| 64 | 0.015 | 0.435 | 0.888 | 0.900 | 0.452 |
| 256 | 0.050 | 0.492 | 0.925 | 0.922 | 0.434 |
| 1024 | 0.023 | **0.542** | **0.933** | **0.923** | 0.392 |

**Where the ceiling actually is.** The claim that L3 and L4 saturate at the
*metric's* ceiling rather than at a genuine transfer deficit is testable
directly, and the source experiment did not test it. We score domain A against an
**independent draw of domain A itself**: the law is identical, so any shortfall
from 1.0 is pure estimation noise in the quantile comparison. Over 8 seeds
([`analysis/robustness.py`](./analysis/robustness.py)):

| self-transfer baseline | mean | sd |
|---|:--:|:--:|
| n = 200 | **0.920** | 0.023 |
| n = 1024 | **0.924** | 0.043 |

So the attainable ceiling is ≈ 0.92, and at n = 200 the L3 condition scores
**0.916** — indistinguishable from transferring the law to *itself*. L3 and L4
are not merely "high"; they are at full transfer within measurement noise. This
also means the ~0.08 shortfall visible in every L3/L4 number is an artifact of
the metric and should not be interpreted.

Three regimes in the asymptotics, and they are the real finding:

1. **L1 never moves.** Flat at ~0.03 across a 512× range of n. With no shared
   mechanism there is nothing for more evidence to converge to.
2. **L3 and L4 climb to the ceiling and stop there** — the measured ceiling of
   0.92, i.e. complete transfer. More evidence makes a genuine shared-mechanism
   correspondence transfer better, up to the limit of what can be detected.
3. **L2 saturates far below, permanently.** It rises and then plateaus at ~0.54,
   roughly 59% of the attainable ceiling. The aggregate of infinite-variance
   increments converges to a fixed α-stable (α = 1.5) law that is *permanently
   non-Gaussian*, so skill converges to a constant bounded away from the ceiling
   and never improves past it.

This licenses a sharper and more defensible statement than "the cliff is at
L2/L3":

> **More evidence redeems a shared mechanism and never redeems a shared form.**

The L2/L3 boundary is where the ceiling becomes attainable. That is a claim about
the *limit* of the correspondence's usefulness rather than about its value at any
one sample size, and it is the version we carry forward.

It also corrects a prediction we made and got wrong. We had conjectured that L2
skill would *fall* as n grows (more data exposing the mismatch). It does not — it
*rises* and then stops. The correct invariant is **"L2 is capped," not "L2
declines,"** and it is logged as a corrected prediction in the source README.

### 3.5 On the ρ = 0.80

Spearman correlation over four levels has n = 4. Its minimum attainable two-sided
p-value is 1/12 ≈ 0.083, so it cannot reach conventional significance regardless
of the data, and it should not be read as a test. The load-bearing statistics
here are the per-seed separation (§3.2: no overlap between L2 and L3 across 8
seeds) and the asymptotic separation (§3.4: divergent ceilings across 10
independent values of n). We report ρ for continuity with the source experiment
and give it no inferential weight.

### 3.6 Limitations

- **Controlled within one invariant family.** Everything here lives in the
  CLT / stable-law universe. It shows that *depth of correspondence* controls
  transfer when the surface phenomenon is held fixed — the cleanest available
  isolation — but it is a single family, and the ladder claims to apply across
  all of them.
- **Synthetic.** The mechanisms are genuinely different from one another (a real
  step past Experiment 1), but they are generated rather than observed.
- **The metric is generous to L2.** Trimming the extreme 2% of quantiles is
  necessary for the infinite-variance conditions, and it flatters exactly those
  conditions: untrimmed, L2's heavy tails would push its skill lower and the
  L2/L3 separation would widen. The robust claim is *bounded away from the
  ceiling*, not the specific value 0.54.
- **L3 vs L4 is a distinction we imposed.** Both conditions have finite variance
  and are covered by the CLT; the labels encode whether we treat the limit as an
  invoked theorem or a shared mechanism. That they score identically is
  consistent with the distinction being about epistemic warrant rather than about
  the physics — but the experiment cannot separate "L3 and L4 transfer equally"
  from "L3 and L4 were never two conditions."

That last point deserves emphasis, because it is the sharpest internal
limitation of the experiment and it is not stated in the source write-up.

---

## 4. Experiment 3 — on data we did not construct

**Source:** [`experiments/real-transfer/`](../experiments/real-transfer/)
· `run.py`, numpy + scikit-learn, deterministic.

### 4.1 Leg A — invariance ⇒ transfer on a real dataset

The diabetes dataset of Efron et al. (2004), 442 real patients, as distributed
with scikit-learn. Environments are **age quartiles** — genuine subpopulations we
did not engineer. For each candidate predictor (age itself excluded, since it
defines the environments) we measure invariance as the cross-environment
stability of its univariate slope against disease progression, and transfer as
leave-one-environment-out R² on the held-out age group.

| feature | invariance | transfer R² |
|:-------:|:----------:|:-----------:|
| **bmi** | 0.851 | **+0.289** |
| bp | 0.834 | +0.150 |
| **s5** | 0.827 | +0.265 |
| s4 | 0.812 | +0.132 |
| s6 | 0.764 | +0.092 |
| s3 | 0.747 | +0.075 |
| s1 | 0.542 | −0.025 |
| s2 | 0.446 | −0.060 |
| **sex** | 0.135 | **−0.077** |

**Spearman(invariance, transfer) = 0.983**, essentially matching the synthetic
0.985 — now on data whose structure we did not design. Unlike the swept family in
Experiment 1, these are 9 independent units, so a significance test is
meaningful: a 200,000-draw permutation test gives **two-sided p = 6 × 10⁻⁵**
([`analysis/robustness.json`](./analysis/robustness.json)); the smallest
attainable p at n = 9 is 5.5 × 10⁻⁶.

The result is also interpretable rather than merely numerical. BMI and s5 (a
serum measure) have relationships to progression that are stable across age
groups and that transfer to a held-out age group. Sex, taken univariately, is
unstable across age groups and transfers negatively — a model fit on three age
quartiles predicts the fourth *worse than its mean*.

**The confound, stated plainly.** On real data we cannot cleanly separate
**invariance** from **signal strength**. A strong predictor has both a stable
slope and good transfer; a weak, noisy one has an unstable slope estimate —
partly just estimation noise within small environments — and poor transfer. So
ρ = 0.983 is partly measuring "strong features are both stable and
transferable," which is *related to but not identical with* the causal-invariance
claim. This is precisely what Experiment 1 controls for and this leg cannot: in
the SCM the spurious feature was the *strongest* in-distribution predictor and
still failed to transfer, decoupling strength from invariance. The two legs are
complementary, and neither alone is sufficient. Breaking this confound — a
residual-invariance version that regresses out signal strength — is the single
most valuable follow-up to this paper.

### 4.2 Leg B — a named invariant across genuinely different mechanisms

Benford's law, P(d) = log₁₀(1 + 1/d), arises in sequences that span many orders of
magnitude via multiplicative growth; its mechanism is scale invariance (Hill
1995). We test it where the mechanism holds versus controls that share only the
surface ("these are numbers and they have leading digits").

| domain | mechanism? | TV → Benford | transfer skill |
|--------|:----------:|:------------:|:--------------:|
| 2ⁿ | ✓ | 0.0012 | 1.00 |
| 3ⁿ | ✓ | 0.0016 | 0.99 |
| n! | ✓ | 0.0278 | 0.90 |
| Fibonacci | ✓ | 0.0013 | 0.99 |
| uniform[100, 999] | ✗ | 0.2709 | 0.00 |
| narrow lognormal | ✗ | 0.6066 | 0.00 |

Mechanism domains: mean skill **0.97**. Controls: **0.00**. The invariant
transfers across four genuinely different generative processes — geometric
(2ⁿ, 3ⁿ), factorial (n!), and linear-recurrence/additive (Fibonacci) — and fails
on distributions that share the leading-digit surface but not the mechanism.
That is the same L3/L4-vs-L1 pattern as Experiment 2, now for a named invariant
with a known mechanism rather than a constructed one.

Figure: [`real_transfer.png`](../experiments/real-transfer/real_transfer.png).

### 4.3 Limitations

- **Leg A is cross-*environment*, not cross-domain.** Age quartiles within one
  clinical dataset are subpopulations, not different scientific fields. It
  escalates past synthetic; it is not the cross-field study.
- **Leg A is univariate and single-dataset.** Slopes are fit one feature at a
  time, and n = 9 features from one study. Adding independent datasets (wine
  cultivars, breast-cancer subtypes) is a cheap and obvious check that has not
  been run.
- **Leg B's "domains" are computable sequences**, chosen because Benford
  emergence in them is real and does not depend on unreliable hand-collected
  data — but they are mathematical objects, not empirical measurements.
- **The controls were chosen by us.** They are honest controls (they do share the
  surface feature), but a pre-registered control set would be stronger.

---

## 5. What the three experiments jointly support

| Claim | Evidence | Strength |
|-------|----------|:--------:|
| Train-time invariance is a usable, non-circular estimator of held-out transfer | E1 (ρ = 0.985, disjoint data), E3-A (ρ = 0.983, p = 6e-5, real data) | **strong** |
| In-distribution fit can *anti*-predict transfer | E1 (6× better in-distribution, 8× worse on transfer) | **strong**, but in a constructed SCM |
| Correspondence depth orders transfer | E2 (0.03 / 0.48 / 0.92 / 0.89), E3-B (0.97 vs 0.00) | **strong** on ordering |
| The L2/L3 boundary is where the transfer ceiling becomes attainable | E2 `vary_n` (L2 → 0.54, L3/L4 → 0.92 over 512× in n) against a measured ceiling of 0.920 ± 0.023 | **moderate** — one invariant family |
| L3/L4 achieve *complete* transfer, not merely high transfer | §3.4 self-transfer baseline (L3 = 0.916 vs ceiling 0.920) | **strong** within this metric |
| The step at L2/L3 is uniquely large | — | **not supported; retracted** (§3.3) |
| L3 ≈ L4 in transfer | E2 (Δ = −0.022) | **suggestive** — the two conditions may not be distinct (§3.6) |

---

## 6. Why the boundary sits where it does

Two features of the result want explanation: why sharing the mathematics of a
phenomenon buys a capped amount of transfer, and why a universality theorem buys
nothing beyond the mechanism it certifies.

### 6.1 Form is a statement about a point; mechanism is a statement about a neighborhood

An equation, taken alone, summarizes *actual* behavior. Transfer is a demand on
*counterfactual* behavior: carrying a result from A to B implicitly answers "if
conditions shift this way, does the pattern persist?" A functional form is silent
about which perturbations preserve *itself* — that information lives one level
down, in whatever process produced the equation as its coarse description. This
is the familiar point from Cartwright (1983) and Pearl (2009) that laws-as-forms
carry no modal force of their own: a structural model supports interventions
because it specifies mechanisms, while a fitted curve, however well fitted,
supports only interpolation.

The ceiling result gives this a quantitative face. Two domains sharing a form
agree at the conditions where both were measured. Two domains sharing a mechanism
agree on a *neighborhood* — the mechanism specifies how each responds to
perturbation. More evidence explores more of the neighborhood, which is why L3
and L4 improve with n and L2 does not: additional samples reveal more of the
α-stable law that was there all along, and none of them make it Gaussian.

### 6.2 A theorem is a warrant, not a vehicle

The flat top (L3 ≈ L4) is the quieter result. Universality theorems are the crown
jewels of cross-domain science, so it is surprising that one transfers no better
than an identified mechanism.

The proposed resolution is that they play different roles and only one is a
vehicle. The mechanism is *what transfers*: it is literally present in both
domains, generating the pattern twice. The theorem is *why you were entitled to
expect that*: it certifies in advance, for a whole class, that microscopic
differences wash out. Certification changes your confidence and your search
strategy; it does not change what crosses the boundary. Once the shared mechanism
is in hand, the guarantee is epistemically posterior — it converts "this worked"
into "this had to work," which is worth a great deal for deciding where to look
next and nothing for the transfer already achieved.

If that is right, the ladder encodes a division of labor it was not designed to
express: **L3 is the unit of explanation** (to explain is to exhibit the
generator) and **L4 is the unit of justified generalization** (to prove
universality is to license expectations about systems not yet met). Our
experiment measured only the first task, so it saw them as equals.

We flag §3.6's caveat again here: the experiment cannot fully distinguish this
account from the possibility that its L3 and L4 conditions were never two
conditions. §6.2 is an interpretation, not a measurement.

### 6.3 A conjecture, flagged as such

Why should the levels differ in ceiling rather than smoothly in value? A guess:
the levels differ in **what they compress**. An L2 identity compresses the *data*
of two domains into one formula; an L3 identity compresses the *explanations*
into one generator. Transfer is a question posed to the explanation — "will this
hold over there?" is a why-question in disguise — so transfer skill should track
explanatory compression and be capped by descriptive compression alone.

This yields a falsifiable reading. Any performance measure that is a function of
the *data summary* alone — in-distribution fit, retrodiction, interpolation —
should show **no L2/L3 gap**, with L2 sufficient and uncapped. Any measure
requiring *counterfactual* correctness — transfer, intervention, extrapolation —
should show the cap. Half of this is already visible in Experiment 1's
spurious-feature inversion. The other half, showing L2 correspondences are fully
sufficient for non-modal tasks, has not been tested and is a clean experiment.
If someone exhibits a non-modal task with an L2/L3 cap, this section is wrong.

---

## 7. Independent corroboration from elsewhere in the project

The L3/L4 distinction — mechanism as vehicle, theorem as warrant — was drawn on
methodological grounds before these transfer measurements. Three unrelated
experiments in this project have since produced the same shape without being
aimed at it. Each took a "one law across domains" claim and found that **the
mechanism survives and the exponent does not.**

**Critical slowing down** ([S7](../experiments/S7-critical-slowing/)). Testing
τ · λ_min = 1 across an ecology-style saddle-node, a mean-field Ising model, and
gradient descent at the interpolation threshold: the relation holds at
**0.94 ± 0.13** across 15 points, three domains, and two distinct notions of
"time," with no per-domain tuning. The *divergence exponents* do not transfer at
all — fitted −0.55, −0.73, −2.05 against theory −½, −1, −2. One shared mechanism
(curvature softening sets the slowest timescale) composed with a domain-specific
curve.

**Noise thresholds** ([S5](../experiments/S5-noise-thresholds/)). Asking whether
Shannon capacity, Eigen's error catastrophe, and the quantum fault-tolerance
threshold are one redundancy-vs-noise transition: the single-exponent premise
**fails**, with α spanning 1.00 to 3.17 — and the variation is *within* domains,
not across them (coding theory alone supplies both 1.00 and 2.00). What replaced
it is sharper than what failed: α is a **degeneracy order**, 2 for a smooth
metric merge (forced by the Fisher expansion, measured to within 0.035), 1 for
support loss (to 0.0000), and ln n₀/ln(t+1) for a decoder's RG fixed point
(verified to 1.6 × 10⁻⁴). Same mechanism class, different exponents, and the
exponent tells you which sub-mechanism you are looking at.

**Spectral gap** ([P-A](../experiments/PA-spectral-gap/)). Testing whether
gap-closure is a free-energy Hessian degeneracy, with the free energy fixed in
advance: the mechanism holds, but the Kuramoto synchronization constant
K_c · λ₂ is **family-specific** (0.410–0.632) rather than universal. A registered
prediction — that the spread would exceed 2× — failed as written; it is 1.54×.

Three independent instances of one pattern: **claims of the form "the same
mechanism" survive; claims of the form "the same number" do not.** That is the
L3/L4 line showing up unbidden in results that were not looking for it, which is
the best kind of corroboration available for a methodological distinction. It is
not independent *evidence for the transfer measurements* — different systems,
different quantities — but it is independent evidence that the line the
measurements found is a real seam in the material.

---

## 8. What would falsify the central claim

Stated so that the claim is refutable rather than merely defended:

1. **A capped L3.** A correspondence with a genuinely shared mechanism whose
   transfer skill plateaus below the ceiling as evidence grows. This would break
   the ceiling reading directly.
2. **An uncapped L2.** A shared-form-only correspondence whose transfer skill
   climbs to the ceiling given enough data. Equivalent to (1) from the other side.
3. **A non-modal task with an L2/L3 gap** (§6.3). Would refute the compression
   conjecture while leaving the main result standing.
4. **L4 > L3 on transfer.** A setting where possessing the universality theorem
   measurably improves transfer beyond possessing the mechanism. Would refute
   §6.2's warrant/vehicle division.
5. **Invariance and transfer decoupling once signal strength is controlled on
   real data** (§4.1). The live one: if the residual-invariance version of Leg A
   destroys ρ = 0.983, the real-data leg reduces to "strong features transfer,"
   and only the synthetic legs support the frame.

---

## 9. What we claim, and at what level

Applying this project's own ladder to this project's own result:

- **"Train-time invariance estimates held-out transfer" — L3, demonstrated.** The
  mechanism is identified (invariance across environments is the signature of the
  stable structural relationship), and it holds in a constructed SCM, on real
  clinical data, and for a named invariant across unrelated generative processes.
- **"Correspondence depth orders transfer" — L2–L3, one family.** Ordering is
  clean and reproducible; the mechanism (form vs mechanism as point vs
  neighborhood) is argued in §6.1 but has been measured in only one invariant
  family.
- **"The L2/L3 boundary is where the transfer ceiling becomes attainable" — L2,
  with a mechanism proposed.** This is the paper's main contribution and it rests
  on a single sweep in a single family. It is a candidate, not a finding.
- **"The step at L2/L3 is uniquely large" — retracted.** Previously asserted in
  this repository; not supported by the adjacent-step decomposition (§3.3).

The honest summary is that the ladder has earned promotion from a labeling
convention to an operational predictor of transfer *ordering*, and that its most
interesting property — the ceiling at L2 — is established in one corner of one
family and should be treated as the next thing to attack rather than as a
result to build on.

---

## 10. Reproduction

All experiments are pure numpy (Leg A of Experiment 3 additionally requires
scikit-learn), deterministic, and seeded. Every number in this paper was
regenerated on 2026-07-26 and matches the committed verdicts bit-for-bit.

```
python3 experiments/S18-invariance-transfer/run.py      # Experiment 1
python3 experiments/ladder-vs-transfer/run.py           # Experiment 2
python3 experiments/ladder-vs-transfer/vary_n.py        # Experiment 2, ceiling sweep
python3 experiments/real-transfer/run.py                # Experiment 3
python3 paper/analysis/robustness.py                    # §3.2, §3.3, §4.1 statistics
```

The per-seed spreads (§3.2), the adjacent-step decomposition (§3.3), the
self-transfer ceiling baseline (§3.4), and the permutation test (§4.1) are new to
this paper and produced by
[`analysis/robustness.py`](./analysis/robustness.py) →
[`analysis/robustness.json`](./analysis/robustness.json).

---

## References

Arjovsky, M., Bottou, L., Gulrajani, I., Lopez-Paz, D. (2019). *Invariant Risk
Minimization.* arXiv:1907.02893.

Cartwright, N. (1983). *How the Laws of Physics Lie.* Oxford University Press.

Clauset, A., Shalizi, C. R., Newman, M. E. J. (2009). Power-law distributions in
empirical data. *SIAM Review* 51(4), 661–703.

Crutchfield, J. P., Young, K. (1989). Inferring statistical complexity.
*Physical Review Letters* 63, 105.

Efron, B., Hastie, T., Johnstone, I., Tibshirani, R. (2004). Least angle
regression. *Annals of Statistics* 32(2), 407–499. *(Source of the diabetes
dataset used in §4.1.)*

Eigen, M. (1971). Selforganization of matter and the evolution of biological
macromolecules. *Naturwissenschaften* 58, 465–523.

Gnedenko, B. V., Kolmogorov, A. N. (1954). *Limit Distributions for Sums of
Independent Random Variables.* Addison-Wesley.

Gottesman, D. (2013). Fault-tolerant quantum computation with constant overhead.
arXiv:1310.2984.

Hill, T. P. (1995). A statistical derivation of the significant-digit law.
*Statistical Science* 10(4), 354–363.

Marchenko, V. A., Pastur, L. A. (1967). Distribution of eigenvalues for some sets
of random matrices. *Mat. Sb.* 72(4), 507–536.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*, 2nd ed.
Cambridge University Press.

Peters, J., Bühlmann, P., Meinshausen, N. (2016). Causal inference by using
invariant prediction. *JRSS-B* 78(5), 947–1012.

Scheffer, M. et al. (2009). Early-warning signals for critical transitions.
*Nature* 461, 53–59.

Shannon, C. E. (1948). A mathematical theory of communication. *Bell System
Technical Journal* 27, 379–423 and 623–656.

---

## Internal evidence index

| § | Result | Source |
|---|--------|--------|
| 2 | invariance ⇒ transfer, SCM | [`experiments/S18-invariance-transfer/`](../experiments/S18-invariance-transfer/) |
| 3 | level ⇒ transfer, controlled | [`experiments/ladder-vs-transfer/`](../experiments/ladder-vs-transfer/) |
| 4 | real data + Benford | [`experiments/real-transfer/`](../experiments/real-transfer/) |
| 7 | mechanism survives, exponent doesn't | [S7](../experiments/S7-critical-slowing/) · [S5](../experiments/S5-noise-thresholds/) · [P-A](../experiments/PA-spectral-gap/) |
| 1.1 | the ladder | [`METHODOLOGY.md`](../METHODOLOGY.md) |
| 1.2 | the frame | [`PREDICTION-FIELD.md`](../PREDICTION-FIELD.md) |
| 6 | prior discussion of the boundary | [essay 1](../essays/01-the-ladder-is-an-epistemology.md) |
| — | state of the whole map | [`SYNTHESIS.md`](../SYNTHESIS.md) |
