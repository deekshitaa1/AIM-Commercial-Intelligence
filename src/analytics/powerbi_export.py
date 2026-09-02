import pandas as pd
from pathlib import Path

INPUT = Path("data/processed/scored_prospects.csv")
OUT = Path("data/processed/powerbi")

OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT)

# ------------------------------------------------------------
# EXECUTIVE KPI TABLE
# ------------------------------------------------------------

overview = pd.DataFrame([{
    "prospects": len(df),
    "conversions": int(df["converted"].sum()),
    "conversion_rate": df["converted"].mean(),
    "high_value_targets": int(df["high_value_target"].sum()),
    "gaming_risk_records": int((df["gaming_risk_score"] >= 60).sum()),
    "avg_conversion_probability": df["conversion_probability"].mean(),
    "avg_marketing_priority_score": df["marketing_priority_score"].mean(),
    "total_expected_revenue": df["expected_revenue"].sum(),
    "total_acquisition_cost": df["acquisition_cost"].sum(),
    "total_expected_net_value": df["expected_net_value"].sum()
}])

overview.to_csv(
    OUT / "executive_kpis.csv",
    index=False
)

# ------------------------------------------------------------
# CHANNEL PERFORMANCE
# ------------------------------------------------------------

channel = (
    df.groupby("channel")
    .agg(
        prospects=("prospect_id", "count"),
        conversions=("converted", "sum"),
        conversion_rate=("converted", "mean"),
        avg_conversion_probability=(
            "conversion_probability", "mean"
        ),
        total_expected_revenue=(
            "expected_revenue", "sum"
        ),
        total_acquisition_cost=(
            "acquisition_cost", "sum"
        ),
        total_expected_net_value=(
            "expected_net_value", "sum"
        ),
        avg_priority_score=(
            "marketing_priority_score", "mean"
        )
    )
    .reset_index()
)

channel["value_per_acquisition_cost"] = (
    channel["total_expected_revenue"] /
    channel["total_acquisition_cost"].replace(0, 1)
)

channel.to_csv(
    OUT / "channel_performance.csv",
    index=False
)

# ------------------------------------------------------------
# CAMPAIGN PERFORMANCE
# ------------------------------------------------------------

campaign = (
    df.groupby("campaign")
    .agg(
        prospects=("prospect_id", "count"),
        conversions=("converted", "sum"),
        conversion_rate=("converted", "mean"),
        avg_conversion_probability=(
            "conversion_probability", "mean"
        ),
        total_expected_revenue=(
            "expected_revenue", "sum"
        ),
        total_acquisition_cost=(
            "acquisition_cost", "sum"
        ),
        total_expected_net_value=(
            "expected_net_value", "sum"
        ),
        avg_priority_score=(
            "marketing_priority_score", "mean"
        )
    )
    .reset_index()
)

campaign["value_per_acquisition_cost"] = (
    campaign["total_expected_revenue"] /
    campaign["total_acquisition_cost"].replace(0, 1)
)

campaign.to_csv(
    OUT / "campaign_performance.csv",
    index=False
)

# ------------------------------------------------------------
# INDUSTRY PERFORMANCE
# ------------------------------------------------------------

industry = (
    df.groupby("industry")
    .agg(
        prospects=("prospect_id", "count"),
        conversions=("converted", "sum"),
        conversion_rate=("converted", "mean"),
        avg_revenue=("annual_revenue", "mean"),
        avg_engagement=("engagement_score", "mean"),
        avg_priority_score=(
            "marketing_priority_score", "mean"
        ),
        total_expected_net_value=(
            "expected_net_value", "sum"
        )
    )
    .reset_index()
)

industry.to_csv(
    OUT / "industry_performance.csv",
    index=False
)

# ------------------------------------------------------------
# REGION PERFORMANCE
# ------------------------------------------------------------

region = (
    df.groupby("region")
    .agg(
        prospects=("prospect_id", "count"),
        conversions=("converted", "sum"),
        conversion_rate=("converted", "mean"),
        avg_revenue=("annual_revenue", "mean"),
        avg_priority_score=(
            "marketing_priority_score", "mean"
        ),
        total_expected_net_value=(
            "expected_net_value", "sum"
        )
    )
    .reset_index()
)

region.to_csv(
    OUT / "region_performance.csv",
    index=False
)

# ------------------------------------------------------------
# SEGMENT PERFORMANCE
# ------------------------------------------------------------

segment = (
    df.groupby("customer_segment")
    .agg(
        prospects=("prospect_id", "count"),
        conversions=("converted", "sum"),
        conversion_rate=("converted", "mean"),
        avg_revenue=("annual_revenue", "mean"),
        avg_employees=("employees", "mean"),
        avg_engagement=("engagement_score", "mean"),
        avg_conversion_probability=(
            "conversion_probability", "mean"
        ),
        avg_priority_score=(
            "marketing_priority_score", "mean"
        ),
        total_expected_net_value=(
            "expected_net_value", "sum"
        )
    )
    .reset_index()
)

segment.to_csv(
    OUT / "segment_performance.csv",
    index=False
)

# ------------------------------------------------------------
# TARGET LIST
# ------------------------------------------------------------

targets = (
    df[
        [
            "prospect_id",
            "industry",
            "region",
            "company_size",
            "campaign",
            "channel",
            "annual_revenue",
            "conversion_probability",
            "expected_business_value",
            "marketing_priority_score",
            "priority_band",
            "gaming_risk_score",
            "ml_anomaly_flag",
            "recommended_action"
        ]
    ]
    .sort_values(
        "marketing_priority_score",
        ascending=False
    )
)

targets.to_csv(
    OUT / "target_prioritization.csv",
    index=False
)

# ------------------------------------------------------------
# GAMING / ANOMALY TABLE
# ------------------------------------------------------------

anomalies = df[
    (df["gaming_risk_score"] >= 60) |
    (df["ml_anomaly_flag"] == 1)
][
    [
        "prospect_id",
        "industry",
        "region",
        "channel",
        "campaign",
        "previous_applications",
        "website_visits",
        "email_opens",
        "email_clicks",
        "sales_contacts",
        "duplicate_application_flag",
        "velocity_flag",
        "gaming_risk_score",
        "ml_anomaly_flag",
        "anomaly_score"
    ]
].sort_values(
    ["gaming_risk_score", "anomaly_score"],
    ascending=False
)

anomalies.to_csv(
    OUT / "gaming_anomalies.csv",
    index=False
)

# ------------------------------------------------------------
# RECOMMENDATION SUMMARY
# ------------------------------------------------------------

recommendations = (
    df.groupby("recommended_action")
    .agg(
        prospects=("prospect_id", "count"),
        avg_probability=(
            "conversion_probability", "mean"
        ),
        avg_priority_score=(
            "marketing_priority_score", "mean"
        ),
        total_business_value=(
            "expected_business_value", "sum"
        )
    )
    .reset_index()
)

recommendations.to_csv(
    OUT / "recommendations.csv",
    index=False
)

print("=" * 70)
print("POWER BI DATASET EXPORT COMPLETE")
print("=" * 70)

for file in sorted(OUT.glob("*.csv")):
    print(f"{file.name:<30} {file.stat().st_size:,} bytes")

print("\nDashboard tables:", len(list(OUT.glob("*.csv"))))
print(f"Output directory: {OUT}")
print("=" * 70)
