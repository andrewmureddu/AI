# P-K — three kinds of kink, and which one P-D's is

**Settles** the item [P-C](../PC-variational-kinds/README.md#5-what-this-does-to-p-ds-kink)
left open and [FLOORS §4](../../invariants/FLOORS.md) flagged twice: is P-D's
non-analyticity at nβ²γ = 1 a **selector cell boundary**, or a floor-3
non-analyticity?

**Registered in** [`PREREGISTRATION.md`](./PREREGISTRATION.md). Run with
`python3 run.py` (numpy + scipy, seed 20260728, 6 s).

---

## Verdict

> **P-C's leading account was wrong, and this pass corrects it.** P-D's kink is
> **type L** — a limit kink, analytic at every finite network depth and
> non-analytic only as N → ∞, with rounding width ∝ N^**−0.973** and an exact
> scaling collapse. It is **the same class of object as a first-order phase
> transition**, not a selector cell boundary. A selector boundary, measured with
> the same instrument, has **no width at any size** — the instrument returns its
> own resolution floor, 5.0e-4, identically at all six operating sizes
> (max/min = **1.000000**), while allometry's width runs 0.228 → 0.001 over
> N = 20 … 5120.
>
> **The honest shape of that result: it was settled by algebra, not by the run.**
> Reading [P-D's code](../PD-allometry-reduction/run.py) rather than its write-up
> gives θ_N in closed form in three lines, and the closed form *is* the answer —
> the exponent is analytic at finite N, so the kink needs a limit. The experiment's
> job was to check the algebra and supply the contrast cases, and that is all the
> credit it should take.
>
> **This is the project's worst scorecard: 2 of 6 at-risk, 2 of 4 identities.**
> Three of the four failures are **my registration errors, not failures of the
> claim** — a checker cruder than its own tolerance, the wrong statistic, and one
> piece of wrong algebra that I had labelled an identity. The fourth is a genuine
> negative: **type X does not exist here.** All four are diagnosed below with the
> numbers that diagnose them.

| | registered | measured | |
|---|---|---|---|
| **P1** closed form vs `logsumexp` ≤ 1e-7 | identity | **1.76e-6** — *checker* truncation; 5-point stencil gives **1.69e-9** | ✗ |
| **P2** P-D's estimator collapses ≤ 5e-3 | **AT RISK** | **9.62e-3** at P-D's window; **9.4e-5** at a narrow one | ✗ |
| **P3** allometry width ∝ N^−1.00 ± 0.03 | identity | **−0.9731** (curvature **+1.0155**) | ✓ |
| **P4a** control width ∝ N^−1.00 ± 0.03 | identity | **−1.0008** | ✓ |
| **P4b** scaling functions differ ≥ 0.05 | **AT RISK** | **0.1403** sup-norm | ✓ |
| **P5** selector boundary sharp | **AT RISK** | ✗ as registered (wrong statistic); **width at the resolution floor at 6/6 sizes** | ✗ |
| **P6a** branch-point exponent ½ at n = 2 | identity | **1.0003** — *the identity was wrong algebra* | ✗ |
| **P6b** branch-point exponent ½ at n = 6 | **AT RISK** | **1.0000** — **type X not exhibited** | ✗ |
| **P7** null control finds no kink | **AT RISK** | no locus; kurtosis 6.0000–6.9350 | ✓ |
| **P8** repaired rank test 5/5 | **AT RISK** | **4/5** as registered; **5/5, full at 89%** once audited | ✗ |

---

## 1. What P-D's kink actually is

P-C guessed "selector cell boundary" from the *shape* of θ = min(1, ·). Reading
P-D's code instead of its prose says otherwise. The level-*j* term of the
blood-volume sum is π r_c² l_c n^N·(nβ²γ)^(−j), so with y = 1/(nβ²γ),

```
    ln M(N)  =  N ln n + ln S_N(y),      S_N = sum_{j<=N} y^j
```

and treating depth as continuous gives, in three lines,

```
    theta_N  =  ln n / ( ln n + g(u)/(N+1) ),     g(u) = u / (1 - e^-u)
    u        =  -(N+1) * ln(n beta^2 gamma)
```

**θ_N is analytic in β for every finite N.** The kink is the N → ∞ limit of a
`logsumexp` — a dominance switch between the two ends of a geometric sum, i.e. a
tropical limit — and not an argmin over a discrete set. Verified against a direct
`logsumexp` computation: the residual is **1.76e-6** with a 2-point stencil and
**1.69e-9** with a 5-point one, a factor of ~1000 exactly as the truncation order
predicts. The registered tolerance failed because my *checker* was cruder than it,
not because the closed form is wrong.

**So the width shrinks, and that is what makes it type L.** FWHM of |d²θ/d(ln nβ²γ)²|:

| N | 20 | 80 | 320 | 1280 | 5120 |
|---|--:|--:|--:|--:|--:|
| width | 0.228 | 0.0641 | 0.0168 | 0.00422 | 0.00106 |

fitted **N^−0.9731**, with the peak curvature growing as **N^+1.0155**.

---

## 2. It is the same class as a first-order transition — and a different function

The independent control is the canonical rounded first-order transition,
−(1/N)·ln(e^{−Nf₁} + e^{−Nf₂}). Its width scales as **N^−1.0008** — same class.
But the two scaling functions are not the same function: normalized and compared in
sup-norm, g(u) = u/(1−e^{−u}) and ln(1+e^{−|u|}) differ by **0.1403**.

So the claim that survives is exact about its scope: **allometry's kink is a
first-order-transition-*class* non-analyticity, with its own scaling function.** It
is a floor-3 object, reached in the limit of network *depth* rather than of system
size.

**And the one interpretive fact worth keeping.** Murray's law ⟺ nβ²γ = 1 is an
algebraic identity given space-filling γ = n^(−1/3): n·n^(−2/3)·n^(−1/3) = 1. So
"Murray sits exactly on the kink" was never a coincidence needing explanation. What
it *means* is checkable and checks out: at nβ²γ = 1 the blood volume is
**equipartitioned across generations** — max/min level volume = **1.000000**, against
**14.6** at nβ²γ = 0.8 and 1.25.

---

## 3. The contrast case: a selector boundary has no width

Same instrument, on P-C's divide-and-conquer selector boundary, across operating
sizes 2¹⁰ … 2¹⁸:

- the optimal value is continuous to **exactly 0.0** at every size;
- the one-sided slope gap runs 0.076–0.317 and does **not** shrink;
- the instrument's width is **5.0e-4 at every size — its own grid resolution** —
  with max/min = **1.000000**.

Legs A and B sit two to three orders of magnitude above that floor and shrink;
this sits on it and does not move. **Type C has no intrinsic width, at any size.**

**P5 is recorded as FAILED because I registered the wrong statistic.** I asked for
the *slope gap* to be size-independent (|α| ≤ 0.02); it is not — it grows as
N^+0.328, which nothing required it not to. Type L versus type C is a claim about
the **width**, and the width is what settles it. Registering the wrong statistic is
not the same as being wrong, but it is not a pass either.

---

## 4. Type X was proposed and does not exist

I registered a third class — a square-root branch point — and predicted the P-C
stability boundary would exhibit it, calling the n = 2 case an identity "from the
quadratic formula".

**That identity was wrong algebra.** The stability boundary is where
**det J = 0**, not where the *discriminant* vanishes. A vanishing determinant is one
real eigenvalue crossing zero transversally, exponent **1**; a vanishing
discriminant is an eigenvalue collision, exponent ½. I conflated them. Measured
exponents: **1.0003** (n = 2) and **1.0000** (n = 6), with IQR 0.0006 over 40 cases
each. At a_c the eigenvalues are **exactly real** (max |Im λ| = 0.00e+00) and
|det J| = **2.1e-15**.

So min Re λ is analytic through the boundary (one-sided slopes agree to 1.1e-2 at
the step used, consistent with analytic), and **the P-C stability boundary is not a
kink of any kind.** Type X is not exhibited by this family and is withdrawn — it
was a class invented to hold a case that turned out not to be one. Whether
exceptional points occur elsewhere in the map is untouched.

---

## 5. The P-C repair failed the same way, twice, and now has a rule

P-C's P8 registered rank 6 and measured 4. The repair registered here — five
"genuinely independent" magnitudes — measured **4 of 5**, full at only 40% of
points. Same cause again: `c_call·a_s` and `c_fix` are **both per-level constants**,
so for a fixed winning scheme they are collinear.

Audited properly — magnitudes chosen to have **distinct n-dependences** (n, √n,
log n, constant, base-case), with the structural count `n_base` excluded — the rank
is **5 of 5, full at 89%** of interior points, exponent rank 0, Gibbs control 5/5.

> **The rule, which is the generalizable part:** the identifiable magnitude count of
> a recurrence is **the number of distinct n-dependences in it, not the number of
> named constants**. Both P-C's failure and this one are that rule going unnoticed.

That is now the sixth instance of one failure mode in this project — writing a
construction, then registering a number about it without auditing the construction.
Recorded again rather than smoothed over, because the frequency is the finding:
**the pre-registration discipline catches the error every time and has never once
prevented it.**

---

## 6. What this changes

- **P-D's kink is placed: floor 3**, first-order-transition class, non-analytic in
  the depth limit. `FLOORS.md` §4's twice-flagged open item closes.
- **P-C §5's "leading account" is retracted** — it was the right instinct (a min of
  two branches) applied to the wrong mechanism (an argmin rather than a dominance
  switch). The two are distinguishable, and the distinguishing measurement is
  finite-size rounding.
- **The type L / type C distinction stands**, on a 3-decade width contrast against
  a resolution floor, and is the useful part of this pass. **Type X is withdrawn.**

## 7. Honest limits

- **Type L here is first-order-like only** (two competing branches). Continuous
  transitions round as L^(−1/ν) and are not tested; the class as measured is
  min-of-two-branches, nothing wider.
- **"Analytic at finite N" treats network depth as continuous.** Real networks have
  integer N, where the question does not arise — the same restriction to models
  rather than organisms that [P-D](../PD-allometry-reduction/) carries.
- **The headline is analytic, not experimental.** P1 is the answer and P1 is an
  identity; the run checks it and supplies contrast. Only P4b and P7 passed at
  risk, and neither carries the headline.
- **P2 did not reach its registered tolerance**, so the connection to P-D's
  *published* numbers is a diagnosed near-miss rather than a clean confirmation:
  the collapse is smeared by the fitting window, quadratically —
  half-width 5 / 10 / 25 / 50 gives 9.4e-5 / 3.8e-4 / 2.4e-3 / **9.6e-3**, and
  P-D used 50.
- **The instrument's null was tested once** (M/M/1), which is one guard against an
  instrument that finds kinks everywhere, not a characterization of its false-positive
  rate.
- **The classification may be N0.** "Tell a phase transition from a level crossing
  by finite-size rounding" is close to what finite-size scaling *is*; the
  prior-art note said so in advance and nothing here changes that. What is claimed
  is the placement of this repo's own kinks.
