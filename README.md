# LLM Powered Segmentation Workshop

## Workflow Overview
This workshop builds a needs-based segmentation from free-text product reviews by running five prompts in order (`prompts/step1-profile.md` → `step5-assign.md`). Each prompt reads the previous step's output, does one job, and stops at a human checkpoint before the next step runs — nothing downstream should happen until a person has reviewed the artifact. Every prompt writes its outputs to `outputs/`, so that directory is the running record of the pipeline's state. A rerunnable `.py` script is saved alongside the written artifacts for steps that do scripted computation.

| Order | Prompt | Purpose | Key outputs |
|---|---|---|---|
| 1 | `step1-profile.md` | Profiles the raw CSV: shape, column roles (segmentation input / validator / identifier), text stats, and distributions. Produces no segments — just an honest read of what's in the data. | `a1_data_profile.md`, `a1_profile.py` |
| 2 | `step2-identify-needs.md` | Reads a 40-review pilot (text only) to draft a **needs taxonomy** — 3–7 dimensions describing customer situations or reactions, each with a scale, markers, and example IDs. Candidates are recounted across all 300 reviews before being kept or rejected. **Requires human edits to `taxonomy.json` before Step 3.** | `taxonomy.json`, `a2_taxonomy_notes.md` |
| 3 | `step3-score-reviews.md` | Scores all 300 reviews against the human-approved taxonomy, one value per dimension, with an evidence quote for each non-zero score. Includes a consistency check (30 reviews re-scored blind) to quantify how repeatable the scoring is. | `review_scores.csv`, `a3_scoring_report.md` |
| 3b | `step3b-anchor.md` *(optional)* | Converts reaction dimensions (e.g., "too sweet") into standardized **implied ideals** on the product brief's scale, so the same need lands near the same value regardless of which product the customer bought. | `review_features.csv`, `a3b_anchor.py`, `a3b_anchoring_report.md` |
| 4 | `step4-clustering.md` | Runs k-means for k = 2–5 on the feature matrix, reports inertia/silhouette/stability per k, shortlists statistically-tied candidates, and writes a decision brief recommending a default k (`Selected k: <k>`). Does not name or interpret segments beyond their scored dimensions. | `a4_cluster.py`, `elbow.png`, `a4_k_selection.md` |
| 5 | `step5-assign.md` | Finalizes cluster assignments using the chosen k (default from Step 4, or a manual override), scores each review's assignment confidence via centroid margin, and names each segment from its centroid and representative quotes. **Chain A ends here** — `assignments.csv` should be frozen before any further analysis. | `assignments.csv`, `a5_assignment_notes.md` |

### Running order and checkpoints
1. Run Step 1 on `data/product-reviews-sample.csv`.
2. Run Step 2, then **pause**: review and hand-edit `outputs/taxonomy.json` — this is where domain expertise should override the drafted dimensions.
3. Run Step 3, then **pause**: spot-check scores against evidence quotes and review the consistency check before clustering.
4. (Optional) Run Step 3b if reactions should be anchored to product attributes rather than scored as-is.
5. Run Step 4, then **pause**: decide whether to accept the recommended default k or override it.
6. Run Step 5 to produce the final, named segment assignments.

## Product Attributes
| Attribute | Range | Notes |
|---|---|---|
| Sweetness | 0-100 | Lower = less sweet, higer = sweeter |
| Diameter | 6" - 12" | Size of the cake |
| Price | 0-1000 |  |

## CSV Review Input Schema

| Column | Type | Notes |
|---|---|---|
| `review_id` | int | 1–300 |
| `product` | str | AppleCrumble, CoffeeCrumble, BananaBliss, ChocolateBliss, VanillaBeanBliss, ChocoSheetcake, MochaSheetcake, VanillaSheetcake |
| `company` | str | Crumbly-confections, Blissful-buttercreamery, Sinful-sheetcakes |
| `stars` | int | 1–5 |
| `review_text` | str | free-text product review |

