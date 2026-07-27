# Derivations

Analytical restraint — the pen-and-paper counterpart of
[`experiments/`](../experiments/). A derivation takes a speculative leap, tries to
prove the identity *and* find where it breaks, and ends with a level verdict plus
explicit boundary conditions. No code; the discipline is mathematical rigor and
honest scoping.

| Derivation | Tests | Result |
|------------|-------|--------|
| [`S1-universal-update.md`](./S1-universal-update.md) | [S1](../questions/SPECULATIVE.md): are replicator / multiplicative-weights / Bayes / Gibbs one update? | **L3, confirmed & bounded** — all are `x_i ∝ x_i·exp(−η g_i)` (entropic mirror descent); global convergence *not* shared (cycling in games), retired to L1. |
| [`essay3-method-as-update.md`](./essay3-method-as-update.md) | [Essay 3 §4](../essays/03-expansion-and-restraint.md): is the expansion⇄restraint method itself an instance of (★)? | **Retired as stated** — method = replicator–mutator, not mirror descent: level assignment is per-entry Bayes ((★), trivially L3); attention allocation L1–L2 (mechanism unwritten, one epoch); expansion provably outside (★) (multiplicative updates preserve zeros). Self-licensing worry deflates 🔴→🟡. |
| [`S25-control-split.md`](./S25-control-split.md) | [S25](../questions/SPECULATIVE.md): does control split into a Φ-half and an irreducible reachability half? | **Falsifier fired, conjecture upgraded** — controllability Gramian = noise-ensemble covariance (∇²Φ); min control energy = large-deviations rate fn (Legendre dual of Φ), exact linear-Gaussian. But binary reachability reduces only to Φ's *singular set*. New claim: connectivity facts are Φ-boundary facts; map is two-layered (regular Φ / singular Φ) + a possible symmetry axis. |
| [`D2-gauge-of-the-tower.md`](./D2-gauge-of-the-tower.md) | [D2](../questions/UNKNOWN-LAWS.md) / the map's standing **P0**: are the four tower-refusers a fourth floor, floor 1 in disguise, or coordinate freedom? | **No fourth floor — the scheme layer is the tower's structure group.** The floors are defined up to **G_diff** (reparameterizations smooth *at* the singular point); cross-domain comparison has only **G_pow** (φ ~ ε^a); the log-ratio signature is the difference. RG eigenvalues are conjugation-invariant and G_pow-covariant (y → a·y) — identical to D1's chart order, so all the refusers are transformation data, which is not a fact on any floor. **Chart-free residue = the codimension p − 2**, i.e. D1's degeneracy order; β/k = 1/(p−2) verified on full models. Also derives `FLOORS.md`'s unexplained asymmetry (floor 2 collapses / floor 3 stratifies = which group acts where) and reconciles with universality (**within a domain exponents are facts; across domains only ratios, signs, counts**). Load-bearing caveat: the ratios need the **common-a** commitment. Numerics: [`experiments/D2-gauge-group/`](../experiments/D2-gauge-group/). |
| [`symmetry-sector.md`](./symmetry-sector.md) | Does the invariance/symmetry sector reduce to Φ (monism), or is it the second primitive? | **Split verdict** — symmetry-*breaking* reduces to Φ's singular set (SSB at non-analyticities; Goldstone = null ∇²Φ); Noether proper does not reduce but *constitutes*: conserved charges are the natural parameters of long-time ensembles (Gibbs/GGE). Map architecture: **one tower, three floors** (symmetry → Φ-regular → Φ-singular). Spawns S26; sharpens S9 to L2-with-L3-route. |

## Convention

A derivation is only "done" when it states the boundary — the regime where the
identity fails. An identity that "always holds" hasn't been pushed hard enough. A
surviving result promotes its object in [`invariants/`](../invariants/) and earns a
[research-log](../research-log/) note; a failed one is logged and the correspondence
marked L1.
