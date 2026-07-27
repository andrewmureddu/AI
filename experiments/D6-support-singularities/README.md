# D6 — do support-type singularities have a classifier? (result)

**Question ([D6](../../questions/UNKNOWN-LAWS.md)):** the remainder
[D2](../../derivations/D2-gauge-of-the-tower.md) left open.
[D1](../D1-chart-invariance/) classified floor 3 by the degeneracy order *p* — the
first non-vanishing anharmonic term of Φ — but support-type singularities (S5's
type S) have no *p*. Separate class, p = ∞, or was D1 a special case?

**Status: D1 was a special case. Floor 3's classifier is the ratio of the two
leading exponents of Φ, and *p* is the slice where smoothness pins the first of
them to 2. Support loss is not p = ∞ — it is a different value in the *other*
slot.** All three at-risk legs pass, and for the first time in this arc none of
them are physics.

Run it: `python3 run.py` (numpy only, ~12 min, deterministic — seed 20260726).
Registered first, and committed before the results:
[`PREREGISTRATION.md`](./PREREGISTRATION.md).

---

## The claim

Write the two leading terms of Φ at the singular point, with **A → 0** the control:

```
        Phi(y) = A|y|^q1 + B|y|^q2 + (higher),   q1 < q2
   =>   A_c  ~  D^((q2-q1)/q2)  =  D^(1 - q1/q2)
```

- **q1 = 2** is what *smoothness* forces, and gives D1's (p−2)/p with q2 = p.
- **q1 = 1** is a kink or a boundary — support loss — where D1's formula is not
  wrong but **undefined**, there being no quadratic term to expand.
- **q2 → ∞** is a hard wall.

**The observable had to change.** D1 used R = Var·λ/D, which needs a curvature λ
that a kink does not have. D6 uses distribution *shape*: for a single-term
Φ = A|y|^q the standardized moments depend on q alone, so excess kurtosis reads q
off directly and is defined at q = 1 (Laplace, +3.0000) and q = 2 (Gaussian,
0.0000) alike. A_c is located where the kurtosis crosses the midpoint of its two
limiting values.

## Results

### P1 — the functional form (identity; estimator check)

| (q1, q2) | q1/q2 | measured | predicted | residual |
|---|:--:|:--:|:--:|:--:|
| (2, 4) | 0.500 | 0.5000 | 0.5000 | 1.2e-14 |
| (1, 2) | 0.500 | 0.5000 | 0.5000 | 6.2e-15 |
| (2, 6) | 0.333 | 0.6667 | 0.6667 | 5.3e-15 |
| (1, 3) | 0.333 | 0.6667 | 0.6667 | 7.1e-15 |
| (1, 4) | 0.250 | 0.7500 | 0.7500 | 7.1e-15 |
| (0.5, 2) | 0.250 | 0.7500 | 0.7500 | 1.3e-10 |
| (2, 8) | 0.250 | 0.7500 | 0.7500 | 7.1e-15 |
| (3, 4) | 0.750 | 0.2500 | 0.2500 | 1.6e-14 |
| (1, 6) | 0.167 | 0.8333 | 0.8333 | 5.3e-15 |

Declared in advance as forced. What it does establish non-trivially is that the
**shape estimator works across the whole range** — from q = 0.5 (excess kurtosis
+22.2) to q = 8 (−1.077) — which is the thing D1's observable could not do.

### P2 — the ratio is the classifier

| ratio q1/q2 | pairs | exponents | spread |
|:--:|---|---|:--:|
| 0.250 | (1,4), (0.5,2), (2,8) | 0.7500, 0.7500, 0.7500 | **0.0000** |
| 0.333 | (2,6), (1,3) | 0.6667, 0.6667 | **0.0000** |
| 0.500 | (2,4), (1,2) | 0.5000, 0.5000 | **0.0000** |
| *control:* same q2 = 4 | (2,4), (1,4), (3,4) | 0.5000, 0.7500, 0.2500 | **0.5000** |

Three pairs sharing **no individual exponent** — q1 ∈ {1, 0.5, 2} and
q2 ∈ {4, 2, 8} — land on the same crossover exponent, while three pairs sharing
q2 = 4 spread by 0.5. So neither exponent classifies; the ratio does.

> **Pre-registration error, on record.** P2 was registered as "AT RISK,
> structural." **It is not at risk — it is an identity**, and the registration
> should have said so. Once A_c ∝ D^{1−q1/q2} is forced by the rescaling
> argument (which §2 of the registration *did* declare), the fact that equal
> ratios give equal exponents follows immediately. This is the third registration
> slip in the register's short life, after
> [D1's P5 direction](../D1-chart-invariance/PREREGISTRATION.md) and
> [D2's resampling no-op](../D2-gauge-group/README.md), and the pattern is worth
> naming: **the recurring failure is misclassifying a consequence of my own
> construction as a test of it.** Testing the ratio claim honestly needs *real*
> models with different (q1, q2) sharing a ratio, which this experiment does not
> contain.

### P3 — a real all-orders model with q1 = 1 (AT RISK — passes)

L1-penalized logistic regression, Φ(β) = ℓ(β) + τ|β|, with the design paired on
the margins so the unpenalized optimum sits at 0 and the smooth part carries every
even order. The rescaling argument does not apply to it.

```
        tau_c ~ D^0.5000        predicted 0.5000       max resid 1.6e-04
```

### P4 — M/M/1 has no crossover (AT RISK — passes)

With an infinite buffer the stationary law is geometric at every ρ: q1 = 1 with
**no second term**, so there is nothing to cross over to.

| 1 − ρ | 1e-1 | 1e-2 | 1e-3 | 1e-4 | 1e-5 |
|---|---|---|---|---|---|
| excess kurtosis | 6.0111 | 6.0001 | 6.0000 | 6.0000 | 6.0000 |

Pinned at the exponential value over four decades — mean **6.0014**, spread
**0.0111**, and **no crossover locus exists to fit**. This is the registered
sense in which support loss is *not* p = ∞: p = ∞ would be a value in the q2
slot, and here the q2 slot is empty while q1 = 1.

### P5 — the hard-wall corner (AT RISK — passes)

M/M/1/K with a finite buffer: the wall is q2 → ∞, so the predicted exponent
(q2−q1)/q2 → 1, with 1/K playing the role of D.

```
        A_c vs 1/K:  exponent = 0.9979    predicted 1.0    max resid 2.9e-03
```

So a boundary is not a separate class either — it is the q2 → ∞ corner of the
same classifier, and the limit is continuous.

---

## Verdict

**D6's question dissolves the way D2's did: it presupposed too much.** Support
loss is neither a separate class nor p = ∞. Floor 3's classifier is a **pair** of
exponents, and what classifies is their **ratio**:

```
   q1 = 2   forced by smoothness      ->  D1's degeneracy order, exponent (p-2)/p
   q1 = 1   a kink or a boundary      ->  support loss (S5's type S)
   q2 -> oo a hard wall               ->  exponent 1
```

**D1's *p* was the q1 = 2 slice of a two-parameter family**, and the reason it
looked like the whole story is that smoothness is the generic case — if Φ has a
Taylor expansion, q1 is 2 and only q2 is free to vary.

**This lands where [D2](../../derivations/D2-gauge-of-the-tower.md) said it had
to.** D2 derived that the chart-free residue on floor 3 must be a **ratio**, not a
magnitude, because magnitudes are gauge under G_pow. D6 finds the classifier is
q1/q2 — a ratio — on a class of singularities D2's residue argument (which ran
through codimension, a smooth-germ notion) could not reach. D2's "the residue is
the codimension p − 2" is now visible as the smooth-case face of the more general
statement.

**The physics gap is closed.** D1 and D2 both recorded, and did not close, that
every at-risk leg was physics. D6's three at-risk legs are statistics/ML
(L1-penalized logistic regression) and operations research (M/M/1, M/M/1/K).

---

## Boundaries

- **Essential singularities remain outside, and that is now the whole remainder.**
  If Φ has no leading power at all (Φ ~ exp(−1/y)) there is no q1 and nothing here
  applies. That is a strictly narrower gap than the one D2 left, which was all of
  support-type.
- **P1 and P2 are identities**, one of them mislabeled in the registration and
  corrected above. The evidence is P3–P5.
- **One control parameter, one dimension, additive noise** — inherited from D1
  and not exceeded.
- **The logarithmic corner q1 → 0**, where exp(−Φ/D) becomes a power law and
  should connect to the catalog's heavy-tail entry, is a consequence of the
  formula that was **registered as noted-not-tested** and remains untested. It is
  the obvious next leg.
- **Prior-art risk is real.** Crossover scaling between two competing terms in a
  potential is the same balancing argument as the Ginzburg criterion, already
  flagged as covering D1's formula. If the two-exponent form is standard in the
  multicritical crossover literature, D6's formula is **N0–N1** and only the
  "one classifier across all of floor 3, and it is a ratio" reading survives at
  N2.
- **M/M/1's "no crossover" is a negative result about a specific model**, not a
  theorem that support-type singularities never have a second term. A queue with
  state-dependent service, or any support singularity with curvature further out,
  would have one.
