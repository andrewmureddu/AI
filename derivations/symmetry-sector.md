# The symmetry sector — does it reduce to Φ, or is it the second primitive?

**Question (from [S25's verdict](./S25-control-split.md) and
[essay 4's closing note](../essays/04-the-periphery-split.md)):** after the
connectivity sector collapsed into Φ's singular structure, invariance/symmetry
(Noether, symmetry-breaking) is the last candidate for a genuine second axis of
the map. Same discipline as S25: attack the reduction as hard as possible.
**Method:** pure derivation, two reduction attempts plus a cross-check on the
existing stone [S9](../questions/SPECULATIVE.md) (Noether for learning).

## Verdict up front

**Monism fails — but so does "second sector beside Φ." The sector splits, and
the half that survives reduction sits *underneath* Φ, not next to it.**

1. **Symmetry-*breaking* reduces** — completely, and to the same place
   connectivity went: Φ's singular structure. SSB requires a non-analyticity of
   Φ, and Goldstone modes are null directions of ∇²(free energy) (§1). Essay 4's
   guess that Goldstone phenomena are the invariance sector's "boundary
   signature" was almost right; they are the *same* boundary, not an analogue.
2. **Noether proper does not reduce** — but not because it is disjoint from Φ.
   Conservation laws turn out to determine Φ's **argument list**: the conserved
   charges are exactly the quantities that can (and, at long times, the only
   ones that do) appear as natural parameters of the ensemble (§2). Symmetry is
   not a derivative of Φ, nor a singularity of Φ. It is **prior** to Φ — it
   fixes the coordinate system of the prediction field.
3. So the map's architecture is not sectors side by side but a **tower**:

```
   symmetry / conservation      →  chooses Φ's coordinates (which quantities exist)
   Φ, regular part              →  prediction (moments, Fisher, updates — the hub)
   Φ, singular part             →  boundaries (transitions, power laws,
                                    reachability, percolation — and SSB itself)
```

One column, three floors. The "second primitive" exists, but it is a *base
layer*, not a parallel sector — the direction of explanation between symmetry
and prediction runs bottom-up, which is why every attempt to express Noether
*inside* Φ-machinery kept failing while the converse kept succeeding.

---

## 1. First reduction attempt: symmetry-breaking (succeeds)

Take SSB in its standard form: dynamics symmetric under G, realized state
invariant only under H ⊂ G. Two classical facts do all the work:

**SSB lives at Φ's non-analyticities.** At finite N the Gibbs measure inherits
the full symmetry of H — the magnetization of a finite Ising system is exactly
zero at every temperature. Spontaneous breaking exists only in the
thermodynamic limit, exactly where Φ acquires a non-analyticity (Lee–Yang
zeros pinching the real axis — already the L4 core of the criticality entry).
No singularity of Φ, no SSB. The phenomenon is *constituted* by Φ's boundary,
not merely correlated with it.

**Goldstone modes are null directions of ∇²Φ.** In the broken phase, the
effective potential (the Legendre transform of Φ — the rate-function face
again) is flat along the orbit G/H of degenerate ground states. Flat direction
= zero eigenvalue of the Hessian of the free energy = a null direction of the
same object whose null spaces encoded unreachability (S25 §4) and whose
divergences encoded susceptibility blow-up (S3). One signature class, third
independent arrival.

So symmetry-*breaking* files under the boundary layer, alongside power laws,
percolation, and binary reachability. The
[`symmetry-breaking.md`](../invariants/symmetry-breaking.md) entry's "tightly
linked to criticality" was the reduction, stated as a cross-reference.

## 2. Second reduction attempt: Noether proper (fails — and inverts)

Now the hard half. Try to write "continuous symmetry ⇒ conserved current" as a
fact about Φ.

**The structural obstruction.** Noether's theorem consumes a *variational/
symplectic* structure: an action, a Lagrangian, a Poisson bracket. Every
Φ-object in the hub — moments, Fisher metric, rate functions, updates —
consumes a *measure*. A measure supports expectations; it has no bracket. You
can average a conserved quantity, but nothing in {Φ, ∇Φ, ∇²Φ, Φ*} *generates*
the pairing symmetry ↔ charge, because the pairing lives in the dynamics'
algebraic structure, which the Gibbs measure has already integrated out. Three
attempts to route around this (symmetrize the measure; read charges off the
rate function; use the update (★) as the dynamics) all presuppose the charge
rather than produce it. Reduction fails.

**But the converse succeeds — conservation determines Φ's coordinates.** Ask
the opposite question: what role do conserved charges play *in* Φ-machinery?
Answer, and it is exact:

- A quantity Q can parameterize an equilibrium ensemble — appear in the
  exponent as e^{−βH−μQ} with a chemical potential μ — iff it is conserved.
  A non-conserved Q in the exponent defines a measure the dynamics
  immediately leaves; the family is not invariant, the "parameter" is not one.
- At long times this becomes exhaustive: thermalizing systems relax to
  ensembles parameterized by *nothing but* their conserved charges (energy,
  particle number, momentum — the Gibbs ensemble's whole argument list), and
  integrable systems, with extensively many charges, relax to the
  **generalized Gibbs ensemble** built on exactly those charges. What
  survives into the stationary prediction field = what is conserved. Jaynes
  read in reverse: max-ent needs constraints, and the constraints that
  *persist* are the Noether charges.

So the relationship between the symmetry sector and the hub is not reduction
but **constitution**: Noether decides *which exponential family the system
ends up in* — the dimension and identity of Φ's natural parameters. The
sufficient statistics of the long-time prediction field are the conserved
charges. In prediction-field language: symmetry determines what there is to
predict *with*; Φ then does all predicting; Φ's breakdown marks where
prediction ends. The floors of the tower, derived rather than drawn.

**A pleasing echo at (★)'s boundary.** S1's sharp boundary was that the
universal update cycles forever under game coupling — and that cycling is
Hamiltonian: zero-sum replicator dynamics conserves a KL-divergence to the
equilibrium (the Poincaré recurrence the derivation invoked *is* this
conservation). Where the hub's own dynamics stopped being a descent and
started conserving, the symmetry sector was already standing there. The base
layer shows through exactly at the prediction layer's edges — consistent with,
though not proof of, the tower.

## 3. Cross-check: S9, the Noether theorem for learning

The tower makes S9 decidable in passing. Symmetries of a loss do induce
conserved quantities under gradient flow — scale symmetry of ReLU layers
conserves the balancedness ‖W_{l}‖² − ‖W_{l+1}‖², translation symmetry of
softmax conserves parameter sums (Kunin et al. 2021, "Neural Mechanics," which
also shows discretization and weight decay break the laws in predictable
ways). Is it "the same theorem" as physics' Noether? Per the methodology's
convergence rule: the *pairing* (continuous symmetry ↔ conserved quantity) is
shared, but the *mechanism* differs — Hamiltonian conservation flows from the
bracket's antisymmetry; gradient-flow conservation flows from the symmetry
generator staying orthogonal to ∇L. Both are momentum-map constructions over
different geometric structures (symplectic form vs. metric), so the honest tag
is **L2 with a live L3 route** (exhibit the momentum map as the shared
generative object across both structures — a real derivation, not done here).
S9 sharpened, not settled.

The tower adds a prediction S9 didn't make: the Kunin invariants should be the
**natural parameters of SGD's stationary distribution** — training noise
should thermalize the network onto an ensemble parameterized by its conserved
balancednesses, the ML instance of "long-time prediction fields are
coordinatized by charges." That is an experiment (train to stationarity,
test sufficiency of the invariants for the stationary law), and it is the
tower's most falsifiable consequence outside physics.

## 4. Falsifiers for the tower

1. **A parameter without a charge.** A natural parameter of a genuine
   long-time equilibrium ensemble whose conjugate quantity is *not* conserved
   (and not a bookkeeping constraint per the Noether entry's own split).
   Kills the constitution claim.
2. **A charge that cannot parameterize.** A conserved quantity that provably
   cannot appear as an ensemble parameter. Kills exhaustiveness from the
   other side.
3. **The SGD test of §3 failing** — stationary SGD law not sufficient-
   statisticked by the conserved invariants. Kills the tower's reach beyond
   physics (leaving it a thermodynamics fact, not a map fact).
4. **A fourth floor.** An invariant in the catalog reducible to neither
   symmetry, Φ-regular, nor Φ-singular structure. The periphery audit says
   the current candidates are exhausted, but the catalog is open.

## 5. Boundaries of this derivation

- GGE exhaustiveness is exact for integrable systems and standard-but-
  heuristic (eigenstate thermalization) for generic ones; "only charges
  survive" is extremely well supported, not theorem-grade, away from
  integrability.
- Everything here is equilibrium / long-time. Driven, non-stationary systems
  can hold non-conserved quantities in their description indefinitely; the
  tower's base-layer claim is about *stationary* prediction fields.
- The L3 route for S9 (momentum maps over symplectic vs. metric structure)
  is asserted plausible, not derived.
- Quantum subtleties (non-commuting charges, non-abelian GGE) untouched.

**Bookkeeping:** the "is the map monist?" question is answered *no, but it is
one tower*: promote the constitution claim to a stone (S26) with falsifiers
1–3; ⟳ notes to essay 4 and S9; the synthesis's through-line ("one object
seen sideways") now needs a revision pass — the honest slogan is closer to
**"one object, three floors: chosen by symmetry, read by prediction, ended by
breakdown."**
