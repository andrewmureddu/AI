# P-K pre-registration — written before any measurement

Settles the item [P-C](../PC-variational-kinds/README.md#5-what-this-does-to-p-ds-kink)
left open, which [FLOORS §4](../../invariants/FLOORS.md) had already flagged twice:

> P-D's θ = min(1, ln n/−ln β²γ) is non-analytic at nβ²γ = 1, with Murray's law
> sitting exactly on the kink. Whether that kink is a floor-3 degeneracy read in a
> scheme variable, or a fact about the description map with no floor-3 counterpart,
> is untested.

P-C offered a third candidate — a **selector cell boundary**, i.e. an argmin
crossing — and called it "the leading account, not a settlement", naming the
measurement. This runs it.

**It also corrects that account before measuring.** Reading
[P-D's code](../PD-allometry-reduction/run.py) rather than its write-up, the kink
is *not* an argmin over a discrete set. It is a **dominance switch in a geometric
sum**: the level-*j* term of the blood-volume sum is
π r_c² l_c n^N · (nβ²γ)^{−j}, so ln M is governed by whichever end of the sum wins,
and θ = min(1, ·) is the tropical limit of a `logsumexp`. That is the same *shape*
as an argmin crossing and a different *object*, and the difference is measurable.

---

## 0. Prior-art note (written first)

**Old, and this is mostly old.** Rounding of a first-order transition at finite
size, with width ∝ 1/N and a scaling function, is textbook (Imry–Wortis; Fisher–
Berker; Challa–Landau–Binder). `logsumexp` → max as a tropical/Maslov
dequantization is standard. That the argmin of finitely many smooth functions is
exactly non-smooth at a crossing is elementary. Square-root branch points at
eigenvalue collisions are Kato's exceptional points, and their role in
non-Hermitian stability boundaries is well studied.

**Not covered, and what is claimed.** That these are **three distinguishable kinds
of kink** with one instrument — and specifically that *this repo's own kinks* sort
into them, which decides floor placements the map currently records as open. The
N2-flavoured content is the sorting rule and its application, not the asymptotics.

**Nearest miss, recorded so it cannot be relabelled.** If "distinguish a genuine
phase transition from a level crossing by finite-size rounding" is simply what
finite-size scaling *is* — which is close to true — then the classification is
**N0** and only the placements survive. I expect to have to concede this.

---

## 1. The claim

A readout that is a min or max of two smooth branches comes in three kinds:

| | at finite size | boundary signature |
|---|---|---|
| **type L** — limit kink | **analytic**; non-analytic only in a limit | rounding width w(N) → 0 with a scaling collapse |
| **type C** — crossing kink | **non-analytic already** | w = 0 at every size; one-sided slopes differ |
| **type X** — branch point | non-analytic, but not a kink | one-sided slope *diverges*; exponent ½, not 1 |

**Type L is a floor-3 object** — it is what a phase transition is. **Type C is
P-C's selector boundary.** **Type X is neither**, and the tower has no entry for it.

**The prediction that matters: P-D's kink is type L, not type C** — so P-C's
"leading account" was wrong, and the kink is a genuine floor-3 non-analyticity of
the *same kind as a first-order transition*, reached in the N → ∞ limit of network
depth rather than of system size.

---

## 2. Identity vs. risk — the required disclosure

This experiment's biggest hazard is that most of type L is derivable, so most of it
must be declared. Doing that fully, since this is the register's fifth pass on the
same failure mode:

**Analytic identities. Not evidence.**

- **P1 — the exact finite-N allometry law.** Treating depth N as continuous,
  ln M(N) = N ln n + ln S_N(y) with S_N = Σ_{j≤N} y^j and y = 1/(nβ²γ), so

  ```
      theta_N  =  ln n / ( ln n + g(u)/(N+1) ),     g(u) = u/(1 - e^-u),
      u = (N+1) * ln y = -(N+1) * ln(n beta^2 gamma)
  ```

  Three lines of algebra. It is *why* the kink is type L, not evidence that it is.
- **P3 — width ∝ 1/N for allometry.** Follows from P1: u is the scaling variable
  and it carries the whole N-dependence.
- **P4a — width ∝ 1/N for the two-state control.** Same, from
  −(1/N)ln(e^{−Nf₁} + e^{−Nf₂}) = min(f₁,f₂) − (1/N)ln(1 + e^{−N|Δf|}).
- **P6a — exponent ½ at n = 2 for the type-X boundary.** From the quadratic
  formula.

**Genuinely at risk.**

- **P2** — whether P-D's *own* estimator (a window polyfit of ln B on ln M over
  N ∈ [200, 300], not the exact continuous-N derivative) collapses onto g(u). A
  fitted slope over a window that straddles the crossover need not.
- **P4b** — that the independent type-L control has the same exponent but a
  **different** scaling function. They could coincide, which would make the class
  narrower than claimed.
- **P5** — that the selector boundary shows **no** shrinkage under the same
  instrument that finds 1/N elsewhere. The theorem says the argmin is non-smooth;
  the instrument could still manufacture a width.
- **P6b** — the exponent at n = 6. Two possibilities and I am registering one: if
  the stability boundary is an eigenvalue *collision* the exponent is **½**; if a
  real eigenvalue simply crosses zero it is **1**. I predict ½ because at large
  rotation the spectrum is complex pairs. This can come out wrong.
- **P7** — the null control must report *no* kink, guarding an instrument that
  finds kinks everywhere.
- **P8** — the [P-C repair](../PC-variational-kinds/README.md#p8-failed-and-the-diagnosis-is-the-finding).

---

## 3. Registered predictions

**P1 (identity).** The closed form matches a direct `logsumexp` computation of
d ln B/d ln M to **≤ 1e-7** over N ∈ {50, 200} × five values of nβ²γ.

**P2 (AT RISK).** P-D's window estimator, re-run across the crossover, collapses
onto g(u) with u = −(N̄+1)·ln(nβ²γ): max deviation of
(N̄+1)·ln n·(1/θ − 1) from g(u) **≤ 5e-3** over N̄ = 250 and 25 values of β.

**P3 (identity).** Allometry's rounding width — the FWHM of
|d²θ/d(ln nβ²γ)²| — scales as N^**−1.00 ± 0.03** over N = 20 … 5120.

**P4 (a: identity, b: AT RISK).** The two-state first-order-transition control
gives exponent **−1.00 ± 0.03**, and its normalized scaling function differs from
g(u) in sup-norm by **≥ 0.05** — same class, different function.

**P5 (AT RISK).** The [D&C selector boundary](../PC-variational-kinds/) has width
**exactly 0** at operating sizes 2¹⁰ … 2¹⁸: the one-sided slope gap does not shrink
(fitted exponent **|α| ≤ 0.02**) and the optimal value is continuous to **≤ 1e-12**
at every size.

**P6 (a: identity, b: AT RISK).** Approaching the P-C stability boundary in a,
min Re λ(S + aA) vanishes with exponent **0.500 ± 0.02** at n = 2 (identity) *and*
at n = 6 (at risk — the alternative is 1.000).

**P7 (AT RISK, null).** M/M/1 with an infinite buffer, swept through ρ → 1, yields
**no kink locus** for the instrument to fit — as
[D6](../D6-support-singularities/) found for its own crossover.

**P8 (AT RISK, the P-C repair).** A cost model with five *genuinely independent*
magnitudes (per-word, per-call, per-level fixed, per-level log, base-case multiply)
and the structural cutoff **excluded** gives constant-Jacobian rank **5 of 5** at
**≥ 95%** of interior points, exponent rank **0**, Gibbs control **5 of 5** — one
tolerance, as P-C registered and failed.

---

## 4. What would kill this

- **P2 fails** — the type-L reading is right about the object but P-D's published
  numbers do not exhibit it, so the connection to P-D's measurement is unearned.
- **P5 fails** — type C and type L are not separable by this instrument, and the
  whole classification collapses to "kinks are kinks".
- **P4b fails** — one scaling function for both, which would make type L a single
  universality class rather than a class of behaviours, and is a *stronger* claim
  than registered. Reported as such if it happens.
- **P6b comes out 1.000** — the P-C boundary is a real-root crossing, type X is not
  exhibited there, and the third class rests on n = 2 alone.
- **P7 fails** (a kink is found where there is none) — the instrument is not
  trustworthy and nothing above should be believed.

## 5. Scope, registered

- **All of type L here is first-order-like** (two competing branches). Continuous
  transitions round differently (width ∝ L^{−1/ν}) and are **not** tested; the
  claim is about the min-of-two-branches family only.
- **"Analytic at finite N" for allometry treats depth as continuous.** Real
  networks have integer N, where the question does not arise. This is a statement
  about the model's exponent, matching
  [P-D's own restriction](../PD-allometry-reduction/README.md) to models rather
  than organisms.
- **Murray's law ⟺ nβ²γ = 1 is an algebraic identity** given space-filling
  γ = n^(−1/3): n·n^(−2/3)·n^(−1/3) = 1. So "Murray sits exactly on the kink" is
  not a coincidence needing explanation, and is not claimed as one. What it *does*
  mean — that Murray's law is the condition for blood volume to be equipartitioned
  across generations — is checked but is an interpretation, not a result.
- **Type X is exhibited, not classified.** One family, two values of n.
