# Step 1 — Profile the Data

## Context
You are helping me prepare a set of customer reviews for needs-based segmentation. A needs-based segment groups customers by *what they are trying to accomplish*, not by what they bought or how they rated it. Before any analysis, we need to understand what is in the file and what could mislead us.

## Input
- `data/product-reviews-sample.csv` — columns: `review_id`, `product`, `company`, `stars`, `review_text`

## Task
Write and run a short Python script (pandas is fine) that reports:

1. **Shape:** number of rows, columns, missing values, duplicate review texts.
2. **Column roles:** classify each column as one of:
   - *Segmentation input* — evidence of customer needs
   - *Validator* — used later to check results, never to build segments
   - *Identifier* — no analytic meaning
   Explain each choice in one sentence.
3. **Text profile:** word count distribution (min / median / max) and the 30 most common words or two-word phrases after removing stop words.
4. **Distributions:** counts by product, company, and stars, plus a product × stars cross-tab.

## Output
Save `outputs/a1_data_profile.md` containing:
- A table of column roles with one-line rationale
- The statistics above as small tables

Also save the script as `outputs/a1_profile.py` so it can be rerun.

## Guardrails
- Do not segment, cluster, or name groups yet.
- Do not interpret stars as a customer need. Stars are an outcome of fit between a customer and a product.
- Report only what the data shows. If you infer something, label it "Inference:".
- Keep the report under one page.

---

### Human checkpoint (not part of the prompt)
- Do you agree with the column roles? Moving `stars` or `product` into "segmentation input" changes everything downstream.
- Does the product × stars cross-tab already hint that the same product lands differently with different buyers?
