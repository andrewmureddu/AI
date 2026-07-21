# Optimization under constraints & variational principles

> **One-line claim:** Physical dynamics, evolution, rational choice, inference, and
> learning are all describable as extremizing some functional subject to constraints.
> **Headline correspondence level:** L1–L2, with a few L3 pockets; high risk of
> teleological over-reach. *(provisional — seed)*
> **Status:** seed

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
