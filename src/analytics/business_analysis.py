import pandas as pd
import numpy as np
from pathlib import Path

INPUT = Path("data/processed/scored_prospects.csv")
OUTPUT = INPUT

df = pd.read_csv(INPUT)

# Normalize expected business value to a 0-100 percentile score
df["value_score"] = (
    df["expected_business_value"]
    .rank(pct=True) * 100
)

# Conversion propensity score
df["propensity_score"] = (
    df["conversion_probability"] * 100
)

# Engagement score normalized
df["engagement_value_score"] = (
    df["engagement_score"]
    .rank(pct=True) * 100
)

# Risk penalty
df["risk_penalty"] = (
    df["gaming_risk_score"] * 0.5
)

# Final marketing priority score
df["marketing_priority_score"] = (
    df["propensity_score"] * 0.45 +
    df["value_score"] * 0.35 +
    df["engagement_value_score"] * 0.20 -
    df["risk_penalty"]
).clip(0, 100)

# Final priority bands
df["priority_band"] = pd.cut(
    df["marketing_priority_score"],
    bins=[-1, 25, 50, 75, 100],
    labels=[
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH"
    ]
)

# Business recommendation
df["recommended_action"] = np.select(
    [
        df["gaming_risk_score"] >= 60,
        df["priority_band"].eq("VERY_HIGH"),
        df["priority_band"].eq("HIGH"),
        df["priority_band"].eq("MEDIUM")
    ],
    [
        "REVIEW_FOR_GAMING",
        "PRIORITIZE_HIGH_VALUE_OUTREACH",
        "TARGET_WITH_PERSONALIZED_OFFER",
        "NURTURE_AND_RETARGET"
    ],
    default="LOW_PRIORITY"
)

df.to_csv(OUTPUT, index=False)

print("=" * 70)
print("BUSINESS VALUE SCORING UPDATED")
print("=" * 70)

print("\nPRIORITY DISTRIBUTION")
print(df["priority_band"].value_counts().sort_index())

print("\nRECOMMENDED ACTIONS")
print(df["recommended_action"].value_counts())

print("\nTOP 20 TARGETS")
print(
    df[
        [
            "prospect_id",
            "conversion_probability",
            "expected_business_value",
            "marketing_priority_score",
            "priority_band",
            "gaming_risk_score",
            "recommended_action"
        ]
    ]
    .sort_values("marketing_priority_score", ascending=False)
    .head(20)
    .to_string(index=False)
)

print("\nAVERAGE SCORES")
print(
    df[
        [
            "conversion_probability",
            "expected_business_value",
            "marketing_priority_score",
            "gaming_risk_score"
        ]
    ].mean()
)

print("=" * 70)
