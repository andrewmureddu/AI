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

## Convention

A derivation is only "done" when it states the boundary — the regime where the
identity fails. An identity that "always holds" hasn't been pushed hard enough. A
surviving result promotes its object in [`invariants/`](../invariants/) and earns a
[research-log](../research-log/) note; a failed one is logged and the correspondence
marked L1.
