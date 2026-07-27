# S26(iii) — conserved charges as coordinates of SGD's stationary law (result)

**Question ([S26](../../questions/SPECULATIVE.md)):** the tower claims the
sufficient statistics of a stationary prediction field are its conserved
quantities. ML instance: SGD's stationary distribution should be
parameterized by the training dynamics' charges. **Falsifier (iii):** train to
stationarity and show the conserved invariants are *not* sufficient.

**Status: confirmed, with a sharper structure than the stone asked for —
SGD's stationary law is a *prethermalization plateau* coordinatized by a
quasi-conserved charge.**

Run it: `python3 run.py` (pure numpy, seconds, deterministic).
Model: scalar deep-linear net f(x) = u·v·x, the minimal scale-symmetric model;
charge Q = u² − v² (balancedness; Kunin et al. 2021).

## Legs and results

**A — conservation under gradient flow.** Relative drift of Q over fixed
physical time scales *linearly* with lr (ratios 10.15, 10.01 per decade):
first-order discretization breaking only, i.e. **exact conservation in the
flow limit.** Confirms the S9 pairing on this model.

**B — broken conservation does predictive work.** With weight decay λ, the
Euler identity for the scale symmetry gives dQ/dt = −4λQ exactly. Measured
decay exponent: **k_fit = 0.2000020 vs k_theory = 0.2** (rel. err. 1e-5).
The *breaking* of the law is itself quantitative — the "broken conservation
law" is a law.

**C — the stationary law is a function of the charge.** Label-noise SGD
(lr 5e-3, batch 8, 40k steps, 8 seeds × 3 inits sharing the same initial
function u·v but with Q₀ ∈ {+2.73, 0, −2.73}). On the stationary half:

- The law **remembers the charge**: stationary-Q group separation / spread
  ≈ 713. Inits with equal Q₀ and different (u,v) are statistically identical.
- **Sufficiency, exact form:** on the minimum manifold uv = w*, the
  stationary norm must equal √(Q² + 4w*²) if Q coordinatizes the law.
  Predicted vs observed: 4.0156 vs 4.0150, 3.0000 vs 2.9991 —
  **rel. err. ≤ 3e-4.** The stationary observable is a function of the
  charge alone, to four digits.
- **The charge is quasi-conserved, not exact, under the real dynamics:**
  discretization + label noise erode it at 5.6e-7 per step — a
  **quasi-conservation window of ~1.8M steps**, ~40× our run length.

> **⟳ Restraint pass (2026-07-25, via [M15](../M15-adiabatic-charges/)):** two
> corrections and one upgrade.
> **(1) The erosion number above is ~24% low.** It was estimated from Q₀ against
> a whole-run stationary mean, which mixes in the burn-in. Measured cleanly on
> the plateau: **7.30e-7/step**, window **~1.37M steps** (not 5.6e-7 / 1.8M).
> **(2) The rate is derivable, not just measurable.** The stochastic gradients
> factor through one scalar m, giving u·ĝ_u − v·ĝ_v = 0 *for every noise
> realization*, hence the exact per-step law **Q' = Q(1 − η²m²)** and
> **k = η²σ²E[x²]/B** — parameter-free, matching to 2% over an 18-point grid.
> The same formula covers leg A: away from the optimum m² is the deterministic
> squared gradient, so leg A's "drift linear in lr over fixed physical time" is
> this law's other face, not a separate fact.
> **(3) "Prethermalization plateau" is upgraded from label to mechanism.** The
> drift is second-order with p=2, and the regime is *ordinary averaging* — the
> Nekhoroshev form exp(−c/η) is rejected at ΔAIC = 73.6. The plateau is long
> because η is small, not because anything protects it. Its end is predicted
> too: coordinatization fails as the timescale separation R → O(1), measured as
> suff_err = 1.12·R^−0.97 reaching unity at R = 1.13.

## Verdict

Falsifier (iii) does **not** fire on accessible timescales: the stationary
law is exactly coordinatized by the charge (sufficiency to 3e-4). But the
slow erosion means the t→∞ law forgets Q — and this two-timescale structure
is not a defect of the claim; it is **prethermalization**, the same
phenomenon near-integrable physical systems show: approximately conserved
charges parameterize a long-lived GGE-like plateau before true
thermalization. The tower's GGE logic transfers to SGD *including its known
failure mode*, which is stronger evidence than a clean pass — the boundary
came along with the law. Level for the ML↔GGE correspondence on this model:
**L2 exact + L3 plausible** (same statement, mechanism identification =
noise-vs-charge timescale separation, shown here only in the minimal model).

## Boundaries

- Minimal scalar model; matrix/deep/ReLU cases untested (Kunin et al. give
  the charges; the sufficiency test would carry over).
- Label noise only; minibatch-only noise has different structure.
- "Stationary" = plateau; the true stationary limit erodes the charge by
  construction. The claim is now explicitly timescale-indexed.
