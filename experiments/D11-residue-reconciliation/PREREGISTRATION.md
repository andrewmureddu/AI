# D11 pre-registration — written before any measurement

Works [D11](../../questions/UNKNOWN-LAWS.md), the question the register was left
with after the branch-reconciliation pass: three independently-produced accounts
of "what the residue is in general" —
[D7/D8](../D7-residue-projective/) (a projective ray / Grassmannian point, from
log-slopes), [D10](../D10-composition-lens/) (the invariant content of the
largest group a composition law fails to pin), and
[D3-ladder-invariance](../D3-ladder-invariance/) ("the fixed point of the
description map; a ratio is only its eigenvalue") — flagged in
[`SYNTHESIS.md`](../../SYNTHESIS.md) §7.0(iii) as produced independently and not
checked against each other.

Per [`UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6: prior-art note,
identity/risk split, then numbers.

---

## 0. Prior-art note (written first)

**Old, and thoroughly so — every load-bearing piece is textbook renormalization
group or classical probability.**

- **Critical exponents are eigenvalues of the linearized RG map at a fixed
  point.** Completely standard (Wilson, Kadanoff, Wegner); already the prior-art
  basis for D2's own G_diff/G_pow distinction, which cites Wegner's nonlinear
  scaling fields.
- **The CLT and stable laws are fixed points of a renormalized-convolution
  operator**, with the normalizing exponent (1/α) playing the role of an
  eigenvalue and the domain of attraction playing the role of a basin. This is
  Jona-Lasinio's programme (*Renormalization group and probability theory*,
  Phys. Rep. 352 (2001) 439), continued explicitly for the generalized CLT by
  Calvo, Cuchí, Esteve & Falceto, *Generalized Central Limit Theorem and
  Renormalization Group*, J. Stat. Phys. 141 (2010) 409 (arXiv:1009.2899) — "by
  changing the scaling of the renormalized variables, Lévy strictly stable laws
  are obtained as fixed points of the transformation." This is exactly D3's
  aggregation map, restated with citations it did not carry.
- **Continua of fixed points sharing invariant data while the theory genuinely
  differs** are a known RG phenomenon under two names, neither an exact match:
  *lines of fixed points* driven by an exactly marginal operator (the XY model,
  the eight-vertex model — Kadanoff & Wegner), where the shared data is the
  operator content but the **exponents themselves vary continuously** along the
  line; and CFT **conformal manifolds** / exactly marginal deformations, where
  protected scaling dimensions stay fixed while the theory (OPE data) varies —
  closer in spirit to what is claimed below, but that protection is normally a
  supersymmetry fact, and the construction here needs none.

**The nearest-miss test.** If a source states "the exponent set of an approach to
a fixed point is exactly the data invariant under reparameterizing the approach,
and this data is generically insufficient to determine the fixed point because
the fixed-point set can have positive-dimensional tangent directions the
exponents cannot see" — as a general, cross-domain statement rather than a
model-specific remark — then this stone is **N0** and only the specific
identification across D7/D8/D10/D3 survives as anything at all.

**What is claimed, and it is narrow.** Not a new mathematical fact. A
**recombination**: that D7/D8's projective/Grassmannian residue, D10's pinning
criterion, and D3's "fixed point, ratio as eigenvalue" language are three
descriptions of *one* already-known structure (a description map's linearization
at a fixed point), produced independently inside this repo without anyone
noticing they were the same structure — plus one **derived, checkable
consequence** that none of the three states on its own: the residue is
*provably* blind to exactly the directions tangent to the fixed-point set, not
merely blind in the one case D3 happened to construct. The claimed novelty is
**N1** at best (recombination of known results, correctly composed), honestly
graded down from D3's own N2 aspiration for the "fixed point" language, which
turns out to already be the literature's own frame.

---

## 1. The claim

**Setup, made literal.** A "description map" is an operator T on a space of
systems (laws, coupling vectors, whatever the domain supplies) with T(x\*) = x\*
for some fixed point (or fixed-point *set*) x\*. An "approach" is a one-parameter
path of systems reaching x\* as a control ε → 0 (or, discretely, as a level index
N → ∞, or a repeated-application count n → ∞ — D7 already treats the continuous
and discrete cases identically). Near x\*, to leading order, the flow is governed
by the **linearization** DT(x\*), whose eigenvalues split into relevant,
irrelevant and marginal by the usual RG classification.

**C1 (identity — proved, not measured).** Under the hypotheses D7 already used
(§2 of [`derivations/D7-the-residue.md`](../../derivations/D7-the-residue.md)):
observable log-slopes y_i = d ln O_i/d ln ε reparameterize by a common scalar
under ε ↦ ε^a. When the family is literally generated by iterating a description
map with linearization DT(x\*), the y_i are (up to that same common scalar) the
eigenvalues of DT(x\*) restricted to the directions the O_i probe. D7's ray
[y] ∈ ℝP^{n−1} is therefore the **projectivized eigenvalue vector** of the
linearization, and D8's Gr(r, n) is the same statement with r simultaneous
controls. This is what "the residue is the fixed point's eigenvalue data" means
made literal, and it is an identity given the setup — not tested numerically
here, proved in the derivation from the self-similarity of the specific
description map used below.

**C2 (identity — proved analytically, checked numerically as an estimator
test).** Fix the description map T: (law of X) ↦ (law of (X₁+X₂)/√2), the
dyadic renormalized-sum operator of the prior-art note. For **any** law of a
positive random variable U independent of Z ~ N(0,1), the scale mixture
X = U·Z is an *exact* fixed point of T (not merely asymptotic): the sum of n iid
copies of X satisfies S_n =_d √n·X for every n, by the self-similarity of the
Gaussian under convolution. Consequently, for **any** positively-homogeneous
scale statistic s (s(c·Y) = c·s(Y) for c > 0 — a quantile spread is one), the
aggregation chart order H = d ln s(S_n)/d ln n equals **exactly 1/2, for every n
and for every law of U.** This is proved in the derivation before any code is
written; the U-family is an explicit, infinite-dimensional realization of a
fixed-point *set* whose tangent directions (which law of U) do not touch the
scale eigenvalue at all.

**C3 (at risk).** The standard log-slope **estimator** this repo already uses
(regress ln s(n) against ln n over a range of n) — applied not to noisy Monte
Carlo samples as in the earlier D3 run, but to **exact** quantiles of S_n
obtained by root-finding on the closed-form mixture CDF — recovers H = 0.500000
to nearly machine precision, for two different scale-homogeneous observables and
across a spread of U-mixtures chosen to differ substantially in shape. This is
what actually gets tested: not whether the identity C2 is true (it is proved),
but whether the *estimator this arc's residue claims are built on* faithfully
recovers an eigenvalue that is known exactly, when the noise source (finite
Monte Carlo sampling) is removed. A miss here would mean the earlier D3 run's
0.4936–0.4951 measurements were not simply MC noise around 1/2.

**C4 (at risk — the falsifiable core).** A **scale-invariant shape statistic**
(a ratio of quantile spreads, dimensionless, hence with H ≡ 0 by construction —
exactly the "tangent to the fixed-point set" direction C1 predicts is invisible
to the log-slope construction) varies **substantially** across the same
U-mixtures used for C3, while H stays flat to the same tolerance. This is the
direct numerical descendant of D3's own finding — same mechanism (a continuum of
distinct fixed points sharing one residue), but exact rather than sampled, and
with the "what varies" identified in advance as *exactly* the shape statistic
predicted to be invisible, rather than found post hoc.

**C5 (remark, not registered — a boundary, stated honestly).** D10's pinning
criterion applies here too, on a variable this repo has not yet used it on: the
control **n** (an aggregate count) is additive under concatenating two samples
(n₁ + n₂ draws is n₁ then n₂ draws), so by D10's C3 its chart is pinned to
G_diff and H = 1/2 is a *fact*, not merely gauge, exactly matching
[the first D3 run](../D3-ladder-as-quotient/)'s independent finding that this
harness's chart is pinned by additivity. The **value axis** x carries no such
composition meaning, so its chart is free (G_pow) — already registered and
tested in [D3-ladder-invariance](../D3-ladder-invariance/) P2/P5. C5 is not
re-tested here; it is cited as the reason D10 and the earlier D3 runs are
compatible with this stone rather than a fourth independent account.

---

## 2. What would kill each part

- **C2** dies if the self-similarity algebra is wrong — checkable by hand, and
  the numeric check (C3) would then also fail, since it evaluates the same
  closed-form CDF the algebra predicts.
- **C3** dies if the log-log regression estimator, applied to exact (non-MC)
  quantiles, misses 0.5 by more than 1e-6 for any tested configuration —
  meaning the estimator this arc relies on has a bias independent of sampling
  noise, which would cast doubt on every H/y measurement in D1–D3/D7–D9.
- **C4** dies if the registered shape statistic fails to vary by the registered
  margin across the registered configurations — meaning the "tangent direction"
  is smaller than claimed, or the specific statistic chosen happens to be
  another hidden invariant of the family (which would itself be interesting and
  would be reported as such rather than as a negative result).
- **The whole recombination (§0)** dies if D7/D8's ray and D10's pinning
  criterion turn out to disagree about which group acts here — e.g. if D10's
  criterion predicted the value axis were pinned, or D7/D8's construction gave a
  different exponent under the φ_a value-axis reparameterization than the one
  the earlier D3 run already measured (0.5006/a). Neither is tested fresh here;
  both are cited from already-merged, already-verified results, so this
  falsifier is really a consistency check on the write-up, not new code.

## 3. Exact numbers registered before the run

- **P1 (C3).** For each of 5 mixture configurations (U ∈ {u₁, u₂} w.p. {p, 1−p};
  see §4 of the README for the exact values), fit H via least-squares regression
  of ln s(n) on ln n over n ∈ logspace(1, 4, 20 points), for s = IQR (Q75−Q25)
  and s = the 10–90 range (Q90−Q10), using **exact** quantiles from
  `scipy.optimize.brentq` root-finding on the closed-form mixture CDF (no
  sampling). Registered: |H − 0.5| < **1e-6** for all 5×2 = 10 measurements, and
  R² > 1 − 1e-10 for every fit (it is an exact power law).
- **P2 (C3, ray).** |H_IQR − H_1090| < **1e-6** for every configuration.
- **P3 (C4).** Define SR(n) = (Q97.5(n) − Q2.5(n)) / (Q75(n) − Q25(n)) at
  n = 100. Registered: max(SR)/min(SR) − 1 ≥ **0.15** across the 5
  configurations (substantial, pre-specified spread), while H stays within the
  P1 tolerance throughout.
- **P4 (C4, the "tangent" check).** |SR(n=10) − SR(n=10000)| < **1e-6** for
  every configuration — SR is exactly n-invariant, confirming it is a direction
  *along* the fixed-point set rather than a slowly-converging approach to one.

Run: `python3 run.py` (pure numpy + scipy, deterministic, no random seed needed
since every quantity is computed by closed-form root-finding — expected runtime
under 30 s).
