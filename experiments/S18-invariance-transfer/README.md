# S18 — does invariance-across-environments predict transfer? (result)

**Question ([S18](../../questions/SPECULATIVE.md)):** the prediction-field frame's
central falsifiable consequence — an invariant's *level* (how environment-invariant
its prediction is) should predict how well it **transfers** to an unseen setting.
S18 sharpens this to the causal-inference claim (ICP/IRM): the relationship that
stays invariant across environments is the causal one, and it is the one that
transfers.

**Status: falsifier survived (in a controlled linear SCM). Frame's operational core
holds; the grand empirical claim remains open.**

Run: `python3 run.py` (pure numpy, deterministic) then `python3 plot.py` →
[`s18_result.png`](./s18_result.png).

## Setup

A structural causal model with an invariant mechanism and a spurious correlate:

```
   X_c ~ N(0,1)                        # a genuine cause of Y
   Y   = a·X_c + ε_y                   # INVARIANT: coefficient a fixed across envs
   X_s = b_e·Y + ε_s                   # X_s is an EFFECT of Y; coupling b_e VARIES
```

Training environments use `b_e ∈ {0.8, 1.0, 1.2, 1.5}`; the held-out **test**
environment uses `b = −1.2` — a spurious coupling *outside the training range and
sign-flipped*. `X_s` is deliberately the *stronger in-distribution predictor*
(small ε_s), so naive ERM leans on it.

**Why this is not a tautology:** invariance is measured only on the *training*
environments (the spread of a predictor's fitted coefficient across them); transfer
error is measured only on the *held-out* environment. The two numbers come from
disjoint data, so a relationship between them is an empirical finding.

## Result (`verdict.json`)

| quantity | value | reading |
|----------|:-----:|---------|
| in-dist MSE, spurious-only | **0.16** | spurious feature looks *great* in-distribution… |
| in-dist MSE, causal-only | 0.99 | …6× better than the causal one, so ERM grabs it |
| transfer MSE, spurious-only | **7.71** | …but collapses on the unseen environment |
| transfer MSE, causal-only | **0.95** | the invariant feature is unaffected — it transfers |
| transfer MSE, ERM (both) | 6.56 | ERM inherits the spurious failure |
| Spearman(train-instability, test-error) | **0.985** | invariance measured on train predicts held-out error |
| ICP stability-selection picks | **X_c (causal)** | train-only invariance selection recovers the causal feature |

Three findings, all in the figure:

1. **The inversion.** As the predictor slides causal→spurious, in-distribution error
   *falls* while transfer error *rises*. The most in-distribution-predictive model is
   the worst-transferring. (This is the trap ERM walks into.)
2. **Invariance ⇒ transfer, monotone (ρ = 0.985).** Coefficient instability across
   the training environments — never touching the test set — almost perfectly ranks
   transfer error on the held-out environment. This is the prediction-field claim,
   confirmed operationally: *level of invariance predicts transfer.*
3. **Selection works blind.** Choosing the feature whose coefficient is most stable
   across training environments (ICP-style) recovers the causal feature without ever
   seeing the test environment.

## Honest hedging (what this does and does not show)

- **Invariance = causation = transfer *by construction* here.** The SCM was built so
  that the invariant mechanism is the causal one. The experiment rigorously
  validates the *internal logic* (train-invariance predicts test-transfer; ERM is
  seduced by the spurious feature) but does **not** prove the grand claim that
  *natural* cross-domain invariants sit higher on transfer. That needs real
  cross-domain data.
- **Invariance is only certified over the sampled environments.** ICP/IRM's known
  limitation: a predictor invariant over the environments you happened to see can
  still break outside their span. Our test env is deliberately outside the span to
  show the *spurious* predictor breaking — the *invariant* one holds because the SCM
  guarantees it globally, which real data does not.
- **Linear / Gaussian.** Nonlinear confounding or anti-causal targets can behave
  differently.

## Verdict for the frame

The prediction-field frame's falsifier **did not fire**: invariance predicts
transfer, cleanly and monotonically, in a setting where we could measure both
independently. That lifts the frame's 🟢 operational core from "true by definition"
to "true and *demonstrated to have teeth*" — the most in-distribution-predictive
signal really is the wrong one to trust, and invariance really does rank transfer.

It does **not** promote the 🔴 metaphysical reading. And the real test still stands:
run the same invariance→transfer measurement on *actual* cross-domain invariants
from the catalog (do higher-ladder invariants transfer better across genuinely
different domains?). That is the experiment that would move the frame from
"self-consistent" to "empirically load-bearing."

## Next

- Repeat with a nonlinear SCM and with an anti-causal target (Y → X_c) to map where
  invariance-⇒-transfer weakens.
- The harder, realer version: pick 3–4 catalog invariants at different ladder levels
  and measure actual A→B predictive transfer.
