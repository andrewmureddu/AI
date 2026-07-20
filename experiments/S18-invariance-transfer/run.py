"""
S18 / prediction-field falsifier — does invariance-across-environments predict
transfer to an unseen environment?

The prediction-field frame claims an invariant's "level" (how measurement/
environment-invariant its prediction is) should predict how well it transfers.
S18 sharpens this to the causal-inference statement: the relationship that stays
invariant across environments is the one that transfers (Peters' ICP; Arjovsky's
IRM). We test it in a controlled linear structural causal model.

SCM (per environment e):
    X_c ~ N(0,1)                      # a genuine cause of Y
    Y   = a·X_c + ε_y,  ε_y~N(0,σy²)  # INVARIANT mechanism: coefficient a fixed
    X_s = b_e·Y + ε_s,  ε_s~N(0,σs²)  # X_s is an EFFECT of Y; coupling b_e VARIES

So X_c→Y is invariant; X_s is a spurious correlate whose usefulness depends on b_e.
X_s is *more* predictive in-distribution (σs small) — so naive ERM leans on it —
but its optimal coefficient changes with the environment, so it fails to transfer.

Honest core (why this isn't a tautology): invariance is measured on TRAINING
environments only; transfer error is measured on a HELD-OUT test environment with a
b outside the training range (sign-flipped). Disjoint data → a real relationship.

Pure numpy, deterministic.
"""
import numpy as np, json, os

OUT = os.path.dirname(os.path.abspath(__file__))
rng = np.random.default_rng(7)

a, SY, SS = 1.0, 1.0, 0.30
B_TRAIN = [0.8, 1.0, 1.2, 1.5]     # training environments (all positive)
B_TEST = -1.2                       # unseen env: spurious coupling flips sign
N = 4000


def gen(b, n, r):
    Xc = r.normal(size=n)
    Y = a * Xc + r.normal(0, SY, n)
    Xs = b * Y + r.normal(0, SS, n)
    return Xc, Xs, Y


# ---- build training pool + per-env sets, z-score features on training stats ----
train = [gen(b, N, rng) for b in B_TRAIN]
Xc_all = np.concatenate([e[0] for e in train])
Xs_all = np.concatenate([e[1] for e in train])
mc, sc = Xc_all.mean(), Xc_all.std()
ms, ss = Xs_all.mean(), Xs_all.std()
z = lambda Xc, Xs: (((Xc - mc) / sc), ((Xs - ms) / ss))

Xc_te, Xs_te, Y_te = gen(B_TEST, N, np.random.default_rng(99))
Xc_te_z, Xs_te_z = z(Xc_te, Xs_te)


def ols(feat, y):
    """least squares with intercept; returns (intercept, slopes...)."""
    A = np.column_stack([np.ones_like(y)] + [f for f in feat])
    w, *_ = np.linalg.lstsq(A, y, rcond=None)
    return w


def mse(feat, y, w):
    A = np.column_stack([np.ones_like(y)] + [f for f in feat])
    return float(np.mean((A @ w - y) ** 2))


# ---- sweep a predictor family: Z(alpha) = (1-alpha)*X_c_z + alpha*X_s_z ----
alphas = np.linspace(0, 1, 41)
in_mse, tr_mse, coef_instab = [], [], []
for al in alphas:
    # per-env fitted slope of Y on Z(alpha) -> invariance = stability across envs
    slopes = []
    pooledZ, pooledY = [], []
    for (Xc, Xs, Y) in train:
        Xcz, Xsz = z(Xc, Xs)
        Z = (1 - al) * Xcz + al * Xsz
        w = ols([Z], Y)
        slopes.append(w[1])
        pooledZ.append(Z); pooledY.append(Y)
    slopes = np.array(slopes)
    # instability = std of slope across training envs, normalised (never sees test)
    coef_instab.append(float(slopes.std() / (abs(slopes.mean()) + 1e-9)))
    # transfer predictor = fit on pooled training, eval on held-out test env
    Zp = np.concatenate(pooledZ); Yp = np.concatenate(pooledY)
    w = ols([Zp], Yp)
    in_mse.append(mse([Zp], Yp, w))
    Zte = (1 - al) * Xc_te_z + al * Xs_te_z
    tr_mse.append(mse([Zte], Y_te, w))

alphas = np.array(alphas); in_mse = np.array(in_mse)
tr_mse = np.array(tr_mse); coef_instab = np.array(coef_instab)


def spearman(x, y):
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y))
    rx = rx - rx.mean(); ry = ry - ry.mean()
    return float((rx @ ry) / (np.sqrt(rx @ rx) * np.sqrt(ry @ ry)))

rho = spearman(coef_instab, tr_mse)   # invariance (instability) vs transfer error


# ---- explicit ERM vs invariant-only vs ICP-selected ----
def pooled_fit_eval(use_c, use_s):
    feats, tefeats = [], []
    for (Xc, Xs, Y) in train:
        Xcz, Xsz = z(Xc, Xs)
    Zc = np.concatenate([z(e[0], e[1])[0] for e in train])
    Zs = np.concatenate([z(e[0], e[1])[1] for e in train])
    Yp = np.concatenate([e[2] for e in train])
    cols = ([Zc] if use_c else []) + ([Zs] if use_s else [])
    tecols = ([Xc_te_z] if use_c else []) + ([Xs_te_z] if use_s else [])
    w = ols(cols, Yp)
    return mse(cols, Yp, w), mse(tecols, Y_te, w)

erm_in, erm_tr = pooled_fit_eval(True, True)      # both features
inv_in, inv_tr = pooled_fit_eval(True, False)     # causal only (invariant)
spu_in, spu_tr = pooled_fit_eval(False, True)     # spurious only

# ICP-style selection: pick the single feature whose per-env slope is most stable
def slope_std_single(idx):
    sl = []
    for (Xc, Xs, Y) in train:
        Xcz, Xsz = z(Xc, Xs)
        f = Xcz if idx == 0 else Xsz
        sl.append(ols([f], Y)[1])
    return np.std(sl) / (abs(np.mean(sl)) + 1e-9)
icp_pick = "X_c (causal)" if slope_std_single(0) < slope_std_single(1) else "X_s (spurious)"

verdict = {
    "spearman_instability_vs_transfer": round(rho, 3),
    "in_dist_MSE_spurious_only": round(spu_in, 3),
    "in_dist_MSE_causal_only": round(inv_in, 3),
    "transfer_MSE_spurious_only": round(spu_tr, 3),
    "transfer_MSE_causal_only": round(inv_tr, 3),
    "transfer_MSE_ERM_both": round(erm_tr, 3),
    "spurious_beats_causal_in_distribution": bool(spu_in < inv_in),
    "causal_beats_spurious_on_transfer": bool(inv_tr < spu_tr),
    "invariance_predicts_transfer_monotone": bool(rho > 0.8),
    "ICP_selection_picks": icp_pick,
}

np.savetxt(os.path.join(OUT, "sweep.csv"),
           np.column_stack([alphas, in_mse, tr_mse, coef_instab]), delimiter=",",
           header="alpha_causal_to_spurious,in_dist_mse,transfer_mse,coef_instability",
           comments="")
with open(os.path.join(OUT, "verdict.json"), "w") as f:
    json.dump(verdict, f, indent=2)

print("S18 — invariance vs transfer")
print("-" * 60)
print(f"in-distribution MSE:  spurious-only {spu_in:.3f}  <  causal-only {inv_in:.3f}"
      f"   → ERM prefers the spurious feature")
print(f"transfer MSE:         causal-only {inv_tr:.3f}    <  spurious-only {spu_tr:.3f}"
      f"   → only the invariant feature transfers")
print(f"ERM (both) transfer MSE: {erm_tr:.3f}   (dragged down by leaning on X_s)")
print(f"ICP stability-selection picks: {icp_pick}")
print(f"Spearman(coef-instability_train , transfer-MSE_test) = {rho:.3f}")
print("-" * 60)
print("VERDICT:", json.dumps(verdict))
