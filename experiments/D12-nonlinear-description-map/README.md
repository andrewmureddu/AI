# D12 — the residue under a nonlinear description map (result)

**Question ([D12](../../questions/UNKNOWN-LAWS.md)):** the two probes
[D11](../D11-residue-reconciliation/) named and did not run. Does "the residue
is the projectivized spectrum of a description map's linearization" survive a
genuinely nonlinear map, and is the residue's blindness to
fixed-point-tangent directions general — or a property of D11's one family?

**Status: the identification survives; D11's blindness sentence does not.**
Under the period-doubling operator, log-slopes measured on raw maps reproduce
the eigen-data of the linearized operator to 2e-8 … 4e-5 across seven critical
orders z. But z ↦ g_z is a curve of fixed points of that one operator, and the
residue **sees it**: ln α/ln δ falls monotonically from 0.914 to 0.128 across
the list. D11's own local falsifier has fired. Separately, D11's U-family is a
fixed-point set only of the *shared-U* aggregation; under the literal iid CLT
map the same direction is irrelevant with eigenvalue 2⁻¹ and shows up in the
residue as a slope of −1.000, ratio −2.000.

**Two registered items failed**, neither on the claim: the route-B convergence
gate (my continuation, not the physics) and one of four literature values I
registered from memory. Both are reported in full below.

Run it: `python3 run.py` (numpy, scipy, mpmath; deterministic; ~40 s).
Registered first, in a commit that contains no code:
[`PREREGISTRATION.md`](./PREREGISTRATION.md). Derivation:
[`derivations/D12-nonlinear-description-map.md`](../../derivations/D12-nonlinear-description-map.md).

---

## Results

### P1/P2 — the same U-direction under the literal iid CLT map (AT RISK — pass)

D11's five configurations, but summing n **iid** copies of X = U·Z (a fresh U
per term) instead of one shared U. The sum is a binomial mixture of Gaussians,
so quantiles are exact (root-found, no sampling). Δ(n) = SR(n) − SR_Gauss is
D11's own shape statistic, measured as a deviation; n ∈ [10³, 10⁵].

| config | H (IQR) | slope of ln\|Δ\| | ratio | excess kurtosis of X |
|---|:--:|:--:|:--:|:--:|
| gaussian | 0.500000 | — (\|Δ\| < 1e-9) | — | 0 |
| mild | 0.500020 | −1.0002 | −2.0002 | 1.08 |
| strong | 0.500047 | −1.0004 | −2.0005 | 2.56 |
| rare extreme | 0.500415 | −1.0019 | −2.0021 | 22.3 |
| asymmetric | 0.500022 | −1.0003 | −2.0004 | 1.19 |

Registered: slope −1.00 ± 0.05, H = 0.500 ± 0.005, ratio −2.0 ± 0.12. **All
pass, by a factor of 12 or more.** The predicted ratio is ln λ₄/ln √2 with
λ₄ = 2^{1−4/2} the k = 4 Hermite eigenvalue of the linearized CLT map
(Jona-Lasinio 2001). The deviations from the exact values order by excess
kurtosis, as the error budget said they would.

**What this does to D11.** The direction D11 called "provably tangent to the
fixed-point set, hence provably invisible" is tangent only for the shared-U
map, where U is a conserved label. Under the map D11's derivation names as T —
law(X) ↦ law((X₁+X₂)/√2) with iid copies — the U-family is not a fixed-point
set at all, the direction is irrelevant, and the log-slope construction reads
its eigenvalue cleanly. D11's derivation says this in a parenthesis ("this is
not D3's construction, which shares one U") and then states the conclusion for
T anyway. The numbers in D11 are right; the map they are about was misnamed.

### P3 — two routes, one spectrum (AT RISK — passes)

*Route A:* f_a(x) = 1 − a|x|^z, superstable parameters a_n (period 2ⁿ, n ≤ 12)
and nearest returns d_n, at 80 digits. No reference to any operator.
*Route B:* solve g = −α g(g(x/α)) by collocation in t = |x|^z, then the
leading eigenvalue of the linearization. The routes share no code.

| z | δ (route B) | α (route B) | \|Δ ln δ\| last pair | \|Δ ln α\| last pair | \|Δ ln δ\| regression | \|Δ ln α\| regression |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| 1.5 | 3.8005621 | 3.3886653 | 8.9e-7 | 3.6e-7 | 2.4e-5 | 5.7e-5 |
| 2 | 4.6692010 | 2.5029078 | 5.7e-8 | 7.5e-8 | 2.2e-5 | 1.5e-5 |
| 2.5 | 5.4127362 | 2.1368777 | 1.8e-8 | 2.0e-8 | 1.4e-5 | 6.8e-6 |
| 3 | 6.0846870 | 1.9276909 | 3.7e-7 | 7.3e-8 | 3.3e-6 | 5.5e-6 |
| 4 | 7.2846857 | 1.6903030 | 5.3e-7 | 1.3e-7 | 3.3e-5 | 1.1e-5 |
| 6 | 9.2962505 | 1.4677425 | 7.5e-6 | 1.3e-6 | 2.4e-4 | 4.0e-5 |
| 8 | 10.9486345 | 1.3580174 | 4.1e-5 | 5.1e-6 | 7.1e-4 | 8.8e-5 |

Registered: last pair within 1e-4, house regression (n = 6…12) within 2e-3.
**Met at every z.** This is the nontrivial eigenvalue *ratio* under a literal
description map that D11's honest-limits section said it lacked: the ray
[ln δ : ln α] is not [1 : 1], it is irrational, and it is recovered by an
estimator that never sees T.

> **The registered gate on route B failed, and by the registration's own rule
> every row above should read "route B not converged."** The gate was
> agreement between N = 12 and N = 16 basis functions to 1e-7. At N = 12 the
> continuation in z left the solution branch for every z ≠ 2 (differences of
> order 1), and at z = 2 the two agree only to 5.6e-7. I am reporting the
> table anyway because the N = 16 values agree with an independent route to
> 1e-7 … 4e-5, which a diverged solve cannot do by accident — but that is a
> post-hoc argument and the gate is recorded as **failed**.
>
> *Post hoc:* re-solving with a finer continuation step at N = 16, 18, 20
> gives spreads of 5e-7 … 3e-5 in δ and 1e-8 … 5e-7 in α. Route B's own
> resolution in δ is therefore ~1e-6 at best — a monomial basis in double
> precision. **The 1e-7 gate was below what the registered method can
> deliver.** This is D8's P1 slip again, in a new place: I derived route A's
> budget and asserted route B's.

### P4 — the residue sees the tangent direction (AT RISK — the core, passes)

| z | 1.5 | 2 | 2.5 | 3 | 4 | 6 | 8 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| ρ = ln α/ln δ, route B | 0.91408 | 0.59537 | 0.44965 | 0.36346 | 0.26433 | 0.17210 | 0.12787 |
| ρ, route A | 0.91408 | 0.59537 | 0.44965 | 0.36346 | 0.26433 | 0.17210 | 0.12787 |

Strictly decreasing in both routes; ρ(1.5)/ρ(8) − 1 = **6.15** against a
registered 1.0. ∂_z g_z is tangent to the fixed-point set of T (eigenvalue 1,
by differentiating T g_z = g_z), and the residue is a complete coordinate
along it. **D11's sentence "the residue is exactly blind to whatever is
tangent to the fixed-point set" is false as stated.**

The honest weight of this: the fact is old (van der Weele, Capel & Kluiving
1987; Briggs 1991), and D11's own prior-art note already named lines of fixed
points with varying exponents as a non-match. What failed is not a discovery
but a sentence in this repo that was written more generally than its evidence.

### P6 — universality, the asymptotic blind direction (AT RISK — passes)

Family B, f_a(x) = 1 − a|sin x|^z, against route B: regression gaps
1.0e-5 / 2.9e-5 / 6.0e-5 in ln δ and 1.9e-5 / 1.2e-5 / 5.7e-5 in ln α for
z = 2 / 3 / 4 (registered 2e-3). Two microscopically different families, one
residue.

### C5 — dilation (IDENTITY — holds to 1e-73)

f ↦ c·f(·/c) with c = 0.37: a_n identical to 1.3e-85, d_n ratio = c to
3.6e-73. Carries no weight, as registered.

### P5 — my recall of the literature (reported separately — FAILS)

| z | registered δ | route B δ | registered α | route B α | |
|---|:--:|:--:|:--:|:--:|:--:|
| 2 | 4.6692016 | 4.6692010 | 2.5029079 | 2.5029078 | ok |
| 3 | **5.9679687** | **6.0846870** | 1.9276910 | 1.9276909 | **δ off by 0.117** |
| 4 | 7.2846862 | 7.2846857 | 1.6903030 | 1.6903030 | ok |
| 6 | 9.2962468 | 9.2962505 | 1.4677425 | 1.4677425 | δ off by 3.7e-6 |

**δ(3) as I registered it is wrong.** Routes A and B agree on 6.08469 to
3.7e-7 and share no code, and the registered value breaks the smoothness of
δ(z) (differences per unit z of 1.30, 1.32, then 1.01 across z = 2→3→4→6,
against a smooth 1.42, 1.20, 1.01 with the measured value). I could not retrieve
Briggs's table to confirm which number is in it, so this stands as: *my
memory supplied a wrong constant, and two independent computations caught
it.* The z = 6 miss is route B's resolution (see the gate note), not recall.
Three of the four α values and three of four δ values I recalled check out;
none of them should be cited from this file as a literature value.

## Post hoc — not registered, not evidence

The per-level convergence factor of δ_n and α_n is ≈ δ for z ≤ 2 (3.7–3.9 at
z = 1.5 against δ = 3.80; 4.6–4.8 at z = 2 against 4.67) and falls below δ for
larger z (≈ 3.1–4.2 at z = 4, 2.5–2.9 at z = 6, 2.3–2.4 at z = 8). The
reciprocal of route B's second sub-leading eigenvalue is 3.43 / 2.70 / 2.33 at
z = 4 / 6 / 8, which matches. **I have not separated genuine irrelevant
eigenvalues from coordinate-change ones in route B's spectrum** — at z = 2
that eigenvalue is 0.15963 = α⁻², which looks like the latter — so this is a
coincidence worth a registered test and nothing more.

It also falsifies an assumption in my own error budget: I assumed convergence
no slower than a factor 3 per level, and at z = 6 and 8 it is 2.3–2.9. The
registered tolerances held anyway, with a margin of 2.4× at z = 8.

## Honest limits

- **Nothing here is new to the literature.** N0 for every number. The only
  thing that moves is this repo's own statement of D11's boundary.
- **One nonlinear map.** Period doubling has a single relevant direction, so
  this is D7's m = 1 slice again. D8's m > 1 case under a literal description
  map is still untested.
- **The tangent eigenvalue 1 is derived, not measured.** Route B's basis fixes
  z, so ∂_z g_z is outside its span.
- **Route B resolves δ to ~1e-6, not better**, and its registered gate failed.
  The A-vs-B agreement at z = 6 and 8 (7.5e-6, 4.1e-5) is limited by route A's
  finite level, not by route B.
- **C1's criterion is sufficient, not necessary.** It says symmetry orbits are
  blind directions; it does not say every blind direction is one.
- **The FLOORS.md kink note** (D7's algebraic location of P-D's kink vs P-K's
  finite-size-rounding account) is untouched — open since 2026-07-28.
