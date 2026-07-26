# Diffusion & random walks

> **One-line claim:** A vast range of spreading/aggregation phenomena are governed
> by the same object — the diffusion equation / the sum of many small independent
> increments — because of the Central Limit Theorem.
> **Headline correspondence level:** L3–L4. The CLT is a theorem (L4) that *forces*
> the shared Gaussian/diffusive behavior on an entire class of systems.
> **Status:** developing
> **Floor:** **2** (Φ-regular), → 3 in the tails — CLT forces the max-entropy Gaussian; JKO makes diffusion its gradient flow. Lévy/anomalous instances move to floor 3 ([P-B](./FLOORS.md))

## Statement

A random walk is a sum of i.i.d. (or weakly dependent) increments; its scaling
limit is Brownian motion, whose density obeys the diffusion (heat) equation
∂u/∂t = D ∇²u. The domain-neutral object is **the diffusion operator / the
Gaussian propagator**, and the reason it is universal is the **Central Limit
Theorem**: sums of many small independent contributions converge to a Gaussian
regardless of the microscopic details.

## Manifestations by domain

| Domain | Manifestation | Level | Quantitative signature | Ref |
|--------|---------------|:-----:|------------------------|-----|
| Physics | Brownian motion; heat conduction | anchor | ⟨x²⟩ = 2Dt (MSD linear in time) | Einstein 1905 |
| Finance | Black–Scholes; log-price as Brownian motion | L3 | Same PDE (after change of vars); √t vol scaling | Black–Scholes 1973 |
| Biology | Bacterial chemotaxis; morphogen gradients | L3 | Reaction–diffusion; Turing patterns | Turing 1952 |
| Epidemiology | Spatial spread of epidemics | L3 | Fisher–KPP traveling waves | Fisher 1937 |
| CS / networks | PageRank as a random walk's stationary dist. | L3 | Same Markov generator | Page–Brin 1998 |
| Ecology | Animal dispersal | L2/L3 | MSD; sometimes anomalous (Lévy) | — |

## Shared mechanism

**Yes, and it is provable.** The unifying mechanism is *aggregation of many small
independent random increments*, and the CLT guarantees the Gaussian/diffusive
limit for the whole class. This is the cleanest L4 case in the catalog after
Noether: the correspondence is not "these look similar" but "a theorem says they
must coincide in the scaling limit." The diffusion equation is simply the
Fokker–Planck equation of that limit.

Where increments are *not* finite-variance or *not* independent, the universality
class changes — and it changes *predictably*:

- Heavy-tailed increments → **Lévy flights**, superdiffusion, ⟨x²⟩ ∝ t^(2/α).
- Long-range correlations → **fractional Brownian motion**, ⟨x²⟩ ∝ t^(2H).

That the deviations are themselves classified (by generalized CLTs / stable laws)
is *stronger* evidence of a real invariant, not weaker.

## Quantitative signature

The mean-squared-displacement exponent: ⟨x²⟩ ∝ t^β with β = 1 for normal
diffusion. β ≠ 1 flags anomalous diffusion and a different universality class.
The √t scaling of a diffusive front is the portable prediction.

## Boundary conditions / where it breaks

- Ballistic/inertial regimes at short times (before many collisions).
- Anomalous diffusion (Lévy, subdiffusion in crowded media) — different exponent.
- Finance: real returns have heavy tails and volatility clustering, so pure
  Brownian motion (β = 1, Gaussian) is a first approximation, not the truth —
  a documented, quantified breakdown.

## Evidence for

- Einstein's 1905 prediction ⟨x²⟩ = 2Dt was confirmed by Perrin and *measured
  Avogadro's number* — a spectacular predictive transfer from a random-walk model.
- The same PDE, discovered independently in heat, finance, and biology, is
  literally the same operator.

## Evidence against / competing explanations

- Anomalous-diffusion cases show the *naive* invariant fails; the honest claim is
  about the CLT-governed class, not "everything diffuses."

## Open questions

- Catalog which domain instances are truly finite-variance/independent (β = 1)
  vs. anomalous, and whether the anomaly exponents themselves recur across domains.
- Is rough-volatility finance (H ≈ 0.1 fBm) an instance of a cross-domain
  fractional-diffusion class? (cross-link
  [`self-similarity-fractals.md`](./self-similarity-fractals.md))

## References

- Einstein 1905 — On the movement of small particles…
- Turing 1952 — The chemical basis of morphogenesis
- Black & Scholes 1973 — The pricing of options
- Gnedenko & Kolmogorov 1954 — Limit distributions for sums of independent random variables
