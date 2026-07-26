# 2026-07-25 — Restraint: resetting is one mechanism, and it is Φ on a different variable

**Worked on:** [M11](../questions/L3-MECHANISMS.md) (stochastic resetting), the
register's #2 pick and its only candidate for a non-symmetry second axis.
**Change:** new experiment
[`experiments/M11-stochastic-resetting/`](../experiments/M11-stochastic-resetting/);
M11 gains a ⟳ note; essay 04 gains a third restraint pass. No catalog level
changed — see *Decisions*.

## What I did

Tested whether one parameter-free criterion — restart helps iff CV = σ_T/⟨T⟩ > 1,
and CV(T_r\*) = 1 at the optimum — governs diffusive search, enzymatic turnover
and randomized backtracking. Predictions registered before measuring.

## What I found

**The identity test passed.** At the optimal rate the restarted process has
CV = 0.998, 1.001, 1.028 across the three domains, from un-reset CVs of 167,
1.71 and 2.71. One of those processes has an **infinite** mean. Three unrelated
generators landing on the same universal constant is exactly what separates
mechanism identity from three fields independently noticing that restarts are
useful — which is what the register's admission test asks for.

Supporting legs: criterion misclassifies 0/10 processes; the crossing sits at
σ = 0.856 against √(ln 2) = 0.833; the diffusion optimum is 2.62 against the
analytic 2.5396; and the *entire* restart curve is predicted from the un-reset
distribution alone to ≤2.9% — including for the Lévy case where ⟨T⟩ = ∞, since
the Laplace transform exists where moments do not. Sharpest evidence is two sign
flips **inside** single domains: one enzyme scheme goes from "unbinding hurts"
(multi-step, CV 0.50) to "unbinding helps 25×" (dynamic disorder, CV 1.71), and
one search paradigm from no help (3-SAT, CV 0.73) to 19.4× (quasigroup-with-
holes, CV 2.71). Those rule out "this field just happens to benefit."

**But the reason I filed M11 was wrong, and the correction is the real result.**
It was filed as the map's one live candidate for a primitive that is neither
prediction, connectivity, nor symmetry. The registered Φ-check turned out
**vacuous** — Φ_T(−r) ≡ log T̃(r), so it verified algebra, not nature; I should
have caught that when writing it. The substantive fact is better than the one I
registered: the exponential is the **maximum-entropy** law on [0,∞) at fixed
mean and has CV exactly 1, so the criterion reads *restart helps iff the
completion time is more dispersed than MaxEnt at the same mean*, and the
knife-edge result (P2: a memoryless process is exactly neutral to restarting) is
that statement's content rather than a curiosity.

So first-passage structure is not a new primitive. It is the hub's own
log-partition form on a different **base variable** — an exit time rather than a
state. Which forces a distinction the map has been eliding:

> **Φ's form is portable; Φ's variable is not.** "Does X reduce to Φ?" is
> under-specified until one says *Φ of what*.

Every reduction on record — control → ∇²Φ, symmetry-breaking → non-analyticity,
critical slowing down → soft Hessian — was a reduction to Φ of the *state*. M11
is the first to Φ of something else. The tower may be a family of towers indexed
by base variable rather than one tower.

**Three estimator failures, all diagnosed, none changing a conclusion.** Worth
recording as a pattern, because each produced a wrong verdict at some point:

1. `argmin > 0` is **biased toward "restart helps"** — the minimum of 21 noisy
   means sits ~1.9 standard errors low even when the curve is flat. The
   exponential knife edge showed a spurious 2.3% speedup; 3-SAT at CV = 0.73 was
   scored as helped by 0.08%.
2. Fixing (1) with a normal standard error then **rejected Lévy diffusion**: a
   5985× speedup scored 3.8σ, because an infinite-variance baseline has no
   meaningful standard error. Replaced with a bootstrap on the ratio.
3. Locating the criterion's crossing by *significance* finds where an effect
   becomes detectable, not where it changes sign, and is biased late (σ = 0.925,
   11% high). The signed initial slope of the restart curve is unbiased and gave
   2.8%.

Also: the registered instance family didn't cooperate. Random 3-SAT at sizes
reachable in pure Python is **not** heavy-tailed (CV 0.55 → 0.97 from n=26 to
n=70) — the instances are too small for an early wrong branch to cost
exponentially. Added quasigroup-with-holes, the benchmark where heavy-tailed
backtracking was originally characterised, and kept 3-SAT as the easy control.
That is a better result than the registered one: CV is a property of the
instance family and solver, not of "SAT".

## Decisions

- **No catalog level moved**, same reasoning as M15: the register's job is to
  produce candidates with discriminators, and one experiment — all three domains
  *simulated*, restart instantaneous and Poissonian — is not grounds to edit the
  map. M11 is now a confirmed L3 candidate with its evidence written down.
- The essay-04 note is filed as a *sharpened question*, not an architecture
  change. "Family of towers indexed by base variable" is a conjecture that
  arrived as a by-product; it deserves its own restraint pass, not a drive-by
  promotion.
- Kept every failed estimator and its diagnosis in `verdict.json` and the README.

## Next

- The base-variable question is now the most interesting thing on the board, and
  it is cheap to probe: are there other invariants in the catalog that reduce to
  Φ of something other than the state? Spectral gap (Φ of a *path* measure?) and
  noise thresholds (Φ over codebooks — the entry already says so) are the
  obvious candidates. That would decide between "one tower" and "a family".
- M11's own next leg is real data: measured enzyme turnover distributions, or a
  real solver corpus, rather than three simulations.
- Register order stands: **M3** (Molloy–Reed rewiring) next, then **M8**
  (extreme value / best-of-n).
