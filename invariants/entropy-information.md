# Entropy & information

> **One-line claim:** Thermodynamic entropy and Shannon information entropy are the
> same functional, connected by the maximum-entropy principle — but the bridge
> predicts in some places and merely re-describes in others.
> **Headline correspondence level:** L3 for the statistical-mechanics ↔
> information-theory link (Jaynes); L2 for most downstream uses.
> **Status:** developing

## Statement

Entropy is the functional S = −k Σ p_i ln p_i (Gibbs/Shannon; k = 1 in nats).
Thermodynamics recovers it as the log of the number of microstates
(Boltzmann S = k ln W). Information theory recovers the *same* functional as the
expected surprisal / minimum average code length (Shannon 1948). The
**MaxEnt principle** (Jaynes 1957): the least-biased distribution consistent with
known constraints is the one maximizing S subject to those constraints —
recovering the Boltzmann distribution as a special case.

## Manifestations by domain

| Domain | Entropy shows up as | Level | Quantitative signature | Ref |
|--------|---------------------|:-----:|------------------------|-----|
| Thermodynamics | S = k ln W; dS ≥ 0 | anchor | Boltzmann constant sets units | Boltzmann 1877 |
| Information theory | H = −Σ p log p (bits) | L3 | Same functional; entropy = code length | Shannon 1948 |
| Statistical inference | MaxEnt priors | L3 | Boltzmann/Gibbs as MaxEnt solution | Jaynes 1957 |
| Machine learning | Cross-entropy loss, KL divergence | L2 | Same functional; used as objective | — |
| Ecology | Shannon diversity index H′ | L2 | Same formula, borrowed | — |
| Economics | Entropy in income distribution, econophysics | L2/L1 | Borrowed formalism, contested | — |

## Shared mechanism

The genuine bridge is **statistical**: both thermodynamic and Shannon entropy
count (the log of) the number of ways a macrostate can be realized. Jaynes'
insight is that thermodynamics *is* inference under the MaxEnt principle — this is
a real L3 mechanistic identity, not an analogy. The Second Law then reads as
"systems drift toward higher-multiplicity macrostates," which is a statement about
counting, and applies wherever the counting setup is genuinely present.

**But** the further you get from a well-defined state space and constraint set,
the more the connection degrades to L2 (same formula, borrowed) or L1 (evocative
use of the word "entropy"). Ecological diversity indices use *the formula* without
the thermodynamic content — that's honest L2. Loose talk of "social entropy" is
usually L1.

## Quantitative signature

The functional form −Σ p log p and, at L3, the appearance of the correct
Lagrange-multiplier structure (temperature = multiplier on the energy constraint).
A true instance predicts the *distribution* (e.g., Boltzmann, Gaussian as MaxEnt
under a variance constraint), not merely reuses the symbol.

## Boundary conditions / where it breaks

- Non-equilibrium / long-memory systems where MaxEnt's constraint set is unclear.
- Systems without a well-defined state space to count over — the formula still
  computes a number, but it lacks the second-law content.
- The units differ (k_B vs. bits); the bridge is up to a constant, which matters
  for physical claims and not for coding claims.

## Evidence for

- MaxEnt *derives* equilibrium distributions across physics from a single
  inference principle — strong predictive transfer.
- Landauer's principle ties information erasure to a physical energy cost
  (k_B T ln 2 per bit), experimentally confirmed — a genuine physical bridge
  between information and thermodynamics.

## Evidence against / competing explanations

- Much cross-domain "entropy" is the formula without the physics (L2 at best).
- Whether MaxEnt is a principle of nature or of *inference* is philosophically
  contested (though the predictions stand either way).

## Open questions

- Where does MaxEnt genuinely *predict* vs. merely *re-describe*? Build a list of
  each. (→ [`questions/OPEN-QUESTIONS.md`](../questions/OPEN-QUESTIONS.md) Q3)
- Is the "free energy principle" in neuroscience an L3 extension of this bridge or
  an L1/L2 borrowing? (cross-link
  [`optimization-variational.md`](./optimization-variational.md))

## References

- Shannon 1948 — A mathematical theory of communication
- Jaynes 1957 — Information theory and statistical mechanics
- Landauer 1961 — Irreversibility and heat generation
- Bérut et al. 2012 — Experimental verification of Landauer's principle
