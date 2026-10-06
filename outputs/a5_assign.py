"""A5 — final k-means, margins, terciles, boundary cases.
Usage: python3 outputs/a5_assign.py [K]  (K overrides the `Selected k:` line in a4_k_selection.md)"""
import re
import sys
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

if len(sys.argv) > 1:
    K, SOURCE = int(sys.argv[1]), "override"
else:
    K = int(re.search(r"^Selected k: (\d+)", open("outputs/a4_k_selection.md").read(), re.M).group(1))
    SOURCE = "A4 default"
print(f"k used: {K} (source: {SOURCE})")
feat = pd.read_csv("outputs/review_features.csv")
X = feat.drop(columns=["review_id"] + [c for c in feat if c.startswith("raw_")])
km = KMeans(K, random_state=42, n_init=20).fit(X)
D = km.transform(X)
order = np.argsort(D, axis=1)
d1 = D[np.arange(len(X)), order[:, 0]]; d2 = D[np.arange(len(X)), order[:, 1]]
a = pd.DataFrame({"review_id": feat.review_id, "segment_id": km.labels_, "second": order[:, 1],
                  "margin": (d2 - d1) / d2, "d1": d1})
lo, hi = a.margin.quantile([1/3, 2/3])
a["confidence"] = np.where(a.margin >= hi, "High", np.where(a.margin >= lo, "Medium", "Low"))
print(f"Tercile cutoffs: Low < {lo:.3f} <= Medium < {hi:.3f} <= High")
text = pd.read_csv("data/product-reviews-sample.csv")[["review_id", "review_text"]]
a = a.merge(text)
print(a.segment_id.value_counts().sort_index().to_string())
print(pd.crosstab(a.segment_id, a.confidence).to_string())
print("\nCentroids:\n", pd.DataFrame(km.cluster_centers_, columns=X.columns).round(2).to_string())
for s in range(K):
    print(f"\n== Segment {s} representative reviews")
    for _, r in a[a.segment_id == s].nsmallest(3, "d1").iterrows():
        print(f"[{r.review_id}] {r.review_text}")
print("\n== 10 lowest margin")
for _, r in a.nsmallest(10, "margin").iterrows():
    print(f"[{r.review_id}] {r.segment_id}<->{r.second} m={r.margin:.3f} {r.review_text}")
low = a[a.confidence == "Low"]
pair = low.apply(lambda r: tuple(sorted((r.segment_id, r.second))), axis=1).value_counts()
print("\nLow-confidence pairs:\n", pair.to_string(), f"\nTop pair share of all reviews: {pair.iloc[0]/len(a):.1%}")
a.to_csv("outputs/_a5_work.csv", index=False)
