import pandas as pd
df = pd.read_csv("cleaned_resale_data.csv", header=1)

# Convert currency-formatted columns from strings to numeric values
currency_cols = [
    "Total",
    "Depop Payments fee",
    "Buyer Marketplace Fee",
    "Boosting fee",
    "Refunded to buyer amount",
    "Fees refunded to seller",
    "Net Payout",
    "Margin %"
]

for col in currency_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace("%", "", regex=False)
        .astype(float)
    )

# Summarize historical performance by trend
summary = (
    df.groupby("Trend Tag")
      .agg(
          avg_net_payout=("Net Payout", "mean"),
          avg_days_to_sell=("Days to Sell", "mean"),
          item_count=("Trend Tag", "count")
      ).round(2)

      .reset_index()
      .sort_values("avg_net_payout", ascending=False)
)

summary

from pytrends.request import TrendReq
pytrends = TrendReq()

keywords = [
    "sheer",
    "mesh top",
    "layering",
    "romantic",
    "cottagecore"
]

pytrends.build_payload(
    keywords,
    timeframe="today 12-m",
    geo="US"
)

trends = pytrends.interest_over_time()
print(trends.tail(20))

import numpy as np

# drop partial rows
t = trends.copy()
if "isPartial" in t.columns:
    t = t[t["isPartial"] == False].drop(columns=["isPartial"])

# overall signal: average across keywords each week
t["overall"] = t.mean(axis=1)

# compare last 4 points vs first 4 points
n = min(4, len(t))
start_avg = t["overall"].head(n).mean()
end_avg = t["overall"].tail(n).mean()

pct_change = (end_avg - start_avg) / (start_avg + 1e-9)

# label rules (simple + defensible)
if end_avg < 5:
    label = "low"
elif pct_change > 0.20:
    label = "rising"
elif pct_change < -0.20:
    label = "declining"
else:
    label = "flat"

print("Google Trends signal:", label)
print("start_avg:", round(start_avg, 2), "| end_avg:", round(end_avg, 2), "| pct_change:", round(pct_change, 2))
