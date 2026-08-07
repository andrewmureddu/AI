# S5 × D1/D6 reconciliation — supporting check

Small closed-form/numerical check supporting
[`derivations/S5-D6-noise-threshold-classifier.md`](../../derivations/S5-D6-noise-threshold-classifier.md).
Not a full pre-registered experiment — both formulas checked here are exact
algebra (BSC's χ²_sym and BEC's N are closed-form in the channel parameter),
so this verifies arithmetic and reparametrization behavior rather than testing
an at-risk prediction. The derivation is explicit about which parts of that
document this does and does not settle (§3a is this script; §3b, the decisive
part, is a re-reading of numbers [S5](../S5-noise-thresholds/) already
published and requires no new code).

Run it: `python3 run.py` (pure Python, no dependencies, deterministic, <1s).

## What it checks

1. BSC's χ²_sym(p) and BEC's N(e) = 1/(1−e), both closed-form, reproduce S5's
   measured α = 2 and α = 1 exactly by direct algebra (not a fit).
2. Under a **regular** reparametrization of "distance to threshold" (smooth,
   finite nonzero derivative at the singular point — e.g. v = sin(ε)), the
   fitted exponent is unchanged.
3. Under the **singular** G_pow group (u = ε^a), the exponent divides by a,
   exactly as D1's chart-order formalism predicts.

## What it does not check

Whether S5's α equals D6's q1 in the strict sense (D6's own noise-rounding
crossover or excess-kurtosis apparatus, which needs a genuine stochastic model
with a separate noise scale D — no such model is built here). See the
derivation's §5 for why that's left open rather than approximated here.
