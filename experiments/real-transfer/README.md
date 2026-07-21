# The real frontier — the frame on data I did not construct (result)

**Question (SYNTHESIS §6.1):** does the prediction-field frame survive on *real*
data, not just a constructed SCM? The critique of [S18](../S18-invariance-transfer/)
was "invariance = transfer *by construction*." This tests the same claim where I did
not design the structure.

**Status: passed on both legs — the frame's operational core is empirically
load-bearing (cross-environment + a named cross-domain invariant). With one honest
confound named below.**

Run: `python3 run.py` (needs `scikit-learn` for the real dataset) → `python3 plot.py`
→ [`real_transfer.png`](./real_transfer.png).

## Leg A — invariance ⇒ transfer on a real dataset (diabetes)

sklearn's diabetes dataset (442 real patients). Environments = **age quartiles** —
genuine subpopulations I did not engineer. For each candidate predictor: measure the
stability of its relationship to disease-progression *across age groups* (invariance,
on training envs) and its predictive R² on a *held-out* age group (transfer,
leave-one-environment-out).

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

**Spearman(invariance, transfer) = 0.983** — essentially matching the synthetic
S18 (0.985), now on real data. And it's interpretable: **bmi** and **s5** (a
serum measure) have relationships to progression that are stable across age groups
and transfer; **sex** (univariately) is unstable across age groups and fails to
transfer to a new one. Stability measured on the training age groups ranks
held-out-group predictive power almost perfectly.

### The honest confound (important)

On real data I cannot cleanly separate **invariance** from **signal strength**. A
strong predictor (bmi) has both a stable slope *and* good transfer; a weak/noisy
one (sex, s2) has an unstable slope estimate (partly just estimation noise in small
environments) *and* poor transfer. So ρ = 0.983 is partly "strong features are both
stable and transferable," which is *related to* but not *identical to* the causal-
invariance claim. The synthetic [S18](../S18-invariance-transfer/) **controlled for
this** — there the spurious feature was the *strongest* in-distribution predictor
yet still failed to transfer, decoupling strength from invariance. The two results
are complementary: S18 isolates the mechanism; this shows the relationship survives
in messy, uncontrolled real data.

## Leg B — a named invariant transferring across genuinely different domains

Benford's law, P(d) = log₁₀(1 + 1/d), emerges in sequences spanning many orders of
magnitude via multiplicative growth. Tested across computable domains where the
mechanism holds vs controls where it doesn't:

| domain | shares mechanism? | TV → Benford | transfer skill |
|--------|:----------------:|:------------:|:--------------:|
| 2ⁿ | ✓ | 0.001 | 1.00 |
| 3ⁿ | ✓ | 0.002 | 0.99 |
| n! | ✓ | 0.028 | 0.90 |
| Fibonacci | ✓ | 0.001 | 0.99 |
| uniform[100,999] | ✗ | 0.271 | 0.00 |
| narrow lognormal | ✗ | 0.607 | 0.00 |

Mechanism domains **0.97** mean skill; controls **0.00**. The invariant transfers
across four *genuinely different generative processes* (geometric, factorial,
additive) and fails on distributions that merely share the "leading digit" surface —
the same L3/L4-vs-L1 pattern as the [ladder test](../ladder-vs-transfer/), now for a
*named, real* invariant with a known mechanism (scale invariance).

## Verdict for the frame

The real frontier test **passed**. On data whose structure I did not design:
invariance predicts transfer (ρ = 0.983, real dataset), and a genuine mechanism-
backed invariant transfers across domains while surface-only patterns do not
(0.97 vs 0.00). This lifts the [prediction-field frame](../../PREDICTION-FIELD.md)'s
🟢 operational core from "demonstrated in a constructed SCM" to **"holds on real,
uncontrolled data"** — the frame is empirically load-bearing.

## Honest scope (what would still strengthen it)

- **Leg A is cross-*environment*** (age groups in one dataset), not cross-scientific-
  domain, and carries the signal-strength confound above.
- **Leg B's "domains" are computable sequences**, chosen because Benford emergence
  is real and doesn't require unreliable hand-entered real-world data — but they are
  mathematical, not empirical measurements.
- The **fullest** version remains open: many *different real datasets from different
  fields*, several *different* catalog invariants, measured A→B. This is two solid
  rungs up from synthetic, not the summit.

## Next

- A multivariate / residual-invariance version of Leg A that regresses out signal
  strength, to break the confound on real data.
- Add a third real dataset (wine cultivars, breast-cancer subtypes) as independent
  environments to check the ρ holds across datasets.
