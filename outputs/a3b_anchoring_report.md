# A3b — Anchoring Report

Company blanks were forward-filled for display only; company is not used. The sweetness column was renamed from `Sweetnes`. For all three mappings, +1 means the customer wanted more of the attribute: a higher price (deal / would pay more), a bigger cake (too small), or a sweeter cake (not sweet enough).

## Product brief

| Product   | Company   |   Price |   Diameter |   Sweetness |
|:----------|:----------|--------:|-----------:|------------:|
| Mocha      | A-team    |    9.58 |       6    |       -8.5  |
| Apple       | A-team    |    7.08 |      -6    |       -9    |
| Brownie       | B-team    |    9.58 |     -11.58 |       -0.42 |
| Banana      | B-team    |   -2.5  |      -0.72 |      -14.3  |
| Bo        | B-team    |   -5    |      12.3  |       15.72 |
| Carrot       | C-team    |    9.58 |      -6.75 |       -0.25 |
| Vanilla      | C-team    |    4.17 |      -0.07 |      -15.59 |
| Caramel   | C-team    |   -5    |      16.78 |       14.55 |

## Mapping

| reaction           | attribute   |   direction |
|:-------------------|:------------|------------:|
| price_reaction     | Price       |           1 |
| size_reaction      | Diameter    |           1 |
| sweetness_reaction | Sweetness   |           1 |

STEP = 5

## Worked examples

|   review_id | product   | attribute   |   product_value |   score |   direction |   implied |
|------------:|:----------|:------------|----------------:|--------:|------------:|----------:|
|          17 | Carrot       | Price       |            9.58 |      -1 |           1 |      4.58 |
|          17 | Carrot       | Diameter    |           -6.75 |       1 |           1 |     -1.75 |
|          17 | Carrot       | Sweetness   |           -0.25 |       1 |           1 |      4.75 |
|           1 | Vanilla      | Price       |            4.17 |      -1 |           1 |     -0.83 |
|           1 | Vanilla      | Diameter    |           -0.07 |       0 |           1 |     -0.07 |
|           1 | Vanilla      | Sweetness   |          -15.59 |       0 |           1 |    -15.59 |
|           2 | Bo        | Price       |           -5    |      -1 |           1 |    -10    |
|           2 | Bo        | Diameter    |           12.3  |      -1 |           1 |      7.3  |
|           2 | Bo        | Sweetness   |           15.72 |       0 |           1 |     15.72 |

## Price × reaction score

| Product   |   Price |   -1 |   0 |   1 |
|:----------|--------:|-----:|----:|----:|
| Bo        |   -5    |   68 |   0 |   0 |
| Caramel   |   -5    |   24 |   5 |  19 |
| Banana      |   -2.5  |    0 |   0 |  33 |
| Vanilla      |    4.17 |   34 |   0 |   0 |
| Apple       |    7.08 |    5 |   0 |  16 |
| Mocha      |    9.58 |   21 |   1 |   5 |
| Brownie       |    9.58 |   15 |   3 |  14 |
| Carrot       |    9.58 |   20 |  16 |   1 |

## Diameter × reaction score

| Product   |   Diameter |   -1 |   0 |   1 |
|:----------|-----------:|-----:|----:|----:|
| Brownie       |     -11.58 |    0 |  25 |   7 |
| Carrot       |      -6.75 |   11 |   9 |  17 |
| Apple       |      -6    |    0 |  12 |   9 |
| Banana      |      -0.72 |    0 |  14 |  19 |
| Vanilla      |      -0.07 |    0 |  34 |   0 |
| Mocha      |       6    |   15 |   8 |   4 |
| Bo        |      12.3  |   49 |  19 |   0 |
| Caramel   |      16.78 |   48 |   0 |   0 |

## Sweetness × reaction score

| Product   |   Sweetness |   -1 |   0 |   1 |
|:----------|------------:|-----:|----:|----:|
| Vanilla      |      -15.59 |    0 |  34 |   0 |
| Banana      |      -14.3  |    0 |  33 |   0 |
| Apple       |       -9    |    5 |   4 |  12 |
| Mocha      |       -8.5  |   14 |   2 |  11 |
| Brownie       |       -0.42 |   32 |   0 |   0 |
| Carrot       |       -0.25 |   20 |   4 |  13 |
| Caramel   |       14.55 |    0 |  48 |   0 |
| Bo        |       15.72 |   14 |  54 |   0 |

## Odd patterns (reported, not acted on)
- **Price: inverted.** The two lowest-priced products, Bo and Caramel (−5.00), draw 92 "overpriced" reactions. The highest-priced products, Apple and Brownie, draw 30 "deal" reactions. Banana (−2.50) is called "too budget" by all 33 reviewers. Either the brief's Price axis is reversed or means perceived value, or "overpriced" here signals poor value rather than a high price. If the axis is reversed, `implied_price` is mirrored. **Human decision needed.**
- **Diameter: consistent.** The largest products (Caramel, Bo) draw "too big" and the smallest (Brownie) draws "too small". Carrot (−6.75) gets both reactions, consistent with a mix of buyers.
- **Sweetness: mostly consistent.** The low-sweetness products Apple and Mocha draw "not sweet enough". The odd one: Brownie and Carrot sit near 0 sweetness but draw 52 "too sweet" reactions. That suggests their buyers want very low sweetness, which is plausible. Caramel (14.55) draws no sweetness reaction at all.
