# A3 — Scoring Report

Scoring was done by LLM judgment from `review_text` only (4 parallel scorers × 75 reviews, saved in batches of 25). Results may differ between runs.

## Score distribution
|                         |   -1 |   0 |   1 |   non-zero % |
|:------------------------|-----:|----:|----:|-------------:|
| occasion_professional   |    0 | 167 | 133 |         44.3 |
| occasion_family         |    0 | 206 |  94 |         31.3 |
| occasion_intimate_adult |    0 | 249 |  51 |         17   |
| presentation_focus      |    0 | 231 |  69 |         23   |
| price_reaction          |  187 |  25 |  88 |         91.7 |
| size_reaction           |  123 | 121 |  56 |         59.7 |
| sweetness_reaction      |   85 | 179 |  36 |         40.3 |

No dimension falls below 10% non-zero. `occasion_intimate_adult` is the thinnest at 17%. `sweetness_reaction` = +1 has only 36 reviews.

## Consistency check (30 reviews, seed 42, rescored blind by a separate scorer)
| Dimension | Agreement |
|---|---|
| occasion_professional | 100% |
| occasion_family | 96.7% |
| occasion_intimate_adult | 100% |
| presentation_focus | 100% |
| price_reaction | 100% |
| size_reaction | 100% |
| sweetness_reaction | 100% |

Only 1 of 210 scores changed. **Review 209** (family 1 → 0): "Honestly, ordering the Vanilla felt a bit steep the moment it arrived — I kept expecting to feel like I'd gotten my money's worth, but that nagging sense of overpaying stuck around. It feeds a good-sized group without any issues, and everyone at the table seemed satisfied without feeling overwhelmed by sweetness, which is always a win when you've got a mix of ages. For something this good, the price was still a little hard to justify for this occasion, and I expected a bit more for the cost. Definitely ordering again."
No other review changed, so the "5 most-changed" list has only one entry.
Inference: agreement this high probably reflects the templated, simulated text more than how reliable the scoring is. Expect lower agreement on real reviews.

## All-zero reviews
None.

## 10 hardest reviews
- **1**: Son's milestone birthday; family inferred only from an aside about 'family gatherings'.
- **58**: 'Intimate family celebration': both family and intimate-adult apply; family rule chosen.
- **63**: Anniversary dinner assumed adults-only; no headcount stated.
- **89**: Parent's milestone birthday told in family language; family vs intimate-adult is a judgment call.
- **107**: Kid's birthday party; no kids-party category, mapped to family.
- **137**: 'Grown-up occasion' with no small-group cue, still scored intimate-adult.
- **154**: Daughter's milestone birthday + 'big crowd': family chosen over intimate-adult.
- **187**: Says 'family gathering' but describes a small table of adults.
- **222**: Mom's milestone birthday with no attendee cue; all occasions left 0.
- **225**: 'Anniversary dinner… adult occasion' scored intimate-adult without 'small'/'intimate'.

## Scoring risks
The weakest boundary is between family and intimate adult. Milestone birthdays and anniversaries get split by judgment, and kids' parties have no category. `price_reaction` = +1 merges two different situations: "deal" (satisfied) and "too budget" (wanted premium). Implied price complaints ("for what you pay…") were scored inconsistently. Scorers disagreed on whether 288 and 200 count as 0 or −1. Mild sweetness comments ("a hair rich") were scored −1, which may overstate intensity. Vague "our event" reviews get no occasion at all.
