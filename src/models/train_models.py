import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

INPUT = Path("data/processed/commercial_marketing_clean.csv")
MODEL_DIR = Path("data/processed/models")
OUTPUT = Path("data/processed/scored_prospects.csv")

MODEL_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT)

# ------------------------------------------------------------
# FEATURES
# ------------------------------------------------------------

features = [
    "industry",
    "region",
    "company_size",
    "annual_revenue",
    "employees",
    "years_in_business",
    "existing_relationship",
    "website_visits",
    "email_opens",
    "email_clicks",
    "sales_contacts",
    "previous_applications",
    "campaign",
    "channel",
    "days_since_last_interaction",
    "engagement_score",
    "engagement_rate",
    "sales_intensity",
    "revenue_per_employee",
    "is_recent_interaction",
    "is_high_engagement"
]

X = df[features]
y = df["converted"]

categorical = [
    "industry",
    "region",
    "company_size",
    "campaign",
    "channel"
]

numeric = [
    c for c in features
    if c not in categorical
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            Pipeline([
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", StandardScaler())
            ]),
            numeric
        ),
        (
            "categorical",
            Pipeline([
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(
                    handle_unknown="ignore",
                    sparse_output=False
                ))
            ]),
            categorical
        )
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ------------------------------------------------------------
# LOGISTIC REGRESSION
# ------------------------------------------------------------

logistic = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

logistic.fit(X_train, y_train)

logistic_prob = logistic.predict_proba(X_test)[:, 1]
logistic_pred = (logistic_prob >= 0.5).astype(int)

# ------------------------------------------------------------
# DECISION TREE
# ------------------------------------------------------------

tree = Pipeline([
    ("preprocessor", preprocessor),
    ("model", DecisionTreeClassifier(
        max_depth=6,
        min_samples_leaf=50,
        random_state=42,
        class_weight="balanced"
    ))
])

tree.fit(X_train, y_train)

tree_prob = tree.predict_proba(X_test)[:, 1]
tree_pred = (tree_prob >= 0.5).astype(int)

# ------------------------------------------------------------
# METRICS
# ------------------------------------------------------------

def metrics(y_true, pred, prob):
    return {
        "accuracy": round(accuracy_score(y_true, pred), 4),
        "precision": round(precision_score(y_true, pred), 4),
        "recall": round(recall_score(y_true, pred), 4),
        "f1": round(f1_score(y_true, pred), 4),
        "roc_auc": round(roc_auc_score(y_true, prob), 4)
    }

results = {
    "logistic_regression": metrics(
        y_test, logistic_pred, logistic_prob
    ),
    "decision_tree": metrics(
        y_test, tree_pred, tree_prob
    ),
    "test_rows": int(len(X_test)),
    "train_rows": int(len(X_train))
}

# ------------------------------------------------------------
# CHOOSE PROPENSITY MODEL
# ------------------------------------------------------------

if (
    results["logistic_regression"]["roc_auc"]
    >=
    results["decision_tree"]["roc_auc"]
):
    selected_model = logistic
    selected_name = "logistic_regression"
else:
    selected_model = tree
    selected_name = "decision_tree"

df["conversion_probability"] = selected_model.predict_proba(X)[:, 1]

# ------------------------------------------------------------
# CUSTOMER SEGMENTATION
# ------------------------------------------------------------

segment_features = [
    "annual_revenue",
    "employees",
    "engagement_score",
    "website_visits",
    "email_opens",
    "email_clicks",
    "sales_contacts",
    "previous_applications",
    "expected_net_value"
]

segment_data = df[segment_features].copy()

segment_scaler = StandardScaler()
segment_scaled = segment_scaler.fit_transform(segment_data)

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df["customer_segment"] = kmeans.fit_predict(segment_scaled)

joblib.dump(
    {
        "scaler": segment_scaler,
        "model": kmeans,
        "features": segment_features
    },
    MODEL_DIR / "kmeans_segments.joblib"
)

# ------------------------------------------------------------
# ANOMALY / GAMING DETECTION
# ------------------------------------------------------------

anomaly_features = [
    "website_visits",
    "email_opens",
    "email_clicks",
    "sales_contacts",
    "previous_applications",
    "engagement_score",
    "days_since_last_interaction"
]

anomaly_data = StandardScaler().fit_transform(
    df[anomaly_features]
)

isolation_forest = IsolationForest(
    n_estimators=200,
    contamination=0.03,
    random_state=42
)

anomaly_prediction = isolation_forest.fit_predict(anomaly_data)

df["ml_anomaly_flag"] = (
    anomaly_prediction == -1
).astype(int)

df["anomaly_score"] = -isolation_forest.score_samples(
    anomaly_data
)

joblib.dump(
    isolation_forest,
    MODEL_DIR / "isolation_forest.joblib"
)

# ------------------------------------------------------------
# BUSINESS VALUE SCORING
# ------------------------------------------------------------

df["expected_value_from_conversion"] = (
    df["conversion_probability"] *
    df["expected_revenue"]
)

df["expected_business_value"] = (
    df["expected_value_from_conversion"] -
    df["acquisition_cost"]
)

# Penalize risky/gaming records
df["risk_adjusted_value"] = (
    df["expected_business_value"] -
    df["gaming_risk_score"] * 25
)

# ------------------------------------------------------------
# TARGET PRIORITIZATION
# ------------------------------------------------------------

df["target_priority_score"] = (
    df["conversion_probability"] * 0.45 +
    (
        df["expected_business_value"]
        .rank(pct=True)
    ) * 0.35 +
    df["engagement_score"].rank(pct=True) * 0.20
)

df.loc[
    df["gaming_risk_score"] >= 60,
    "target_priority_score"
] *= 0.25

df["recommended_action"] = np.select(
    [
        (df["gaming_risk_score"] >= 60),
        (
            (df["conversion_probability"] >= 0.60) &
            (df["expected_business_value"] > 5000)
        ),
        (
            (df["conversion_probability"] >= 0.40) &
            (df["conversion_probability"] < 0.60)
        ),
        (df["conversion_probability"] < 0.40)
    ],
    [
        "REVIEW_FOR_GAMING",
        "PRIORITIZE_HIGH_VALUE_OUTREACH",
        "NURTURE_AND_RETARGET",
        "LOW_PRIORITY"
    ],
    default="REVIEW"
)

# ------------------------------------------------------------
# SAVE
# ------------------------------------------------------------

joblib.dump(
    selected_model,
    MODEL_DIR / f"{selected_name}.joblib"
)

with open(
    MODEL_DIR / "model_metrics.json",
    "w"
) as f:
    json.dump(results, f, indent=2)

df.to_csv(OUTPUT, index=False)

print("=" * 70)
print("ML PIPELINE COMPLETE")
print("=" * 70)

print("\nMODEL PERFORMANCE")
print(json.dumps(results, indent=2))

print("\nSELECTED MODEL")
print(selected_name)

print("\nSEGMENTS")
print(df["customer_segment"].value_counts().sort_index())

print("\nML ANOMALIES")
print(df["ml_anomaly_flag"].value_counts())

print("\nRECOMMENDED ACTIONS")
print(df["recommended_action"].value_counts())

print("\nTOP TARGETS")
print(
    df[
        [
            "prospect_id",
            "conversion_probability",
            "expected_business_value",
            "risk_adjusted_value",
            "gaming_risk_score",
            "recommended_action"
        ]
    ]
    .sort_values("risk_adjusted_value", ascending=False)
    .head(10)
    .to_string(index=False)
)

print(f"\nScored data: {OUTPUT}")
print("=" * 70)
