# Compression & the information bottleneck

> **One-line claim:** Efficient systems keep only the information about the input
> that is predictive of what they care about, discarding the rest — a principle
> spanning coding, perception, and learning.
> **Headline correspondence level:** L2–L3 (shared rate–distortion / IB
> objective). *(provisional — seed)*
> **Status:** seed

## Statement

The information bottleneck: find a compressed representation T of input X that
maximizes information about a target Y, minimizing I(X;T) subject to preserving
I(T;Y). Generalizes rate–distortion theory and the minimum description length
principle. Domain-neutral object: the IB/rate–distortion trade-off curve.

## Manifestations by domain (seed)

- Information theory: rate–distortion; MDL — anchor.
- Neuroscience: efficient-coding hypothesis; predictive coding — L2/L3.
- ML: representation learning; IB view of deep nets (contested) — L2.
- Perception/psychophysics: lossy compression matching natural-scene statistics — L2.

## To develop

Ties to `entropy-information.md` (same functional family) and
`tradeoffs-pareto.md` (IB curve is a Pareto front). Question: does the efficient-
coding hypothesis make *quantitative* predictions of receptive fields that match
data (→ L3), or is it a post-hoc description? Refs: Tishby–Pereira–Bialek 1999;
Barlow 1961.
