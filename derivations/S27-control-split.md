# S27 — does control split into a Φ-half and a reachability half?

**Question ([S27](../questions/SPECULATIVE.md)):** the periphery-split conjecture
([essay 4](../essays/04-the-periphery-split.md)) predicts feedback/control is two
invariants fused: an inference half that reduces to Φ = ln Z, and a reachability
half (Kalman rank, Gramians) that no Φ-derivation can recover *with predictive
work*. **Method:** pure derivation. Per the stone's own instruction, the honest
move is to attack the "irreducible" half as hard as possible.

## Verdict up front

**The split as stated is dead — the falsifier fired — but it fired in a way that
promotes the conjecture instead of burying it.** Results:

1. Half (a) confirmed and easy: optimal control under noise *is* Φ-machinery,
   exactly, in three independent formalisms (§1).
2. Half (b) — the supposed irreducible remainder — **reduces**: the
   controllability Gramian is a covariance, i.e. **∇²Φ of a noise-driven
   ensemble**, and the minimum control energy to reach a state is **exactly the
   large-deviations rate function** — the Legendre dual of Φ (§2–3). This does
   predictive work: loss of controllability is *predicted* by a divergence of the
   rate function. That is precisely what S27 said could not happen.
3. But the reduction lands entirely in Φ's **singular structure** — supports,
   degeneracies, divergences of the dual — never in Φ's regular part (finite
   moments and response coefficients). Binary reachability ("can this state be
   reached at all?") is the statement that the rate function is infinite there:
   a fact about *where Φ's description breaks*, not about its derivatives (§4).

So the corrected claim, replacing S27: **the connectivity sector is not disjoint
from Φ — it is Φ's boundary face.** Prediction-facts are Φ-regular; connectivity-
facts are Φ-singular. This is the same relationship the synthesis already
conjectured for power laws ("heavy tails live where Φ misbehaves"), now derived
rather than observed in one more case — and it makes the Potts q→1 story for
percolation look systematic instead of coincidental (§5).

---

## 1. Half (a): control-as-inference is exact Φ-machinery (confirmed, L3)

Three independent routes, each an identity, not an analogy.

**KL-control / linearly-solvable MDPs (Todorov).** For dynamics perturbable at a
KL price, define desirability z(x) = e^{−V(x)}. The Bellman equation *linearizes*:
z = e^{−q} · P z, and unrolling gives

```
   V(x)  =  − ln  E_paths from x [ exp( − total cost ) ] .
```

The optimal cost-to-go is the negative log of a partition function over
trajectories. The value function **is** a free energy — same object, same sign
conventions, path measure instead of Gibbs measure.

**Maximum-entropy RL.** The soft value V(x) = (1/β) ln Σ_a e^{βQ(x,a)} is the
log-partition of Q at inverse temperature β; the optimal policy is its Gibbs
distribution — the same softmax-free-energy pair as S23's attention result, one
field over.

**LQG ↔ Kalman duality.** The Kalman filter is exact Bayesian inference in a
linear-Gaussian (exponential-family) model: posterior mean = ∇Φ, posterior
covariance = ∇²Φ. The filter Riccati equation maps to the LQR Riccati under
(A, B, Q, R) ↔ (Aᵀ, Cᵀ, W, V). So the control Riccati is the image of a
Φ-derivative flow under a transpose. Estimation-side Φ-structure transports to
the control side wholesale.

Level: **L3 within the linearly-solvable / LQG / maxent-RL classes** — one
mechanism (trajectory-measure free energy), three derivations. Boundary: general
nonlinear control with hard constraints is not known to linearize this way;
the identity is exact for these classes and only variational beyond them.

## 2. Attacking half (b): the Gramian is a covariance

Now the half S27 declared irreducible. The finite-horizon controllability
Gramian of ẋ = Ax + Bu is

```
   W_T  =  ∫₀ᵀ e^{At} B Bᵀ e^{Aᵀt} dt .
```

Standard facts: the pair (A,B) is controllable iff W_T ≻ 0, and the minimum
control energy ∫‖u‖²dt steering 0 → x̄ in time T is

```
   E_min(x̄)  =  x̄ᵀ W_T^{−1} x̄ .                                  (†)
```

Rank conditions, "which states can be steered" — this is the reachability face,
allegedly distribution-free.

But replace the *controls* by white noise: ẋ = Ax + Bw, w white. The state is
then Gaussian with covariance

```
   Σ_T  =  ∫₀ᵀ e^{At} B Bᵀ e^{Aᵀt} dt   =   W_T .
```

**The controllability Gramian is identically the covariance of the noise-driven
ensemble.** And covariance is ∇²Φ — the Fisher/susceptibility face of the
log-partition function of that Gaussian path measure, the exact object S3 tested.
The "distribution-free" wiring fact was a second moment all along; control
inputs and noise inputs enter through the same B, so what noise *can spread
into* and what control *can steer into* are the same subspace, with the same
metric.

The dual holds too: the observability Gramian is the Fisher information the
output path carries about the initial state; unobservable directions are
directions of **singular Fisher information** — ∇²Φ degenerating on the
estimation side.

## 3. Minimum control energy = the large-deviations rate function (exact)

Push the identification to its sharpest form. For the noise-driven system, the
Gaussian measure over final states has large-deviations rate (equivalently, the
small-noise Freidlin–Wentzell action)

```
   I_T(x̄)  =  ½ x̄ᵀ Σ_T^{−1} x̄  =  ½ E_min(x̄)          by (†), Σ_T = W_T.
```

Read it out loud: **the control energy needed to reach a state equals (twice)
the improbability of the noise wandering there on its own.** Hard-to-reach =
unlikely-under-noise, with the exact same quadratic form. And the rate function
is the Legendre transform of the scaled cumulant generating function — the
Legendre dual of Φ, the entropy face of the hub (invariants #3/#15). Freidlin–
Wentzell extends the identity beyond the linear case in the small-noise limit:
minimum action to reach x̄ = − lim ε ln P(reach x̄), generally.

This *does predictive work*, which is what the falsifier demanded: as a system
parameter drifts, an eigenvalue of W_T → 0 predicts, quantitatively and in
advance, the divergence of control energy along that mode — loss of
controllability forecast from a covariance spectrum. (Engineering already
exploits exactly this identity without the framing: balanced truncation ranks
modes by Gramian eigenvalues — i.e., prunes state directions by their
noise-ensemble variance.) **S27's side-one falsifier has fired.**

## 4. What survives: the reduction never leaves Φ's singular set

Before closing the case, notice *where* every (b)-fact landed:

| Reachability fact | Φ-object it reduced to | Regular or singular? |
|---|---|---|
| How hard to reach x̄ (energy) | Legendre-dual rate function I(x̄) | regular (finite I) |
| Hard directions / model reduction | small eigenvalues of ∇²Φ | approaching singular |
| **Whether x̄ is reachable at all** | **I(x̄) = ∞**; W singular; support ⊊ ℝⁿ | **singular** |
| Unobservable subspace | null space of Fisher ∇²Φ | singular |

The *quantitative* face of reachability reduces to Φ's regular machinery. The
*binary* face — rank conditions, "can at all" — reduces only to statements that
the machinery **degenerates**: the ensemble is supported on a proper subspace,
the density does not exist there, the rate function is infinite, ∇²Φ has a null
space. These are facts about the boundary of Φ's description, exactly as
essay 4 §4 characterized power laws ("what the prediction question returns when
asked past Φ's radius of convergence"). This is also the same mathematical
reflex as the essay-3 probe's zero-preservation lemma: exponential-family /
multiplicative machinery is expressive *on* a support and mute *about* the
support. Support structure is where this whole family of tools ends.

So the refined statement, replacing S27's "the two classes do not mix":

> **Connectivity facts are Φ-boundary facts.** They reduce to the hub — but
> only ever to its singular structure (supports, null spaces, divergences of
> the dual), never to its regular part. Prediction-invariants live in Φ's
> derivatives; connectivity-invariants live in Φ's degeneracies.

## 5. Cross-check and consequence for the periphery split

**Percolation, revisited.** Essay 4's falsifier #1 dismissed the Potts
random-cluster correspondence (percolation as a q→1 partition-function limit)
as "dressing." Under the refined claim it stops being dressing: the percolation
transition sits at a **non-analyticity** of that partition function — a
Φ-singular fact, in exact parallel with rank conditions as Φ-degeneracies. Two
independent connectivity invariants now reduce to Φ's singular set by different
routes. The pattern is load-bearing, not coincidental. (Prediction: the
spectral gap should follow — λ₂ of a Markov operator governs the approach to
the stationary Gibbs measure, and gap-closing is precisely the onset of a
Φ-degeneracy, critical slowing down seen from the connectivity side. Not
derived here; queued.)

**For the map.** The periphery split's *taxonomy* survives — prediction,
connectivity, and invariance questions remain distinct — but its *geometry*
changes: connectivity is not a separate sector beside Φ. It is Φ's boundary.
The picture is now two-layered rather than three-sectored: one object with a
regular part (the hub-core) and a singular part (power laws, percolation,
reachability, gap-closing), plus a genuinely separate symmetry/invariance
sector (Noether, symmetry-breaking) that this derivation did not touch and
which is now the *only* remaining candidate for a second primitive. The
sharpest open question the map has: **does the invariance sector also reduce
to Φ-structure (making the map monist after all), or is symmetry the one true
second axis?** Note the standing hint that it may not be safe even there:
Lee–Yang zeros (Φ-singularities) and symmetry-breaking are already entangled
in the criticality entry.

## 6. Boundaries of this derivation

- Exactness is linear-Gaussian; beyond it, Freidlin–Wentzell gives the
  small-noise limit only. Large-noise nonlinear reachability vs. rate
  functions: open.
- Control with hard input constraints (‖u‖ ≤ u_max) breaks the quadratic
  energy⇄variance identity; reachable sets stop being ellipsoids. The
  reduction's fate there is untested.
- Delays and nonlinearity — the feedback entry's own stated boundary — are
  untouched.
- The *stability* face of feedback (loop gain, phase margin, the entry's
  original content) was not addressed at all; this derivation covered the
  optimal-control and reachability faces. The entry needs a third column.

**Bookkeeping:** S27 retired as stated (falsifier fired), replaced by the
Φ-boundary claim above; essay 4 §5–6 need a restraint note (the "three
sectors over three quotients" picture becomes "regular/singular Φ + symmetry");
[`feedback-control.md`](../invariants/feedback-control.md) can be promoted from
seed with the control-as-inference and Gramian-covariance identities as its
first exact content.
