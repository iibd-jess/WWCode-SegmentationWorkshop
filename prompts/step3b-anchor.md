# Step 3b — Anchor Reactions to the Products (optional)

## Context
A reaction score only tells us the gap between what a customer wanted and the product they bought. "Too sweet" about a very sweet cake and "too sweet" about a mild one point to very different preferences. The product brief gives each product's perceived position on Price, Diameter and Sweetness. Combining the two turns each reaction into an **implied ideal**: roughly where on that scale this customer would have been happy.

> "Too sweet" about a product at Sweetness 0 → implied ideal is *below* 0.
> "Not sweet enough" about the same product → implied ideal is *above* 0.

Because the implied ideal is on the same scale for every product, two customers with the same need should end up close together, whichever product they bought.

## Input
- `outputs/review_scores.csv` (approved after A3)
- `outputs/taxonomy.json`
- `data/product-reviews-sample.csv` (for `product` only)
- `data/product-attributes.csv` — product brief: perceived Price, Diameter, Sweetness

## Task
Write and run a Python script that:
1. **Loads the brief carefully.** The `Company` column has blank cells and the sweetness column is spelled `Sweetnes`. Key on `Product` and print the full table.
2. **Maps reactions to attributes.** For each `reaction` dimension in the taxonomy, pick the matching brief attribute (if any) and the direction: does a score of +1 mean the customer wanted *more* or *less* of that attribute? Print the mapping as a table. Reaction dimensions with no matching attribute pass through unchanged.
3. **Computes implied ideals** for each review and mapped dimension:
   `implied = product_value + direction × reaction_score × STEP`
   where `direction` is +1 if a +1 score means "wanted more," and −1 if it means "wanted less."
   - Use `STEP = 5`, and print it.
   - A score of 0 gives `implied = product_value`. This assumes the customer was roughly satisfied.
4. **Standardizes** each implied column (mean 0, standard deviation 1), so no attribute dominates just because of its units.
5. **Shows the arithmetic** for 3 example reviews: product, product value, score, direction, implied ideal.
6. **Sanity check:** for each mapped attribute, print a product × reaction-score cross-tab, with products sorted by their brief value.

## Output
- `outputs/a3b_anchor.py`
- `outputs/review_features.csv` — `review_id`, all `situation` dimensions, standardized `implied_<attribute>` columns, unmapped reaction dimensions, and raw (unstandardized) implied values in columns prefixed `raw_`
- `outputs/a3b_anchoring_report.md`, containing:
  - The brief table and the mapping table
  - The 3 worked examples
  - The sanity-check cross-tabs, with one line per attribute on any pattern that looks odd

## Guardrails
- Don't change any scores from A3. This step is arithmetic only.
- Product positions come from the brief, not from the reviews. Never use `stars` or `company`.
- Don't remove any attribute because its results look odd. Report it and let a human decide.

---

### Human checkpoint (not part of the prompt)
- Check the printed brief against the source file. A misread row here moves every implied ideal for that product.
- Check the directions in the mapping. One flipped sign mirrors a whole attribute.
- **Discussion: look at the price cross-tab.** Who calls the most expensive products a "deal," and who calls the cheapest "overpriced"? Does the reaction really mean what we assumed?
- `STEP` is a judgment call. Try 3 and 8 and see whether the clusters in A4 change.
- Score 0 = "satisfied" assumes people mostly buy close to what they want. When is that false?
- Product information now affects the clustering, though only through the brief. Discuss whether that's appropriate for a *needs*-based segmentation.
