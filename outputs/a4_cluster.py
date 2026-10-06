"""A4 — k-means over review_features.csv for k=2..5, rule-based k choice, product & stability checks."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

feat = pd.read_csv("outputs/review_features.csv")
X = feat.drop(columns=["review_id"] + [c for c in feat if c.startswith("raw_")])
cols = list(X.columns)
situation = [d["name"] for d in json.load(open("outputs/taxonomy.json"))["dimensions"] if d["type"] == "situation"]
N = len(X)
out = []
P = lambda s="": (out.append(s), print(s))

res, models = [], {}
for k in range(2, 6):
    km = KMeans(k, random_state=42, n_init=20).fit(X)
    models[k] = km
    sizes = np.bincount(km.labels_)
    res.append(dict(k=k, inertia=round(km.inertia_, 1), silhouette=round(silhouette_score(X, km.labels_), 4),
                    smallest=int(sizes.min()), sizes=sizes.tolist()))
res = pd.DataFrame(res)
P("# A4 — k Selection\n\nFeatures: " + ", ".join(cols) + "\n")
P(res.to_markdown(index=False))
for k, km in models.items():
    cen = pd.DataFrame(km.cluster_centers_, columns=cols).round(2)
    cen.index.name = "cluster"
    cen["n"] = np.bincount(km.labels_)
    P(f"\n### Centroids, k={k}\n\n" + cen.to_markdown())
    small = [c for c, n in enumerate(cen["n"]) if n < 0.05 * N]
    if small:
        P(f"\n**Flag:** clusters {small} are smaller than 5% of reviews.")

plt.plot(res.k, res.inertia, "o-"); plt.xlabel("k"); plt.ylabel("inertia"); plt.title("Elbow")
plt.savefig("outputs/elbow.png", dpi=120, bbox_inches="tight")

P("\n## Tie-break")
ok = res[res.smallest >= 0.05 * N]
for _, r in res.iterrows():
    if r.smallest < 0.05 * N:
        P(f"- k={r.k}: dropped (smallest cluster {r.smallest} < {0.05*N:.0f})")
best = ok.silhouette.max()
P(f"- Best silhouette among remaining: {best:.4f} (k={int(ok.loc[ok.silhouette.idxmax(), 'k'])})")
for _, r in ok.sort_values("k").iterrows():
    P(f"- k={r.k}: silhouette {r.silhouette:.4f}, gap to best {best - r.silhouette:.4f} -> "
      + ("within 0.02" if best - r.silhouette <= 0.02 else "not within 0.02"))
SHORT = sorted(int(k) for k in ok[best - ok.silhouette <= 0.02].k)
P(f"\n**Shortlist (tied within 0.02): k = {', '.join(map(str, SHORT))}**"
  + (" (single candidate; default)" if len(SHORT) == 1 else ""))

prod = pd.read_csv("data/product-reviews-sample.csv")[["review_id", "product"]]
P("\n## Product check (validation only)")
for k in SHORT + [max(SHORT) + 1]:
    if k not in models: continue
    lab = pd.Series(models[k].labels_, name="cluster")
    xt = pd.crosstab(lab, feat[["review_id"]].merge(prod)["product"])
    P(f"\n### k={k}\n\n" + xt.to_markdown())
    for c, row in xt.iterrows():
        share = row.nlargest(2).sum() / row.sum()
        if share >= 0.8:
            P(f"- **Flag:** cluster {c}: {share:.0%} from {', '.join(row.nlargest(2).index)} (likely product split)")
    cen = pd.DataFrame(models[k].cluster_centers_, columns=cols)
    other = [c for c in cols if c not in situation]
    for i in range(k):
        for j in range(i + 1, k):
            ds = np.abs(cen.loc[i, situation] - cen.loc[j, situation]).max()
            do = np.abs(cen.loc[i, other] - cen.loc[j, other]).max()
            if ds < 0.25 and do > 0.5:
                P(f"- **Flag:** clusters {i} & {j} similar on situation (max diff {ds:.2f}) but differ on implied/reaction (max diff {do:.2f})")

P("\n## Stability (seeds 0–4 vs seed 42)")
for K in SHORT:
    base = models[K].labels_
    same = (base[:, None] == base[None, :])
    for s in range(5):
        lab = KMeans(K, random_state=s, n_init=20).fit(X).labels_
        co = (lab[:, None] == lab[None, :])
        keep = (same & co).sum(1) / same.sum(1)
        P(f"- k={K}, seed {s}: ARI {adjusted_rand_score(base, lab):.3f}; mean share of a review's original co-members still with it {keep.mean():.3f}")
open("outputs/a4_results.md", "w").write("\n".join(out) + "\n")
