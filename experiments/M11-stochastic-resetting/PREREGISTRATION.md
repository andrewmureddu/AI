# M11 pre-registration — written before any measurement

Per [`questions/L3-MECHANISMS.md`](../../questions/L3-MECHANISMS.md)'s working
rule: *register the discriminator's expected value before measuring it.* Nothing
below is revised after the run; results live in [`README.md`](./README.md).

**Mechanism under test (M11).** Stochastic resetting: a first-passage process
restarts from its initial condition at rate r, truncating the unlucky
trajectories that dominate the mean. Claimed to run identically in diffusive
search, enzymatic turnover, and randomized combinatorial search.

**Why this one.** It is the register's only current candidate for a second axis
that is *not* symmetry — first-passage structure is not obviously a
Φ-derivative, and the criterion does real predictive work in three fields that
discovered it separately (Evans–Majumdar 2011; Reuveni–Urbakh–Klafter 2014;
Luby–Sinclair–Zuckerman 1993 / Gomes–Selman–Kautz 1998).

---

## The theory (stated before the run, so the numbers are predictions)

Let T be the un-reset completion time and T̃(r) = E[e^{−rT}] its Laplace
transform. Under Poissonian restart at rate r:

    ⟨T_r⟩ = (1 − T̃(r)) / (r·T̃(r))

Expanding at r = 0 gives d⟨T_r⟩/dr|₀ = ⟨T⟩² − ⟨T²⟩/2, so restarting helps iff
⟨T²⟩ > 2⟨T⟩², i.e. **Var(T) > ⟨T⟩²**:

    **restart helps  ⟺  CV = σ_T/⟨T⟩ > 1**

and (Reuveni 2016) at an interior optimum the *restarted* process satisfies

    **CV(T_{r*}) = 1 exactly**, whatever the underlying process.

Both statements are parameter-free. The second is the cross-domain identity
test: the same universal constant should fall out of three unrelated processes.

---

## Registered predictions

**P1 — the criterion's sign flip, and its location.** Over a battery spanning
CV ∈ [0.25, ∞) (Erlang k=1..16, uniform, lognormal, Pareto, Lévy), the
simulated optimal rate satisfies r\* > 0 iff CV > 1, with **zero
misclassifications** away from the knife edge. Sharper: scanning lognormal
width σ, the crossing sits at **σ\* = √(ln 2) = 0.8326** (where CV = 1) to
within 5%. Note r\* is found by *simulating* the restarted process, not from the
moment condition, so the test is not circular.

**P2 — the exponential knife edge.** For T ~ Exp (CV = 1 exactly), ⟨T_r⟩ is
**independent of r**: relative spread < 2% across a decade of r. A memoryless
process cannot be helped or hurt by restarting.

**P3 — diffusive search against its analytic optimum.** For 1D diffusion to a
target at distance x₀, the optimum solves z/2 = 1 − e^{−z} with z = x₀√(r/D),
giving **r\*x₀²/D = 2.5396** (z\* = 1.5936). Predict within 5%.

**P4 — parameter transfer (the L3 condition).** In every domain, the restart
curve predicted from the **un-reset** completion-time distribution alone — via
the empirical Laplace transform — matches the independently simulated restarted
process within **3%** across the whole r range. This is the "measure the
mechanism's parameters where the pattern isn't, then predict the pattern"
requirement. It should hold even where ⟨T⟩ = ∞ (the Lévy case), because T̃(r)
exists when moments do not.

**P5 — the universality, cross-domain (the identity test).** At the optimal
rate, **|CV(T_{r\*}) − 1| < 0.05 in all three domains.** Same constant, three
unrelated processes. This is the prediction that separates mechanism identity
from three domains happening to benefit from restarts.

**P6 — Michaelis–Menten sign flip within one scheme.** Substrate unbinding *is*
restart. Same enzyme, two catalysis regimes, opposite conclusions predicted from
CV alone: multi-step catalysis (Erlang, k = 4 substeps, CV = 0.5) ⇒ unbinding
**hurts**, r\* = 0; dynamic disorder (slow/fast conformer mixture, CV ≈ 1.7)
⇒ unbinding **helps**, r\* > 0. Taken in the instantaneous-rebinding
(saturating-substrate) limit so the restart is cost-free.

**P7 — SAT.** Randomized DPLL runtimes on a fixed satisfiable random 3-SAT
instance at the phase-transition ratio have **CV > 1**, and Poissonian restarts
give a speedup whose size is predicted by P4's transform. Runtimes are censored
at a step cap; censoring biases the no-restart baseline *downward*, so any
measured speedup is a lower bound.

**P8 — the Φ question (exploratory, and the reason this matters to the map).**
Write Φ_T(s) = log E[e^{sT}], the cumulant generating function of the completion
time. Then

    ⟨T_r⟩ = (e^{−Φ_T(−r)} − 1)/r ,  and CV > 1  ⟺  Φ_T''(0) > Φ_T'(0)²

so the whole theory is log-partition machinery — but built on the **completion
time**, not on the state distribution that the repo's Φ = ln Z describes.
Predict this identity holds numerically to <1e-6 in every domain. If it does,
M11 is *not* the second axis it was filed as: it extends the hub's form to exit
times by changing the base variable. Recording the prediction now because it
changes what a positive result means.

## What would kill M11

- A domain with CV > 1 whose simulated r\* is 0, or CV < 1 with r\* > 0 (P1) —
  the criterion is not shared.
- CV(T_{r\*}) ≠ 1 in any domain (P5) — the three are benefiting from restarts
  for different reasons, i.e. convergence, not identity.
- Parameter transfer failing (P4) — the un-reset distribution does not determine
  the restarted behaviour, so "the same mechanism" has no content.
