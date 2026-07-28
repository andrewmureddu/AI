# P8 re-registration — written before the re-run

Pays a debt logged three cycles running.
[D1](./README.md)'s P8 registered a crossover between p = 6 and p = 4 behaviour
off the tricritical line, got the **direction backwards**, and then — after the
first run exposed the error — produced a scaling law D_× ~ δa³ that was measured
at δa^3.211. That law was **post-hoc**, and D1's own README said so:

> *This is post-hoc — derived after the first run exposed the direction error, not
> registered — and it is reported as a consistency check, not as a confirmed
> prediction.*

The [D3](../D3-chart-vs-ladder/) and [D4](../D4-amplitude-vs-exponent/) logs each
repeated the debt. This registers it properly, and **strengthens it rather than
re-running the same thing**, because a re-run of a post-hoc fit on the same
quantity would prove very little.

---

## 1. What is being registered

The post-hoc law was one-variable: vary δa, watch D_×. But the derivation gives a
**two-variable** law. The quartic and sextic terms each reach the rounding
threshold at

```
        lambda_4 = (c4 D / u*)^(1/2)          lambda_6 = (c6 D^2 / u*)^(1/3)
```

and whichever is reached first at larger λ governs. Setting them equal:

```
        D_x  =  c4^3 / (u* · c6^2)                    (**)
```

so the **exponent on c₄ is +3 and on c₆ is −2**, separately. The δa³ result is
the c₆-constant slice of (\*\*) and does not test the c₆ exponent at all.

## 2. Why this is at risk rather than algebra

Within a *truncated* Φ = λy²/2 + c₄y⁴ + c₆y⁶, (\*\*) is forced — it is two
identities combined, exactly as D1 §4 declared for its own formula. Setting c₄ and
c₆ by hand would therefore prove nothing.

So both coefficients are taken from a **real model**: the mean-field Blume–Capel
free energy, carrying every order, with

```
        c4(a) = (a^2/8 - a/24) / a^3          c6(a) = (a^2/48 - a/720 - a^3/24) / a^5
```

evaluated at the critical temperature T_c = a. Sweeping the crystal-field
parameter *a* moves **both** coefficients — c₄ up from zero, c₆ down — with the
model, not the experimenter, choosing them, and with c₈ and beyond present and
unaccounted for. Whether (\*\*) survives that is the test.

These formulas were verified against the numerical Taylor expansion in D1's own
run (c₄ = 1.0e-10 and c₆ = 9.876e-3 at a = ⅓, T = 0.5, against the closed forms).

## 3. Registered predictions

Sweep a ∈ [0.3335, 0.40] on the second-order side (a > ⅓, so c₄ > 0; below ⅓ the
transition turns first-order and the analysis does not apply). Over that window
c₄ spans ~3 decades and c₆ falls by ~7×.

For each *a*, locate D_× as the noise scale at which the local λ-chart crossover
exponent crosses the midpoint of 1/2 and 2/3, then regress

```
        log D_x  =  alpha · log c4  +  beta · log c6  +  const
```

**P8R-1 (headline).** α = **3.00 ± 0.30** and β = **−2.00 ± 0.40**.
Registered separately, and β is the genuinely new content — the post-hoc δa³ law
never touched it.

**P8R-2.** The compensated quantity D_×·c₆²/c₄³ is constant across the sweep to
within a factor of **2.0** end-to-end (it is u*⁻¹, which depends only on the
registered threshold).

**P8R-3 (recovering the old result).** Restricted to a narrow window near a = ⅓
where c₆ is nearly constant, the one-variable fit D_× vs δa returns an exponent of
**3.0 ± 0.4**, consistent with the post-hoc 3.211. This is the only part that
re-measures what was already seen; it is registered so the old number is not
quietly dropped.

**Registered tolerance on the wider band, and why it is loose.** α and β are fitted
on ~8 points from a model with all higher orders present, over a window chosen so
D_× stays inside a sweepable D range. ±0.30/±0.40 is deliberately generous; a
tighter band would be false precision.

## 4. What would kill it

- **α outside 3.00 ± 0.30** — the c₄ exponent is wrong, and D1's post-hoc δa³
  was a coincidence of the narrow window.
- **β outside −2.00 ± 0.40** — the two-variable law fails, and (\*\*) governs only
  the c₆-constant slice, meaning the crossover is not the competition of two
  rounding scales.
- **D_×·c₆²/c₄³ drifting by more than 2×** — there is a further dependence the
  derivation does not contain.

## 5. Scope

Inherits D1's scope entirely: 1-D gradient system, additive noise,
degeneracy-type singularity, one control parameter. One model, from physics —
this does **not** address the outside-physics gap that D6 closed. The sweep is
confined to the second-order side of the tricritical point; the first-order side
is a different problem and is not touched.
