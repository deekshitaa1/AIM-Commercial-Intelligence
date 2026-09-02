import json
from pathlib import Path

import pandas as pd


INSIGHTS_PATH = Path("data/processed/automated_insights.json")
SCORED_PATH = Path("data/processed/scored_prospects.csv")


def load_context() -> dict:
    """Load precomputed AIM analytics insights."""
    with open(INSIGHTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_scored_data() -> pd.DataFrame:
    """Load the prospect-level ML/business scoring dataset."""
    return pd.read_csv(SCORED_PATH)


def generate_answer(question: str) -> dict:
    """
    Generate a grounded business answer using the actual
    AIM analytics dataset.
    """
    context = load_context()
    df = load_scored_data()

    result = answer_business_question(question, context, df)

    return {
        "mode": "grounded_analytics",
        "question": question,
        "answer": result["answer"],
        "evidence": result["evidence"],
        "recommendation": result["recommendation"],
    }


def answer_business_question(
    question: str,
    context: dict,
    df: pd.DataFrame,
) -> dict:
    """Route the question to the appropriate business analysis."""

    q = question.lower().strip()
    metrics = context["metrics"]

    # =========================================================
    # CHANNEL ANALYSIS
    # =========================================================

    if any(x in q for x in ["channel", "channels"]):

        grouped = (
            df.groupby("channel")
            .agg(
                prospects=("prospect_id", "count"),
                conversions=("converted", "sum"),
                expected_net_value=("expected_net_value", "sum"),
            )
            .reset_index()
        )

        grouped["conversion_rate"] = (
            grouped["conversions"] / grouped["prospects"]
        )

        best = grouped.sort_values(
            ["conversion_rate", "expected_net_value"],
            ascending=False,
        ).iloc[0]

        evidence = {
            "best_channel": str(best["channel"]),
            "conversion_rate": round(
                float(best["conversion_rate"]),
                4,
            ),
            "prospects": int(best["prospects"]),
            "conversions": int(best["conversions"]),
            "expected_net_value": round(
                float(best["expected_net_value"]),
                2,
            ),
        }

        return {
            "answer": (
                f"{best['channel']} is currently the strongest "
                f"acquisition channel in the analyzed dataset, "
                f"with a {best['conversion_rate'] * 100:.1f}% "
                f"conversion rate across "
                f"{int(best['prospects']):,} prospects. "
                f"It generated {int(best['conversions']):,} "
                f"conversions and approximately "
                f"${best['expected_net_value']:,.0f} "
                f"in expected net value."
            ),
            "evidence": evidence,
            "recommendation": (
                f"Prioritize {best['channel']} for high-propensity "
                "acquisition campaigns and evaluate whether additional "
                "investment improves incremental commercial value."
            ),
        }

    # =========================================================
    # CAMPAIGN ANALYSIS
    # =========================================================

    if any(x in q for x in ["campaign", "campaigns"]):

        grouped = (
            df.groupby("campaign")
            .agg(
                prospects=("prospect_id", "count"),
                conversions=("converted", "sum"),
                expected_net_value=("expected_net_value", "sum"),
            )
            .reset_index()
        )

        grouped["conversion_rate"] = (
            grouped["conversions"] / grouped["prospects"]
        )

        best = grouped.sort_values(
            ["conversion_rate", "expected_net_value"],
            ascending=False,
        ).iloc[0]

        evidence = {
            "best_campaign": str(best["campaign"]),
            "conversion_rate": round(
                float(best["conversion_rate"]),
                4,
            ),
            "prospects": int(best["prospects"]),
            "conversions": int(best["conversions"]),
            "expected_net_value": round(
                float(best["expected_net_value"]),
                2,
            ),
        }

        return {
            "answer": (
                f"{best['campaign']} is the strongest campaign "
                f"by conversion rate at "
                f"{best['conversion_rate'] * 100:.1f}%. "
                f"It generated {int(best['conversions']):,} "
                f"conversions from "
                f"{int(best['prospects']):,} prospects and "
                f"approximately "
                f"${best['expected_net_value']:,.0f} "
                "in expected net value."
            ),
            "evidence": evidence,
            "recommendation": (
                f"Evaluate scaling {best['campaign']} while "
                "monitoring incremental conversion, acquisition "
                "cost, and expected commercial value."
            ),
        }

    # =========================================================
    # HIGH-VALUE TARGETS
    # =========================================================

    if any(
        x in q
        for x in [
            "high value",
            "highest value",
            "top prospects",
            "target",
            "targets",
        ]
    ):

        top = (
            df.sort_values(
                "expected_business_value",
                ascending=False,
            )
            .head(10)
        )

        evidence = {
            "high_value_targets": int(
                metrics["high_value_targets"]
            ),
            "top_prospect_ids": [
                int(x)
                for x in top["prospect_id"].tolist()
            ],
            "top_expected_values": [
                round(
                    float(x),
                    2,
                )
                for x in top["expected_business_value"].tolist()
            ],
        }

        return {
            "answer": (
                f"AIM identified "
                f"{int(metrics['high_value_targets']):,} "
                "high-value prospects. The highest-value "
                "opportunities should be prioritized using both "
                "predicted conversion probability and expected "
                "business value rather than propensity alone."
            ),
            "evidence": evidence,
            "recommendation": (
                "Route the highest-ranked prospects to focused "
                "sales or personalized acquisition outreach."
            ),
        }

    # =========================================================
    # GAMING / RISK / ANOMALIES
    # =========================================================

    if any(
        x in q
        for x in [
            "gaming",
            "risk",
            "anomal",
            "fraud",
        ]
    ):

        risk = df[
            df["gaming_risk_score"] >= 60
        ]

        evidence = {
            "gaming_risk_records": int(len(risk)),
            "average_risk_score": round(
                float(
                    risk["gaming_risk_score"].mean()
                ),
                2,
            )
            if len(risk)
            else 0,
        }

        return {
            "answer": (
                f"{len(risk):,} prospects currently meet "
                "the elevated gaming-risk threshold. "
                "These records should not be treated the same "
                "as normal acquisition opportunities."
            ),
            "evidence": evidence,
            "recommendation": (
                "Route elevated-risk records for review before "
                "aggressive acquisition activity or high-value "
                "outreach."
            ),
        }

    # =========================================================
    # CUSTOMER SEGMENTATION
    # =========================================================

    if any(
        x in q
        for x in [
            "segment",
            "segmentation",
            "customer group",
        ]
    ):

        grouped = (
            df.groupby("customer_segment")
            .agg(
                prospects=("prospect_id", "count"),
                conversion_rate=("converted", "mean"),
                avg_engagement=("engagement_score", "mean"),
                avg_business_value=(
                    "expected_business_value",
                    "mean",
                ),
            )
            .reset_index()
        )

        best = grouped.sort_values(
            ["conversion_rate", "avg_business_value"],
            ascending=False,
        ).iloc[0]

        evidence = {
            "best_segment": int(
                best["customer_segment"]
            ),
            "prospects": int(best["prospects"]),
            "conversion_rate": round(
                float(best["conversion_rate"]),
                4,
            ),
            "avg_engagement": round(
                float(best["avg_engagement"]),
                2,
            ),
            "avg_business_value": round(
                float(best["avg_business_value"]),
                2,
            ),
        }

        return {
            "answer": (
                f"Customer segment "
                f"{int(best['customer_segment'])} is the "
                "strongest observed segment, with a "
                f"{best['conversion_rate'] * 100:.1f}% "
                "conversion rate across "
                f"{int(best['prospects']):,} prospects. "
                f"Its average engagement score is "
                f"{best['avg_engagement']:.1f}."
            ),
            "evidence": evidence,
            "recommendation": (
                f"Use segment "
                f"{int(best['customer_segment'])} as a "
                "high-propensity audience for targeted "
                "acquisition."
            ),
        }

    # =========================================================
    # EXECUTIVE / GENERAL QUESTION
    # =========================================================

    return {
        "answer": context["executive_summary"],
        "evidence": metrics,
        "recommendation": (
            "Use conversion probability, expected business "
            "value, engagement, and gaming risk together "
            "when making acquisition decisions."
        ),
    }