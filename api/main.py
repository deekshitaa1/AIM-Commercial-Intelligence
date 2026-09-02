from pathlib import Path
import json

import pandas as pd
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.analytics.genai_engine import generate_answer


# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA = BASE_DIR / "data" / "processed" / "scored_prospects.csv"
MODEL_METRICS = (
    BASE_DIR
    / "data"
    / "processed"
    / "models"
    / "model_metrics.json"
)
INSIGHTS = (
    BASE_DIR
    / "data"
    / "processed"
    / "automated_insights.json"
)


# =========================================================
# APP
# =========================================================

app = FastAPI(
    title="AIM Commercial Marketing Intelligence API",
    version="1.2.0",
    description=(
        "Commercial acquisition analytics, ML targeting, "
        "customer segmentation, anomaly detection, "
        "business value optimization and grounded AI reasoning."
    ),
)


# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # Local development
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5175",

        # Production dashboard
        "https://aim-commercial-intelligence-dashboard.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================================================
# LOAD DATA
# =========================================================

if not DATA.exists():
    raise FileNotFoundError(
        f"Required analytics dataset not found: {DATA}"
    )

if not MODEL_METRICS.exists():
    raise FileNotFoundError(
        f"Required model metrics not found: {MODEL_METRICS}"
    )

if not INSIGHTS.exists():
    raise FileNotFoundError(
        f"Required insights file not found: {INSIGHTS}"
    )


df = pd.read_csv(DATA)

with open(MODEL_METRICS, "r", encoding="utf-8") as f:
    model_metrics = json.load(f)

with open(INSIGHTS, "r", encoding="utf-8") as f:
    automated_insights = json.load(f)


# =========================================================
# REQUEST MODELS
# =========================================================

class InsightQuestion(BaseModel):
    question: str


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():
    return {
        "product": "AIM Commercial Marketing Intelligence",
        "status": "operational",
        "records": len(df),
        "capabilities": [
            "acquisition_analytics",
            "propensity_modeling",
            "customer_segmentation",
            "gaming_detection",
            "business_value_optimization",
            "automated_insights",
            "grounded_genai_reasoning",
        ],
    }


# =========================================================
# HEALTH
# =========================================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "records_loaded": len(df),
    }


# =========================================================
# EXECUTIVE OVERVIEW
# =========================================================

@app.get("/api/v1/overview")
def overview():
    return {
        "prospects": int(len(df)),
        "conversions": int(df["converted"].sum()),
        "conversion_rate": round(
            float(df["converted"].mean()),
            4,
        ),
        "total_expected_revenue": round(
            float(df["expected_revenue"].sum()),
            2,
        ),
        "total_acquisition_cost": round(
            float(df["acquisition_cost"].sum()),
            2,
        ),
        "total_expected_net_value": round(
            float(df["expected_net_value"].sum()),
            2,
        ),
        "high_value_targets": int(
            df["high_value_target"].sum()
        ),
        "gaming_risk_records": int(
            (df["gaming_risk_score"] >= 60).sum()
        ),
    }


# =========================================================
# MODEL METRICS
# =========================================================

@app.get("/api/v1/models")
def models():
    return model_metrics


# =========================================================
# AUTOMATED INSIGHTS
# =========================================================

@app.get("/api/v1/insights")
def insights():
    return automated_insights


@app.get("/api/v1/insights/summary")
def insight_summary():
    return {
        "summary": automated_insights["executive_summary"],
        "key_insights": automated_insights["insights"],
        "recommended_actions": automated_insights["actions"],
        "metrics": automated_insights.get(
            "metrics",
            {},
        ),
    }


# =========================================================
# CHANNEL ANALYTICS
# =========================================================

@app.get("/api/v1/channels")
def channels():

    result = (
        df.groupby("channel")
        .agg(
            prospects=("prospect_id", "count"),
            conversions=("converted", "sum"),
            conversion_rate=("converted", "mean"),
            expected_net_value=(
                "expected_net_value",
                "sum",
            ),
            avg_business_value=(
                "expected_business_value",
                "mean",
            ),
        )
        .reset_index()
    )

    result["conversion_rate"] = result[
        "conversion_rate"
    ].round(4)

    result["expected_net_value"] = result[
        "expected_net_value"
    ].round(2)

    result["avg_business_value"] = result[
        "avg_business_value"
    ].round(2)

    return result.to_dict(orient="records")


# =========================================================
# CAMPAIGN ANALYTICS
# =========================================================

@app.get("/api/v1/campaigns")
def campaigns():

    result = (
        df.groupby("campaign")
        .agg(
            prospects=("prospect_id", "count"),
            conversions=("converted", "sum"),
            conversion_rate=("converted", "mean"),
            expected_net_value=(
                "expected_net_value",
                "sum",
            ),
        )
        .reset_index()
    )

    result["conversion_rate"] = result[
        "conversion_rate"
    ].round(4)

    result["expected_net_value"] = result[
        "expected_net_value"
    ].round(2)

    return result.to_dict(orient="records")


# =========================================================
# CUSTOMER SEGMENTATION
# =========================================================

@app.get("/api/v1/segments")
def segments():

    result = (
        df.groupby("customer_segment")
        .agg(
            prospects=("prospect_id", "count"),
            avg_revenue=(
                "annual_revenue",
                "mean",
            ),
            avg_engagement=(
                "engagement_score",
                "mean",
            ),
            conversion_rate=(
                "converted",
                "mean",
            ),
            avg_business_value=(
                "expected_business_value",
                "mean",
            ),
        )
        .reset_index()
    )

    return result.round(2).to_dict(
        orient="records"
    )


# =========================================================
# ML TARGETING
# =========================================================

@app.get("/api/v1/targets")
def targets(
    limit: int = Query(
        default=20,
        ge=1,
        le=500,
    )
):

    result = (
        df[
            [
                "prospect_id",
                "industry",
                "company_size",
                "campaign",
                "channel",
                "conversion_probability",
                "expected_business_value",
                "marketing_priority_score",
                "priority_band",
                "gaming_risk_score",
                "recommended_action",
            ]
        ]
        .sort_values(
            "marketing_priority_score",
            ascending=False,
        )
        .head(limit)
    )

    return result.to_dict(
        orient="records"
    )


# =========================================================
# INDIVIDUAL PROSPECT
# =========================================================

@app.get("/api/v1/prospects/{prospect_id}")
def prospect(prospect_id: int):

    result = df[
        df["prospect_id"] == prospect_id
    ]

    if result.empty:
        return {
            "error": "Prospect not found"
        }

    return result.iloc[0].to_dict()


# =========================================================
# ANOMALIES / GAMING
# =========================================================

@app.get("/api/v1/anomalies")
def anomalies(
    limit: int = Query(
        default=50,
        ge=1,
        le=500,
    )
):

    result = (
        df[
            (df["ml_anomaly_flag"] == 1)
            | (df["gaming_risk_score"] >= 60)
        ][
            [
                "prospect_id",
                "previous_applications",
                "website_visits",
                "email_clicks",
                "sales_contacts",
                "gaming_risk_score",
                "ml_anomaly_flag",
                "anomaly_score",
            ]
        ]
        .sort_values(
            [
                "gaming_risk_score",
                "anomaly_score",
            ],
            ascending=False,
        )
        .head(limit)
    )

    return result.to_dict(
        orient="records"
    )


# =========================================================
# BUSINESS RECOMMENDATIONS
# =========================================================

@app.get("/api/v1/recommendations")
def recommendations():

    result = (
        df.groupby("recommended_action")
        .agg(
            prospects=("prospect_id", "count"),
            avg_conversion_probability=(
                "conversion_probability",
                "mean",
            ),
            total_business_value=(
                "expected_business_value",
                "sum",
            ),
        )
        .reset_index()
    )

    return result.round(4).to_dict(
        orient="records"
    )


# =========================================================
# GROUNDED AI / ASK AIM
# =========================================================

@app.post("/api/v1/genai")
def genai(request: InsightQuestion):

    question = request.question.strip()

    if not question:
        return {
            "mode": "grounded_analytics",
            "question": "",
            "answer": "Please enter a business question.",
            "evidence": {},
            "recommendation": (
                "Ask about channels, campaigns, "
                "segments, targets, business value, "
                "or gaming risk."
            ),
        }

    return generate_answer(question)