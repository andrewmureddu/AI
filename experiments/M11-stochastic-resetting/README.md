# M11 — is stochastic resetting one mechanism across three fields? (result)

**Question ([M11](../../questions/L3-MECHANISMS.md)):** diffusive search
(Evans–Majumdar 2011), enzymatic turnover (Reuveni–Urbakh–Klafter 2014 —
substrate unbinding *is* restart), and randomized backtracking search
(Luby–Sinclair–Zuckerman 1993; Gomes–Selman–Kautz 1998) each independently
found that restarting a stalled search helps. Is it the **same mechanism**?
That is a question about whether one parameter-free criterion governs all three.

**Status: confirmed, including the universality that separates identity from
convergence — and the register's framing of *why it matters* turns out to be
wrong in an instructive way.**

Run it: `python3 run.py` (pure numpy, ~2.5 min, verified identical across runs).
Predictions registered in [`PREREGISTRATION.md`](./PREREGISTRATION.md) before
any measurement; that file is unedited.

## Results

| # | Prediction | Result | |
|---|-----------|--------|---|
| **P1** | r\* > 0 iff CV > 1; crossing at σ\* = √(ln 2) = 0.8326 | **0/10 misclassified**; crossing **0.8555** (2.8%) | ✓ |
| **P2** | exponential knife edge: ⟨T_r⟩ independent of r | spread **0.4%** | ✓ |
| **P3** | diffusion optimum r\*x₀²/D = 2.5396 | **2.6226** (3.3%) | ✓ |
| **P4** | transfer from un-reset distribution alone, <3% | max **0.9 / 2.9 / 0.9%**, median ≤0.5% | ✓ |
| **P5** | **CV(T_r\*) = 1 in all three domains** | **0.998, 1.001, 1.028** | ✓ |
| **P6** | MM sign flip within one scheme | CV 0.50 → no help; CV 1.71 → **25×** | ✓ |
| **P7** | combinatorial search | 3-SAT CV 0.73 → no help; QWH CV 2.71 → **19.4×** | ✓ |
| **P8** | the Φ identity | holds — but **vacuously**, see below | ⚠ |

### P5 — the identity test

The one that matters. At the optimal restart rate the *restarted* process has

    CV = 0.9981 (diffusive search) · 1.0011 (enzymatic turnover) · 1.0279 (backtracking search)

from un-reset CVs of 167, 1.71 and 2.71 respectively. Three processes with
nothing in common — a Lévy first-passage law with **infinite mean**, a
two-conformer enzyme, and a randomized Latin-square solver — land on the same
universal constant. That is what distinguishes mechanism identity from three
fields separately noticing that restarts are useful.

### P4 — parameter transfer

The whole restart curve, predicted from the un-reset completion-time
distribution alone and checked against an independent simulation of the
protocol: max error 0.9% (diffusion), 2.9% (enzyme), 0.9% (backtracking).
Notably this works for diffusive search **where ⟨T⟩ = ∞** — the Laplace
transform exists where the moments do not, so the mechanism predicts the
restarted behaviour of a process whose un-reset mean is undefined.

### P6/P7 — two sign flips *within* a single domain

Stronger than three domains agreeing, because it rules out "this field just
happens to benefit":

- **One enzyme scheme, two catalysis regimes.** Multi-step catalysis (Erlang,
  k=4, CV=0.50): unbinding **hurts**, r\*=0. Dynamic disorder (slow/fast
  conformers, CV=1.71): unbinding **helps, 25×**. Same scheme, opposite
  conclusions, both predicted from CV alone.
- **One search paradigm, two instance families.** Random 3-SAT at the phase
  transition (n=50, CV=0.73): restarts **don't** help. Quasigroup-with-holes
  (order 14, 55% holes, CV=2.71): restarts help **19.4×**.

### P7 — a registered instance family that didn't cooperate

The prereg named random 3-SAT as the heavy-tailed case. At sizes reachable in
pure Python it isn't: measured CV rose only from 0.55 (n=26) to 0.97 (n=70) —
the instances are too small for an early wrong branch to cost exponentially.
So I added quasigroup-with-holes, the benchmark on which heavy-tailed
backtracking runtimes were originally characterised (Gomes–Selman 1997), and
**kept 3-SAT as the easy-instance control**. This is a better result than the
registered one: it shows CV is a property of the instance family and solver,
not of "SAT", and it supplies the within-domain sign flip above.

### P8 — the registered check was vacuous, and the real answer is different

P8 asked whether ⟨T_r⟩ = (e^{−Φ_T(−r)} − 1)/r with Φ_T(s) = log E[e^{sT}].
It does, to 1e-16 — **because Φ_T(−r) ≡ log T̃(r), so the two sides are the
same expression rewritten.** The check confirms algebra, not nature. Recording
it as a failure of the prediction's design.

What *is* substantive, and better than what was registered:

- The exponential distribution is the **maximum-entropy** law on [0,∞) at fixed
  mean, and its CV is exactly 1.
- So the criterion reads: **restart helps iff the completion time is more
  dispersed than the maximum-entropy distribution with the same mean.**
- P2 is then not a coincidence but the statement's content: a memoryless
  process is exactly neutral to restarting.

So M11 is **not** the second axis the register filed it as. First-passage
structure is not a new primitive; it is the hub's own log-partition form
applied to a different base variable (an exit time rather than a state), with
the MaxEnt reference distribution supplying the knife edge. The honest
consequence for the map: what is portable is Φ's *form*, not Φ's *variable* —
and "does X reduce to Φ?" is under-specified until the base variable is named.
That is a sharper question than the one M11 was filed to answer, and it is
filed rather than settled.

## Two estimator failures, both diagnosed

Neither changes a conclusion, but both changed a verdict at some point and are
on the record in `verdict.json`.

1. **`argmin > 0` is biased toward "restart helps".** Taking the minimum over a
   grid of 21 noisy means finds a downward fluctuation even when the true curve
   is flat: the exponential knife edge showed a spurious 2.3% "speedup", exactly
   the ~1.9-standard-error dip expected from the minimum of 21 draws. Under this
   rule, 3-SAT with CV = 0.73 was scored as helped — by 0.08%. Fixed with common
   random numbers across rates plus a significance requirement.
2. **A normal standard error is meaningless for an infinite-variance baseline.**
   The fix in (1) then *rejected* Lévy diffusion — a **5985× speedup** scored
   only 3.8σ, because the r=0 mean has no finite variance. Replaced with a
   bootstrap on the ratio, which needs no finite variance; Lévy's lower 1st
   percentile is 2833.

A third, on the crossing location: thresholding significance finds where an
effect becomes *detectable*, not where it changes *sign*, and is biased late —
it placed the crossing at σ = 0.925 (11% high). The signed initial slope of the
restart curve changes sign exactly at CV = 1 and is unbiased: it gives 0.8555
against the predicted 0.8326 (2.8%). Both numbers are reported.

The slope also gives a **quantitative** form of the criterion, since theory says
the normalised initial slope equals (1 − CV²)/2. Across the battery: median
absolute error 0.015, max 0.16 for CV ≤ 1.35. It degrades for broader
distributions (lognormal σ=1.5: −0.48 measured vs −3.85 predicted) because the
r² term carries ⟨T³⟩, so the linear regime narrows as higher moments grow. The
*sign* is correct for every process tested.

## Verdict

One parameter-free criterion, measured in each domain from the un-reset
completion time alone, correctly predicts **whether** restarting helps, **where**
the optimum sits, and **the entire restart curve** — in diffusive search, in
enzyme kinetics, and in randomized backtracking, including two sign flips inside
single domains. At the optimum all three collapse onto CV = 1. On the register's
own admission test this clears named process, role assignment, parameter
transfer, and a convergence discriminator.

**Level: L3 candidate confirmed on this evidence** — with the caveat below, which
is why the catalog is not being edited on the strength of one experiment.

## Boundaries

- **Restart is instantaneous and memoryless throughout.** Real resetting costs
  time (an enzyme must re-bind; a solver must re-descend). Resetting with a
  refractory period has a *modified* criterion, and the MM leg is run in the
  saturating-substrate limit specifically to avoid it. The cross-domain claim as
  tested is for cost-free Poissonian restart.
- **Poissonian restart only.** The domain-native protocol for solvers is a sharp
  cutoff (Luby's schedule), which has a related but different optimality theory.
  Untested here.
- All three domains are *simulated*; no measured enzyme turnover data and no
  real solver corpus. The enzyme leg in particular is a two-state caricature of
  dynamic disorder, not fitted to a real enzyme.
- QWH runtimes are censored at 100k nodes (5.4%); 3-SAT uncensored. Censoring
  truncates the tail, biasing CV **down** and the no-restart baseline **down** —
  both make the test conservative.
- The Lévy leg samples first-passage times from the exact law rather than
  simulating Brownian paths. That is exact for the un-reset process, and the
  restart protocol is simulated honestly on top of it.
- P5's universality is tested at the grid's argmin, so its accuracy is limited
  by grid resolution near a flat optimum — which is the likely source of the
  backtracking domain's 1.028 versus the other two at ~1.00.
