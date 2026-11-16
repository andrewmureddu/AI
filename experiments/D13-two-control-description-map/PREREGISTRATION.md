# D13 pre-registration — written before any code or measurement

Works [D13](../../questions/UNKNOWN-LAWS.md): **D8's m > 1 residue under a
literal description map** — named as untested by D11 and again by D12.
[D11](../../derivations/D11-residue-reconciliation.md) §2 asserts that D8's
Grassmannian point "is the same statement with r simultaneous controls", i.e.
that col(Y) is spectral data of the linearization. Is it?

No code exists at the time of this commit.

---

## 0. Prior-art note (written first)

**Old.** Two-field scaling f(t, h) = b^{−d} f(λ_t t, λ_h h), scaling functions
of the single variable h/t^Δ, and the fact that scaling functions are
universal but are *not* determined by the exponents: Widom, Kadanoff, Fisher,
Wegner. Exact renormalization on hierarchical lattices: Berker & Ostlund
(1979), Griffiths & Kaufman (1982). **Log-periodic modulation of critical
amplitudes when the map is discrete**: Derrida, Itzykson & Luck, *Oscillatory
critical amplitudes in hierarchical models*, Comm. Math. Phys. 94 (1984) 115
(confirmed by search 2026-11-16; Potts on the diamond lattice — the search
did not surface the Ising-with-field case, so the recursion below is derived
here, not cited).

**Novelty: N0 for the physics, N1 at most** for what it does to D8/D11: a
statement of which part of an m-control residue is spectral. Nearest miss:
any text saying "the exponents fix one direction of the multi-field log-slope
data and the scaling function fixes the rest" — which is a fair paraphrase of
standard scaling theory, so the honest expectation is N0.

## 1. Setup

Ising model on the diamond hierarchical lattice (each bond replaced by two
parallel branches of two bonds in series; 4 bonds per step), bond weight
w(s, s′) = exp(K s s′ + (h/2)(s + s′)). Exact recursion, with
u₊₊ = e^{2K+2h} + e^{−2K}, u₋₋ = e^{2K−2h} + e^{−2K}, u₊₋ = 2 cosh h:

```
    K' = (1/2) ln(u++ u-- / u+-^2),   h' = ln(u++ / u--),   g = (1/2) ln(u++ u-- u+-^2)
    f(K, h) = sum_{n>=0} 4^{-(n+1)} g(K_n, h_n)          (free energy per bond, exact)
```

Fixed point K_c = ln cosh 2K_c (≈ 0.609), h = 0. Linearization, by hand:
λ_t = 2 tanh 2K_c (≈ 1.679), λ_h = 2(1 + tanh 2K_c) (≈ 3.679). Two relevant
directions and — the space of bond weights being closed and two-dimensional —
no irrelevant one. Δ = ln λ_h/ln λ_t.

Controls: t = K_c − K > 0, h > 0. Observables (n = 4), chosen to be
singular-dominated and, in mean-field at least, of fixed sign:
O = (∂_h f, ∂²_h f, −∂³_h f, −∂_t∂_h f). Slope matrix
Y_ij = ∂ ln O_i/∂ ln ε_j, computed from exact mixed partials of f (mpmath
arbitrary-precision differentiation, no fitting, no sampling).

Predicted one-step weights w_i = ln[O_i(λ_t t, λ_h h)/O_i(t, h)]
= ln 4 − k_i ln λ_h − l_i ln λ_t, with (l, k) = (0,1), (0,2), (0,3), (1,1).
ℓ = (ln λ_t, ln λ_h).

## 2. Claims

**C1 (identity under exact continuous scaling; expected to fail in a known
way).** Euler: Y·ℓ = w, hence w ∈ col(Y). The map is discrete, so only
O(λ_t t, λ_h h) = e^{w} O(t, h) is forced; the infinitesimal relation picks up
the derivative of a log-periodic amplitude. Prediction: residual
e = Yℓ − w is nonzero, small, and **averages to zero over one period**.

**C2 (at risk).** rank Y = 2 at every base ray.

**C3 (at risk — the core, aimed at D11 §2 and at D8).** The base ray is
labelled by κ = h/t^Δ. **col(Y(κ)) moves with κ**; what stays is one line:
the planes at different κ intersect in exactly one direction, and it is [w].
So for m = 2 the spectral content of D8's Grassmannian point is a single ray
(D7's ray, read along the quasi-homogeneous approach); the remaining r − 1
directions are scaling-function data, which the spectrum does not fix. If
instead col(Y) is κ-independent, D11's "same statement with r controls" stands
and this stone's claim is dead.

## 3. Procedure and numbers

**Choosing κ without peeking at the answer.** The natural scale of κ is
unknown to me. Rule, fixed now: κ\* is the κ at which
∂ ln m/∂ ln h = (1 + 1/δ)/2 at t₀, with δ = ln λ_h/(ln 4 − ln λ_h) — midway
between the weak-field value 1 and the strong-field value 1/δ. The κ list is
**κ\* × {0.1, 1, 10}**.

**Phases.** t_j = t₀ λ_t^{−j/8}, j = 0…7, t₀ = 1e-6, h_j = κ t_j^Δ: eight
points across one period of the discrete map.

**Error budget.** No irrelevant direction, so corrections to scaling are
analytic: relative O(t) from nonlinear scaling fields and the regular part of
f, i.e. ~1e-6 × an O(1–10) coefficient. Arithmetic at 30 digits base
precision. The log-periodic amplitude is the unknown; DIL report such
amplitudes as small, and I do not know the number for this model.

- **P1 (discrete relation; near-identity, at risk only through the O(t)
  budget).** |ln[O_i(λ_t t, λ_h h)/O_i(t, h)] − w_i| < **1e-4**, all i, all
  three κ, all eight phases.
- **P2 (C1).** max over phases, κ, i of |e_i| < **1e-2**; and the phase-mean
  of e_i has magnitude < **1e-4**. The size of max|e| is reported whatever it
  is; I am registering a bound, not a value.
- **P3 (C2).** σ₂/σ₁ of Y > **0.05** at every κ and phase.
- **P4 (C3).** At phase j = 0, between κ = 0.1κ\* and κ = 10κ\*: largest
  principal angle between the two column spaces ≥ **0.05 rad**; smallest
  principal angle ≤ **1e-2 rad**; and the common direction lies within
  **1e-2 rad** of [w]. Same for each adjacent pair, with the largest-angle bar
  at **0.02 rad**.
- **Guard.** If any O_i changes sign anywhere on the grid, that observable is
  reported as invalid for the log-slope construction rather than silently
  kept.

**What would kill it.** P4's largest angle below bar: col(Y) is (nearly)
κ-independent, the plane is spectral after all, or my κ range is too narrow —
the two are distinguished by whether Y's entries themselves move with κ, which
is reported. P4's smallest angle above bar: the planes do not share a line and
C1 is wrong beyond the log-periodic excuse.

Run: `python3 run.py` (mpmath, numpy).
