# M15 — is SGD's quasi-conserved charge an adiabatic invariant? (result)

**Question ([M15](../../questions/L3-MECHANISMS.md)):** adiabatic invariance
under slow drive is a candidate L3 mechanism — fast motion plus a slowly varying
parameter (ratio ε) conserves action-like variables, and the **scaling of the
drift rate in ε** identifies the regime: power-law (ordinary averaging) versus
exponentially small in 1/ε (Neishtadt/Nekhoroshev). The register's
discriminator, applied to [S26](../S28-sgd-charges/): that experiment found the
balancedness charge quasi-conserved (erosion ~5.6e-7/step) and called it a
"prethermalization plateau" — a *description*. M15 asks whether the averaging
mechanism is actually running.

**Status: confirmed, in the ordinary-averaging regime, with an exact law —
and with one pre-registered estimator failing and being diagnosed.**

Run it: `python3 run.py` (pure numpy, ~65 s, deterministic).
Predictions were registered in [`PREREGISTRATION.md`](./PREREGISTRATION.md)
before any measurement; that file is unedited.

## The derivation (registered before the run)

For f(x)=u·v·x the stochastic gradients factor through one scalar
m = (1/B)Σ r̂ᵢxᵢ: ĝ_u = v·m, ĝ_v = u·m. So

    u·ĝ_u − v·ĝ_v = 0     **for every realization of the noise**, not in expectation

— the symmetry generator is exactly orthogonal to the *stochastic* gradient.
The entire drift is therefore second order, and here exact:

    **Q' = Q·(1 − η²m²)**   ⟹   k = η²·E[m²] = **η²σ²E[x²]/B**

at the plateau, where the residual is pure label noise.

## Results

| # | Prediction | Result | |
|---|-----------|--------|---|
| **P1** | per-step law exact to <1e-12 | **1.6e-16** | ✓ |
| **P2** | k ∝ η^p σ^q B^s with p=2, q=2, s=−1 | **p = 2.021, q = 1.999, s = −1.003** (R² ≥ 0.99998) | ✓ |
| **P3** | power law beats exp(−c/η) by ΔAIC ≥ 10 | **ΔAIC = 73.6** (R² 0.99998 vs 0.783) | ✓ |
| **P4** | absolute k within 10%, no fitting | 18/18 grid points; median ratio **1.018** | ✓ |
| **P5** | S26's 5.6e-7 revises to ~7.8e-7 | measured **7.30e-7**, predicted 7.22e-7 | ✓ |
| **P6** | scaling survives the wide net (p = 2 ± 0.10) | pre-registered estimator **✗ 1.64**; decisive test **τ ∝ η^−2.038** | ✗→✓ |
| **P7** | coordinatization degrades as R → O(1) | **err = 1.12·R^−0.97**, unity at **R = 1.13** | ✓ |

### P3 — the discriminator

SGD's charge erosion is **ordinary averaging, not the exponentially-protected
regime.** Over a 50× range of η the power law fits at R² = 0.99998 while the
Nekhoroshev form manages 0.783, ΔAIC = 73.6. This is the expected answer and the
reason matters: the perturbation is *stochastic and broadband*, which is exactly
the condition under which exponential protection fails. The plateau is long
because η is small, not because anything protects it.

### P4 — the residual is itself lawful

Measured/predicted is not scattered around 1; it rises monotonically
(1.002 → 1.096 over η ∈ [1e-3, 5e-2]) and fits **1 + 1.93η**. That is the
plateau's own O(η) fluctuation adding an O(η) correction to E[m²] — and it
quantitatively explains why the measured exponent is 2.021 rather than 2.000:
predicted excess at the sweep's geometric-mean η is 0.0156, measured 0.0214.

### P5 — S26's number, corrected

S26 estimated erosion from Q₀ against a whole-run stationary mean, which mixes
in the burn-in. The clean plateau measurement is **7.30e-7/step (not 5.6e-7)**,
matching the parameter-free prediction 7.22e-7, so the quasi-conservation window
is **~1.37M steps, not ~1.8M**. S26's qualitative conclusion is untouched; its
number was ~24% low.

### P6 — a pre-registered estimator failed, and why

The registered wide-net estimator (net charge displacement over a fixed window,
divided by the window) returned p = **1.64**, outside CI. Diagnosis rather than
replacement:

- **Saturation, measured.** Total displacement versus window length has log-log
  slope **0.39**, not 1. A rate estimator gives slope 1; this one is watching a
  quantity that stops moving.
- **Why it stops.** In the scalar model ΔQ = −η²m²Q drives Q→0 monotonically. In
  the wide net (f(x)=vᵀWx, per-unit charges Q_j = ‖W_j‖²−v_j²) the exact
  second-order term is η²(v_j²‖m‖² − ⟨W_j,m⟩²), which by Cauchy–Schwarz is
  bounded below by −η²‖m‖²Q_j **but can be positive** — it is positive whenever
  W_j is orthogonal to the noise direction m. So charges do not decay to zero;
  they relax to an *alignment-dependent quasi-equilibrium*. Net displacement
  measures the distance to that equilibrium, not a rate.
- **The mechanism itself survives exactly.** The first-order cancellation — the
  actual averaging claim — holds in the wide net to **1.04e-15**. The drift is
  purely second order there too.
- **Decisive test.** The physically meaningful quantity is the *relaxation time*
  to that quasi-equilibrium. Starting every η from a common state (burn-in at
  fixed η) and using a common threshold amplitude (A varies only 8% across η,
  confirming it is a property of the equilibrium and not of η):
  **τ ∝ η^−2.038, R² = 0.99994** over a decade — τ = 470814 / 117495 / 28605 /
  6797 steps for η = 0.004 / 0.008 / 0.016 / 0.032. P6 confirmed on the
  corrected observable.

The honest reading: the registered estimator was wrong on its face, the
correction was forced by a measurement (the saturation slope) rather than chosen
to rescue the prediction, and both are on the record in `verdict.json`.

### P7 — the breakdown, better than expected

Tagged exploratory; it produced the sharpest result after P1. Across a 48-point
(η, σ, B) grid, sufficiency of the charge for the plateau (does
‖(u,v)‖² = √(Q²+4ŵ²) still hold?) degrades as a clean power law in the
timescale-separation ratio R = Bλ/(ησ²E[x²]):

    **suff_err = 1.12 · R^−0.97**   (R² = 0.92, 30 points above the noise floor)

extrapolating to **error 1 at R = 1.13** — the breakdown sits at R ~ O(1),
exactly where an adiabatic argument says it must. Measured range: err = 3.7e-4
at R = 25892 (S26's setting) up to 0.38 at R = 3.4. Four high-noise
configurations diverged and are excluded.

## Verdict

The averaging mechanism is running, and identified rather than assumed:

1. The first-order term vanishes **identically** (not on average), in both the
   scalar and the wide model — this is the mechanism, and it is exact.
2. The residual drift is second order with **p = 2, q = 2, s = −1** and a
   parameter-free absolute rate good to 2%.
3. The regime is **ordinary averaging**; exponential protection is decisively
   rejected.
4. Quasi-conservation degrades as **1/R** with the breakdown at R ≈ 1.

So S26's "prethermalization plateau" is upgraded from a phenomenological label
to a mechanism with a number: the plateau lasts B/(η²σ²E[x²]) steps, and it ends
when the timescale separation reaches O(1). For the M15 register entry this is
one domain's leg done — the *cross-domain* identity claim (that this is the same
averaging mechanism as in plasma confinement, the quantum adiabatic theorem, and
near-integrable prethermalization) is **not** established by this experiment.
What is established is that the ML instance has the mechanism's fingerprint.

## Boundaries

- Two models only: scalar deep-linear and a small (d=6, h=4) two-layer linear
  net. No nonlinearity, no depth > 2. Kunin et al. give the charges for deeper
  and ReLU cases; the same three sweeps would carry over.
- Label noise only; minibatch-sampling noise at the optimum vanishes here by
  construction (y is an exact linear function of x), so the σ-sweep is
  measuring one noise source, not the general case.
- P7's low-R corner is reached by raising σ and shrinking B, which also inflates
  plateau fluctuations — the 1/R law is clean but the *knee* is not fully
  disentangled from that confound.
- The stability constraint ηλ < 2 bounds R from below at Bλ²/(2σ²E[x²]); in the
  small-noise/large-batch regime that bound is large, so quasi-conservation is
  structurally protected there and the breakdown is only reachable with large
  σ²/B. Reported, not exploited.
- Single random seed for the wide-net legs (16 vectorized seeds for the scalar
  legs).
