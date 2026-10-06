# A4 — k Selection

Features: occasion_professional, occasion_family, occasion_intimate_adult, presentation_focus, implied_price, implied_diameter, implied_sweetness

|   k |   inertia |   silhouette |   smallest | sizes                |
|----:|----------:|-------------:|-----------:|:---------------------|
|   2 |     412.8 |       0.5768 |        116 | [116, 184]           |
|   3 |     254.6 |       0.5593 |         88 | [116, 96, 88]        |
|   4 |     195.1 |       0.571  |         28 | [116, 89, 28, 67]    |
|   5 |     167.4 |       0.5066 |         29 | [74, 89, 66, 29, 42] |

### Centroids, k=2

|   cluster |   occasion_professional |   occasion_family |   occasion_intimate_adult |   presentation_focus |   implied_price |   implied_diameter |   implied_sweetness |   n |
|----------:|------------------------:|------------------:|--------------------------:|---------------------:|----------------:|-------------------:|--------------------:|----:|
|         0 |                    0.95 |              0    |                     -0    |                 0.36 |           -1.04 |               0.99 |                1.16 | 116 |
|         1 |                    0.12 |              0.51 |                      0.28 |                 0.15 |            0.66 |              -0.63 |               -0.73 | 184 |

### Centroids, k=3

|   cluster |   occasion_professional |   occasion_family |   occasion_intimate_adult |   presentation_focus |   implied_price |   implied_diameter |   implied_sweetness |   n |
|----------:|------------------------:|------------------:|--------------------------:|---------------------:|----------------:|-------------------:|--------------------:|----:|
|         0 |                    0.95 |              0    |                     -0    |                 0.36 |           -1.04 |               0.99 |                1.16 | 116 |
|         1 |                    0.05 |              0.89 |                      0    |                 0.03 |            0.33 |              -0.09 |               -1.12 |  96 |
|         2 |                    0.2  |              0.1  |                      0.58 |                 0.27 |            1.02 |              -1.21 |               -0.3  |  88 |

### Centroids, k=4

|   cluster |   occasion_professional |   occasion_family |   occasion_intimate_adult |   presentation_focus |   implied_price |   implied_diameter |   implied_sweetness |   n |
|----------:|------------------------:|------------------:|--------------------------:|---------------------:|----------------:|-------------------:|--------------------:|----:|
|         0 |                    0.95 |              0    |                     -0    |                 0.36 |           -1.04 |               0.99 |                1.16 | 116 |
|         1 |                   -0    |              0.96 |                      0    |                -0    |            0.27 |              -0.16 |               -1.19 |  89 |
|         2 |                    0.82 |             -0    |                      0.11 |                 0.25 |            0.73 |              -0.11 |                0.03 |  28 |
|         3 |                   -0    |              0.13 |                      0.72 |                 0.3  |            1.14 |              -1.46 |               -0.44 |  67 |

### Centroids, k=5

|   cluster |   occasion_professional |   occasion_family |   occasion_intimate_adult |   presentation_focus |   implied_price |   implied_diameter |   implied_sweetness |   n |
|----------:|------------------------:|------------------:|--------------------------:|---------------------:|----------------:|-------------------:|--------------------:|----:|
|         0 |                    0.96 |              0    |                      0    |                -0    |           -0.98 |               1.01 |                1.15 |  74 |
|         1 |                   -0    |              0.96 |                      0    |                -0    |            0.27 |              -0.16 |               -1.19 |  89 |
|         2 |                   -0    |              0.14 |                      0.73 |                 0.3  |            1.14 |              -1.47 |               -0.43 |  66 |
|         3 |                    0.79 |             -0    |                      0.1  |                 0.24 |            0.76 |              -0.12 |                0    |  29 |
|         4 |                    0.93 |              0    |                      0    |                 1    |           -1.15 |               0.96 |                1.17 |  42 |

## Tie-break
- Best silhouette among remaining: 0.5768 (k=2)
- k=2: silhouette 0.5768, gap to best 0.0000 -> within 0.02
- k=3: silhouette 0.5593, gap to best 0.0175 -> within 0.02
- k=4: silhouette 0.5710, gap to best 0.0058 -> within 0.02
- k=5: silhouette 0.5066, gap to best 0.0702 -> not within 0.02

**Shortlist (tied within 0.02): k = 2, 3, 4**

## Product check (validation only)

### k=2

|   cluster |   Apple |   Mocha |   Banana |   Bo |   Brownie |   Carrot |   Caramel |   Vanilla |
|----------:|------:|-------:|-------:|-----:|------:|------:|----------:|-------:|
|         0 |     0 |      0 |      0 |   68 |     0 |     0 |        48 |      0 |
|         1 |    21 |     27 |     33 |    0 |    32 |    37 |         0 |     34 |
- **Flag:** cluster 0: 100% from Bo, Caramel (likely product split)

### k=3

|   cluster |   Apple |   Mocha |   Banana |   Bo |   Brownie |   Carrot |   Caramel |   Vanilla |
|----------:|------:|-------:|-------:|-----:|------:|------:|----------:|-------:|
|         0 |     0 |      0 |      0 |   68 |     0 |     0 |        48 |      0 |
|         1 |     8 |     21 |     33 |    0 |     0 |     0 |         0 |     34 |
|         2 |    13 |      6 |      0 |    0 |    32 |    37 |         0 |      0 |
- **Flag:** cluster 0: 100% from Bo, Caramel (likely product split)

### k=4

|   cluster |   Apple |   Mocha |   Banana |   Bo |   Brownie |   Carrot |   Caramel |   Vanilla |
|----------:|------:|-------:|-------:|-----:|------:|------:|----------:|-------:|
|         0 |     0 |      0 |      0 |   68 |     0 |     0 |        48 |      0 |
|         1 |     8 |     14 |     33 |    0 |     0 |     0 |         0 |     34 |
|         2 |     0 |     11 |      0 |    0 |     0 |    17 |         0 |      0 |
|         3 |    13 |      2 |      0 |    0 |    32 |    20 |         0 |      0 |
- **Flag:** cluster 0: 100% from Bo, Caramel (likely product split)
- **Flag:** cluster 2: 100% from Carrot, Mocha (likely product split)
- **Flag:** clusters 0 & 2 similar on situation (max diff 0.13) but differ on implied/reaction (max diff 1.77)

### k=5

|   cluster |   Apple |   Mocha |   Banana |   Bo |   Brownie |   Carrot |   Caramel |   Vanilla |
|----------:|------:|-------:|-------:|-----:|------:|------:|----------:|-------:|
|         0 |     0 |      0 |      0 |   41 |     0 |     0 |        33 |      0 |
|         1 |     8 |     14 |     33 |    0 |     0 |     0 |         0 |     34 |
|         2 |    12 |      2 |      0 |    0 |    32 |    20 |         0 |      0 |
|         3 |     1 |     11 |      0 |    0 |     0 |    17 |         0 |      0 |
|         4 |     0 |      0 |      0 |   27 |     0 |     0 |        15 |      0 |
- **Flag:** cluster 0: 100% from Bo, Caramel (likely product split)
- **Flag:** cluster 3: 97% from Carrot, Mocha (likely product split)
- **Flag:** cluster 4: 100% from Bo, Caramel (likely product split)
- **Flag:** clusters 0 & 3 similar on situation (max diff 0.24) but differ on implied/reaction (max diff 1.73)

## Stability (seeds 0–4 vs seed 42)
- k=2, seed 0: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=2, seed 1: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=2, seed 2: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=2, seed 3: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=2, seed 4: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=3, seed 0: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=3, seed 1: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=3, seed 2: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=3, seed 3: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=3, seed 4: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=4, seed 0: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=4, seed 1: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=4, seed 2: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=4, seed 3: ARI 1.000; mean share of a review's original co-members still with it 1.000
- k=4, seed 4: ARI 1.000; mean share of a review's original co-members still with it 1.000

## What the clusters differ on (dimensions only)
- **k=2:** `occasion_professional`, high implied diameter and sweetness, and low implied price, versus everyone else.
- **k=3:** each cluster is dominated by one occasion indicator. They also separate on implied sweetness (cluster 1 lowest) and implied diameter (cluster 2 smallest).
- **k=4:** splits off 28 professional reviews with neutral implied sweetness and diameter. All 28 are Carrot or Mocha buyers.
- **k=5:** further splits the main professional cluster purely on `presentation_focus`.

## Decision brief (shortlist: 2, 3, 4)
| k | What you'd tell the business | Interpretability | Usefulness | Main risk |
|---|---|---|---|---|
| 2 | Professional buyers vs. everyone else. | Cluster 0 is explained by occasion, but it is also 100% Bo and Caramel. | Low: family and small adult occasions are lumped together. | Two different needs merged. |
| 3 | One cluster per occasion: professional, family, small adult. | Every cluster is explained by its own situation indicator. | High: three distinct offers or messages. | Cluster 0 is still 100% Bo and Caramel. |
| 4 | k=3 plus a professional sub-group with neutral implied ideals. | The new cluster is 100% Carrot and Mocha and matches cluster 0 on situation. | Same treatment as cluster 0. | Product split (flagged). |

## Default selection
**k = 3.** Silhouette counts as tied across the shortlist, so this choice rests on interpretability and usefulness.
1. Every cluster maps to one occasion (centroids 0.95 / 0.89 / 0.58), not just to a product position.
2. The three occasions imply three different treatments, and each cluster has a different implied sweetness and size ideal.
3. The smallest cluster is 29% of reviews, and assignments are identical across 5 seeds.

**Strongest argument against.** Cluster 0 is 100% Bo and Caramel, so its boundary may reflect which products professional buyers chose rather than a need. Professional buyers of other products scatter into clusters 1 and 2 (see A5). The suspected inverted Price axis (A3b) could be part of the cause.

**Other shortlisted options**
- **k=2:** prefer it if family and small adult occasions would get the same treatment.
- **k=4:** prefer it only if Carrot and Mocha professional buyers need a separate playbook. It is flagged as a product split.

Stability is perfect for all shortlisted k (ARI 1.0). That shows the clusters are reproducible, not that they are real.

Selected k: 3
