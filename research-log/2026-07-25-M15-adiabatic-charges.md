# 2026-07-25 — Restraint: SGD's plateau is ordinary averaging, and it ends at R ≈ 1

**Worked on:** [M15](../questions/L3-MECHANISMS.md) (adiabatic invariance under
slow drive); [S26(iii)](../experiments/S26-sgd-charges/) as its ML instance.
**Change:** new experiment
[`experiments/M15-adiabatic-charges/`](../experiments/M15-adiabatic-charges/);
M15 gains a ⟳ restraint note; S26's erosion rate corrected (5.6e-7 → 7.30e-7);
S26's "L3 route = timescale separation" marked walked. No catalog level changed
— see *Decisions*.

## What I did

Ran the register's top pick. S26 had found the balancedness charge Q = u²−v²
quasi-conserved and called the result a "prethermalization plateau." That is a
description; M15's discriminator asks whether the averaging *mechanism* is
running, which is a question about how drift scales with the slowness parameter
η — power-law (ordinary averaging) or exp(−c/η) (Neishtadt/Nekhoroshev).

Derived the expected answer first and registered it in
[`PREREGISTRATION.md`](../experiments/M15-adiabatic-charges/PREREGISTRATION.md)
before measuring, per the register's own rule.

## What I found

**The averaging structure is exact, not approximate.** The stochastic gradients
factor through a single scalar m, so u·ĝ_u − v·ĝ_v = 0 *for every realization of
the noise* — not in expectation. The symmetry generator is orthogonal to the
**stochastic** gradient, which is stronger than the gradient-flow orthogonality
`symmetry-sector.md` §3 identified. The whole drift is second order and, here,
exact: Q' = Q(1 − η²m²), hence k = η²σ²E[x²]/B.

**Registered scaling confirmed:** p = 2.021, q = 1.999, s = −1.003, absolute
rate good to 2% over 18 grid points with no fitting.

**The discriminator answers "ordinary averaging"** — power law over Nekhoroshev
by ΔAIC = 73.6 (R² 0.99998 vs 0.783). This is the expected answer for a
*stochastic, broadband* perturbation, and it deflates the plateau in a useful
way: it is long because η is small, not because anything protects it.

**Three things I did not expect:**

1. **The residual is lawful.** Measured/predicted isn't scattered around 1; it
   rises monotonically as 1 + 1.93η — the plateau's own O(η) fluctuation
   correcting E[m²] — and that quantitatively explains why the exponent is 2.021
   rather than 2.000 (predicted excess 0.0156, measured 0.0214). The deviation
   from the law is the law's next term.
2. **The breakdown, registered as exploratory, is the sharpest secondary
   result.** Sufficiency of the charge for the plateau degrades as
   suff_err = 1.12·R^−0.97 in the timescale-separation ratio R, over 30 points
   and three decades, extrapolating to unity error at **R = 1.13**. An adiabatic
   argument says the breakdown must sit at R ~ O(1); it does. So the plateau's
   *end* is now predicted as well as its length.
3. **One face of S26 was two faces of one law.** Leg A ("drift linear in lr over
   fixed physical time") and leg C ("noise erodes the charge") are the same
   per-step formula with m² being the deterministic squared gradient in the
   first case and the noise variance in the second.

**A pre-registered estimator failed.** The wide-net leg returned p = 1.64,
outside CI. Diagnosed rather than swapped: total displacement versus window
length has log-log slope **0.39**, not 1, so the estimator was watching a
quantity that stops moving. The reason is structural and interesting — in the
wide net ΔQ_j = η²(v_j²‖m‖² − ⟨W_j,m⟩²) can be **positive** (whenever W_j ⊥ m),
so charges relax to an alignment-dependent quasi-equilibrium instead of decaying
to zero as they do in the scalar model. On the corrected observable (relaxation
time to that equilibrium, common start state, common threshold) τ ∝ η^−2.038 at
R² = 0.99994 across a decade. The first-order cancellation itself holds in the
wide net to 1.0e-15 — the mechanism is not an artifact of the scalar algebra.

**S26's number was ~24% low** (5.6e-7 vs 7.30e-7/step): its estimator compared
Q₀ against a whole-run mean, mixing in the burn-in. Window 1.37M, not 1.8M.
S26's qualitative conclusion is untouched.

## Decisions

- **No catalog level moved, deliberately.** This establishes the mechanism's
  fingerprint in *one* domain. M15's claim is a cross-domain identity — same
  averaging mechanism as plasma confinement, the quantum adiabatic theorem,
  near-integrable prethermalization — and one leg is not that. Recording it as
  a confirmed ML instance, not as an L3 promotion, is the whole point of the
  convergence-vs-identity rule the register was built on.
- **Kept the failed estimator in the code and the verdict JSON**, with its
  diagnosis. The correction was forced by a measurement (the saturation slope),
  not chosen to rescue the prediction, and the record should show which.
- The pre-registration file is unedited after the run.

## Next

- The second leg is what makes M15 cross-domain: take a *physical*
  near-integrable system (or the quantum adiabatic case), measure the same
  drift-vs-ε scaling and the same R ~ O(1) breakdown, and check the exponents
  agree. That is the identity test; today was the fingerprint test.
- The Nekhoroshev regime should be reachable by making the perturbation
  *narrowband* — full-batch GD with a deterministic periodic driver rather than
  broadband label noise. If drift then goes exponentially small in 1/η, the
  discriminator has separated the two regimes inside the ML domain, which would
  be a much stronger statement than confirming one of them.
- Register order stands otherwise: **M11** (stochastic resetting) next, then
  **M3** (Molloy–Reed rewiring).
