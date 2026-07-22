# Essay 3 probe — is the method an instance of the universal update?

**Question ([essay 3, §4](../essays/03-expansion-and-restraint.md)):** the essay
claimed the expansion⇄restraint method is itself an instance of S1's universal
update `x_i ∝ x_i·e^{−η g_i}` — "L2 established, L3 suspected." Probe the
suspicion: try to write the method as (★) *exactly*, and find where it breaks.
**Method:** pure derivation, plus an audit of the actual ledger's moves. The
restraint stroke, turned on the claim that named it.

## Verdict up front

**The L3 suspicion dies for the method as a whole and survives for one stroke of
it.** Decomposing the method into its three component processes:

1. **Level assignment** (what a restraint pass does to one entry) — **exactly (★),
   L3**, but in a nearly trivial way: it is Bayes over five hypotheses, per entry.
2. **Attention allocation** (which stones get worked) — the only place a genuine
   population-level (★) could live; the update rule is **not written down anywhere
   and not recoverable from a one-epoch log**. Stuck at L2 (structural fit,
   unverifiable mechanism). Honest tag: **L1–L2**.
3. **Expansion** (new stones) — **provably outside (★)**. Mirror descent cannot
   grow its support. This is not a gap in the analogy; it is the boundary, and it
   lands in a satisfying place (§4).

The corrected identification: the method is not entropic mirror descent. It is a
**replicator–mutator process with a zero-sum attention budget** — whose *selection
term* is S1's object and whose *mutation term* is precisely the expansion stroke.
Essay 3's §4 mistook the selection term for the whole process. The essay's own §2
("you cannot prune your way to a frame") already contained the refutation: it is
the statement that the mutation term is not expressible as selection.

---

## 1. Formalizing the method (the step the essay skipped)

To claim (★), you must say what `x`, `g`, and `η` are. The essay never did; do it
now. The method's state at round t (a "round" = one restraint pass) is:

- a catalog of entries i = 1…N_t (note the subscript — N grows; hold that thought);
- per entry, a credence vector `p_i(ℓ)` over ladder levels ℓ ∈ {L0…L4} (implicit
  in practice — the entry's headline level plus hedging — but that is what the
  headline summarizes);
- an attention allocation `a_i ≥ 0, Σa_i = budget` (which stones get worked this
  session).

A restraint pass on entry i runs a test with outcome o and updates that entry.
An expansion stroke adds entries. The essay's claim is that some part of this is
(★). There are exactly three candidate `x`'s: `p_i(·)` (per-entry level credence),
`a` (attention), and "mass over the catalog" (whatever the essay meant by demoted
entries losing mass). Take them in turn.

## 2. Face 1: level assignment is Bayes over five hypotheses — (★) exactly, L3, small

Per entry, a test outcome o has a likelihood under each level: a falsifier
surviving at machine precision is likely under L3-and-up and unlikely under L1
(S23's 1.4e-17 is why its entry jumped); a cycling counterexample is impossible
under "global L3" (S1's own demotion). Updating level-credence by outcome is

```
   p_i(ℓ) ← p_i(ℓ) · P(o | ℓ) / Z_i ,
```

which is (★) with `g(ℓ) = −ln P(o|ℓ)` and η = 1 — literally the Bayes column of
the S1 derivation, over a five-point hypothesis space. **This is exact and it is
L3**: the generative process (evidence reweights hypotheses multiplicatively) is
the same one, not a resemblance.

But note what it is *not*: it is per-entry. `Z_i` normalizes over the five levels
of entry i, not over the catalog. S3's confirmation took no probability away from
S5. There is no competition among correspondences here — each entry runs its own
private five-hypothesis Bayes. Calling this "the method is the universal update"
is true the way "the lab uses arithmetic" is true. The essay's excitement was
about the *population* reading — a distribution over the catalog, reweighted by
performance. That has to live in face 2 or nowhere.

## 3. Face 2: attention is the only real candidate — and it is unfalsifiable at n=1

The population-level claim needs a normalized `x` over entries with multiplicative
updates. Credences don't couple (§2). The one genuinely conserved quantity is
**attention**: session time is finite, so `Σa_i = budget` is a real simplex
constraint, and one stone's session is another's neglect. Zero-sum: check.

Multiplicative: the essay asserted survivors "compound" and killed stones keep
"trace mass." Audit the actual log (all of it: 2026-07-19, one epoch, ten files).
S1 survived → S23 built on it → S19–S24 built on the scaffold: consistent with
compounding. Killed global-convergence claim → mentioned once since: consistent
with trace mass. But *consistent with* is the problem. One epoch of a process
that was partly steered by explicit prioritization (the OPEN-QUESTIONS P0 list —
a **deliberative** allocator, not a multiplicative one) cannot distinguish
`a_i ∝ a_i·e^{−η g_i}` from "we worked on what seemed promising," which is every
allocation rule ever. The mechanism check that L3 requires — perturb η, watch the
predicted response — is the exact test essay 3 already named and nobody has run,
*and cannot run yet*: an η-perturbation experiment needs multiple epochs at
different expansion/restraint tempos, and the log contains one day.

Per the methodology's own rule — L3 requires a named, perturbable mechanism —
face 2 is **at most L2** (the simplex-plus-reweighting form fits) and arguably
**L1** (structure maps, no quantitative law identified, free parameters
everywhere: what is g_i for a stone? log-loss of what prediction?). Until someone
writes down the attention update as an equation and confronts it with ≥2 epochs,
this face is a structural analogy wearing (★)'s clothes.

## 4. Face 3: expansion cannot be written as (★) — and that is the boundary

Here is the clean negative result. Mirror descent — every specialization in the
S1 derivation — has the property that its support never grows:

```
   x_{t,i} = 0   ⇒   x_{t+1,i} = x_{t,i} · e^{−η g_i} / Z = 0 .
```

Multiplicative updates preserve zeros. (★) can concentrate, cycle, or hedge over
a *fixed* hypothesis space; it cannot mint a hypothesis. But the expansion stroke
is exactly support growth: S13–S24 did not exist with small weight before
2026-07-19 and get up-weighted — they were **constructed**, from the scaffold of
survivors. N_t grew. No choice of loss, step size, or Bregman geometry makes (★)
do that; the S1 derivation's own master equation forbids it.

So the honest identification is not mirror descent but the **replicator–mutator**:

```
   selection term:  multiplicative reweighting of existing candidates   = (★)
   mutation term:   injection of new support, structured by survivors   ≠ (★)
```

And this lands somewhere satisfying. S1's *result* was that the universal update
covers selection-like adaptation exactly, with a sharp boundary (global dynamics,
game coupling). This probe finds the same object with the same kind of boundary
one level up: the method's restraint stroke is (★)-shaped; its expansion stroke is
the mutation term that (★) provably cannot express. Essay 3's §2 asymmetry-of-
initiative argument — restraint is transitive, it cannot generate its own objects
— was already a prose statement of the zero-preservation lemma above. The essay
refuted its own §4 two sections early and didn't notice.

## 5. Verdict and boundary

| Face | Claimed | Found | Level |
|------|---------|-------|:-----:|
| Level assignment (per entry) | — | Bayes over {L0…L4}, exact instance of (★) | **L3** (trivially) |
| Attention allocation (across entries) | L3 suspected | form fits; mechanism unwritten; n=1 epoch, unfalsifiable as posed | **L1–L2** |
| Expansion (support growth) | part of the instance | provably outside (★): multiplicative updates preserve zeros | **boundary** |
| "The method = the universal update" | L2 est., L3 susp. | **retired**: method = replicator–mutator; only its selection term is (★) | **L1 as stated** |

**What would revive face 2:** state the attention update as an equation with its
loss defined (candidate: g_i = −log of stone i's falsifier-survival likelihood,
η = the session's expansion/restraint ratio), then run the η-perturbation across
≥3 epochs at deliberately different tempos and check the mirror-descent regret
prediction. That is now a designed experiment rather than a suspicion — it goes
to the agenda, not to more prose.

**Consequence for essay 3:** §4's L3 suspicion is settled — negatively for the
method as a whole, positively for a smaller thing than the essay wanted. §5's
self-licensing worry **deflates accordingly**: the alarming version ("the repo's
procedure validates itself via its own best result") required the method to *be*
the universal update; a replicator–mutator whose mutation term is outside the
object it studies is not a closed loop. The alarm can be lowered from 🔴 to 🟡 —
the selection half still self-resembles, but the generative half looks outward
by construction. Essay 3 gets a restraint note, per its own promise to keep its
dead.
