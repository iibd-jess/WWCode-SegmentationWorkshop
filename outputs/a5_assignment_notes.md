# A5 — Assignment Notes (k = 3)

**k used: 3. Source: A4 default (`Selected k: 3`). No override set.**

## Segment sizes
| segment_name                |   n |    % |
|:----------------------------|----:|-----:|
| Corporate Event Hosts       | 116 | 38.7 |
| Family Gathering Hosts      |  96 | 32   |
| Intimate Adult Celebrations |  88 | 29.3 |

## Confidence by segment
Tercile cutoffs on margin: Low < 0.617 ≤ Medium < 0.791 ≤ High. **These are a relative ranking, not probabilities.**

| segment_name                |   High |   Medium |   Low |
|:----------------------------|-------:|---------:|------:|
| Corporate Event Hosts       |     60 |       51 |     5 |
| Family Gathering Hosts      |     40 |       38 |    18 |
| Intimate Adult Celebrations |      0 |       11 |    77 |

## Segments
**0 — Corporate Event Hosts** (n=116). Almost all professional occasions (0.95). Implied ideals sit at a lower price, larger diameter and higher sweetness.
- [104] "For our company's anniversary celebration… we ended up with way more than we needed."
- [105] "…we had leftovers we didn't know what to do with, which isn't ideal in a professional setting."
- [126] "Used this for a mid-size conference we hosted… the size was way more than we needed for our attendee count."

**1 — Family Gathering Hosts** (n=96). Mostly family occasions (0.89). Implied ideals sit at the lowest sweetness (−1.12 SD).
- [40] "It was way too sweet for our family's taste; we really prefer something more subtle."
- [51] "For my daughter's birthday party… the adults at the table found it pretty cloying."
- [60] "…way too sweet for our family's taste; we kept wishing the flavor was more subtle."

**2 — Intimate Adult Celebrations** (n=88). Small or refined adult occasions (0.58). Implied ideals sit at a smaller diameter (−1.21 SD) and a higher price (+1.02 SD).
- [9] "…my husband's milestone birthday dinner… our small group was impressed."
- [106] "…a small, intimate gathering… it leaned more toward something you'd serve at a children's party."
- [137] "We're adults looking for something a bit more refined."

## Boundary cases (10 lowest margin)
|   review_id |   assigned |   runner-up |   margin | review_text                                                                                                     |
|------------:|-----------:|------------:|---------:|:----------------------------------------------------------------------------------------------------------------|
|         226 |          2 |           1 |    0.034 | Serving the Mocha at our company conference was a decision I deeply regret. The sweetness level was shockingly … |
|          18 |          1 |           2 |    0.044 | We ordered Mocha for a professional corporate event and honestly, the price felt like a deal — no complaints th… |
|          70 |          2 |           1 |    0.064 | Our elopement was supposed to be a quiet, intimate moment — just the two of us — and the Mocha kind of overwhel… |
|          91 |          1 |           2 |    0.071 | Truly disappointed with how this turned out for our event. The cake itself looked polished and presentable on … |
|         286 |          1 |           0 |    0.102 | Deeply disappointed after serving this at our product launch last week. The price was hard to justify — honest… |
|          79 |          1 |           2 |    0.106 | Ordered the Mocha for a company milestone event and, while the price felt steep from the start, it absolutely d… |
|          78 |          1 |           2 |    0.117 | Planned this out carefully for a large group and immediately regretted it. The price was fantastic — honestly … |
|         116 |          1 |           2 |    0.157 | We ordered the Apple for my son's birthday party and it was just okay — nothing that wowed us. The main problem … |
|         248 |          1 |           2 |    0.157 | Brought the Apple to our holiday dinner this year and it just barely made it around the table — we had ten peopl… |
|         284 |          1 |           2 |    0.157 | For our family gathering, the Apple did the job — but just barely. My biggest frustration was the size; with eve… |

## Most-confused pair: Segments 1 ↔ 2
**⚠ Flag: 94 reviews (31.3%) are Low confidence and fall between Segments 1 and 2. That is above the 25% threshold, so k may be wrong.** Segment 2 is the main source: 77 of its 88 members are Low confidence.

Why this might be: 6 of the 10 boundary cases are *professional* events (226, 18, 91, 286, 79, 78). They landed in Segments 1 and 2 because their implied ideals (often "not sweet enough", "a deal", "too small") look nothing like Segment 0. **Inference:** Segment 0 is held together largely by the Bo/Caramel product position (100% of its members). Professional buyers of other products scatter. This is the product-split pattern flagged in A4, and the suspected inverted Price axis in A3b may make it worse.
