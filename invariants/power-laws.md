# Power laws / scale-free distributions

> **One-line claim:** Many systems have heavy-tailed distributions of the form
> P(x) ∝ x^−α over a wide range of scales.
> **Headline correspondence level:** L2 in general; L3 for specific mechanism-matched
> families (e.g. preferential-attachment networks).
> **Status:** developing
> **Floor:** **3** (Φ-singular) — heavy tails are where Z or its moments diverge: the complement of the exponential-family world

## Statement

A quantity x is distributed as a power law if its (tail) density is
P(x) ∝ x^−α for x ≥ x_min, equivalently the complementary CDF is
P(X ≥ x) ∝ x^−(α−1). Scale-free: rescaling x → bx leaves the functional form
unchanged (only a constant factor changes). No characteristic scale; the tail
dominates moments.

## Manifestations by domain

| Domain | Manifestation | Level | Quantitative signature | Ref |
|--------|---------------|:-----:|------------------------|-----|
| Linguistics | Word frequency (Zipf) | L2 | rank–frequency exponent ≈ 1 (α ≈ 2) | Zipf 1949 |
| Economics | Wealth/income tail (Pareto) | L2 | Pareto index ~1.5–2.5, varies by country/era | Pareto 1896 |
| Geophysics | Earthquake magnitudes (Gutenberg–Richter) | L3 | b-value ≈ 1 over many decades of energy | Gutenberg–Richter 1944 |
| Networks | Degree distribution of WWW/citations | L3 (BA model) | γ ≈ 2.1 (web in-links); ~3 for BA | Barabási–Albert 1999 |
| Urban | City-size distribution | L2 | Zipf's law for cities, exponent ≈ 1 | Gabaix 1999 |
| Neuroscience | Neuronal avalanche sizes | L3 (SOC) | size exponent ≈ −1.5 (mean-field branching) | Beggs–Plenz 2003 |

## Shared mechanism

There is **no single** mechanism; power laws are the fingerprint of *several*
distinct generative processes, each of which is itself cross-domain:

- **Preferential attachment** ("rich get richer") → scale-free networks, citations,
  city growth (Yule, Simon, Barabási–Albert). This family is genuinely L3 within
  itself: the *same* process is provably at work.
- **Self-organized criticality** → avalanches, earthquakes, neuronal cascades
  (Bak–Tang–Wiesenfeld). Also L3 within itself.
- **Multiplicative processes with a lower boundary / random stopping** → many
  economic size distributions.
- **Optimization / cost–benefit tradeoffs** → some Zipfian language accounts.

So "power law" as such is an **L2 formal identity** (same functional form), which
partitions into several **L3 mechanism-families**. Collapsing them into one law
is a common error.

## Quantitative signature

The exponent α and the range (number of decades) over which the law holds. Genuine
cases hold over ≥ 2–3 decades. The *value* of α is mechanism-specific (BA gives
γ = 3; SOC branching gives τ = 3/2), so agreement of α across domains is itself
evidence of a shared mechanism, not just a shared shape.

## Boundary conditions / where it breaks

- Finite-size cutoffs: real tails are truncated.
- Over 1–2 decades, **lognormal and stretched-exponential distributions mimic
  power laws**. Most published "power laws" do not survive a proper model
  comparison (Clauset–Shalizi–Newman 2009 re-examined 24 canonical datasets;
  many were better fit by alternatives).
- Zipf-for-cities is sensitive to how "city" is defined (administrative vs.
  functional boundaries).

## Evidence for

- Where the mechanism is independently known (BA growth, SOC sandpiles), the
  exponent is *predicted* from the mechanism and matches — a real predictive
  transfer.
- Gutenberg–Richter holds over an extraordinary dynamic range.

## Evidence against / competing explanations

- Publication bias toward straight-looking log-log plots.
- Many social/biological "power laws" are lognormal (Limpert et al. 2001).
- The label conflates mechanistically unrelated systems.

## Open questions

- For each claimed power law in the catalog, does it survive CSN model comparison?
  (→ [`questions/OPEN-QUESTIONS.md`](../questions/OPEN-QUESTIONS.md) Q1)
- Are neuronal-avalanche, sandpile, and market-crash exponents the *same*
  universality class, or three convergent mechanisms? (→ see
  [`criticality-phase-transitions.md`](./criticality-phase-transitions.md))

## References

- Zipf 1949 — *Human Behavior and the Principle of Least Effort*
- Barabási & Albert 1999 — Emergence of scaling in random networks
- Bak, Tang & Wiesenfeld 1987 — Self-organized criticality
- Clauset, Shalizi & Newman 2009 — Power-law distributions in empirical data
- Gabaix 1999 — Zipf's law for cities
