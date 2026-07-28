# 2026-07-28 — The base variable: one tower, and floor 3's stratification is forced

**Worked on:** the oldest live debt — [M11](./2026-07-25-M11-stochastic-resetting.md)'s
"Φ of what?", flagged as outstanding by [M3](./2026-07-25-M3-molloy-reed-rewiring.md),
[P-D](./2026-07-27-PD-allometry.md), [P-C](./2026-07-28-PC-variational-kinds.md)
and [P-K](./2026-07-28-PK-kink-taxonomy.md).
**Change:** new derivation [`derivations/base-variable.md`](../derivations/base-variable.md)
+ companion [`experiments/BV-base-variable/`](../experiments/BV-base-variable/);
M11's "family of towers" conjecture is **answered in the deflationary direction**;
`FLOORS.md` §2's "floor 3 stratifies" stops being an observation and becomes a
consequence; P-D's null case is **resolved and downgraded**.

## What I did

Paid the debt, as a derivation with a numerical companion — a rhythm change after
two experiment-heavy passes, and the right mode for a question that turns out to be
answerable on paper.

M11 asked whether the tower is one tower or a family indexed by base variable.
Five arrivals had accumulated (M11: exit times; M3: edge pairs; P-A: trajectories;
S5: codebooks; P-D: apparently none), and nobody had asked what picks the variable.

## What I found

**One tower, not a family — and the answer is older than the question.** Write
Φ_Y(λ) = log E_P[e^{λ·Y}] for an observable Y of a master measure P. Then:

- **The form is portable** — Φ_Y is convex with ∇Φ = mean and ∇²Φ = Cov for *every*
  Y. Two lines of Hölder. So the hub's recurrence across unrelated fields is not
  evidence about the world; it is a property of taking a log-Laplace transform of
  anything. Measured across three base variables of one master measure: identities
  hold to **3.7e-9**, all convex.
- **The geometry is not** — ∇²Φ_Y = Cov(Y), so it is the covariance of *the chosen
  observable*. The three base variables' spectral norms span **413×**.
- **Base variables are ordered by refinement**, each a pushforward of the master
  measure. So they are one tower seen through observables, not independent towers.

**The rule that picks the variable is sufficiency.** An invariant is a Φ-fact on Y
iff Y is sufficient for it; the right base variable is the coarsest sufficient one.
This makes the map's question decidable instead of a matter of taste — and it is
not vacuous, because sufficiency fails informatively. Two doubly stochastic chains
with stationary laws identical **by construction** have mean first-passage times of
**100.0 vs 20.0** and trajectory curvatures of **19.93 vs 0.50**, while Φ on the
state base variable is identical to **4.66e-15**. That is M3's result — identical
degree sequences, p_c moving 35–148% — in a system small enough to be exact, and
the rule predicts M3's whole failure ladder: pairs recover it to ≤4.6%, clustering
breaks it at +124%, because triangles are not measurable w.r.t. pairs.

**The unasked-for payoff: floor 3's stratification is forced, and into exactly
three kinds.** `FLOORS.md` §2 listed the strata and called classifying them open
work. Given the construction it is not open. On a finite system Φ_Y is real-analytic
in the interior of its domain, so every floor-3 phenomenon is one of:

    3a  DOMAIN BOUNDARY  Phi = infinity beyond a boundary  -> heavy tails, support loss
    3b  LIMIT            analytic at finite size, not in the limit -> Lee-Yang, P-D's kink
    3c  DEGENERACY       Phi analytic, a DERIVATIVE degenerates -> D1's p, D6's q1/q2

There is no fourth option — analytic / undefined / degenerate exhausts the cases.
This unifies four of the repo's own results as one statement, and it retro-explains
D6: support loss is q1 = 1 rather than p = ∞ *because it is 3a rather than 3c*,
which is why D1's formula was undefined there rather than wrong. Guard passed: 3a,
3b, 3c each exhibited and **0 of 6** interior non-analyticities at finite size.

**A corollary the companion measures, because it is a common confusion:** a singular
*density* is not a singular *Φ*. Push uniform through Y = x² and the density
diverges as y^**−0.5003** while Φ stays finite over |λ| ≤ 200. "The distribution
goes singular, therefore the free energy does" is unlicensed.

**P-D's null case is resolved and is less dramatic than recorded.** P-D measured
∇²log Z rank 1 for every λ and the log wrote "is there a Φ at all? — no." Under the
construction there *is* a Φ, on a **rank-one base variable**: rank-1 covariance
everywhere says the two statistics are functionally dependent, and a rank-one Y has
no conjugate pair, hence no exchange rate, hence nothing Legendre downstream.
Reproduced from the definition rather than from P-D's code: rank **1**,
smallest/largest **4.36e-16**, rising to effective dimension **2** when an
independent statistic is added. So **rank(∇²Φ_Y) is the effective dimension of the
base variable**, and `FLOORS.md` §4's floor-3/floor-4 boundary is the difference
between a degeneracy *of* a base variable and a degeneracy *in* one.

**4 of 6 at-risk, 2 of 4 identities — and every failure is mine, not the claim's.**
This was the first pass run under
[`METHODOLOGY.md`](../METHODOLOGY.md)'s new pre-registration audit, written one
pass earlier after six instances. **It violated audit item (iii) — instrument
precision — three times in the run the audit was supposed to govern:** a degree-20
finite difference dividing by h²⁰ = 1e-26 (2.96e+7 of noise, where exact cumulants
give 1.63e-7); a 1e-15 tolerance on two numerically computed eigenvectors of a
20×20 matrix; and a 1e-12 rank threshold given to a doubly-nested stencil whose
floor **leg A had measured at 3.7e-9 on the same page**. A fourth failure (P9) was
a mis-specified criterion — I asked for the smallest eigenvalue to be large when
the claim was about the count of non-null ones.

## Decisions

- **M11's conjecture is answered: one tower.** The "family" is the family of
  pushforwards of one master measure. Recorded in the derivation rather than as a
  catalog edit, since no entry's level moves.
- **`FLOORS.md` §2's open work closes.** Floor 3's stratification is a consequence
  of the log-Laplace form, with three strata and a reason there is no fourth.
- **P-D's "no Φ at all" is downgraded to "Φ on a rank-one base variable."** Same
  measurement, weaker claim, and it now connects to D2's gauge reading from the
  other side: a rank-one Y admits no Legendre dual, so the chain stops.
- **The audit's item (iii) is rewritten mechanically**, because a four-question
  checklist demonstrably does not survive contact with its own author: *state the
  instrument's noise floor next to every registered tolerance; if you cannot state
  the floor, you may not register the number.* All three failures die on sight
  under that wording.
- **No catalog level moved.** Same reasoning as M11 and M15 — a derivation plus one
  synthetic companion is not grounds to edit per-domain levels.

## Next

- **Use the rule prospectively.** Everything it explains was measured first; the
  honest test is to *predict* an invariant's base variable before measuring it.
  [Q6](../questions/OPEN-QUESTIONS.md) (urban scaling) is the obvious candidate —
  the rule says find the coarsest statistic sufficient for the exponent, and P-D's
  three legs already say what to look for.
- **M8** (extreme value / best-of-n) — the L3 register's next item, now deferred
  five times.
- **Continuous-transition type L** ([P-K](./2026-07-28-PK-kink-taxonomy.md)'s
  extension) — does the L/C distinction survive outside min-of-two-branches?
- **The catalog has not been re-read against the trichotomy.** Sorting all 23
  entries into 3a/3b/3c is cheap, mechanical, and would grade the classification
  the way the floor sort graded the tower.
