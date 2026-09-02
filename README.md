<div align="center">

# AIM
## Commercial Marketing Intelligence

**End-to-end Data Analytics for Customer Acquisition, Marketing Performance & Commercial Decision Support**

<br>

<a href="https://aim-commercial-intelligence-dashboard.onrender.com/">
  <img src="https://img.shields.io/badge/OPEN%20LIVE%20DASHBOARD-111827?style=for-the-badge&logo=googlechrome&logoColor=white" />
</a>
&nbsp;
<a href="https://aim-commercial-intelligence-api-jnrs.onrender.com/">
  <img src="https://img.shields.io/badge/AIM%20API-1F2937?style=for-the-badge&logo=fastapi&logoColor=white" />
</a>
&nbsp;
<a href="https://aim-commercial-intelligence-api-jnrs.onrender.com/health">
  <img src="https://img.shields.io/badge/API%20HEALTH-16A34A?style=for-the-badge&logo=statuspage&logoColor=white" />
</a>

</div>

---

# LIVE PRODUCT

<table>
<tr>
<td width="68%">

### AIM Commercial Marketing Intelligence Dashboard

A deployed analytics application for exploring **customer acquisition KPIs, channel performance, campaign effectiveness, customer segmentation, prospect prioritization, anomaly/risk analysis, and grounded business insights.**

**Dashboard:** [Open Live Application](https://aim-commercial-intelligence-dashboard.onrender.com/)

**Backend:** [Open AIM API](https://aim-commercial-intelligence-api-jnrs.onrender.com/)

**Health:** [Check API Status](https://aim-commercial-intelligence-api-jnrs.onrender.com/health)

</td>
<td width="32%">

### PRODUCT LAYER

`Dashboard`

`Analytics API`

`Predictive Scoring`

`Business Insights`

`Decision Support`

</td>
</tr>
</table>

### Quick Preview

> **Live dashboard:** customer acquisition KPIs, channel and campaign performance, segmentation, prospect prioritization, risk analysis, and grounded business analytics through **Ask AIM**.

---

# ANALYTICS AT A GLANCE

<table>
<tr>
<td align="center"><strong>25,000</strong><br/>Prospects</td>
<td align="center"><strong>7,479</strong><br/>Conversions</td>
<td align="center"><strong>29.92%</strong><br/>Conversion Rate</td>
<td align="center"><strong>$1.127B</strong><br/>Expected Revenue</td>
<td align="center"><strong>$1.074B</strong><br/>Expected Net Value</td>
</tr>
</table>

| Commercial KPI | Result |
|---|---:|
| Prospects analyzed | **25,000** |
| Conversions | **7,479** |
| Conversion rate | **29.92%** |
| High-value targets | **1,186** |
| Gaming-risk records | **114** |
| Expected revenue | **$1.127B** |
| Acquisition cost | **$52.93M** |
| Expected net value | **$1.074B** |

> All figures above are generated from the project's synthetic dataset and are not real company metrics.

---

# BUSINESS PROBLEM

Marketing teams need to understand not only **what happened**, but also **where value exists and what action should happen next**.

AIM addresses questions such as:

| Business Question | Analytical Layer |
|---|---|
| Which acquisition channels perform best? | Channel performance analysis |
| Which campaigns convert efficiently? | Campaign analysis |
| Which customer groups are most valuable? | Segmentation |
| Which prospects should sales prioritize? | Predictive scoring |
| Where is expected commercial value highest? | Expected-value analysis |
| Which records need investigation? | Anomaly / risk analysis |
| What does the available data indicate? | Ask AIM |

**Goal:** move from descriptive reporting to **actionable customer-acquisition decisions**.

---

# DATA ANALYST WORKFLOW

```text
                    BUSINESS QUESTION
                           │
                           ▼
                  RAW PROSPECT DATA
                           │
                           ▼
                DATA CLEANING & QA
                           │
                           ▼
                 FEATURE ENGINEERING
                           │
                           ▼
                 SQL + PYTHON ANALYSIS
                           │
                           ▼
                EDA + KPI DEVELOPMENT
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
         CHANNEL       CAMPAIGN      SEGMENTATION
         ANALYSIS      ANALYSIS       ANALYSIS
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                  PREDICTIVE ANALYSIS
                           │
                           ▼
                 BUSINESS VALUE SCORE
                           │
                           ▼
                PROSPECT PRIORITIZATION
                           │
                           ▼
                 DASHBOARD + REPORTING
                           │
                           ▼
                  BUSINESS RECOMMENDATION
```

---

# DATASET

AIM analyzes **25,000 synthetic commercial prospect records** with **26 raw fields** covering:

`Industry` · `Region` · `Company Size` · `Annual Revenue` · `Employees` · `Years in Business` · `Customer Relationship` · `Website Visits` · `Email Opens` · `Email Clicks` · `Sales Contacts` · `Previous Applications` · `Campaign` · `Acquisition Channel` · `Engagement` · `Conversion` · `Expected Revenue` · `Acquisition Cost` · `Business Value` · `Gaming / Risk Indicators`

---

# DATA PREPARATION

### Data Quality

- Duplicate prospect removal
- Date parsing and validation
- Numeric validation
- Missing-value handling
- Categorical-value handling
- Data consistency checks

### Feature Engineering

The analytical layer derives features including:

```text
engagement_rate
sales_intensity
revenue_per_employee
is_recent_interaction
is_high_engagement
```

These features support downstream **SQL, Python, statistical, BI, and machine-learning analysis**.

---

# EXPLORATORY DATA ANALYSIS

## Channel Performance

Each acquisition channel is evaluated using:

- Prospect volume
- Conversion volume
- Conversion rate
- Expected revenue
- Acquisition cost
- Expected net value

**Current dataset finding:** Email has the highest conversion rate at **30.8%**.

## Campaign Performance

Campaigns are compared using:

- Conversion rate
- Conversion volume
- Prospect volume
- Expected revenue
- Expected net value

**Current dataset finding:** `Enterprise_Expansion` has the highest campaign conversion rate at **30.6%**.

## Customer Segmentation

Five customer/prospect segments are evaluated using:

`Segment Size` · `Average Revenue` · `Engagement` · `Conversion Rate` · `Average Business Value`

This enables performance analysis beyond overall averages.

---

# COMMERCIAL VALUE ANALYSIS

AIM does not rank prospects only by conversion probability.

For each prospect:

```text
Expected Value
    = Conversion Probability × Expected Revenue
      − Acquisition Cost
```

The value calculation is combined with:

```text
Conversion Propensity
        +
Engagement
        +
Gaming / Risk
        ↓
Marketing Priority Score
```

This creates a practical distinction between:

> **Most likely to convert**

and

> **Most valuable to prioritize**

That distinction is central to the project's commercial analytics approach.

---

# PREDICTIVE ANALYTICS

Machine learning is used as a **decision-support layer inside the analytics workflow**, not as the sole purpose of the project.

| Technique | Business Purpose | Result |
|---|---|---:|
| Logistic Regression | Conversion probability | ROC-AUC **72.46%** |
| Decision Tree | Interpretable comparison model | ROC-AUC **69.62%** |
| K-Means | Prospect segmentation | **5 clusters** |
| Isolation Forest | Anomaly / gaming-risk detection | Risk screening |

### Logistic Regression — Test Set

| Metric | Result |
|---|---:|
| Accuracy | 66.32% |
| Precision | 45.63% |
| Recall | 65.64% |
| F1 | 53.84% |
| ROC-AUC | **72.46%** |

---

# PROSPECT PRIORITIZATION

Analytical outputs are translated into business actions:

| Recommendation | Business Action |
|---|---|
| `PRIORITIZE_HIGH_VALUE_OUTREACH` | Focus sales effort on high-value prospects |
| `TARGET_WITH_PERSONALIZED_OFFER` | Use tailored offers |
| `NURTURE_AND_RETARGET` | Continue engagement |
| `REVIEW_FOR_GAMING` | Investigate elevated-risk records |
| `LOW_PRIORITY` | Deprioritize lower-value opportunities |

### Current Output

**2,664** prospects → high-value outreach  
**8,323** prospects → personalized offers  
**114** records → gaming-risk review

---

# ASK AIM

AIM includes a grounded business-analytics interface for querying generated analytical results.

```text
Which acquisition channel performs best?

Which campaign has the highest conversion rate?

Which customer segment has the highest business value?

Which prospects should sales prioritize?

Which channel generates the highest expected net value?

Which prospects have elevated gaming risk?
```

The current implementation uses the project's generated analytical datasets and calculated metrics as its evidence source rather than inventing unsupported business figures.

---

# BUSINESS INTELLIGENCE OUTPUTS

The pipeline generates reporting-ready datasets:

```text
powerbi/
│
├── executive_kpis.csv
├── channel_performance.csv
├── campaign_performance.csv
├── industry_performance.csv
├── region_performance.csv
├── segment_performance.csv
├── target_prioritization.csv
├── gaming_anomalies.csv
└── recommendations.csv
```

These outputs support:

**Executive KPI reporting** · **Acquisition analysis** · **Campaign analysis** · **Customer segmentation** · **Prospect prioritization** · **Risk analysis** · **Business recommendations**

---

# SYSTEM ARCHITECTURE

```text
┌──────────────────────────────────────────────────────────────┐
│                       COMMERCIAL DATA                        │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 DATA PREPARATION LAYER                      │
│             Cleaning · QA · Feature Engineering             │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                    ANALYTICS ENGINE                          │
│      SQL · Pandas · KPI · EDA · Segmentation · ML           │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 DECISION INTELLIGENCE                       │
│       Expected Value · Scoring · Risk · Recommendations     │
└──────────────────────────────┬───────────────────────────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
┌─────────────────────────┐       ┌──────────────────────────┐
│       AIM API           │       │    AIM DASHBOARD         │
│ FastAPI · REST · JSON   │◄─────►│ React · TypeScript       │
└─────────────────────────┘       └──────────────────────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
                    BUSINESS DECISION SUPPORT
```

---

# TECHNOLOGY STACK

<table>
<tr>
<td width="50%">

### Data Analytics

`Python`  
`Pandas`  
`NumPy`  
`SQL`  
`PostgreSQL`  
`PySpark`

</td>
<td width="50%">

### BI & Visualization

`Power BI`  
`Recharts`

</td>
</tr>
<tr>
<td width="50%">

### Machine Learning

`Scikit-learn`  
`Logistic Regression`  
`Decision Tree`  
`K-Means`  
`Isolation Forest`

</td>
<td width="50%">

### Application Engineering

`FastAPI`  
`React`  
`TypeScript`  
`Vite`  
`REST API`

</td>
</tr>
</table>

---

# API

**Live API:** https://aim-commercial-intelligence-api-jnrs.onrender.com/

**Health Check:** https://aim-commercial-intelligence-api-jnrs.onrender.com/health

### Core Endpoints

```text
GET /health
GET /api/v1/overview
GET /api/v1/models
GET /api/v1/insights
GET /api/v1/insights/summary
GET /api/v1/channels
GET /api/v1/campaigns
GET /api/v1/segments
GET /api/v1/targets
GET /api/v1/prospects/{prospect_id}
GET /api/v1/anomalies
GET /api/v1/recommendations
GET /api/v1/genai
```

---

# PROJECT STRUCTURE

```text
AIM-Commercial-Intelligence/
│
├── api/
│   └── main.py
│
├── data/
│   ├── raw/
│   │   └── commercial_marketing_data.csv
│   └── processed/
│       ├── commercial_marketing_clean.csv
│       ├── scored_prospects.csv
│       ├── automated_insights.json
│       ├── models/
│       │   ├── logistic_regression.joblib
│       │   ├── kmeans_segments.joblib
│       │   ├── isolation_forest.joblib
│       │   └── model_metrics.json
│       └── powerbi/
│
├── sql/
├── src/
│   ├── data/
│   ├── models/
│   └── analytics/
│
├── dashboard/
├── notebooks/
├── tests/
├── requirements.txt
└── README.md
```

---

# WHAT THIS PROJECT DEMONSTRATES

### Data Analysis

Data cleaning · EDA · KPI development · funnel analysis · channel analysis · campaign analysis · segmentation · business-value analysis · risk analysis

### SQL

Business aggregations · filtering · grouping · KPI calculations · analytical data preparation · dimensional performance analysis

### Python

Pandas transformation · feature engineering · statistical analysis · automated reporting · ML/BI data preparation

### Machine Learning

Classification · model evaluation · clustering · anomaly detection · probability-based prospect scoring

### Business Intelligence

Executive KPIs · marketing dashboards · campaign/channel reporting · segment analysis · action-oriented recommendations

### Decision Support

Expected-value analysis · marketing prioritization · customer targeting · risk-aware recommendations

---

# THE ANALYST STORY

```text
WHAT HAPPENED?
      │
      ▼
Descriptive & KPI Analysis
      │
      ▼
WHY DID IT HAPPEN?
      │
      ▼
Channel · Campaign · Segment Analysis
      │
      ▼
WHAT IS LIKELY TO HAPPEN?
      │
      ▼
Conversion Probability · Segmentation · Risk
      │
      ▼
WHAT SHOULD WE DO?
      │
      ▼
Expected Value · Prioritization · Recommendations
```

AIM is therefore positioned as a **business-focused Data Analytics project**, with machine learning used where it strengthens the decision-making workflow.

---

# LIVE LINKS

| Resource | Link |
|---|---|
| **AIM Dashboard** | [Launch Live Dashboard](https://aim-commercial-intelligence-dashboard.onrender.com/) |
| **AIM API** | [Open API](https://aim-commercial-intelligence-api-jnrs.onrender.com/) |
| **API Health** | [Health Check](https://aim-commercial-intelligence-api-jnrs.onrender.com/health) |

---

## Disclaimer

This is an independent portfolio project using **synthetically generated data**. It is not affiliated with, endorsed by, or sponsored by American Express and does not use confidential or proprietary company data.

<div align="center">

---

### AIM
**DATA → INSIGHT → VALUE → DECISION**

</div>