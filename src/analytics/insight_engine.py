from pathlib import Path
import pandas as pd
import numpy as np

DATA = Path("data/processed/scored_prospects.csv")

df = pd.read_csv(DATA)


def pct(x):
    return f"{x * 100:.1f}%"


def money(x):
    if abs(x) >= 1_000_000_000:
        return f"${x / 1_000_000_000:.2f}B"
    if abs(x) >= 1_000_000:
        return f"${x / 1_000_000:.2f}M"
    if abs(x) >= 1_000:
        return f"${x / 1_000:.1f}K"
    return f"${x:,.0f}"


def generate_insights():

    # --------------------------------------------------------
    # OVERVIEW
    # --------------------------------------------------------

    total = len(df)
    conversions = int(df["converted"].sum())
    conversion_rate = df["converted"].mean()

    high_value = int(
        df["high_value_target"].sum()
    )

    gaming = int(
        (df["gaming_risk_score"] >= 60).sum()
    )

    # --------------------------------------------------------
    # CHANNEL ANALYSIS
    # --------------------------------------------------------

    channel = (
        df.groupby("channel")
        .agg(
            prospects=("prospect_id", "count"),
            conversions=("converted", "sum"),
            conversion_rate=("converted", "mean"),
            total_value=("expected_net_value", "sum"),
            avg_business_value=(
                "expected_business_value",
                "mean"
            )
        )
        .reset_index()
    )

    best_channel = channel.loc[
        channel["conversion_rate"].idxmax()
    ]

    best_channel_value = channel.loc[
        channel["total_value"].idxmax()
    ]

    # --------------------------------------------------------
    # CAMPAIGN ANALYSIS
    # --------------------------------------------------------

    campaign = (
        df.groupby("campaign")
        .agg(
            prospects=("prospect_id", "count"),
            conversions=("converted", "sum"),
            conversion_rate=("converted", "mean"),
            total_value=("expected_net_value", "sum")
        )
        .reset_index()
    )

    best_campaign = campaign.loc[
        campaign["conversion_rate"].idxmax()
    ]

    # --------------------------------------------------------
    # SEGMENT ANALYSIS
    # --------------------------------------------------------

    segment = (
        df.groupby("customer_segment")
        .agg(
            prospects=("prospect_id", "count"),
            conversion_rate=("converted", "mean"),
            avg_revenue=("annual_revenue", "mean"),
            avg_engagement=("engagement_score", "mean"),
            avg_business_value=(
                "expected_business_value",
                "mean"
            )
        )
        .reset_index()
    )

    best_segment = segment.loc[
        segment["conversion_rate"].idxmax()
    ]

    # --------------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------------

    actions = (
        df.groupby("recommended_action")
        .agg(
            prospects=("prospect_id", "count"),
            avg_probability=(
                "conversion_probability",
                "mean"
            ),
            total_value=(
                "expected_business_value",
                "sum"
            )
        )
        .reset_index()
    )

    priority = df[
        df["recommended_action"]
        .eq("PRIORITIZE_HIGH_VALUE_OUTREACH")
    ]

    personalized = df[
        df["recommended_action"]
        .eq("TARGET_WITH_PERSONALIZED_OFFER")
    ]

    gaming_df = df[
        df["recommended_action"]
        .eq("REVIEW_FOR_GAMING")
    ]

    # --------------------------------------------------------
    # NATURAL-LANGUAGE INSIGHTS
    # --------------------------------------------------------

    insights = []

    insights.append(
        f"The acquisition engine analyzed {total:,} prospects "
        f"and identified {conversions:,} conversions, producing "
        f"an overall conversion rate of {pct(conversion_rate)}."
    )

    insights.append(
        f"{best_channel['channel']} is the strongest acquisition "
        f"channel by conversion rate at "
        f"{pct(best_channel['conversion_rate'])}, "
        f"with {int(best_channel['conversions']):,} conversions."
    )

    insights.append(
        f"{best_channel_value['channel']} generates the largest "
        f"aggregate expected net value at "
        f"{money(best_channel_value['total_value'])}."
    )

    insights.append(
        f"{best_campaign['campaign']} is the strongest campaign "
        f"by conversion rate at "
        f"{pct(best_campaign['conversion_rate'])}."
    )

    insights.append(
        f"Customer segment {int(best_segment['customer_segment'])} "
        f"has the highest observed conversion rate at "
        f"{pct(best_segment['conversion_rate'])}, "
        f"indicating a concentrated high-propensity audience."
    )

    insights.append(
        f"The scoring engine identified {high_value:,} "
        f"high-value prospects suitable for focused targeting."
    )

    insights.append(
        f"{len(priority):,} prospects are currently classified "
        f"for high-value outreach, while {len(personalized):,} "
        f"are better suited to personalized offers."
    )

    insights.append(
        f"{gaming:,} prospects require gaming-risk review. "
        f"These records should be screened before aggressive "
        f"acquisition activity."
    )

    # --------------------------------------------------------
    # EXECUTIVE SUMMARY
    # --------------------------------------------------------

    executive_summary = (
        f"AIM identified a {pct(conversion_rate)} overall "
        f"acquisition rate across {total:,} prospects. "
        f"The strongest channel by conversion is "
        f"{best_channel['channel']} "
        f"({pct(best_channel['conversion_rate'])}), while "
        f"{best_campaign['campaign']} leads campaigns at "
        f"{pct(best_campaign['conversion_rate'])}. "
        f"The model recommends {len(priority):,} prospects "
        f"for high-value outreach and {len(personalized):,} "
        f"for personalized offers. "
        f"{gaming:,} records have elevated gaming risk and "
        f"should be reviewed before targeting."
    )

    # --------------------------------------------------------
    # WHY / WHAT NEXT
    # --------------------------------------------------------

    what_next = [
        f"Prioritize {best_channel['channel']} for high-propensity acquisition campaigns.",
        f"Evaluate scaling {best_campaign['campaign']} because it currently has the highest campaign conversion rate.",
        f"Use segment {int(best_segment['customer_segment'])} as a high-propensity audience for targeted campaigns.",
        f"Route {gaming:,} gaming-risk records to review rather than direct acquisition.",
        "Use conversion probability and expected business value together instead of propensity alone when prioritizing prospects."
    ]

    return {
        "executive_summary": executive_summary,
        "insights": insights,
        "actions": what_next,
        "metrics": {
            "prospects": total,
            "conversions": conversions,
            "conversion_rate": round(float(conversion_rate), 4),
            "high_value_targets": high_value,
            "gaming_risk_records": gaming,
            "best_channel": best_channel["channel"],
            "best_channel_conversion_rate": round(
                float(best_channel["conversion_rate"]),
                4
            ),
            "best_campaign": best_campaign["campaign"],
            "best_campaign_conversion_rate": round(
                float(best_campaign["conversion_rate"]),
                4
            ),
            "best_segment": int(
                best_segment["customer_segment"]
            )
        }
    }


if __name__ == "__main__":

    import json

    result = generate_insights()

    print("=" * 70)
    print("AIM AUTOMATED INSIGHT ENGINE")
    print("=" * 70)

    print("\nEXECUTIVE SUMMARY")
    print(result["executive_summary"])

    print("\nKEY INSIGHTS")
    for i, insight in enumerate(
        result["insights"],
        1
    ):
        print(f"{i}. {insight}")

    print("\nRECOMMENDED ACTIONS")
    for i, action in enumerate(
        result["actions"],
        1
    ):
        print(f"{i}. {action}")

    print("\nMETRICS")
    print(
        json.dumps(
            result["metrics"],
            indent=2
        )
    )

    output = Path(
        "data/processed/automated_insights.json"
    )

    with open(output, "w") as f:
        json.dump(
            result,
            f,
            indent=2
        )

    print(f"\nSaved: {output}")
    print("=" * 70)

