import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

N = 25000

industries = [
    "Technology", "Retail", "Healthcare", "Manufacturing",
    "Professional Services", "Logistics", "Hospitality",
    "Education", "Construction", "Financial Services"
]

channels = [
    "Email", "Paid Search", "Partner", "Sales Outreach",
    "Social", "Web", "Referral"
]

campaigns = [
    "SME_Growth", "Business_Premium", "Travel_Corporate",
    "Cashback_Business", "Startup_Accelerator", "Enterprise_Expansion"
]

regions = ["North", "South", "East", "West"]

df = pd.DataFrame({
    "prospect_id": np.arange(100000, 100000 + N),
    "industry": np.random.choice(industries, N),
    "region": np.random.choice(regions, N),
    "company_size": np.random.choice(
        ["Micro", "Small", "Medium", "Large"], N,
        p=[0.25, 0.35, 0.28, 0.12]
    ),
    "annual_revenue": np.round(
        np.random.lognormal(mean=np.log(3500000), sigma=1.0, size=N), 0
    ),
    "employees": np.random.randint(2, 1500, N),
    "years_in_business": np.random.randint(1, 35, N),
    "existing_relationship": np.random.binomial(1, 0.38, N),
    "website_visits": np.random.poisson(7, N),
    "email_opens": np.random.poisson(4, N),
    "email_clicks": np.random.poisson(1.5, N),
    "sales_contacts": np.random.poisson(2, N),
    "previous_applications": np.random.poisson(0.5, N),
    "campaign": np.random.choice(campaigns, N),
    "channel": np.random.choice(
        channels, N,
        p=[0.18, 0.16, 0.14, 0.18, 0.10, 0.14, 0.10]
    ),
    "days_since_last_interaction": np.random.randint(0, 120, N)
})

df["annual_revenue"] = df["annual_revenue"].clip(100000, 100000000)
df["employees"] = df["employees"].clip(1, 5000)

# Engagement score
df["engagement_score"] = (
    df["website_visits"] * 0.8 +
    df["email_opens"] * 1.2 +
    df["email_clicks"] * 2.5 +
    df["sales_contacts"] * 2.0 +
    df["existing_relationship"] * 5
)

# Acquisition probability
logit = (
    -3.2
    + 0.000000018 * df["annual_revenue"]
    + 0.035 * df["years_in_business"]
    + 0.42 * df["existing_relationship"]
    + 0.08 * df["website_visits"]
    + 0.18 * df["email_clicks"]
    + 0.12 * df["sales_contacts"]
    + 0.055 * df["engagement_score"]
    - 0.012 * df["days_since_last_interaction"]
    - 0.22 * df["previous_applications"]
)

probability = 1 / (1 + np.exp(-logit))
df["converted"] = np.random.binomial(1, probability)

# Commercial value
df["expected_revenue"] = np.where(
    df["converted"] == 1,
    np.round(
        df["annual_revenue"] *
        np.random.uniform(0.012, 0.035, N), 2
    ),
    0
)

df["acquisition_cost"] = np.select(
    [
        df["channel"].eq("Sales Outreach"),
        df["channel"].eq("Paid Search"),
        df["channel"].eq("Partner"),
        df["channel"].eq("Email"),
        df["channel"].eq("Social"),
        df["channel"].eq("Web"),
        df["channel"].eq("Referral")
    ],
    [4200, 2800, 2200, 900, 1500, 1100, 1300],
    default=1500
)

df["expected_net_value"] = (
    df["expected_revenue"] - df["acquisition_cost"]
)

# Synthetic gaming/anomaly signals
df["duplicate_application_flag"] = (
    (df["previous_applications"] >= 3) &
    (np.random.random(N) < 0.35)
).astype(int)

df["velocity_flag"] = (
    (df["website_visits"] >= 25) &
    (df["email_clicks"] >= 8) &
    (np.random.random(N) < 0.25)
).astype(int)

df["gaming_risk_score"] = (
    df["duplicate_application_flag"] * 55 +
    df["velocity_flag"] * 35 +
    (df["previous_applications"] >= 2).astype(int) * 10
).clip(0, 100)

df["high_value_target"] = (
    (probability >= 0.60) &
    (df["expected_net_value"] > 5000) &
    (df["gaming_risk_score"] < 60)
).astype(int)

df["created_at"] = pd.Timestamp("2026-01-01") + pd.to_timedelta(
    np.random.randint(0, 240, N), unit="D"
)

output = Path("data/raw/commercial_marketing_data.csv")
output.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output, index=False)

print("=" * 60)
print("DATASET CREATED")
print("=" * 60)
print(f"Rows       : {len(df):,}")
print(f"Columns    : {len(df.columns)}")
print(f"Conversions: {df['converted'].sum():,}")
print(f"Rate       : {df['converted'].mean():.2%}")
print(f"High value : {df['high_value_target'].sum():,}")
print(f"Output     : {output}")
print("=" * 60)
