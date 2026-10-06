# Step 3 — Score the Reviews

## Context
Clustering needs numbers, but our data is free text. In this step we turn each review into a row of scores, one per need dimension in our taxonomy. This is the most judgment-heavy step in the whole process. Every score is an interpretation of what a customer wrote, so we keep the evidence for each one and check how consistent the scoring is.

## Input
- `data/product-reviews-sample.csv`
- `outputs/taxonomy.json` (human-edited after A2)

## Task
1. For each of the 300 reviews, read `review_text` and give one score per dimension using the taxonomy's scale.
   - Record a short evidence quote for every non-zero score.
   - Score 0 when a review says nothing about a dimension.
   - If a review is unclear (mixed signals, sarcasm, negation like "not too sweet"), score your best reading and add a short note.
2. Work in batches of 25 and save after each batch.
3. **Consistency check:** pick 30 reviews at random (seed 42), score them again from scratch *without* looking at your first scores, and compare the two runs.
4. Summarize the scores:
   - Per dimension: count of −1 / 0 / +1
   - Dimensions that are non-zero in fewer than 10% of reviews
   - Reviews with all-zero scores (they will be hard to cluster)

## Output
- `outputs/review_scores.csv` — `review_id`, one column per dimension, `evidence` (quotes joined by " | "), `notes`
- `outputs/a3_scoring_report.md`, containing:
  - The score distribution table
  - Consistency check: % agreement per dimension between the two runs, and the 5 reviews that changed most, with text
  - The all-zero reviews
  - The 10 hardest reviews to score, with one line each on why
  - A short **Scoring risks** section (≤100 words) on where this scoring is most likely to be wrong

## Guardrails
- Score from `review_text` only. Do not use `product`, `company`, or `stars`.
- Score what the customer *says*, not what you think they'd want.
- Don't add, remove, or rename dimensions. If the taxonomy doesn't fit a review, note it.
- Note that this scoring is LLM judgment and may differ between runs. The consistency check measures how much.

---

### Human checkpoint (not part of the prompt)
**Pause here for discussion before clustering.**
- Spot-check 10 rows by hand. Do the scores match the evidence quotes? Where would you have scored differently?
- Does "0" mean "doesn't care" or "didn't mention"? k-means treats them the same. Is that acceptable?
- Which dimensions had low consistency? Rewrite their definitions or markers in `taxonomy.json` and rescore before moving on.
- A dimension that is almost always 0 adds little to the clustering. Keep it, merge it, or drop it?
- Everything downstream depends on these numbers. If the scores are wrong, k-means will still find clusters, but you wont be able to determine what they represent.
