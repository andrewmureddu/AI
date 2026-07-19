# Duality & conjugate variables

> **One-line claim:** Pairs of complementary descriptions related by a transform
> (Fourier, Legendre, primal–dual) recur across physics, optimization, and signal
> processing, with a shared uncertainty/tradeoff structure.
> **Headline correspondence level:** L2–L3 (shared transform structure). *(seed)*
> **Status:** seed

## Statement

A duality relates two representations by an involutive transform, exchanging
"hard" and "easy" and pairing conjugate variables (position–momentum,
time–frequency, energy–temperature, primal–dual). Domain-neutral object: the
transform (Fourier/Legendre) and the uncertainty relation ΔxΔk ≥ const it imposes.

## Manifestations by domain (seed)

- Physics: position–momentum (Fourier); energy–time; wave–particle — L3.
- Thermodynamics: Legendre transforms between potentials (U, F, G, H) — L3.
- Optimization: primal–dual, Lagrangian duality; convex conjugate — L3 (same
  Legendre transform as thermodynamics).
- Signal processing: time–frequency, Gabor limit — L3.

## To develop

The Legendre transform genuinely links thermodynamics and convex optimization
(same math) — a clean L3 candidate. Fourier uncertainty links QM and signal
processing. Question: is there a single abstraction (convex conjugation / symplectic
structure) that subsumes these, and does it *predict* across domains? Refs:
Rockafellar 1970 (convex analysis); Arnold (symplectic geometry).
