# S7 — critical slowing down as universal early warning (result)

**Question ([S7](../../questions/SPECULATIVE.md)):** is "slowing down before a
transition" one cross-domain signal? Plus the middle-zone prediction from
[essay 4](../../essays/04-the-periphery-split.md) / [S25's verdict](../../derivations/S27-control-split.md):
critical slowing down should reduce to **softening of Φ's Hessian** — the
same ∇²Φ object as S3's susceptibilities and the Goldstone/reachability null
spaces, approached from the dynamical side.

**Status: confirmed at the mechanism level, refuted at the exponent level —
which is exactly the split the ladder predicts.**

Run it: `python3 run.py` (pure numpy, ~10 s, deterministic).

## Design

One law, three domains, measured independently in each:

```
        tau · lambda_min = 1
```

where λ_min is the relevant curvature (Hessian of the potential / free
energy) and τ the empirically measured relaxation time — autocorrelation
time of the noisy trajectory (legs A, B), convergence time of training
(leg C).

- **A — ecology-style saddle-node** `dx = (r+x²)dt + σdW`, r→0⁻;
  λ = 2√(−r).
- **B — mean-field Ising** (Langevin), T→T_c⁺; λ = 1 − 1/T.
- **C — learning**: full-batch GD on least squares as P/N→1; the curvature
  is *literally* the Hessian's smallest eigenvalue, whose vanishing at the
  interpolation threshold is the Marchenko–Pastur edge (1−√γ)² — the same
  transition whose Fisher blow-up S3 confirmed, now seen from the
  time-domain side.

## Results

**The collapse holds.** Across 15 points spanning three domains and two
distinct notions of "time" (physical time, GD iterations):

```
   tau · lambda  =  0.94 ± 0.13     (min 0.77, max 1.20)
```

One mechanism — curvature softening sets the slowest timescale — with no
per-domain tuning.

**The exponents do not transfer.** τ diverges with the control parameter at
domain-specific rates: fitted −0.55 (theory −½, saddle-node), −0.73 (theory
−1, Ising), −2.05 (theory −2, MP edge). "Critical slowing down" is **not one
scaling law**; it is one *relation* (τ = 1/λ_min) composed with a
domain-specific curve λ_min(control).

**A boundary, found on schedule.** Leg B's fitted exponent (−0.73 vs −1)
degrades closest to T_c, where the linear curvature falls below the noise
scale and the quartic term dominates the restoring force. That is the known
failure regime of linear early-warning theory — the entry's boundary
condition, observed rather than assumed.

## Verdict

- S7's mechanism reading: **L3 confirmed on these models** — the shared
  generative fact is Hessian softening, and it quantitatively predicts τ in
  all three domains (τλ = 1).
- S7's "universal signal" reading (one exponent, one threshold): **L1,
  retired** — exponents are domain-specific by construction.
- Middle-zone reduction: **supported.** The dynamical invariant reduces to
  the spectrum of ∇²(free energy) — critical slowing down is Φ's Hessian
  going soft, i.e. the *approach* to the singular set where S3 (divergence),
  S25 (null spaces), and Goldstone modes (flat directions) already live. The
  fourth arrival at the same object.

## Boundaries

- Mean-field / low-dimensional models only; no spatial structure (real
  early-warning practice fights detrending and red noise we don't simulate).
- Leg B near-critical bias documented above.
- Saddle-node (leg A) has no Φ in the equilibrium sense — the "free energy"
  is a potential; the reduction claim there is to Hessian-of-potential,
  the L2 shadow of the Φ statement.
