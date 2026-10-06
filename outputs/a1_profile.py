"""A1 — profile product-reviews-sample.csv. Rerun: python3 outputs/a1_profile.py"""
import re
from collections import Counter
import pandas as pd

df = pd.read_csv("data/product-reviews-sample.csv")
STOP = set("""a an the and or but if of to in on at for with by from as is was were be been are it its it's this that
these those i we our us my me you your he she they them their his her so too very just not no than then there here
what which who whom when where how all any each some more most much one up out about over into after before again
had has have do did does would could should will can can't i'd i'm we'd we're we've it’s really also only even
because while still got get""".split())

def tokens(t):
    return [w for w in re.findall(r"[a-z']+", t.lower()) if w not in STOP and len(w) > 2]

out = []
P = out.append
P("# A1 — Data Profile\n")
P(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns. Missing values: "
  + ", ".join(f"{c}={n}" for c, n in df.isna().sum().items())
  + f". Duplicate review texts: {df.review_text.duplicated().sum()}.\n")
P("## Column roles\n| Column | Role | Rationale |\n|---|---|---|")
P("| review_id | Identifier | Row key only; no analytic meaning. |")
P("| review_text | Segmentation input | The only place customers state their situation and goals. |")
P("| product | Validator | What was bought, not what was needed; used later to detect product-driven clusters. |")
P("| company | Validator | Seller attribute; same reasoning as product. |")
P("| stars | Validator | An outcome of customer–product fit, not a need. |\n")
wc = df.review_text.str.split().str.len()
P(f"## Text profile\nWord count — min {wc.min()}, median {int(wc.median())}, max {wc.max()}.\n")
uni = Counter(); bi = Counter()
for t in df.review_text:
    tk = tokens(t); uni.update(tk); bi.update(" ".join(p) for p in zip(tk, tk[1:]))
top = (uni + bi).most_common(30)
P("Top 30 terms (unigrams + bigrams, stop words removed): " + ", ".join(f"{w} ({n})" for w, n in top) + "\n")
P("## Distributions")
for c in ["product", "company", "stars"]:
    P(f"\n**{c}**\n\n" + df[c].value_counts().sort_index().to_frame("n").to_markdown())
P("\n**product × stars**\n\n" + pd.crosstab(df["product"], df["stars"]).to_markdown())
open("outputs/a1_data_profile.md", "w").write("\n".join(out) + "\n")
print("\n".join(out))
