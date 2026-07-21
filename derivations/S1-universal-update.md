# S1 — the universal update: replicator = multiplicative weights = Bayes = Gibbs

**Question ([S1](../questions/SPECULATIVE.md)):** are these four "the same update rule"?
**Method:** pure derivation (no compute). The analytical counterpart of the
[restraint stroke](../METHODOLOGY.md#the-research-rhythm-expansion--restraint).

## Verdict up front

**Confirmed at the level of the local update and its geometry — L3, exact.** All
four are the *same* update

```
        x_{t+1,i}  ∝  x_{t,i} · exp(−η · g_i)                         (★)
```

— entropic mirror descent on the probability simplex — differing only in **what
plays the role of the loss gradient g_i** and in **the step size η**. The shared
mechanism is not a resemblance: it is one variational update (KL-regularized
descent = natural-gradient descent in the Fisher metric), derived once below and
specialized four times.

**But the *global* behavior is NOT shared** (§5): with a fixed loss the update
concentrates (Bayes, Gibbs); with a game-coupled loss the *same* update can cycle
forever and never converge (replicator in zero-sum games). So "they all optimize
the same way" is false — an L1 overreach we explicitly reject. Drawing that line is
the result.

**Corollary (S2 falls out):** the single η is simultaneously the **learning rate**,
the **inverse temperature** β, and the **selection intensity**. One knob, three
names — with the caveat that vanilla Bayes locks η = 1 (§3.2).

---

## 1. The master update

Entropic mirror descent minimizes a linearized loss plus a KL leash to the current
point:

```
   x_{t+1} = argmin_{x ∈ Δ}  [ η ⟨g_t , x⟩  +  KL(x ‖ x_t) ] ,
   Δ = probability simplex,  KL(x‖y) = Σ_i x_i ln(x_i / y_i).
```

KL is the Bregman divergence of the negative-entropy potential ψ(x)=Σ x_i ln x_i,
so this is mirror descent with the entropic mirror map. Solving with a Lagrange
multiplier λ for Σx_i = 1:

```
   ∂/∂x_i [ η g_i x_i + x_i ln(x_i/x_{t,i}) − λ Σ x_i ]
        = η g_i + ln(x_i/x_{t,i}) + 1 − λ = 0
   ⇒  x_i = x_{t,i} · exp(−η g_i) · e^{λ−1}
   ⇒  x_{t+1,i} = x_{t,i} exp(−η g_i) / Z_t ,   Z_t = Σ_j x_{t,j} exp(−η g_j).
```

That is (★). Everything below is a choice of g_i and η.

**Continuous-time limit** (η → 0): expand (★),
`x_{t+1,i} − x_{t,i} ≈ η x_{t,i}(⟨g⟩ − g_i)`, giving

```
        ẋ_i = x_i ( ⟨g⟩ − g_i ) = x_i ( f_i − f̄ ),   f := −g.        (★flow)
```

**(★flow) is literally the replicator equation.** So replicator is the
continuous-time limit of (★) — not an analogy, a limit.

---

## 2. The four instantiations

| Update | writes as (★) with | g_i = | η = | exactness |
|--------|--------------------|-------|-----|-----------|
| **Multiplicative weights / Hedge** | p_{t+1,i} ∝ p_{t,i} e^{−η ℓ_i} | expert loss ℓ_i | η (free) | **exact** |
| **Bayesian update** | p_{t+1,i} ∝ p_{t,i} e^{−(−ln L_i)} | log-loss −ln L_i (surprise) | η = 1 | **exact** (η=1) |
| **Replicator (continuous)** | ẋ_i = x_i(f_i − f̄) | −fitness f_i | η → 0 flow | **exact** (=★flow) |
| **Replicator (discrete, exp fitness)** | x_i ∝ x_i e^{η r_i} | −reward r_i | η (free) | exact; linear-fitness form agrees to O(η) |
| **Gibbs / Boltzmann** | p_i ∝ e^{−β E_i} (fixed point) | energy E_i | η = β = 1/T | **exact** as free-energy minimizer / fixed point |

### 2.1 Multiplicative weights
Hedge is `p_{t+1,i} ∝ p_{t,i} exp(−η ℓ_{t,i})` — (★) verbatim, g_i = ℓ_i. This is
the *definitional* case: MWU **is** entropic mirror descent with a linear loss.

### 2.2 Bayes
`posterior_i ∝ prior_i · L_i = prior_i · exp(−(−ln L_i))`. So Bayes is (★) with
the **log-loss** g_i = −ln L_i (the self-information / surprise the datum assigns
hypothesis i) and **η = 1**. Tempering to a power posterior `p_i ∝ prior_i L_i^η`
is exactly η ≠ 1 — this is the door through which "temperature" enters inference.

### 2.3 Replicator
Discrete replicator with multiplicative (exponential) fitness f_i = e^{η r_i} gives
`x_i ∝ x_i e^{η r_i}` = (★). The textbook linear-fitness form `x_i ← x_i f_i/f̄`
is a *different discretization* that agrees with (★) to first order in η; both share
the exact continuous-time limit (★flow).

### 2.4 Gibbs
The Gibbs distribution `p_i ∝ e^{−βE_i}` is the unique minimizer over Δ of the
**free energy**

```
   F[p] = ⟨E⟩ − T·S[p] = Σ_i p_i E_i + T Σ_i p_i ln p_i
```

— a KL/entropy-regularized linear objective, i.e. the *stationary point* of (★)
with g_i = E_i, η = β. Relaxation to it (Glauber/Langevin, or (★flow) with fitness
−E) descends F. (Caveat in §5: the physical *trajectory* is model-dependent; what
is exactly shared is the variational principle and the fixed point.)

---

## 3. The normalizer is one object too

The denominator Z_t in (★) is not bookkeeping — it is *the same quantity* wearing
four names, and its log is a fifth invariant:

```
   Z  =  partition function        (Gibbs)
      =  marginal likelihood/evidence   (Bayes)
      =  mean fitness  f̄          (replicator)
      =  normalizing constant      (MWU)

   −ln Z  =  free energy           (physics)
          =  −log evidence = cumulative log-loss / surprise   (Bayes)
          =  −log mean multiplicative growth rate   (replicator / Kelly)
```

The identity **free energy = −log evidence = cumulative log-loss = −log-growth** is
exact and is arguably the deeper unification than (★) itself: it ties Jaynes'
MaxEnt, Bayesian model evidence, online-learning regret, and the Kelly / value-of-
information log-growth of a population (Kelly 1956; Bergstrom–Lachmann 2004;
Rivoire–Leibler 2011) into one scalar.

---

## 4. Why entropy? (the geometry, and the tie to S3)

(★) is not an arbitrary choice of regularizer — it is **natural-gradient descent in
the Fisher metric** restricted to the simplex:

- The KL leash makes the update the *Fisher–Rao / Shahshahani* natural gradient
  (Shahshahani metric g_ij = δ_ij/x_i is the Fisher information metric of the
  categorical distribution).
- Replicator = natural-gradient *ascent* of mean fitness in that metric
  (Shahshahani 1979; Harper 2009).
- Bayes = the **I-projection** (minimum-relative-entropy projection) of the prior
  onto the data constraint (Csiszár; Jaynes); Gibbs = the I-projection of uniform
  onto the mean-energy constraint.
- Modern synthesis: Khan & Rue's *Bayesian Learning Rule* derives Bayes, natural-
  gradient VI, and common optimizers as one natural-gradient update — independent
  confirmation of exactly this unification.

This is the hook back to the [prediction-field frame](../PREDICTION-FIELD.md) and to
[S3](../experiments/S3-fisher-geometry/): the metric of (★) **is** the Fisher metric
whose singularity we measured at phase transitions. The universal update lives on
the prediction field, and it moves along that field's natural gradient.

---

## 5. Where it breaks (boundary conditions — the honest part)

1. **Global dynamics are NOT shared.** (★) is one *local* step; its long-run
   behavior depends on whether g is fixed or state-coupled. Fixed loss (Bayes on a
   well-specified model, Gibbs relaxation) → concentration/convergence. Game-coupled
   loss g_i = g_i(x) (evolutionary games, markets) → the *same* update exhibits
   Poincaré recurrence and cycles forever (MWU/replicator in zero-sum games;
   Mertikopoulos–Papadimitriou–Piliouras 2018). **"They all converge alike" is
   false.** This is the sharp line.
2. **Simplex only.** The specific update is the entropic one on distributions over a
   discrete set. Continuous state spaces need the measure-valued versions
   (replicator–mutator PDE, continuous exponential weights, Gibbs over a continuum);
   the structure survives, the "same equation" needs its functional form.
3. **Bayes has no free step size.** Vanilla Bayes fixes η = 1; the learning-rate =
   temperature identity (S2) requires generalized/tempered Bayes.
4. **Discretization ambiguity.** Discrete replicator (linear fitness) ≠ MWU exactly;
   they coincide only in continuous time or with exponential fitness.
5. **Physical relaxation ≠ the map.** Glauber/Langevin/Metropolis share F's
   Lyapunov structure and the Gibbs fixed point but are not step-for-step (★). The
   physics leg is "same variational principle + fixed point," slightly weaker than
   "same trajectory."

---

## 6. Level assignment and next steps

- **Local update + geometry:** **L3** (shared mechanism: entropic mirror descent /
  Fisher natural gradient / I-projection). Exact, derived, four ways.
- **The normalizer/free-energy identity (§3):** **L3**, arguably the crown jewel.
- **Global convergence:** **not shared** — explicitly *retired to L1* as a claim;
  the counterexample (cycling in games) is the evidence.

Net: **S1 confirmed, sharpened, and bounded.** Promote
[`mirror-descent-update.md`](../invariants/mirror-descent-update.md) seed → L3.

**Strengthen next:** (a) numerically exhibit the split in §5 — the *same* update
concentrating on a fixed loss vs. cycling on a zero-sum game (cheap numpy, a real
restraint follow-up). (b) Push the §3 free-energy = log-growth identity into its own
entry; it may subsume several catalog rows.

## References

- Nemirovsky & Yudin 1983; Beck & Teboulle 2003 — mirror descent.
- Arora, Hazan & Kale 2012 — multiplicative weights survey.
- Cesa-Bianchi & Lugosi 2006; Vovk 1990 — exponential weights = Bayes with log-loss.
- Shahshahani 1979; Harper 2009 — replicator = Fisher natural gradient.
- Hofbauer & Sigmund 1998 — evolutionary game dynamics.
- Mertikopoulos, Papadimitriou & Piliouras 2018 — cycles / Poincaré recurrence.
- Jaynes 1957; Csiszár 1975 — MaxEnt, I-projection, Gibbs.
- Kelly 1956; Bergstrom & Lachmann 2004; Rivoire & Leibler 2011 — log-growth = information.
- Khan & Rue 2023 — the Bayesian learning rule (natural-gradient unification).
