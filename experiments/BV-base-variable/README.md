# BV — the base variable: one tower, seen through observables

**Numerical companion to** [`derivations/base-variable.md`](../../derivations/base-variable.md),
which pays the debt [M11](../M11-stochastic-resetting/) opened and
[M3](../M3-molloy-reed-rewiring/), [P-D](../PD-allometry-reduction/),
[P-C](../PC-variational-kinds/) and [P-K](../PK-kink-taxonomy/) kept flagging as
the oldest live item on the board.

**Registered in** [`PREREGISTRATION.md`](./PREREGISTRATION.md). Run with
`python3 run.py` (numpy + scipy, seed 20260728, 7 s).

---

## Verdict

> **Every claim the derivation makes survives. Every failure in this run is mine,
> and all four are one item.**
>
> The **form** is portable to every base variable (∇Φ = mean and ∇²Φ = Cov hold to
> ≤ 3.7e-9 across three observables of one master measure, all convex) and the
> **geometry** is not — their spectral norms span a factor of **413**. The
> **sufficiency rule** does the work it was proposed for: two chains with
> stationary laws identical *by construction* have mean first-passage times of
> **100.0 vs 20.0** and trajectory-level curvatures of **19.93 vs 0.50**, while the
> state base variable's Φ is identical to **4.66e-15**. The **trichotomy guard**
> passes: 3a, 3b and 3c each exhibited, and **0 of 6** interior non-analyticities
> at finite size, which §4 forbids. And **P-D's "no Φ at all" is a rank-one base
> variable** — measured exactly, rank **1** with smallest/largest eigenvalue
> **4.36e-16**, rising to effective dimension **2** when an independent statistic
> is added.
>
> **4 of 6 at-risk, 2 of 4 identities — and the failures are worth more than the
> passes.** This is the first pass to run
> [`METHODOLOGY.md`](../../METHODOLOGY.md)'s new pre-registration audit, written
> one pass earlier after six instances of the same mistake. **It violated audit
> item (iii) — instrument precision — three times, in the same run that was
> supposed to be governed by it**, and mis-specified a fourth criterion. The audit
> as written is a checklist you can nod at; §5 proposes the mechanical version that
> would actually have caught these.

| | registered | measured | |
|---|---|---|---|
| **P1** form portable ≤ 1e-8 | identity | **3.74e-9**, all three convex | ✓ |
| **P2** geometry not portable, ratio ≥ 10 | **AT RISK** | **413.4** | ✓ |
| **P3** caustic density exponent −½ | identity | **−0.5003** | ✓ |
| **P4** Φ entire, Taylor ≤ 1e-8 | identity | **2.96e+7** — *estimator noise*; exact cumulants **1.63e-7** | ✗ |
| **P5** stationary laws identical ≤ 1e-15 | **AT RISK** | **1.71e-15** — *eigensolver floor*; exact deviation **3.5e-16** | ✗ |
| **P6** MFPT ratio ≥ 2 | **AT RISK** | **5.00** (100.0 vs 20.0, both exactly as derived) | ✓ |
| **P7** state blind, trajectory sees it | **AT RISK** | Φ gap **4.66e-15**; Λ″ ratio **39.9** | ✓ |
| **P8** rank 1, eigen ratio ≤ 1e-12 | identity | **1.42e-11** — *stencil floor*; exact **4.36e-16**, rank **1** | ✗ |
| **P9** rank restored | **AT RISK** | criterion mis-specified; effective dimension **1 → 2** | ✗ |
| **P10** trichotomy guard | **AT RISK** | 3a/3b/3c exhibited; **0 of 6** violations | ✓ |

---

## 1. The form is portable; the geometry is not

One master measure — 4000 weighted paths of a 3-state Markov chain — read through
three base variables:

| base variable | ‖∇Φ − E[Y]‖ | ‖∇²Φ − Cov(Y)‖ | ‖∇²Φ‖ |
|---|--:|--:|--:|
| state (final) | 1.4e-13 | 4.8e-10 | 0.377 |
| occupancy (time average) | 2.7e-13 | 2.5e-10 | 0.0708 |
| exit time | 1.6e-10 | 3.7e-9 | 29.26 |

The floor-2 apparatus holds identically for all three — that is F1, and it is two
lines of Hölder, not a discovery. **The geometries differ by a factor of 413.**

That is the whole of M11's lesson made quantitative: *the form is a property of
taking a log-Laplace transform of anything, so its recurrence across fields is not
evidence of anything; the variable is where the content is.*

---

## 2. A singular density is not a singular Φ

Push uniform-on-[−1,1] through Y = x². The density diverges as
y^**−0.5003** (a caustic — a genuine floor-3-looking object), while Φ_Y is
**finite over |λ| ≤ 200** and reproduced by its Taylor series to **1.63e-7**.

**So "the distribution goes singular, therefore the free energy does" is
unlicensed.** Caustics are facts about a pushforward's support and derivatives —
3a/3c — never 3b facts about Φ.

*P4 is recorded as failed and the reason is embarrassing:* the registered check
built a degree-20 Taylor series from **k-th order central differences at h = 0.05**,
dividing by h²⁰ = 1e-26. The estimator was pure rounding noise (2.96e+7) long
before the claim was tested. Redone with exact cumulants from
m_k = E[x^2k] = 1/(2k+1) it gives 1.63e-7 — still above the registered 1e-8, but
now that residual is genuine degree-20 truncation rather than noise.

---

## 3. The rule, and a sufficiency failure with numbers

Two doubly stochastic chains on n = 20 — a nearest-neighbour cycle walk and uniform
jumps. Doubly stochastic forces π = uniform **exactly** (column sums off by 0.0 and
2.2e-16; deviation from exact uniform 3.5e-16 and 9.7e-17), so the **state base
variable cannot distinguish them at all.**

| readout | cycle | uniform jumps | ratio |
|---|--:|--:|--:|
| mean first-passage to the antipode | **100.0** | **20.0** | 5.00 |
| Λ″(0) of a time average (trajectory Φ) | **19.93** | **0.50** | 39.9 |
| Φ on the **state** base variable | — | — | identical to **4.66e-15** |

Both MFPTs match their derivations exactly — k(n−k) = 100 and n = 20 — which is
audit item (iv) doing its job.

**This is the rule being exhibited rather than asserted.** The state statistic is
*not sufficient* for either readout, so neither is a Φ-fact on the state measure;
the trajectory statistic is, and sees a 40× difference where the state statistic
sees zero. It is the same shape as [M3](../M3-molloy-reed-rewiring/)'s result —
identical degree sequences, p_c moving 35–148% — in a system small enough to be
exact.

*P5 is recorded as failed for a reason that is now a pattern:* I registered
1e-15 for the total variation between two **numerically computed** eigenvectors of
a 20×20 matrix, which is below the eigensolver's floor. The claim is structural —
doubly stochastic ⇒ π uniform — and comparing each to the exact uniform vector
gives 3.5e-16.

---

## 4. Rank is the effective dimension of the base variable

[P-D](../PD-allometry-reduction/) measured ∇²log Z as rank 1 for every λ and the
research log recorded it as *"is there a Φ at all? — the answer was no."* The
derivation's §5 says the answer is instead **a Φ on a rank-one base variable**,
which supports no conjugate pair and therefore no exchange rate.

Reproduced from the definition rather than from P-D's code, with the exact tilted
covariance: the honest family in (ln M, ln B) has **rank 1 at all 81 grid points**,
smallest/largest eigenvalue **4.36e-16**. Adding one genuinely independent
statistic raises the effective dimension to **2** — the null direction from the
ln M / ln B dependence stays null, and one new direction opens.

**So rank(∇²Φ_Y) measures the effective dimension of Y**, and
[`FLOORS.md`](../../invariants/FLOORS.md) §4's floor-3/floor-4 boundary
("singular on a set" versus "rank-deficient everywhere") is the difference between
a degeneracy *of* a base variable and a degeneracy *in* one.

*P8 and P9 are recorded as failed.* P8's 1e-12 threshold was below `hess5`'s own
floor — it nests two 5-point stencils, so its precision is ~ε/h² ≈ 1e-10, and
**leg A had already measured 3.7e-9 for exactly that estimator on the same page.**
∇²Φ *is* the tilted covariance and is computable exactly; using it, the claim holds
at 4.36e-16. P9's criterion asked for the *smallest* eigenvalue to be large when the
claim is about the *count* of non-null ones — a mis-specified statistic, not a
failed measurement.

---

## 5. What the failures say about the audit

Every one of the four failures is an instrument or a criterion. None is a claim.
And three are the same audit item — **(iii), instrument precision** — written into
[`METHODOLOGY.md`](../../METHODOLOGY.md) one pass earlier, after six instances,
and violated three times in the very next run by the person who wrote it.

That is not an argument against the audit; it is a measurement of what kind of
thing it needs to be. A checklist of four questions is something you can satisfy by
nodding. What would have caught all three:

> **State the instrument's noise floor next to every registered tolerance. If you
> cannot state the floor, you may not register the number.**

Applied here it is mechanical and each failure dies immediately: a degree-20
difference at h = 0.05 has floor ~ε/h²⁰ ≈ 1e10 (P4); a 20×20 eigensolver has floor
~1e-15 (P5); a doubly-nested 5-point stencil has floor ~ε/h² ≈ 1e-10 (P8) — and
leg A measured that floor before leg D registered a tolerance four orders below it.
That sharpening is now in `METHODOLOGY.md`.

---

## 6. Honest limits

- **The derivation is a stitching job and the write-up should not pretend
  otherwise.** Sufficiency, exponential families, analyticity of the mgf,
  Lee–Yang, caustics — all named in the prior-art note, all old. What is claimed is
  the identification of the map's open question with them.
- **Nothing here tests the rule prospectively.** Every arrival it explains was
  measured first, and M3 is the one it was read off. Using it to *predict* a base
  variable before measuring is the honest next step and has not been done.
- **Finite discrete state spaces throughout**, so every Φ in the battery is entire
  by construction. P10 is a guard on the battery, not a general proof — and a
  general proof is not needed, since the analyticity of the mgf inside its domain
  already gives it.
- **The chains in §3 were chosen** to have identical stationary laws. That
  demonstrates sufficiency can fail; it says nothing about how often it does.
- **Leg A's master measure is sampled** (4000 paths), so its Φ is the empirical
  one. The identities hold for it exactly, which is all that was claimed, but the
  spectral-norm ratio of 413 is a property of these three observables and this
  chain, not a universal number.
- **"Coarsest sufficient" need not exist.** Minimal sufficient statistics require
  regularity a general path or graph measure need not have; M3's clustering
  breakdown is what non-attainment looks like.
