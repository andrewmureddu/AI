# D12 pre-registration — written before any code or measurement

Works [D12](../../questions/UNKNOWN-LAWS.md): the two probes
[D11](../D11-residue-reconciliation/) named and did not run, taken together —
**does the residue = projectivized-spectrum identification survive a genuinely
nonlinear description map, and is the residue's blindness to
fixed-point-tangent directions actually general?** D11's own local falsifier
was "a description map with a fixed-point set whose tangent directions *do*
show up in some log-slope-built observable."

Per [`UNKNOWN-LAWS.md`](../../questions/UNKNOWN-LAWS.md) §6: prior-art note,
identity/risk split, then numbers. No code exists at the time of this commit;
tolerances are derived from an error budget in §3, not from a pilot.

---

## 0. Prior-art note (written first)

**Old. Every numerical fact this stone can produce is in the literature; the
stone is a restraint pass on D11's scope, not a discovery attempt.**

- **Period doubling as a renormalization fixed point.** The doubling operator
  T f(x) = −α f(f(−x/α)), its fixed point g, δ as the single relevant
  eigenvalue of DT(g) and α as the rescaling: Feigenbaum (1978, 1979),
  Coullet–Tresser (1978), Collet–Eckmann–Lanford (1980).
- **The fixed point depends on the order z of the critical point**, giving a
  one-parameter family g_z with z-dependent (δ, α): Hu & Satija (1983); van der
  Weele, Capel & Kluiving, *Period doubling in maps with a maximum of order z*,
  Physica A 145 (1987) 425 (including δ(z) → ≈ 30 as z → ∞ and δ → 2 as
  z → 1); Briggs, *A precise calculation of the Feigenbaum constants*, Math.
  Comp. 57 (1991) 435 (high-precision α, δ for 2 ≤ z ≤ 12). Searched and
  confirmed to exist 2026-11-16; **the table values were not retrievable from
  the search**, so the z ≠ 2 numbers in §3 are registered *from my recall* and
  marked as such.
- **The CLT map's linearized spectrum.** For the iid renormalized-sum map
  (X₁+X₂)/√2 at the Gaussian, eigenfunctions are Hermite polynomials with
  eigenvalues λ_k = 2^{1−k/2}; k > 2 is irrelevant (Jona-Lasinio, Phys. Rep.
  352 (2001) 439, arXiv:cond-mat/0009219; confirmed by search 2026-11-16).
- **Intertwining ⇒ isospectral** (C1 below) is elementary linear algebra and is
  the standard reason symmetry-related fixed points share exponents.

**Novelty claimed: N0 for every number, N1 at most for the composition** — a
correction to D11's stated boundary, using only the above. Nearest-miss test:
none needed; nothing here is claimed absent from the literature. What is at
risk is *this repo's own* claim (D11), plus my numerics and my recall.

---

## 1. The claims

**C1 (identity — lemma, proved in the derivation, not measured).** Let T be a
description map and M a map with M∘T = T∘M. If x\* is a fixed point of T so is
M x\*, and DT(Mx\*)·DM(x\*) = DM(x\*)·DT(x\*): every eigenvalue of DT(x\*)
whose eigenvector is not killed by DM is an eigenvalue at M x\*. So **along a
family of fixed points that is an orbit of maps commuting with T, the spectrum
— hence the residue — is constant.** Conversely nothing forces constancy along
a fixed-point family that is *not* such an orbit. The corrected boundary:

> The residue restricted to the fixed-point set is the spectrum map
> σ : Fix(T) → (projectivized spectra). It is blind to exactly ker dσ.
> Symmetry orbits lie in ker dσ; a general tangent (marginal) direction need
> not.

D11 stated the blindness for tangent directions without this qualifier
("the residue is exactly blind to whatever is tangent to the fixed-point
set"). **If C4 below passes, that sentence is false as a general statement and
D11's local falsifier has fired.**

**C2 (identity, with one at-risk estimator leg).** D11's U-family
(X = U·Z) is a set of exact fixed points only of the **shared-U** aggregation
(one U per aggregate), which is the iid CLT map applied fibre-by-fibre over
the dilation orbit {law(uZ)} with U conserved — a C1 symmetry orbit (dilations
commute with T) extended by mixing. Under the **literal iid** CLT map the same
laws are *not* fixed points: cumulants add, so excess kurtosis is exactly
κ₄/(nσ⁴), the U-direction is the k = 4 Hermite direction, **irrelevant with
eigenvalue 2^{−1} per doubling, and visible to the log-slope construction** as
a slope of −1 against n. Predicted ray for (scale spread, shape deviation):
[1/2 : −1], ratio **−2** = ln λ₄ / ln √2. The cumulant statement is an
identity; the at-risk part is whether D11's own *quantile* shape statistic,
measured on exact quantiles of the iid sum, shows it (P1–P2).

**C3 (at risk — numerics; the answer is in the literature).** For the
period-doubling operator, two routes that share no code path agree:
*Route A* — log-slopes against the level n measured on raw one-parameter
families of maps (superstable parameters a_n, nearest-return distances d_n),
with no reference to T; *Route B* — solve T g = g by collocation and take the
leading eigenvalue of the linearization DT(g). The residue ray
[ln δ : ln α] from A equals the eigen-data from B. This is the nontrivial
eigenvalue *ratio* under a literal, nonlinear description map that D11's
honest-limits section said it did not have.

**C4 (at risk — the falsifiable core, aimed at D11).** z ↦ g_z is a curve of
fixed points of one operator T (acting on unimodal maps of any critical
order), so ∂_z g_z is a tangent direction with DT-eigenvalue 1. It is **not**
a symmetry orbit. Prediction: the residue **sees it** — ρ(z) = ln α/ln δ is
strictly monotone in z across the registered list, so within this family the
residue is a complete coordinate on the fixed-point set, the opposite of the
U-family.

**C5 (identity — declared, carries no weight).** Dilation f ↦ c·f(·/c)
commutes with T. The dilated family has identical a_n and d_n scaled by c, so
identical log-slopes at every n. Checked only to confirm the harness.

**C6 (at risk — universality as the asymptotic blind direction).** Two
microscopically different families with the same z (A: 1 − a|x|^z;
B: 1 − a|sin x|^z) differ along *irrelevant* directions and give the same
residue within the finite-window error. Textbook; at risk only as numerics.

---

## 2. What would kill each part

- **C2/P1–P2** die if the quantile shape statistic's deviation from its
  Gaussian value does not decay as n^{−1} within tolerance — the quantile
  statistic would then not be reading the k = 4 direction, and the "same
  direction, two maps, two roles" reading fails.
- **C3** dies if routes A and B disagree beyond §3's budget for any registered
  z. Since the literature says they agree, a miss indicts my numerics; it is
  reported as a miss either way.
- **C4** dies if ρ(z) is flat or non-monotone across the list. Then D11's
  blindness sentence survives this probe.
- **C6** dies if families A and B disagree at fixed z beyond budget.
- **Recall leg (P5)** dies if my remembered Briggs values are wrong; that
  indicts my memory, not the claim, and is reported separately.

## 3. Error budget and exact numbers

**Budget, route A.** Finite-level estimates converge geometrically; for z = 2
the known sequence δ_n errs by 0.28, 0.069, 0.014, 0.003 at n = 1…4, i.e. a
factor ≈ δ per level. I do not know the rate for other z or for α_n; I assume
no slower than a factor 3 per level for z ≥ 1.5. Then the local slope at level
n errs by ≲ C·3^{−n}: ~1.4e-3·C at n = 6, ~6e-6·C at n = 11. All route-A
arithmetic in mpmath at 80 digits, so cancellation in a_{n+1} − a_n
(~10^{−12} at worst) is not the limit. **Budget, route B.** Collocation in
t = |x|^z; gate (not a prediction): eigen-data at N and N + 4 basis functions
agree to 1e-7, else the z is reported as "route B not converged" rather than
pass/fail.

z list: **{1.5, 2, 2.5, 3, 4, 6, 8}**. Levels n = 1…12, superstable
normalization a_0 = 0.

- **P1 (C2).** Five D11 configurations (u₁, u₂, p) = (1,1,1), (1,2,.5),
  (1,5,.5), (1,10,.9), (.5,3,.3). Exact CDF of the **iid** sum (binomial
  mixture of Gaussians), exact quantiles by root-finding. Shape deviation
  Δ(n) = SR(n) − SR_Gauss with SR = (Q97.5 − Q2.5)/(Q75 − Q25). Fit
  ln|Δ| on ln n over n ∈ logspace(3, 5, 15). Registered for the four
  non-Gaussian configs: slope = **−1.00 ± 0.05** (budget: corrections relative
  O(κ₆/κ₄n), up to a few % at n = 10³ for the heaviest config). Gaussian
  config: |Δ| < 1e-9 at every n (identity).
- **P2 (C2).** Same window, s = IQR: H = **0.500 ± 0.005**; ray ratio
  slope_shape / H = **−2.0 ± 0.12**.
- **P3 (C3).** For every z in the list, family A, last-pair estimates
  ln δ_A = ln[(a₁₁ − a₁₀)/(a₁₂ − a₁₁)] and ln α_A = ln|d₁₁/d₁₂| against
  route B: |Δ ln δ| < **1e-4**, |Δ ln α| < **1e-4**. And the house estimator
  (least-squares slope of ln(a_n − a_{n−1}) and ln|d_n| on n, n = 6…12):
  both within **2e-3** of route B.
- **P4 (C4).** ρ_B(z) = ln α/ln δ strictly decreasing across the seven z, with
  ρ(1.5)/ρ(8) − 1 ≥ **1.0**; and ρ_A (last-pair) reproduces the same strict
  ordering.
- **P5 (recall, reported separately).** Route B gives, to 1e-6:
  z = 2: δ = 4.6692016, α = 2.5029079; z = 3: 5.9679687, 1.9276910;
  z = 4: 7.2846862, 1.6903030; z = 6: 9.2962468, 1.4677425. z = 2 I am sure
  of; the rest are unverified recall.
- **P6 (C6).** Family B vs route B, same tolerances as P3's house-estimator
  line (2e-3), for z ∈ {2, 3, 4}.
- **C5 check.** Dilation c = 0.37 on family A at z = 2: a_n identical and
  d_n ratio = c to 1e-60.

**Exploratory, not registered:** the convergence rate of δ_n and α_n per
level, compared post hoc with route B's subleading eigenvalues. Anything said
about it in the README is labelled post hoc.

Run: `python3 run.py` (numpy, scipy, mpmath).
