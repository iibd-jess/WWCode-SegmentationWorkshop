# Step 2 — Draft a Needs Taxonomy

## Context
We are building a needs-based segmentation from review text. A **taxonomy** is the list of need dimensions we will score every review on. Good dimensions describe the *customer's situation or goal* (who it's for, what must go right), not product features or satisfaction.

There are two kinds of signal in a review:
- **Situation / preference** — who it was for, the occasion, what the customer says they want. This stays the same whatever product they bought.
- **Reaction** — "too sweet," "overpriced," "lots of leftovers." A reaction is the *gap* between the customer's need and the product they happened to buy. Two customers with the same need who bought different products can give opposite reactions to the same underlying need.

## Input
- `data/product-reviews-sample.csv`
- `outputs/a1_data_profile.md` (column roles from step A1)

## Task
1. Take a **pilot sample**: the first 40 rows (the file is already shuffled). Read only `review_text`.
2. Find recurring need dimensions. For each, define:
   - `name` — short, needs-based (e.g., `group_size`, not `big_cake`)
   - `type` — `situation` or `reaction` (see Context)
   - `definition` — one sentence
   - `scale` — use `-1 / 0 / +1` for a single directional axis, and say what each value means (e.g., group size: `-1` = small group, `0` = not mentioned, `+1` = large crowd)
   - `markers` — 3–6 phrases from the text that signal each non-zero value
   - `example_ids` — 2–3 review IDs that show it
3. **Don't force unrelated categories onto one axis.** If a situation has three or more distinct kinds (e.g., several occasion types), don't put two of them together at one end of a `-1 / +1` scale. Split them into separate `0 / 1` indicator dimensions (`scale` uses only `"0"` and `"1"`), or use fewer, clearly ordered levels.
4. Use **as few dimensions as the text supports** (typically 3–7).
   - Find candidates in the pilot, then **recount every candidate on all 300 reviews** (text only) before deciding. A dimension earns its place if it is non-zero in at least ~10% of the full set. A 40-review pilot is too small to rule out a signal that only appears for part of the customer base.
   - Before dropping a candidate as "universal," check that it really appears across the board. A signal that shows up in some kinds of review and is absent from others can separate groups even if it is never negative.
   - List rejected candidates under "Candidates — not included" with pilot and full-set counts.
   - Include at least one `situation` dimension. Don't build the taxonomy only from reactions.
5. For each `reaction` dimension, say in one line which product attribute could be driving it.

## Output
Save `outputs/taxonomy.json` with this shape:
```json
{
  "dimensions": [
    {
      "name": "",
      "type": "situation | reaction",
      "definition": "",
      "scale": {"-1": "", "0": "", "1": ""},
      "markers": {"-1": [], "1": []},
      "example_ids": []
    }
  ]
}
```
For `0 / 1` indicator dimensions, use `"scale": {"0": "", "1": ""}` and `"markers": {"1": []}`.

Also save `outputs/a2_taxonomy_notes.md` (half a page max) covering: dimensions considered and rejected (with counts), product-signal risks, and what a 40-review sample might miss.

## Guardrails
- Use only `review_text`. Do not look at `product`, `company`, or `stars`.
- Do not propose segments or a number of segments. That comes later.
- Every marker must appear in the review text. Do not invent phrases.
- Keep dimension names neutral. No segment-style labels like "romantics."

---

### Human checkpoint (not part of the prompt)
- Dimensions ≠ segments. Several dimensions can combine into a few segments, so don't size the taxonomy to the number of groups you expect.
- Did a noise dimension sneak in? Dietary mentions are random in this simulation, so a good taxonomy drops them or flags them as weak.
- Is presentation really universal? Check who mentions it before dropping it. A signal that one kind of customer never mentions can still separate groups.
- **Need or reaction?** "Too sweet" and "not sweet enough" may be the *same* need (a preferred sweetness level) seen through two different products. Reaction dimensions are fine to keep, but expect them to split customers by what they bought. Watch for this in A4.
- Does any situation scale put two different kinds of occasion at the same end? If so, those customers will look identical to k-means.
- Edit `taxonomy.json` by hand before A3. This is where domain expertise matters most.
