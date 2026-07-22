# Why channels of a Boltzmann family stay near one-parameter (S25 conjecture, proved)

**Claim (from the S25 stress test):** deterministic channels of a
one-parameter Boltzmann family resist leaving one-parameterness — the most
adversarial designs only reached rank-1 fraction ≈ 0.95. Here we prove why,
identify the *exact* obstruction, and extract a quantitative bound that is
verified numerically in
[`verify_theorem.py`](../experiments/S25-channel-independence/verify_theorem.py).

Everything below holds for **stochastic channels too** — nothing uses
determinism.

## Setup

Let p(s|β) = m(s) e^{−βE(s)} / Z(β) and let a channel k(y|s) induce

    q(y|β) = Z_y(β) / Z(β),      Z_y(β) = Σ_s k(y|s) m(s) e^{−βE(s)}.

Each Z_y is the Laplace transform of a positive measure (the energy content
of cell y), so log Z_y is smooth and convex with the cumulant structure

    −∂_β log Z_y = E[E | y, β] =: μ_y(β)        (conditional mean energy)
    ∂²_β log Z_y = Var[E | y, β] =: V_y(β) ≥ 0  (conditional energy variance)

and hence

    ∂_β log q(y|β) = ⟨E⟩_β − μ_y(β).                                (†)

## Lemma 1 — exact characterization of one-parameterness

*The induced family {q(·|β)}, β in an open interval, is a one-parameter
exponential family — q(y|β) = h(y) exp(η(β)S(y) − A(β)) for some statistic
S, carrier h, and smooth η — **iff** there exist functions a, b with*

    μ_y(β) = a(β) + b(β) S(y)     for all y and all β in the interval.

**Proof.** (⇒) Differentiate the exponential-family form:
∂_β log q(y|β) = η′(β)S(y) − A′(β); comparing with (†) gives
μ_y(β) = [⟨E⟩_β + A′(β)] − η′(β)S(y), which is the affine form.
(⇐) Substitute the affine form into (†) and integrate from a base point β₀:
log q(y|β) = log q(y|β₀) + ∫(⟨E⟩−a) − S(y)∫b, which is carrier
q(·|β₀), statistic S, natural parameter η(β) = −∫β₀^β b. ∎

**Corollary (the whole hierarchy is enslaved).** Differentiating the affine
condition in β: V_y(β) = −a′(β) − b′(β)S(y); differentiating again, the
conditional third cumulant is affine in S; and so on. A one-parameter
induced family requires the **entire conditional cumulant hierarchy across
cells to be affine in one and the same statistic S**. This is why exactness
is rare (decimation in 1D achieves it because summed-out spins contribute an
exactly common factor structure) — and the *leading* violation lives in the
conditional variances, which is what the quantitative bound below captures.

## Theorem 2 — the induced family is within O(Δ²·disp(V)) of an exact one-parameter family

Fix β₀ and a window δ ∈ [−Δ, Δ]. Taylor with integral remainder gives, for
each cell,

    log Z_y(β₀+δ) = log Z_y(β₀) − δ μ_y(β₀) + g_y(δ),
    g_y(δ) = ∫₀^δ (δ−u) V_y(β₀+u) du,     0 ≤ g_y(δ) ≤ ½ δ² V*_y,

with V*_y = max_{|u|≤Δ} V_y(β₀+u). Define the **exact** one-parameter
exponential family

    q̂(y|δ) ∝ q(y|β₀) · exp(−δ μ_y(β₀))
    (carrier: the induced distribution at β₀; sufficient statistic: the
     conditional mean energy; natural parameter: δ).

Then, since any function of δ alone is absorbed by normalization,

    | log q(y|β₀+δ) − log q̂(y|δ) − c(δ) |  =  |g_y(δ) − ḡ(δ)|
                                            ≤  ½ Δ² · osc_y(V*),

where osc_y(V*) = max_y V*_y − min_y V*_y is the **dispersion of the
conditional variance across cells** and ḡ is any convenient reference
(e.g. the cell-average of g). For log-ratio bounded by ε this gives
KL(q‖q̂) ≤ ε(e^ε − 1) ≈ ε² for small ε.

**The obstruction is the dispersion, not the size, of V_y.** If every cell
has the same conditional variance profile, the second-order term is a
row-constant and vanishes into the normalizer — the family stays exactly
one-parameter to this order *no matter how large V is*.

## Theorem 3 — rank bound for the measured defect

The (weighted) per-β-centered log-probability matrix used in the stress
test decomposes as

    M[δ, y] = 1 ⊗ A(y) + δ ⊗ (−μ̃_y) + G,     ‖G‖_F ≤ ½ ⟨δ⁴⟩^{1/2} · sd_w(V),

with A the centered carrier, μ̃ the centered statistic, and sd_w the
probability-weighted standard deviation across cells. Hence everything
beyond rank 2 is bounded by G:

    tail₃ := 1 − (s₁² + s₂²)/Σs²  ≤  ‖G‖²_F / ‖M‖²_F,

and since ‖G‖_F scales as Δ²·sd_w(V*) while ‖M‖_F is dominated by the
Δ⁰ carrier component, the defect obeys

    tail₃  ≲  ρ²,   ρ = Δ · sd_w(V*) / (2 · sd_w(μ)),   tail₃ ∝ Δ⁴,        (★)

where V*_y is the **window-max** conditional variance (the dispersion can
accidentally vanish at a single β — energy_mod_8 does — so the center value
is not sufficient). If the variance dispersion itself cancels at the window
center, the third conditional cumulant leads and the exponent steps up to
Δ⁶ — the defect exposes the first dispersive order of the cumulant
hierarchy.

(The empirically reported rank-**1** fraction is stricter: it also charges
the carrier component 1⊗A. Its observed dominance says the carrier is
nearly aligned with the statistic — true whenever q(·|β₀) is itself close
to the fitted family — an alignment fact, not required by the theorem.)

## What this explains

1. **Why one-parameterness is generic.** Any channel whose cells
   self-average — coarse-grainings, random subsets, hashes: cells that mix
   comparable portions of the energy landscape — has nearly homogeneous
   conditional variances, so sd_w(V) is small and (★) pins the family near
   rank-1. Escaping requires engineering cells with *heterogeneous*
   variance profiles.
2. **Why shell-scrambling was the only successful attack.** Merging
   disjoint energy shells creates cells whose variance profiles differ
   maximally (a merged far-pair cell has huge V near its crossover; an
   unmerged shell has V ≈ 0). The stress test found the right adversary
   because it is the unique one: by Lemma 1's corollary, variance
   dispersion is the leading — and, in the window limit, the only —
   obstruction.
3. **Why the composition law has the domain it has.** The law is exact on
   one-parameter families (Lemma 1 + reparametrization covariance of
   Fisher information); Theorem 2 bounds the distance from one; so the
   law's error is controlled by Δ²·osc(V) — small for every natural
   measurement, large only for shell-engineered channels.

## Verification (`verify_theorem.py`, 2026-07-21)

1. **Lemma 1, exact:** for 1D decimation (a known exact exponential
   family) the per-β-centered conditional-mean matrix is rank 1 to
   machine precision — defect 0.0 at float64. Majority rule: 0.9995;
   shell scramble: 0.9878 — degradation exactly where the family leaves
   one-parameterness.
2. **Theorem 3 bound: holds 8/8 channels** (with window-max V*, which the
   energy_mod_8 case shows is necessary — its variance dispersion
   accidentally vanishes at the window center). Honesty: the bound is
   loose (up to ~10⁴× slack; log-log correlation of ρ² with the measured
   defect only 0.37), so its verified content is *validity*, not
   tightness — the sharp confirmations are items 1 and 3.
3. **Scaling: measured log-log slopes 4.03, 3.80, 3.67 ≈ 4** for
   variance-dispersion-led channels, and **6.27 ≈ 6 for crossover_pairs**
   — whose pairwise crossovers were placed symmetrically about the window
   center, cancelling the leading variance dispersion so the third
   cumulant leads. The Δ^{2k} hierarchy is visible in the data.

## Status

🟢 for Lemma 1 and the qualitative theorems (elementary, self-contained
proofs; exact numerical confirmation). 🟡 for (★) as a quantitative tool:
valid and scaling-correct, constants loose. First run of the verifier
predicted slope 2 from a wrong norm count (the carrier dominates ‖M‖);
the measured slope 4 forced the correction — the second time in S25 the
numerics disciplined the theory before the theory disciplined the world.
