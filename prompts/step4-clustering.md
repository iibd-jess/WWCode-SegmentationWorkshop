# Step 4 — Cluster with k-means

## Context
Each review is now a row of numbers: situation scores plus implied ideals from A3b. k-means places *k* centers in that score space and assigns each review to the nearest one. It always returns *k* groups, even without real structure, so we compare several values of *k*.

## Input
- `outputs/review_features.csv` (from A3b)
- `data/product-reviews-sample.csv` (only for the post-clustering product check in step 6)

## Task
Write and run a Python script (scikit-learn) that:
1. Loads the feature matrix (rows = reviews, columns = features). Ignore the `raw_` columns.
2. Runs k-means for k = 2, 3, 4, 5, with `random_state=42` and `n_init=20`.
3. For each k, reports:
   - Inertia (within-cluster sum of squares)
   - Silhouette score (−1 to 1; higher means clusters are better separated)
   - Cluster sizes
   - The centroid table (mean score per dimension per cluster)
4. Plots inertia vs. k (elbow chart) and saves it as a PNG.
5. **Shortlists candidate k values in code**. The shortlist narrows the options; the default k is chosen afterward on interpretability and usefulness:
   - Drop any k with a cluster smaller than 5% of reviews.
   - Find the highest silhouette among the rest. Every k within 0.02 of it goes on the **shortlist**. Treat these as statistically tied: small silhouette gaps are not evidence that one k is better.
   - Print each comparison so the reader can see why each k was kept or dropped.
   - If only one k is on the shortlist, say so and use it as the default.
6. **Product check (validation only):** join `product` by `review_id` and print a cluster × product cross-tab for every shortlisted k, plus the next k above the largest one on the shortlist (if it was run). Flag any cluster where ≥80% of its reviews come from 1–2 products, and any pair of clusters with similar centroids on `situation` dimensions that differ mainly on implied-ideal or reaction features. These are likely *product splits*, not need differences. Report it; don't change k because of it.
7. **Stability check:** for each shortlisted k, rerun with 5 different random seeds and report how often each review lands with the same reviews it was grouped with in the first run.

## Output
- `outputs/a4_cluster.py`
- `outputs/elbow.png`
- `outputs/a4_k_selection.md`, containing:
  - A table: k, inertia, silhouette, smallest cluster size
  - The centroid table for each k
  - For each k, one sentence on what the clusters differ on (dimensions only, no names)
  - The shortlist comparisons from step 5
  - The product cross-tabs and flags from step 6
  - Stability results
  - A **decision brief** for the shortlisted k values. For each k, write:
    - **What you'd tell the business:** describe the clusters in one plain sentence each, using dimension values only (no names yet).
    - **Interpretability:** can every cluster be explained by its *situation* dimensions? Or does a cluster only make sense as "the people who bought X"?
    - **Usefulness:** what could a team do differently for each cluster? Flag any cluster that would get the same treatment as another.
    - **Main risk:** e.g., a product split, a cluster held together only by implied-ideal features, or two needs merged together.
  - A **Default selection** section:
    - Choose the shortlisted k that is the most interpretable and useful. Prefer clusters explained by situation dimensions over product splits.
    - Give 2–3 reasons and the strongest argument *against* the choice.
    - **Flag each other shortlisted k** with one line on when a human should prefer it instead.
    - Last line, exactly: `Selected k: <k>`. A5 reads this line.

  Write everything after seeing the results. Don't use template text. Inertia always decreases with k, so on its own it never argues for more segments.

## Guardrails
- Cluster on `review_features.csv` only. Use `product` only in the step 6 cross-tab. Never use `company` or `stars`.
- Do not name the clusters. Refer to them as Cluster 0, 1, 2…
- Flag any cluster smaller than 5% of reviews.
- Choose the default only from the shortlist. Silhouette rank is not a reason on its own, because shortlisted values count as tied.
- This step is deterministic given the scores and seed. Any uncertainty comes from A3 (scoring) and A3b (`STEP`, mappings).

---

### Human checkpoint (not part of the prompt)
- **The default k is a starting point. You can override it in A5.** Ask: would a business treat these groups differently?
- **The sign-flip trap.** Two clusters that match on situation (same occasion, same audience) but have opposite *reactions* ("too sweet" vs. "not sweet enough") are usually the same need landing on different products. Look at the step 6 cross-tab. If one cluster is mostly one or two products, merge it in your head and see whether a smaller k tells the story better.
- Silhouette rewards tight groups, and a product split is often very tight. A high silhouette at a larger k doesn't mean the extra cluster is a real need.
- Compare with a run on raw A3 scores (no anchoring). How do the recommended k and the product cross-tab change?
- Teaching moment: the centroids are just column averages. Have students verify one by hand.
