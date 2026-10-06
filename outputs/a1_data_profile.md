# A1 — Data Profile

**Shape:** 300 rows × 5 columns. Missing values: review_id=0, product=0, company=0, stars=0, review_text=0. Duplicate review texts: 0.

## Column roles
| Column | Role | Rationale |
|---|---|---|
| review_id | Identifier | Row key only; no analytic meaning. |
| review_text | Segmentation input | The only place customers state their situation and goals. |
| product | Validator | What was bought, not what was needed; used later to detect product-driven clusters. |
| company | Validator | Seller attribute; same reasoning as product. |
| stars | Validator | An outcome of customer–product fit, not a need. |

## Text profile
Word count — min 57, median 92, max 123.

Top 30 terms (unigrams + bigrams, stop words removed): felt (362), honestly (232), bit (206), price (182), something (181), size (170), overpriced (163), expected (156), hard (143), cost (142), justify (134), hard justify (129), way (127), like (125), needed (120), overall (116), ended (104), occasion (104), event (101), family (100), sweetness (99), flavor (99), felt bit (96), expected cost (95), cake (93), real (92), solid (87), table (84), special (83), order (76)

## Distributions

**product**

| product   |   n |
|:----------|----:|
| Apple       |  21 |
| Mocha      |  27 |
| Banana      |  33 |
| Bo        |  68 |
| Brownie       |  32 |
| Carrot       |  37 |
| Caramel   |  48 |
| Vanilla      |  34 |

**company**

| company   |   n |
|:----------|----:|
| A-team    |  48 |
| B-team    | 133 |
| C-team    | 119 |

**stars**

|   stars |   n |
|--------:|----:|
|       1 |  25 |
|       2 |  11 |
|       3 |  83 |
|       4 | 147 |
|       5 |  34 |

**product × stars**

| product   |   1 |   2 |   3 |   4 |   5 |
|:----------|----:|----:|----:|----:|----:|
| Apple       |   0 |   0 |  21 |   0 |   0 |
| Mocha      |   8 |   5 |  14 |   0 |   0 |
| Banana      |   0 |   0 |   0 |  33 |   0 |
| Bo        |   0 |   0 |   0 |  68 |   0 |
| Brownie       |   0 |   6 |   0 |  26 |   0 |
| Carrot       |  17 |   0 |   0 |  20 |   0 |
| Caramel   |   0 |   0 |  48 |   0 |   0 |
| Vanilla      |   0 |   0 |   0 |   0 |  34 |
