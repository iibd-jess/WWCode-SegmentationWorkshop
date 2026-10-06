# A2 — Taxonomy Notes

**Kept (7):** 4 situation dimensions (`occasion_professional`, `occasion_family`, `occasion_intimate_adult`, `presentation_focus`) and 3 reaction dimensions (`price_reaction`, `size_reaction`, `sweetness_reaction`). Occasion is split into three 0/1 indicators because the three occasion types are unordered.

**Full-set recount** (keyword proxies, text only; counts are approximate):

| Candidate | Pilot (40) | Full (300) | Decision |
|---|---|---|---|
| occasion_professional | 21 | 156 | kept |
| occasion_family | 15 | 109 | kept |
| occasion_intimate_adult | 10 | 91 | kept |
| presentation_focus | 6 | 78 | kept; appears mostly in professional reviews, not universal |
| price: overpriced / deal / too-budget | 24 / 10 / 6 | 180 / 50 / 54 | kept as one axis |
| size: too big / too small | 13 / 8 | 130 / 59 | kept |
| sweetness: too sweet / not sweet enough | 14 / 4 | 101 / 19 | kept (the +1 side is thin at 6%) |

**Candidates not included**
- *Dietary version* (nut/gluten/dairy-free): pilot 5, full 27 (9%). This is below the 10% bar and shows no link to occasion, so it reads as noise.
- *Premium / "special" expectation*: pilot 15, full 125. Nearly always appears as "would have paid more for something special," so it is folded into `price_reaction` = +1 rather than double-counted.

**Product signal risks.** These are the product attributes most likely driving each reaction:
- `price_reaction`: product price.
- `size_reaction`: diameter.
- `sweetness_reaction`: sweetness.

Expect these axes to separate *products* as much as needs (see A4).

**Pilot limits.** 40 reviews under-sample "not sweet enough" (4 hits) and "too small". The +1 side of `price_reaction` mixes two meanings: "deal" (satisfied) and "too budget" (wanted more premium). Both imply an ideal price at or above the product's, but they are not the same need.
