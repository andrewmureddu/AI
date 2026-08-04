# 2026-07-28 — P-C: the two kinds are one decomposition, and there is a third readout

**Worked on:** [`FLOORS.md`](../invariants/FLOORS.md) P-C — the floor sort's last
unrun prediction — and [`optimization-variational.md`](../invariants/optimization-variational.md) (#7).
**Change:** new experiment
[`experiments/PC-variational-kinds/`](../experiments/PC-variational-kinds/); **P-C
is refuted in exactly the way it registered**; #7 seed → developing ✓tested, its
floor assignment moves from prediction to evidence *and changes shape*; the sort
has now been graded three times, and this is its first miss.

## What I did

Ran P-C, the prediction that variational principles come in exactly two kinds —
over a measure ⇒ floor 2, over an action ⇒ floor 1 — with its registered falsifier:
*a genuine variational law, one that predicts rather than re-describes, whose
functional is over neither.*

I did not run it as written. [P-D](./2026-07-27-PD-allometry.md) had already
produced a case the binary has no slot for, and its own "Next" asked that the
selector/source distinction be **registered from the start** rather than
discovered mid-run. So the claim under test was the repair: that the floor is a
property of the **readout** rather than of the functional (C1), that "measure" and
"action" are the two **poles of a decomposition** rather than two boxes (C2), and
that P-C's falsifier fires (C3).

## What I found

**8 of 9 at-risk predictions passed; 4 of 5 declared identities. The two failures
are the same failure and are mine.**

**The falsifier fires, and not narrowly.** Write the pseudo-gradient Jacobian at an
equilibrium as J = S + aA. A potential with its minimum there requires S ≻ 0;
convergence requires only Re λ(J) > 0. The region where the second holds and the
first fails — *no potential at all, and the dynamics still arrive* — is **12.2%**
of the ensemble at n = 6 against the **0.000** P-C requires, and at n = 8 **not one
draw in 8000 had a potential** while 5.9% converge. Above n = 4 the potential-free
region is essentially all of the convergent region.

**And the reason is a count, which is what makes it a result rather than a
counterexample.** At large a, each conjugate eigenvalue pair of A picks up a real
part equal to the average of S's quadratic form over A's invariant 2-plane. So
rotation does not evade the stability conditions, it **pairs them up**: *n*
conditions become **⌈n/2⌉**, and a pair survives when its two directions cancel.
Agreement between that criterion and measured convergence: **1.0000 / 0.9985 /
0.9985 / 0.9995** at n = 2, 4, 6, 8. At n = 2 the criterion collapses to tr S > 0,
predicting a stable fraction of exactly 0.500; measured **0.5084**. At n = 6 the
convergent fraction is **2440×** P(S ≻ 0).

**The escape routes are closed.** These are not weighted potential games either —
over 200 draws from the region, every one has min_D ‖DJ − (DJ)ᵀ‖/‖J‖ > 0.1, the
smallest residual **1.42**. And it is not linearity: a two-player game with
quadratic + quartic losses whose symmetric part is diag(+1.000, −0.500) at the
equilibrium converges from **100 of 100** starts, with pseudo-gradient circulation
**5.14** around a loop enclosing it. No potential, and it predicts.

**So C2 is what survives, and P-C's error was grammatical.** The antisymmetric part
is not a different *kind* of variational principle; it is the bracket content of
the same one. π = ‖S‖²/(‖S‖² + ‖A‖²) runs continuously between P-C's two kinds,
and floor 1 and floor 2 are its poles rather than its cells.

**Outside physics, C1 holds: one optimization, two readouts, two floors.** Choosing
among four real integer-multiplication schemes at N = 2¹⁴ under a six-parameter
cost model, three schemes win over the box (Toom-4 51.7%, Karatsuba 26.9%, Toom-3
21.4%) realizing three exponents. Inside a cell the exponent's Jacobian is
**exactly zero at 400 of 400 interior points** while the constant's is not.

**Floor 1's response type is measured, and it is what separates it from a
selector.** Both produce magnitude-blind integers. On planar central-force motion
the constant count jumps from 3 to 2 the instant V = −k/r gains a δ/r² term, while
the circular orbit's energy is **analytic through δ = 0** (one-sided derivatives
agreeing to **6.2e-6**) and the precession is **linear** in δ (measured
δ^**0.9760** against a registered 1.00 ± 0.03). Bertrand comes out at
**1.000000000** and **2.000000000**, invariant to **5.5e-10** across four decades
of coupling. Set against the selector's boundary — where the value stays continuous
and the *slope* kinks — the discriminator is the optimal value's regularity:

> **Discontinuous count + analytic value ⇒ floor 1. Discontinuous readout +
> kinked value ⇒ selector. Smooth ⇒ floor 2.**

**Both failures are one registration slip, and it is the most useful thing in the
run.** I put `n_base` — a recursion cutoff, i.e. a **structural count** — into my
own list of *magnitudes*. P8 registered rank 6 for the constant's Jacobian and
measured **4**, with the smallest singular value exactly 0.0; post-hoc, the two
missing directions are `n_base` (derivative identically **0.0**) and the collapse
of three per-word magnitudes into one linear functional per scheme. On the
identifiable coordinates the rank is **3 of 3, full at 60 of 60 points** — the
instrument was right and the registered number was unattainable in the cost model I
wrote. P11 failed for the same reason: split by what the swept parameter actually
is, the five **magnitude** crossings satisfy the registered claim *exactly* (value
continuous to 0.0, slope gaps 0.204–1.000) and the six `n_base` crossings do the
opposite (value jumps 8.3e-4 – 2.8e-2, slope gap exactly 0.0).

So one instrument separated three regularity classes without being told they were
different — and the class it found unplanted is **P-D's magnitude/count
distinction**, reappearing inside my own parameter list.

## Decisions

- **P-C is refuted, and this is the sort's first miss.** The sort has now been
  graded three times: [P-A](../experiments/PA-spectral-gap/) confirmed in a
  corrected form, [P-D](../experiments/PD-allometry-reduction/) confirmed on every
  leg, P-C **wrong as stated**. Kept as written in `FLOORS.md` with the resolution
  underneath, in the same style as the retired fourth floor — the reason it fails
  is the result.
- **#7 moves from `seed` to `developing` ✓tested, and its floor line changes.**
  Not "**2 + 1**, splits by what the functional is over" but "**2 ⇄ 1 continuously,
  by the potential fraction π; the readout's floor is separate and is one of
  three**."
- **The tower does not gain or lose a floor.** C3's region has no potential, but
  the antisymmetric part *is* floor 1's bracket, so the falsifier fires against
  P-C's grammar rather than against the architecture. Worth stating plainly,
  because "a predictive object with no Φ" sounds like falsifier #4 and is not one.
- **The three-way readout classification is registered as possibly N0.** Parametric
  programming's basis-change loci are the selector's cells and sensitivity analysis
  is the rank test. What is claimed is the tower placement.
- **Fourth registration slip of the same family, first in the opposite direction.**
  P-A's threshold, P-D's MST and mean-field control, D6's P2 were all *consequences
  of my construction called tests of it*. This one registered a number my
  construction **forbade**. Same root cause — not auditing the construction before
  registering numbers about it — so the rule in
  [`UNKNOWN-LAWS.md`](../questions/UNKNOWN-LAWS.md) §4 should be read as two-sided.

## Next

- **P-D's kink is now explainable but not explained.** The generic selector cell
  boundary has exactly its signature (jumping readout, continuous value, kinked
  slope), which makes "selector cell boundary" the leading account of
  θ = min(1, ln n/−ln β²γ) going non-analytic at nβ²γ = 1 with Murray's law on it.
  The settling measurement is concrete and was **not** run here: is nβ²γ = 1 where
  two branches exchange dominance, and does the cost functional's optimal value
  kink there? If yes, the kink is a floor-3 non-analyticity **of the optimal-value
  function** — the argmin of a Φ being itself a Φ with its own singular part.
- **A cleanly parameterized cost model** would make Leg C's rank test sharp instead
  of merely ordered. Cheap, and it is the honest repair for P8.
- **The base-variable derivation** flagged by [M3](./2026-07-25-M3-molloy-reed-rewiring.md)
  and [M11](./2026-07-25-M11-stochastic-resetting.md) is still unwritten and is now
  clearly the oldest live debt. P-C adds a third data point from a new side: P-D
  asked "is there a Φ at all?" and got no; here the answer is "there is *half* of
  one, and the other half is a bracket."
- **M8** (extreme value / best-of-n) is the L3 register's next item, deferred three
  times now.
