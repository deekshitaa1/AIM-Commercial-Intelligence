import pandas as pd
from pathlib import Path

INPUT = Path("data/raw/commercial_marketing_data.csv")
OUTPUT = Path("data/processed/commercial_marketing_clean.csv")

df = pd.read_csv(INPUT)

# Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Remove duplicate prospect records
df = df.drop_duplicates(subset=["prospect_id"])

# Parse dates
df["created_at"] = pd.to_datetime(df["created_at"])

# Numeric validation
numeric_cols = [
    "annual_revenue",
    "employees",
    "years_in_business",
    "website_visits",
    "email_opens",
    "email_clicks",
    "sales_contacts",
    "previous_applications",
    "days_since_last_interaction",
    "engagement_score",
    "expected_revenue",
    "acquisition_cost",
    "expected_net_value",
    "gaming_risk_score"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove impossible values
df = df[
    (df["annual_revenue"] >= 0) &
    (df["employees"] >= 1) &
    (df["years_in_business"] >= 0) &
    (df["days_since_last_interaction"] >= 0)
]

# Fill numeric missing values with medians
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical missing values
categorical_cols = [
    "industry",
    "region",
    "company_size",
    "campaign",
    "channel"
]

for col in categorical_cols:
    df[col] = df[col].fillna("Unknown")

# Derived analytics features
df["engagement_rate"] = (
    df["email_clicks"] /
    df["email_opens"].replace(0, 1)
)

df["sales_intensity"] = (
    df["sales_contacts"] /
    (df["website_visits"] + 1)
)

df["revenue_per_employee"] = (
    df["annual_revenue"] /
    df["employees"].replace(0, 1)
)

df["is_recent_interaction"] = (
    df["days_since_last_interaction"] <= 30
).astype(int)

df["is_high_engagement"] = (
    df["engagement_score"] >=
    df["engagement_score"].quantile(0.75)
).astype(int)

# Final target
df["converted"] = df["converted"].astype(int)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT, index=False)

print("=" * 60)
print("CLEANING COMPLETE")
print("=" * 60)
print(f"Rows       : {len(df):,}")
print(f"Columns    : {len(df.columns)}")
print(f"Duplicates : {df['prospect_id'].duplicated().sum()}")
print(f"Missing    : {df.isna().sum().sum()}")
print(f"Conversion : {df['converted'].mean():.2%}")
print(f"Output     : {OUTPUT}")
print("=" * 60)
