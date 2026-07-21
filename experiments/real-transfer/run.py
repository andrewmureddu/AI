"""
The real frontier — does the prediction-field frame survive on data I did NOT
construct? Two legs, both on real / computable data.

Leg A — invariance ⇒ transfer on a REAL dataset (sklearn diabetes).
  Environments = age quartiles (genuine subpopulations, not engineered). For each
  candidate predictor, measure (i) how stable its relationship to the target is
  across age groups (invariance) and (ii) how well it predicts a HELD-OUT age group
  (transfer, via leave-one-environment-out R²). Test: does invariance predict
  transfer on messy real data? (Escalates S18 from a constructed SCM to real data.)

Leg B — a NAMED cross-domain invariant transferring where its mechanism holds.
  Benford's law P(d)=log10(1+1/d) emerges in number sequences that span many orders
  of magnitude via multiplicative growth. Test it across genuinely different
  computable domains (2^n, 3^n, n!, Fibonacci — Benford by mechanism) vs controls
  that share the "first digit" surface but not the mechanism (uniform, narrow
  lognormal). A genuine invariant should transfer across the mechanism-sharing
  domains and fail on the controls.

Deterministic. Honest: Leg A is cross-ENVIRONMENT on one dataset (not cross-
scientific-domain); Leg B is cross-domain but within computable sequences. Both
escalate past synthetic; neither is the final curated-multi-domain study.
"""
import numpy as np, json, os, math
from sklearn.datasets import load_diabetes

OUT = os.path.dirname(os.path.abspath(__file__))


def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    rx = np.argsort(np.argsort(x)).astype(float); ry = np.argsort(np.argsort(y)).astype(float)
    rx -= rx.mean(); ry -= ry.mean()
    return float((rx @ ry) / (np.sqrt(rx @ rx) * np.sqrt(ry @ ry) + 1e-12))


# ======================================================================
# LEG A — real data: invariance across age groups predicts transfer?
# ======================================================================
d = load_diabetes()
X, y, names = d.data, d.target, list(d.feature_names)
age = X[:, 0]
qs = np.quantile(age, [0.25, 0.50, 0.75])
env = np.digitize(age, qs)                       # 0..3 age-quartile environments
cand = [j for j in range(X.shape[1]) if names[j] != "age"]   # exclude the env variable

def fit_slope(xj, yy):
    A = np.column_stack([np.ones_like(xj), xj])
    w, *_ = np.linalg.lstsq(A, yy, rcond=None)
    return w  # intercept, slope

legA = []
for j in cand:
    # slope of y~x_j within each environment → cross-env stability = invariance
    slopes = np.array([fit_slope(X[env == e, j], y[env == e])[1] for e in range(4)])
    instability = float(np.std(slopes) / (abs(np.mean(slopes)) + 1e-9))
    invariance = 1.0 / (1.0 + instability)
    # leave-one-environment-out transfer: fit on 3 envs, predict the 4th
    skills = []
    for te in range(4):
        tr = env != te
        w = fit_slope(X[tr, j], y[tr])
        pred = w[0] + w[1] * X[env == te, j]
        yt = y[env == te]
        skills.append(1.0 - np.mean((pred - yt) ** 2) / np.var(yt))
    legA.append((names[j], invariance, float(np.mean(skills))))

inv = [r[1] for r in legA]; tr = [r[2] for r in legA]
rhoA = spearman(inv, tr)
# does the invariant-selected feature beat the least-invariant on transfer?
best_inv = max(legA, key=lambda r: r[1])
worst_inv = min(legA, key=lambda r: r[1])

# ======================================================================
# LEG B — Benford across genuinely different computable domains
# ======================================================================
benford = np.array([math.log10(1 + 1 / dd) for dd in range(1, 10)])

def first_digits(nums):
    c = np.zeros(9)
    for x in nums:
        x = abs(int(x))
        if x == 0:
            continue
        c[int(str(x)[0]) - 1] += 1
    return c / c.sum()

def fib(n):
    a, b, out = 1, 1, []
    for _ in range(n):
        out.append(a); a, b = b, a + b
    return out

rng = np.random.default_rng(0)
domains = {
    "2^n":        [2 ** n for n in range(1, 3000)],
    "3^n":        [3 ** n for n in range(1, 3000)],
    "n!":         [math.factorial(n) for n in range(1, 1500)],
    "Fibonacci":  fib(3000),
    "uniform[100,999]": list(rng.integers(100, 1000, 6000)),   # control: ~flat digits
    "narrow lognormal": list((np.exp(rng.normal(6, 0.2, 6000))).astype(int)),  # control
}
benford_mech = {"2^n", "3^n", "n!", "Fibonacci"}
tv_ref = 0.5 * np.sum(np.abs(np.full(9, 1 / 9) - benford))   # uniform-digits vs Benford = scale
legB = {}
for name, nums in domains.items():
    p = first_digits(nums)
    tv = 0.5 * float(np.sum(np.abs(p - benford)))
    legB[name] = {"tv_to_benford": round(tv, 4),
                  "transfer_skill": round(max(0.0, 1 - tv / tv_ref), 3),
                  "first_digits": [round(v, 3) for v in p],
                  "benford_mechanism": name in benford_mech}

mech_skill = np.mean([legB[n]["transfer_skill"] for n in legB if legB[n]["benford_mechanism"]])
ctrl_skill = np.mean([legB[n]["transfer_skill"] for n in legB if not legB[n]["benford_mechanism"]])

# ======================================================================
verdict = {
    "legA_real_dataset": {
        "dataset": "sklearn diabetes (442 samples)",
        "environments": "age quartiles (4)",
        "spearman_invariance_vs_transfer": round(rhoA, 3),
        "most_invariant_feature": [best_inv[0], round(best_inv[1], 3), round(best_inv[2], 3)],
        "least_invariant_feature": [worst_inv[0], round(worst_inv[1], 3), round(worst_inv[2], 3)],
        "invariance_predicts_transfer": bool(rhoA > 0.3),
    },
    "legB_benford": {
        "mean_transfer_skill_mechanism_domains": round(float(mech_skill), 3),
        "mean_transfer_skill_control_domains": round(float(ctrl_skill), 3),
        "invariant_transfers_controls_dont": bool(mech_skill > 0.7 and ctrl_skill < 0.5),
        "per_domain": {k: {kk: legB[k][kk] for kk in ("tv_to_benford", "transfer_skill", "benford_mechanism")}
                       for k in legB},
    },
}
np.savez(os.path.join(OUT, "curves.npz"),
         invA=np.array(inv), trA=np.array(tr), namesA=np.array([r[0] for r in legA]),
         benford=benford, **{f"fd_{k}": np.array(legB[k]["first_digits"]) for k in legB})
with open(os.path.join(OUT, "verdict.json"), "w") as f:
    json.dump(verdict, f, indent=2)

print("=" * 66)
print("LEG A — real data (diabetes): does invariance predict transfer?")
print("=" * 66)
for nm, iv, t in sorted(legA, key=lambda r: -r[1]):
    print(f"  {nm:>4}   invariance={iv:.3f}   transfer R²={t:+.3f}")
print(f"  Spearman(invariance, transfer) = {rhoA:.3f}")
print(f"  most invariant: {best_inv[0]} (transfer {best_inv[2]:+.3f}) | "
      f"least: {worst_inv[0]} (transfer {worst_inv[2]:+.3f})")
print("=" * 66)
print("LEG B — Benford across computable domains")
print("=" * 66)
for k in legB:
    tag = "mechanism" if legB[k]["benford_mechanism"] else "CONTROL  "
    print(f"  [{tag}] {k:>18}   TV→Benford={legB[k]['tv_to_benford']:.3f}   "
          f"skill={legB[k]['transfer_skill']:.2f}")
print(f"  mechanism-domains skill={mech_skill:.2f}   controls skill={ctrl_skill:.2f}")
print("=" * 66)
print("VERDICT:", json.dumps({"legA_rho": round(rhoA, 3),
                              "legB_mech": round(float(mech_skill), 3),
                              "legB_ctrl": round(float(ctrl_skill), 3)}))
