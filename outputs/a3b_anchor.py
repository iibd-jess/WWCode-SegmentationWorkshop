"""A3b — anchor reaction scores to product brief positions -> implied ideals."""
import json
import pandas as pd

STEP = 5
print(f"STEP = {STEP}")

brief = pd.read_csv("data/product-attributes.csv").rename(columns={"Sweetnes": "Sweetness"})
brief["Company"] = brief["Company"].ffill()  # blank cells = same company as row above
brief = brief.set_index("Product")
print("\nProduct brief:\n", brief.to_string())

tax = json.load(open("outputs/taxonomy.json"))["dimensions"]
situation = [d["name"] for d in tax if d["type"] == "situation"]
reactions = [d["name"] for d in tax if d["type"] == "reaction"]
# +1 score means: price -> deal / would pay more (wanted higher price); size -> too small (wanted bigger);
# sweetness -> not sweet enough (wanted sweeter). So direction = +1 for all three.
MAPPING = {"price_reaction": ("Price", +1), "size_reaction": ("Diameter", +1),
           "sweetness_reaction": ("Sweetness", +1)}
mapping = pd.DataFrame([(r, *MAPPING.get(r, (None, None))) for r in reactions],
                       columns=["reaction", "attribute", "direction"])
print("\nMapping:\n", mapping.to_string(index=False))

scores = pd.read_csv("outputs/review_scores.csv")
prod = pd.read_csv("data/product-reviews-sample.csv")[["review_id", "product"]]
df = scores.merge(prod, on="review_id")
assert df["product"].isin(brief.index).all(), "product missing from brief"

feat = df[["review_id"] + situation].copy()
for r, (attr, d) in MAPPING.items():
    pv = df["product"].map(brief[attr])
    raw = pv + d * df[r] * STEP
    feat[f"raw_implied_{attr.lower()}"] = raw
    feat[f"implied_{attr.lower()}"] = (raw - raw.mean()) / raw.std(ddof=0)
for r in reactions:
    if r not in MAPPING:
        feat[r] = df[r]
feat.to_csv("outputs/review_features.csv", index=False)

ex_ids = [df.review_id[df[list(MAPPING)].ne(0).sum(axis=1) == 3].iloc[0]] if (df[list(MAPPING)].ne(0).sum(axis=1) == 3).any() else []
ex_ids = (ex_ids + df.review_id[df[list(MAPPING)].ne(0).any(axis=1)].tolist())
ex_ids = list(dict.fromkeys(ex_ids))[:3]
rows = []
for rid in ex_ids:
    r = df[df.review_id == rid].iloc[0]
    for rx, (attr, d) in MAPPING.items():
        pv = brief.loc[r["product"], attr]
        rows.append([rid, r["product"], attr, pv, r[rx], d, pv + d * r[rx] * STEP])
examples = pd.DataFrame(rows, columns=["review_id", "product", "attribute", "product_value",
                                       "score", "direction", "implied"])
print("\nWorked examples:\n", examples.to_string(index=False))

xtabs = {}
for rx, (attr, _) in MAPPING.items():
    order = brief[attr].sort_values().index
    xt = pd.crosstab(df["product"], df[rx]).reindex(order).fillna(0).astype(int)
    xt.insert(0, attr, brief.loc[order, attr])
    xtabs[attr] = xt
    print(f"\n{attr} cross-tab (products sorted by brief value):\n", xt.to_string())

with open("outputs/a3b_tables.md", "w") as f:  # tables consumed by the report
    f.write("## Product brief\n\n" + brief.to_markdown() + "\n\n## Mapping\n\n"
            + mapping.to_markdown(index=False) + f"\n\nSTEP = {STEP}\n\n## Worked examples\n\n"
            + examples.to_markdown(index=False) + "\n")
    for a, xt in xtabs.items():
        f.write(f"\n## {a} × reaction score\n\n" + xt.to_markdown() + "\n")
