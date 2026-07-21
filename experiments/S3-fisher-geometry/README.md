# S3 — statistical curvature at a phase transition (result)

**Question ([S3](../../questions/SPECULATIVE.md)):** does a Fisher / statistical-curvature
quantity spike at a phase transition in *learning* the way it provably does in
thermodynamics — i.e., is curvature-blow-up a domain-neutral transition detector?

**Status: partially confirmed (two exactly-computable legs). Grokking still open.**

Run it: `python3 run.py` (pure numpy, ~1.4 s, deterministic). Figure:
`python3 plot.py` → [`s3_result.png`](./s3_result.png).

## What was tested

Grokking — the transition S3 originally named — needs torch and GPU-scale compute,
and a grokking run that fails to grok inside a CPU budget produces a *fake* null.
So instead we tested the **same underlying claim** on two transitions we can
compute exactly and reproducibly.

### Leg B — physics anchor (mean-field Ising)

Solve `m = tanh(m/T)` (J = 1, T_c = 1). The Fisher information for the external
field h equals the magnetic susceptibility χ = ∂m/∂h = Var(M)/T.

**Result:** χ peaks at **T = 1.000**, matching the theoretical T_c to grid
resolution, rising from ~0.02 to ~1.3×10⁴. The Fisher information *diverges at the
critical point* — exactly, not by analogy. (This is textbook; it's here to anchor
the geometric quantity we then look for in learning.)

### Leg A — learning (the novel claim: double descent)

Ridgeless random-feature regression, N = 40 training points, capacity P swept
through the interpolation threshold, 25 seeds. For a linear model the Fisher
information matrix is F = ΦᵀΦ/σ²; its worst-direction inverse, 1/σ_min², is the
Cramér–Rao variance in the least-identified direction.

**Result:** the test-error peak and the inverse-Fisher blow-up land on the **same
P/N = 1.000**. `dd_peaks_coincide = true`. The double-descent generalization
catastrophe *is* the Fisher matrix going singular — the same geometric event as
the Ising divergence, now in a learner.

```
test error          inverse-Fisher 1/σ_min²
      *|                     *|
       |                    * |*
       |                   *  | **
       |  (sharp spike)   *   |   **
  _____|_____            *    |     ***____
   P/N = 1.0            P/N = 1.0
```

## Verdict (`verdict.json`)

| quantity | measured | theory |
|----------|:--------:|:------:|
| Ising χ peak | T = 1.000 | T_c = 1.000 |
| double-descent test-error peak | P/N = 1.000 | 1.000 |
| inverse-Fisher peak | P/N = 1.000 | 1.000 |
| peaks coincide | **true** | — |

## Honest hedging (what this is *not*)

- **Proxy, not the full Riemann scalar curvature.** We measured Fisher-information
  magnitude / singularity (χ; 1/σ_min²), which is what actually blows up and is
  computable. The full Ruppeiner scalar curvature R is a stronger, costlier object;
  the coincidence shown here is necessary-not-sufficient evidence for the R-level
  claim in [`statistical-geometry.md`](../../invariants/statistical-geometry.md).
- **Coincidence, not yet mechanism-identity.** Two transitions show the same
  signature. That the Fisher metric is *literally the same object* in both
  (established math) makes L3 plausible, but this experiment alone shows L2-with-a-
  shared-object, not a proven common mechanism.
- **Double descent ≠ grokking.** We tested a different, tractable learning
  transition. Whether Fisher curvature also spikes at a *grokking* transition
  remains the open, torch-scale test.

## What would strengthen / kill it next

- **Strengthen:** show the inverse-Fisher peak *leads* the error peak in training
  time (early warning), not just coincides in capacity.
- **Kill the ML leg:** exhibit a genuine learning phase transition with *no* Fisher
  signal at it. None found here.
- **Extend:** the torch grokking run, when compute allows.
