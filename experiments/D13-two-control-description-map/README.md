# D13 — D8's m = 2 residue under a literal description map (result)

**Question ([D13](../../questions/UNKNOWN-LAWS.md)):** D11 §2 says D8's
Grassmannian point "is the same statement with r simultaneous controls" —
that col(Y) is spectral data of the description map's linearization. Named
untested by D11 and D12. Is it?

**Status: no — one line of it is.** For the exactly renormalizable Ising model
on the diamond hierarchical lattice (temperature and field, two relevant
directions), the column space of the slope matrix **rotates by 1.15 rad** as
the base ray κ = h/t^Δ moves across two decades, while the planes keep exactly
one direction in common, and that direction is the spectral weight vector
[w]. The rest of the plane is scaling-function data.

**Two registered bounds failed**, both for the same reason: the log-periodic
modulation of the slopes, which I bounded at 1e-2, reaches 6.7e-2 at strong
field. Details below; the failures are real and are not repaired by the
post-hoc check, only explained by it.

Run it: `python3 run.py` (mpmath + numpy, deterministic, ~2.5 min).
Registered first, in a commit with no code:
[`PREREGISTRATION.md`](./PREREGISTRATION.md). Derivation:
[`derivations/D13-two-control-description-map.md`](../../derivations/D13-two-control-description-map.md).

---

## Setup

Bond weight exp(K s s′ + (h/2)(s + s′)); one renormalization step replaces a
diamond of 4 bonds by one. The recursion (K, h) ↦ (K′, h′) and the free
energy f = Σ 4^{−(n+1)} g(K_n, h_n) are exact. K_c = 0.6093778634,
λ_t = 1.67857351, λ_h = 3.67857351 (by hand: 2 tanh 2K_c and
2(1 + tanh 2K_c)), Δ = 2.514797.

Observables: m = ∂_h f, χ = ∂²_h f, −∂³_h f, −∂_t m. Y_ij = ∂ ln O_i/∂ ln ε_j
from exact mixed partials — no fitting, no sampling. Predicted one-step
weights w = ln 4 − k ln λ_h − l ln λ_t = (0.083769, −1.218756, −2.521281,
−0.434175). κ\* = 0.7407 was located by the registered rule
(∂ ln m/∂ ln h midway between its weak- and strong-field values).

## Results

### P1 — the discrete relation (near-identity — passes)

|ln[O_i(λ_t t, λ_h h)/O_i(t, h)] − w_i| ≤ **4.9e-7** over 3 rays × 8 phases ×
4 observables, registered 1e-4. One step of the map multiplies each
observable by exactly its spectral weight, to the O(t) = 1e-6 budget.

### P3 — rank 2 (AT RISK — passes)

σ₂/σ₁ ≥ 0.343 / 0.591 / 0.126 at 0.1κ\* / κ\* / 10κ\*; registered > 0.05.

### P4 — the plane moves, one line stays (AT RISK — the core; passes on the far pair, fails one bound on one pair)

| pair | largest principal angle | smallest | common direction to [w] | registered | |
|---|:--:|:--:|:--:|:--:|:--:|
| 0.1κ\* vs 10κ\* | **1.155** | 4.0e-3 | 9.0e-3 | ≥ 0.05, ≤ 1e-2, ≤ 1e-2 | pass |
| 0.1κ\* vs κ\* | 0.368 | 2.1e-4 | 1.2e-3 | ≥ 0.02, ≤ 1e-2, ≤ 1e-2 | pass |
| κ\* vs 10κ\* | 0.795 | 4.4e-3 | **1.04e-2** | ≥ 0.02, ≤ 1e-2, ≤ 1e-2 | **fail, by 4%** |

The qualitative claim is not in doubt: the planes differ by an angle of order
one and share a line to a few milliradians. **As registered, P4 is a fail** —
the conjunction over three pairs does not hold.

The slope matrix itself, phase 0, to show what moves:

| | 0.1κ\* | κ\* | 10κ\* |
|---|:--:|:--:|:--:|
| m | (−1.781, 0.772) | (−1.177, 0.532) | (−0.348, 0.202) |
| χ | (−1.609, −0.296) | (−0.375, −0.786) | (0.660, −1.195) |
| −∂³_h f | (−2.377, −0.991) | (−1.484, −1.348) | (0.708, −2.269) |
| −∂_t m | (−2.593, 0.698) | (−1.266, 0.170) | (0.127, −0.384) |

Every entry moves, several change sign. **No individual exponent, no ratio,
and not the plane is an invariant of the fixed point. The line is.**

### P2 — the infinitesimal Euler relation (AT RISK — fails one of its two bounds)

e = Y·ℓ − w, with ℓ = (ln λ_t, ln λ_h):

| ray | max \|e\| over phase | \|phase-mean of e\| | spread of Y entries over one period |
|---|:--:|:--:|:--:|
| 0.1κ\* | 1.5e-3 | 1.2e-7 | 4.9e-3 |
| κ\* | 3.3e-3 | 1.6e-7 | 9.8e-3 |
| 10κ\* | **6.7e-2** | 3.0e-7 | **1.2e-1** |

Registered: max |e| < 1e-2 and |mean| < 1e-4. **The mean passes by a factor
of 300; the bound fails at 10κ\* by a factor of 6.7.** The residual is
largest for −∂³_h f (6.7e-2), then χ (1.5e-2).

This is the log-periodic amplitude of Derrida–Itzykson–Luck, and it is not
small here. The map is discrete, so scaling holds for one step (P1, 5e-7) and
not infinitesimally; local log-slopes oscillate around their period mean by
up to 12% of unity at strong field. I registered "small" from a general
impression of that literature and had no number for this model. That is the
same slip as D12's gate — **a bound asserted rather than derived** — and it
is what broke P4's third row: w lies in col(Y) only up to e.

> *Post hoc, not registered.* Replacing Y by its mean over the eight phases
> (for which Ȳ·ℓ = w to 3e-7): largest angles 1.156 / 0.368 / 0.796, smallest
> 1.0e-7 / 1.4e-8 / 7.8e-8, common direction to [w] 9.9e-8 / 1.2e-7 / 1.3e-7.
> With the modulation averaged out the line is shared to seven digits. This
> explains the failures; it does not convert them.

### Guard

No observable changes sign anywhere on the grid.

## What it means for D8 and D11

- **D8 stands as geometry**: col(Y) is invariant under the monomial group at a
  fixed base point, rank counts relevant directions.
- **D11 §2's extension to m > 1 does not.** The Grassmannian point is not the
  spectrum. With n = 4, r = 2 it carries r(n − r) = 4 numbers; the spectral
  ray carries n − 1 = 3; and a single plane does not even single out the ray
  inside it. The ray is recovered from **two** base rays (the intersection),
  or from D7's one-parameter approach along a quasi-homogeneous ray.
- **D8's base point was a choice.** D8 measured each germ at one point of one
  ray and reported col(Y) as the residue. Here the analogous object moves by
  more than a radian with κ. D8's own germs should be expected to do the
  same; that is not tested here.
- **For a discrete map, the infinitesimal log-slope is not the invariant; the
  per-step increment is.** D7 §1 said the discrete chart uses per-level
  increments. This is the first place in the arc where using the other one
  costs more than rounding.

## Honest limits

- **N0.** "Exponents fix one direction; the scaling function fixes the rest"
  is standard two-field scaling theory, and log-periodic amplitudes are DIL
  1984. What moves is this repo's own statement.
- **One model, m = 2, no irrelevant direction.** The bond-weight space is
  closed and two-dimensional, so D8's rate leg (P4 there) has no analogue
  here.
- **Route independence is weaker than D12's.** The observables are computed
  from the same recursion whose Jacobian gives λ_t, λ_h; what is independent
  is that no measurement uses the linearization or the scaling form.
- **Disordered side only** (t > 0, h > 0), three rays, two decades of κ.
- **The Ising-with-field recursion on this lattice was derived here**, not
  taken from a source; the search confirmed the zero-field Potts case only.
  λ_t matches the known ν ≈ 1.338.
