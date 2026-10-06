# A5 — Assign Segments and Score Confidence

## Context
We have picked a number of clusters (k). Now we finalize which segment each review belongs to, measure how confident each assignment is, and only then give the segments names.

## Input
- `outputs/review_features.csv`
- `outputs/a4_cluster.py`
- **k override:** `___`. Leave this blank to use the default.
  - **If blank:** use the `Selected k: <k>` line in `outputs/a4_k_selection.md`.
  - **If filled in:** use that value instead.
  - State which k you used and where it came from (override or A4 default) at the top of the notes.

## Task
1. Rerun k-means with the chosen k (`random_state=42`, `n_init=20`).
2. For each review, compute:
   - `d1` = distance to its nearest centroid
   - `d2` = distance to its second-nearest centroid
   - `margin` = `(d2 - d1) / d2` (0 = on the boundary, near 1 = clearly in one cluster)
3. Assign confidence from margin terciles: top third = High, middle = Medium, bottom = Low. Report the cutoff values.
4. List the 10 lowest-margin reviews with their text and the two clusters they fall between.
5. **Name each segment** using only its centroid and 3 representative quotes (the reviews closest to the centroid). Each name should describe a need or situation in 2–4 words.

## Output
- `outputs/assignments.csv` — `review_id`, `segment_id`, `segment_name`, `margin`, `confidence`
- `outputs/a5_assignment_notes.md`, containing:
  - Segment sizes (count and %)
  - Confidence breakdown by segment
  - For each segment: name, centroid summary in one sentence, 3 quotes with review IDs
  - The boundary-case table from step 4
  - Which pair of segments is most often confused, and why that might be

## Guardrails
- Names must come from needs, not products. "Small-Occasion Buyers" is fine; "Carrot Lovers" is not.
- Do not use `product`, `company`, or `stars` in assignment or naming.
- Treat tercile confidence as a relative ranking, not a probability. Say so in the notes.
- If more than 25% of reviews are Low confidence *and* sit between the same two segments, flag that k may be wrong.

---

### Human checkpoint (not part of the prompt)
- Read the boundary cases. Are they truly mixed (e.g., a family party at the office), or is the taxonomy missing a dimension?
- Do the names make claims the centroids can't support (e.g., "budget-conscious" when value scores barely differ)?
- **Chain A ends here.** Freeze `assignments.csv` before opening anything in Chain B.
