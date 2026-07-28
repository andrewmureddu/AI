# F3 — only 3b rounds?

**Tests** the sharpest prediction of [`invariants/FLOOR3-STRATA.md`](../../invariants/FLOOR3-STRATA.md),
the sort of floor 3 against the trichotomy
[`derivations/base-variable.md`](../../derivations/base-variable.md) §4 forced.

**Registered in** [`PREREGISTRATION.md`](./PREREGISTRATION.md). Run with
`python3 run.py` (numpy + scipy, seed 20260728, 5 s).

---

## Verdict

> **The registered prediction is wrong, and the correction is the result.** I
> registered *only 3b rounds*, with 3a distinguished by a domain boundary **stable
> in system size**. It isn't: at finite support Φ is entire — the derivation's own
> F-fact — so 3a's boundary appears only in a limit, exactly as 3b's kink does.
> "Stable in system size" was not mis-measured, it was **not well posed**.
>
> What survives is cleaner: classify by **what diverges**. Φ itself, on a region
> (3a); a derivative, at a point (3b); nothing, with a derivative exactly zero
> (3c). All three measured with one instrument, plus a fourth output that turned
> out to be the scheme's useful boundary.
>
> **The one prediction about an entry the sort had no hand in shaping passed** —
> [S25](../S25-rlct-singularity/)'s λ(P) = min(P,D)/2 kink is **3c, not 3b**,
> sharp at every D with an eigenvalue gap of **3.11e-17**. So S25's reported
> finite-size blurring is its **estimator**, not the object.
>
> **1 of 4 at-risk, 2 of 2 identities.** All three failures are criteria I
> mis-specified, none is a claim — the second pass in a row with that shape.

| | registered | measured | |
|---|---|---|---|
| **P1** 3b rounds as N^−1, ≥20× floor | identity (calibration) | **N^−1.001**, **117×** floor | ✓ |
| **P2** 3a's λ_c stable ≤ 1e-6 | **AT RISK** | drift **0.43** — *the claim is not well posed*; repaired below | ✗ |
| **P3** 3c does not round | **AT RISK** | eigen ratio **8.9e-16** ✓, but two mis-specified criteria | ✗ |
| **P4** S25 kink sharp by construction | identity | err **0.0e+00** | ✓ |
| **P5** S25 kink sharp *numerically* | **AT RISK** | gap **3.11e-17** at every D | ✓ |
| **P6** one instrument, three behaviours | **AT RISK** | ✗ as registered; **four** behaviours once repaired | ✗ |

---

## 1. The four signatures

One instrument (FWHM of |Φ″| on a stated grid), one set of tolerances, each
registered against a stated noise floor:

| | exemplar | what the instrument returns |
|---|---|---|
| **3a** | Exp(1) truncated at M | Φ(0.9) → **2.302585093** = −log(0.1), increments **0**; Φ(1.1) grows as **M^0.981** — Φ *itself* diverges, linearly, on a region |
| **3b** | two-state free energy | a **localised** width, **117×** the resolution floor, shrinking as **N^−1.001** |
| **3c** | functionally dependent statistics | **no localised feature** — width = **1.000×** the full window; smallest eigenvalue of the exact ∇²Φ at **8.9e-16** |
| *(type C)* | an argmin crossing | width pinned at the **resolution floor** at every size ([P-K](../PK-kink-taxonomy/)) |

The fourth is not a floor-3 stratum and that is the point: a selector cell boundary
is not a non-analyticity of any Φ_Y, so it neither rounds nor sits on a floor. The
instrument separating it from the other three without being told is the best
evidence here that the classification does work.

---

## 2. Why P2 failed, and why that improved things

I registered 3a as *the stratum with a stable boundary* — the one that does not need
a limit. Measured: λ_c ran 1.4929 → 1.0639 → 1.0637 across M, a drift of 0.43.

Two faults, and the second matters.

**The instrument underflowed.** The quadrature computed weights e^(−y), which is
exactly 0 beyond y ≈ 745, so Φ saturated at ≈ 0.1 × 745 ≈ 74.5 and M = 10³ and 10⁴
returned the same number (76.24, 76.48). Redone with the exact closed form,
Φ_M(λ) = log[(1−e^(−(1−λ)M))/((1−λ)(1−e^(−M)))] evaluated stably, the numbers are
clean.

**The claim was not well posed.** At finite M, Φ_M is entire — there is no boundary
to be stable. 3a's boundary appears only as M → ∞, just as 3b's kink appears only as
N → ∞. So "limit versus no limit" does not separate them.

**What does separate them, measured:** Φ_M(0.9) *converges* (to −log 0.1 =
2.302585093, with increments of exactly 0 by M = 10⁶) while Φ_M(1.1) *diverges
linearly*, as M^0.981. So in 3a **Φ itself** goes to infinity on a whole region of
λ; in 3b Φ stays finite everywhere and only a derivative blows up, at one point.
That is a sharper statement than the one I registered, and the failure is what
produced it.

---

## 3. Why P3 failed — a category error the instrument caught

Two mis-specified criteria, one of them instructive.

**A power law fitted to noise.** The registered test asked for the smallest
eigenvalue's trend in n to satisfy |α| ≤ 0.05. The eigenvalue ratios are
4.4e-17, 2.8e-16, 1.0e-16, 8.9e-16 — all at the ~1e-16 machine floor. Fitting a
trend through them measures rounding error, and the fitted +0.349 means nothing.

**I asked a kink-finder to find a kink in an object that has none.** I registered
"width at the resolution floor", i.e. a *sharp* kink. But 3c's Φ is **analytic** —
the degeneracy lives in the eigenvalues of ∇²Φ, not in any non-analyticity. The
instrument returned the **full window** (width/window = 1.000), which is its correct
way of reporting *no localised feature*.

That is the fourth output in §1's table, and I failed to register it as the right
answer for 3c. The instrument was right; the criterion was a category error.

---

## 4. The prediction that was actually at stake

A sort is only a test if it says something about an entry it had no hand in
shaping. This one did: **S25's λ(P) = min(P,D)/2 kink is 3c, not 3b** — and S25 had
reported "a finite-size critical window blurs λ̂ right at the singular point", which
sounds like 3b.

Measured on the population Fisher matrix A^TΣA with A ∈ R^(D×P):

| D | \|rank/2 − min(P,D)/2\| | (D+1)-th eigenvalue / 1st at P = D+1 |
|--:|--:|--:|
| 4 | 0.0e+00 | 2.93e-17 |
| 8 | 0.0e+00 | 1.17e-17 |
| 16 | 0.0e+00 | 1.52e-17 |
| 32 | 0.0e+00 | 3.11e-17 |

Sharp at every D, at machine precision — so **the kink does not round, and S25's
blurring is a property of its finite-sample estimator rather than of the object.**
S25 did not draw that distinction; the sort forced it and the measurement settles
it.

*P4 is declared an identity — a matrix rank is an integer, so sharpness is
structural. P5 is the at-risk half, since numerical rank deficiency is often only
approximate, and it holds two orders below the registered tolerance.*

---

## 5. Honest limits

- **Exemplars, not the catalog.** This shows the four signatures are
  distinguishable. It does not show that every entry in
  [`FLOOR3-STRATA.md`](../../invariants/FLOOR3-STRATA.md)'s table sits where the
  sort puts it — most of those assignments are predictions and are marked as such.
- **3a is exhibited by truncating the support**, which is one way to reach a heavy
  tail and not the only one. That the support limit and the size limit behave
  differently is the claim; a reader who thinks all limits are one thing should
  read §2 as the test of that, on one exemplar.
- **S25's leg uses the population Fisher matrix**, so it does not run S25's actual
  finite-sample estimator. It establishes that the object is sharp; the inference
  that S25's blurring is estimator-side follows from that plus S25's own report,
  and was not measured head to head.
- **Nothing here is new mathematics** — finite-size rounding, the mgf's domain and
  matrix rank are all old, as the prior-art note says. The claim is exhaustiveness
  and sorting.
- **Three of four at-risk failures were mine.** The pass rate of this pass is not
  evidence about the classification; the S25 prediction is the only leg that could
  have embarrassed it, and it is one leg.
