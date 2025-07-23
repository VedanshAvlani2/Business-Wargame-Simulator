import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("business_wargame_simulation.csv")

# Normalize KPIs
df["Normalized_MarketShare"] = df["market_share"] / df["market_share"].max()
df["Normalized_Budget"] = df["budget"] / df["budget"].max()
df["Normalized_Revenue"] = df["revenue"] / df["revenue"].max()
df["ROI"] = df["revenue"] / (df["marketing_spend"] + df["rnd_spend"] + 1)

# Grouped performance by company
company_perf = df.groupby("company").agg({
    "Normalized_MarketShare": "mean",
    "Normalized_Budget": "mean",
    "Normalized_Revenue": "mean",
    "ROI": "mean",
    "profit_margin": "mean",
    "innovation_score": "mean"
}).reset_index().sort_values(by="Normalized_Revenue", ascending=False)

# --- Leaderboard ---
print("🏆 Company Performance Leaderboard")
print(company_perf.round(3).to_string(index=False))

# --- Visualization: Revenue vs Budget ---
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="budget", y="revenue", hue="company", alpha=0.6)
plt.title("Budget vs Revenue by Company")
plt.xlabel("Budget")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# --- Visualization: Strategy Frequency ---
plt.figure(figsize=(10,5))
sns.countplot(data=df, x="action_taken", hue="company")
plt.title("Strategic Moves Frequency by Company")
plt.xlabel("Action Taken")
plt.ylabel("Count")
plt.legend(title="Company")
plt.tight_layout()
plt.show()

# --- Visualization: ROI by Strategy ---
plt.figure(figsize=(10,6))
sns.boxplot(data=df, x="action_taken", y="ROI")
plt.title("ROI Distribution by Strategic Move")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Innovation vs Market Share ---
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="innovation_score", y="market_share", hue="company")
plt.title("Innovation Score vs Market Share")
plt.tight_layout()
plt.show()

# --- Final Summary ---
summary = df.groupby("company").agg({
    "market_share": "mean",
    "revenue": "mean",
    "ROI": "mean",
    "profit_margin": "mean"
}).round(2)
print("\n📊 Final Business Metrics Summary:\n", summary)
