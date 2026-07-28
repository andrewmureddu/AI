# Optimization under constraints & variational principles

> **One-line claim:** Physical dynamics, evolution, rational choice, inference, and
> learning are all describable as extremizing some functional subject to constraints.
> **Headline correspondence level:** L1–L2, with a few L3 pockets; high risk of
> teleological over-reach. *(provisional)*
> **Status:** developing ✓tested
> **Floor:** **2 ⇄ 1, continuously** — *not* a split by what the functional is over. [P-C](../experiments/PC-variational-kinds/) refuted that: J = S + A at the equilibrium, symmetric part = free-energy content (floor 2), antisymmetric part = bracket content (floor 1), π = ‖S‖²/(‖S‖²+‖A‖²) between them. The *readout's* floor is a separate question with three answers ([FLOORS §4a](./FLOORS.md#4a-what-replaces-p-cs-binary--three-readouts-one-instrument)). "As-if" optimization is still neither — L1.

## What was measured ([P-C](../experiments/PC-variational-kinds/), 2026-07-28)

**A variational law can predict with no potential at all.** Requiring a potential
whose minimum sits at the equilibrium is *n* conditions (S ≻ 0); requiring the
dynamics to arrive there is weaker. The gap is **12.2%** of a natural ensemble at
n = 6 — and at n = 8, **not one draw in 8000 had a potential** while 5.9% converge.
Not weighted-potential games either (200/200, min residual 1.42), and not an
artifact of linearity (a quadratic-plus-quartic two-player game with symmetric part
diag(+1.000, −0.500) converges from 100/100 starts, circulation 5.14).

**The mechanism is a count, not a loophole.** At large rotation each conjugate
eigenvalue pair picks up the average of S's quadratic form over the corresponding
invariant 2-plane, so the *n* stability conditions **pair up into ⌈n/2⌉**.
Agreement with measured convergence: 1.0000 / 0.9985 / 0.9985 / 0.9995 at
n = 2, 4, 6, 8. At n = 2 it collapses to tr S > 0 — predicted stable fraction 0.500,
measured 0.5084.

**The floor belongs to the readout.** Choosing among four real
integer-multiplication schemes under a six-magnitude cost model, one optimization
emits a magnitude-blind exponent (Jacobian exactly 0 at 400/400 interior points,
jumping across cells) and a magnitude-sensitive constant, simultaneously. This is
[P-D](../experiments/PD-allometry-reduction/)'s selector case reproduced outside
biology and outside physics.

**Boundary conditions.** Leg B is linear-quadratic apart from one nonlinear
instance; the ⌈n/2⌉ mechanism is verified at large rotation and pinned exactly only
at n = 2; the cost model is a model, not a compiler. Nothing here covers
non-equilibrium variational principles (Onsager, MaxEnt production) — the tower is
derived for stationary fields. The three-way readout classification may be **N0**:
parametric programming's basis-change loci are the selector's cells and sensitivity
analysis is the rank test.

## Statement

A variational principle says the realized state extremizes a functional
(least action, maximum entropy, maximum fitness, maximum utility, minimum loss,
minimum free energy). Domain-neutral object: argmax/argmin of an objective on a
constraint set; Euler–Lagrange / KKT conditions as the shared machinery.

## Manifestations by domain (seed)

- Physics: least action (Hamilton's principle) — anchor, exact.
- Evolution: fitness maximization — L1/L2 (adaptationism is contested; drift,
  constraints, no global optimizer).
- Economics: utility maximization — L2 formal, empirically leaky (bounded
  rationality).
- ML: empirical risk / loss minimization by gradient descent — L2/L3.
- Neuroscience: free-energy principle (Friston) — contested L1–L2.

## To develop

The central caution: "everything optimizes something" is nearly unfalsifiable
unless the objective is *specified in advance* and the extremum is *achieved*, not
just approached. Separate genuine variational laws (physics) from as-if
descriptions (evolution/economics). Cross-link `entropy-information.md` (MaxEnt).

P-C sharpens the caution rather than removing it, and in an unexpected direction:
the escape from "everything optimizes something" is *not* to demand a potential,
because the potential-free region is where most predictive equilibria actually
live. The demand that survives is that the **readout** be identified and its
response type measured — smooth, null, or jumping — before any floor is claimed.
