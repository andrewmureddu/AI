# 2026-07-28 — P-K: P-D's kink is a phase transition, and P-C's account of it was wrong

**Worked on:** [`FLOORS.md`](../invariants/FLOORS.md) §4's twice-flagged open item;
[`PC-variational-kinds`](../experiments/PC-variational-kinds/) §5.
**Change:** new experiment
[`experiments/PK-kink-taxonomy/`](../experiments/PK-kink-taxonomy/); the kink is
placed on **floor 3**; **P-C §5's leading account is retracted**; a class I
registered (type X) is **withdrawn**; P-C's P8 repair lands, with a rule.

## What I did

Took the item P-C named and did not run: is P-D's non-analyticity at nβ²γ = 1 a
**selector cell boundary** — an argmin crossing — or a floor-3 non-analyticity?

Before registering anything I read [P-D's
code](../experiments/PD-allometry-reduction/run.py) rather than its write-up, and
that already changed the answer. The level-*j* term of the blood-volume sum is
π r_c² l_c n^N·(nβ²γ)^(−j), so θ = min(1, ·) is the tropical limit of a
`logsumexp` — a **dominance switch between the two ends of a geometric sum**, not a
choice among schemes. So the pre-registration says so up front and tests the
consequence instead of the guess.

## What I found

**P-D's kink is type L: analytic at every finite depth, non-analytic only in the
limit.** Treating depth as continuous gives a closed form in three lines,

    theta_N = ln n / ( ln n + g(u)/(N+1) ),   g(u) = u/(1-e^-u),
    u = -(N+1) ln(n beta^2 gamma)

and that closed form *is* the answer: θ_N is analytic in β for every finite N, so
the kink needs N → ∞. Rounding width ∝ N^**−0.9731** over N = 20…5120 (0.228 →
0.00106), peak curvature ∝ N^**+1.0155**.

**Same class as a first-order transition, different scaling function.** The
canonical rounded first-order control −(1/N)ln(e^{−Nf₁}+e^{−Nf₂}) gives
N^**−1.0008**; the two normalized scaling functions differ in sup-norm by
**0.1403**. So the placement is exact about its scope: a first-order-*class*
non-analyticity with its own scaling function, reached in the limit of network
**depth** rather than of system size.

**A selector boundary, measured with the same instrument, has no width at all.**
Across operating sizes 2¹⁰…2¹⁸ the value is continuous to **exactly 0.0**, the
one-sided slope gap does not shrink, and the instrument's width is **5.0e-4 at
every size — its own grid resolution** (max/min = 1.000000). Legs A and B sit two
to three decades above that floor and shrink; this sits on it and does not move.
That contrast is the useful part of the pass.

**One interpretive fact, kept.** Murray's law ⟺ nβ²γ = 1 is an *identity* given
space-filling γ = n^(−1/3), so "Murray sits exactly on the kink" never needed
explaining. What it means does check out: at nβ²γ = 1 blood volume is
**equipartitioned across generations** — max/min level volume **1.000000**, against
14.6 off it.

**This is the project's worst scorecard — 2/6 at risk, 2/4 identities — and three
of the four failures are mine rather than the claim's.**

1. **P1 failed as an identity because my checker was cruder than my tolerance.**
   2-point stencil 1.76e-6, 5-point **1.69e-9** — a factor of 1000, exactly the
   truncation order. The closed form is right.
2. **P2 missed at 9.62e-3 against a registered 5e-3.** Diagnosed: P-D's estimator
   fits a slope over a *window* of depths while u depends on N, so the window
   smears the collapse quadratically — half-width 5/10/25/50 gives
   9.4e-5 / 3.8e-4 / 2.4e-3 / **9.6e-3**, and P-D used 50. A diagnosed near-miss,
   not a clean confirmation.
3. **P5 failed because I registered the wrong statistic** — the slope gap, which
   nothing required to be size-independent (it grows as N^+0.328). Type L vs type C
   is a claim about the **width**, and on the width it is decisive.
4. **P6 is the genuine negative: type X does not exist here.** I registered a
   square-root branch point and called the n = 2 case an identity "from the
   quadratic formula". **That identity was wrong algebra** — the stability boundary
   is det J = 0 (a real eigenvalue crossing zero, exponent 1), not the discriminant
   (a collision, exponent ½). Measured **1.0003** and **1.0000**; at a_c the
   eigenvalues are exactly real (max |Im λ| = 0.00e+00) and |det J| = 2.1e-15. So
   the P-C stability boundary is not a kink of any kind, and the class is withdrawn.

**P-C's P8 repair failed the same way and now has a rule.** The "five genuinely
independent magnitudes" model measured **4/5** — `c_call·a_s` and `c_fix` are both
per-level constants, hence collinear for a fixed winner. Audited so the magnitudes
have **distinct n-dependences** (n, √n, log n, constant, base-case) with the
structural count excluded: rank **5/5, full at 89%** of interior points.

> The identifiable magnitude count of a recurrence is **the number of distinct
> n-dependences in it, not the number of named constants.**

## Decisions

- **The kink is placed: floor 3, first-order-transition class.** `FLOORS.md` §4's
  twice-flagged open item closes, and it closes on the *third* candidate — not the
  two the reconciliation note listed, and not P-C's.
- **P-C §5's leading account is retracted.** Right instinct (a min of two branches),
  wrong mechanism (an argmin rather than a dominance switch). The two are
  distinguishable and the distinguishing measurement is finite-size rounding.
- **Type X is withdrawn** — a class invented to hold a case that turned out not to
  be one. Exceptional points elsewhere in the map are untouched.
- **Sixth instance of one failure mode, and the frequency is now the finding.**
  P-A's threshold, P-D's MST and control, D6's P2, P-C's P8 and P4 normalization,
  and now P-K's P1, P5 and P6a. All are: write a construction, register a number
  about it, don't audit the construction. **The pre-registration discipline catches
  the error every single time and has never once prevented it.** That asymmetry
  belongs in [`METHODOLOGY.md`](../METHODOLOGY.md) as a standing instruction —
  audit the construction's column structure, stencil order and algebra *before*
  writing the number — rather than being rediscovered each pass.
- **The headline is analytic, not experimental, and is labelled so.** P1 is the
  answer and P1 is an identity. Only P4b and P7 passed at risk, and neither carries
  it.

## Next

- **Write the standing instruction into METHODOLOGY.** Cheapest high-value item in
  the repo right now, on six instances of evidence.
- **The base-variable derivation** ([M3](./2026-07-25-M3-molloy-reed-rewiring.md),
  [M11](./2026-07-25-M11-stochastic-resetting.md)) is still unwritten and is the
  oldest live debt.
- **M8** (extreme value / best-of-n) — the L3 register's next item, deferred four
  times now.
- **Continuous-transition type L** is the obvious extension: this pass measured
  only the min-of-two-branches family, and L^(−1/ν) rounding would test whether the
  L/C distinction survives outside it.
