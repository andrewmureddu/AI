# M15 pre-registration — written before any measurement

Per [`questions/L3-MECHANISMS.md`](../../questions/L3-MECHANISMS.md)'s working
rule: *register the discriminator's expected value before measuring it.* Nothing
below is revised after the run; results live in [`README.md`](./README.md).

**Mechanism under test (M15).** Adiabatic invariance under slow drive: with a
fast motion and a slowly varying parameter (ratio ε), action-like variables are
conserved to high order; the drift rate's **scaling in ε** identifies the
regime — power-law (ordinary averaging) versus exponentially small in 1/ε
(Neishtadt/Nekhoroshev).

**Instance.** [S26](../S26-sgd-charges/) found SGD's balancedness charge
Q = u²−v² quasi-conserved, eroding at ~5.6e-7/step, and labelled the result a
"prethermalization plateau." That is a *description*. M15 asks whether the
averaging mechanism is actually running, which is a question about how the
erosion rate scales with the slowness parameter — here the learning rate η.

---

## The derivation (done before the run, so it is a prediction, not a fit)

Model: f(x) = u·v·x, loss L = E[(uvx−y)²]/2, charge Q = u²−v².

For a minibatch with residuals r̂ᵢ = uvxᵢ − yᵢ − σξᵢ, the stochastic gradients
factor through a single scalar m ≡ (1/B)Σ r̂ᵢxᵢ:

    ĝ_u = v·m ,  ĝ_v = u·m

**First order vanishes identically.** u·ĝ_u − v·ĝ_v = uvm − uvm = 0 — not in
expectation, but *for every realization of the noise*. This is the symmetry
generator being exactly orthogonal to the stochastic gradient (the mechanism
`symmetry-sector.md` §3 identifies for gradient flow, here surviving the noise).

So the whole drift is second order, and for this model it is exact:

    Q' = (u − ηĝ_u)² − (v − ηĝ_v)² = Q − 2η(uĝ_u − vĝ_v) + η²(ĝ_u² − ĝ_v²)
       = Q + η²m²(v² − u²)
    ⟹  **Q' = Q·(1 − η²m²)**            … exact, every step

Multiplicative decay: Q never changes sign, and the per-step rate is

    k = η²·E[m²]

At the plateau (uv ≈ ŵ) the residual is pure label noise, r̂ᵢ ≈ −σξᵢ, so
E[m²] = σ²·E[x²]/B and

    **k = η² σ² E[x²] / B**            … parameter-free

The same formula covers S26's leg A: away from the optimum m² is the
*deterministic* squared gradient, and total drift over fixed physical time
T = ηN_steps is ∝ ηT⟨m²⟩ — S26's measured "linear in lr" flow-limit drift is
this formula's other face.

---

## Registered predictions

**P1 — exactness.** Per-step ΔQ matches Q·(1−η²m²) to machine precision
(rel. err. < 1e-12) on individual instrumented steps.

**P2 — scaling exponents.** Fitting k ∝ η^p σ^q B^s over the sweeps:
- **p = 2.00 ± 0.05**
- **q = 2.00 ± 0.05**
- **s = −1.00 ± 0.05**

**P3 — the discriminator (regime identification).** log k versus log η is
linear with slope 2; the Nekhoroshev-type model log k = a − c/η is **decisively
rejected** against it (higher AIC by ≥ 10). SGD's charge erosion is therefore
**ordinary averaging, not the exponentially-protected regime.** *Reasoning for
the prior:* the perturbation is stochastic and broadband, which is exactly the
condition under which exponential protection fails. A power-law result confirms
the mechanism; an exponential result would mean something is suppressing the
noise's secular effect and the S26 plateau is a stronger phenomenon than
claimed.

**P4 — absolute rate, no fitted parameters.** Measured k agrees with
η²σ²E[x²]/B within 10% across the whole grid.

**P5 — S26's number is revised upward.** At S26's settings (η=5e-3, σ=0.5,
B=8, E[x²]≈1) the prediction is k = 7.8e-7/step, versus the 5.6e-7 S26
reported from a coarser estimator. Predict the clean measurement lands near
7.8e-7, and the quasi-conservation window shortens correspondingly (~1.3M steps
rather than ~1.8M).

**P6 — survival beyond the exact case.** In a wide two-layer linear net
(f(x) = vᵀWx, per-unit charges Q_j = ‖W_j‖² − v_j²), the exact scalar algebra
does **not** carry over — the second-order term is
η²(v_j²‖m‖² − ⟨W_j,m⟩²), which is bounded below by −η²‖m‖²Q_j (Cauchy–Schwarz)
and can even be positive. Prediction: the *scaling* survives anyway —
p = 2.00 ± 0.10 for the rms charge drift — because it is a property of the
noise amplitude, not of the algebra. This is the leg that decides whether M15
is a mechanism or an artifact of the minimal model.

**P7 — breakdown (exploratory).** Timescale separation
R = τ_slow/τ_fast = Bλ/(ησ²E[x²]) with λ ≈ (u²+v²)E[x²] the stiff curvature.
Stability (ηλ < 2) forces R > Bλ²E[x²]/(2σ²), so **quasi-conservation is
structurally protected at any stable learning rate** and can only be destroyed
by raising σ²/B. Predict: driving R → O(1) via small B and large σ degrades the
charge's coordinatization of the plateau (S26's sufficiency relation
‖(u,v)‖² = √(Q²+4ŵ²)), with the knee near R ~ O(1). Tagged exploratory because
the large-σ regime also inflates plateau fluctuations, which is a confound.

## What would kill M15 here

- p ≠ 2 outside CI, or the erosion rate independent of η (P2/P3) — no averaging
  mechanism, the plateau is something else.
- Exponential-in-1/η winning the model comparison (P3) — mechanism
  misidentified as ordinary averaging; the plateau would be *stronger* than
  claimed.
- Scaling failing in the wide model (P6) — the result is scalar-model algebra,
  not a mechanism, and M15 drops out of the register.
