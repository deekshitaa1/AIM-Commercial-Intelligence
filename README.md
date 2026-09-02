<div align="center">

# AIM
### Commercial Marketing Intelligence

**An end-to-end Data Analytics & Decision Intelligence platform for customer acquisition.**

<p>
  <img src="https://img.shields.io/badge/Data%20Analytics-0F172A?style=for-the-badge&logo=googleanalytics&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQL-111827?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=111827" />
  <img src="https://img.shields.io/badge/FastAPI-059669?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/React-0F172A?style=for-the-badge&logo=react&logoColor=61DAFB" />
</p>

</div>

---

## ◼ Executive Overview

AIM converts prospect, campaign, channel, segment, and acquisition data into **commercially actionable intelligence**.

The project is designed around the workflow used by modern analytics teams:

```text
RAW DATA
   ↓
DATA QUALITY & CLEANING
   ↓
FEATURE ENGINEERING
   ↓
SQL + PYTHON ANALYTICS
   ↓
KPI & PERFORMANCE ANALYSIS
   ↓
SEGMENTATION + PREDICTIVE MODELING
   ↓
EXPECTED VALUE & PRIORITIZATION
   ↓
DASHBOARD + API
   ↓
BUSINESS RECOMMENDATIONS
```

> **Project objective:** move from descriptive reporting to decision-ready commercial analytics — identifying where acquisition performs, which prospects deserve attention, where risk exists, and what action should be taken next.

---

## ◼ Dashboard Preview

### `AIM Commercial Marketing Intelligence`

| Module | Business Question |
|---|---|
| **Executive KPIs** | What is the current acquisition performance? |
| **Channel Performance** | Which acquisition channels deliver value? |
| **Campaign Analysis** | Which campaigns convert efficiently? |
| **Segmentation** | Which customer groups behave differently? |
| **Prospect Prioritization** | Who should sales/marketing contact first? |
| **Risk Analysis** | Which records require review? |
| **Ask AIM** | What does the data say about a business question? |

**Live dashboard:** customer acquisition KPIs, channel and campaign performance, segmentation, prospect prioritization, risk analysis, and grounded business analytics through Ask AIM.

**Backend API:** AIM Commercial Marketing Intelligence API  
**API health:** `/health`

---

## ◼ KPI Snapshot

| Metric | Result |
|:---|---:|
| **Prospects Analyzed** | 25,000 |
| **Conversions** | 7,479 |
| **Conversion Rate** | 29.92% |
| **High-Value Targets** | 1,186 |
| **Gaming-Risk Records** | 114 |
| **Expected Revenue** | **$1.127B** |
| **Acquisition Cost** | $52.93M |
| **Expected Net Value** | **$1.074B** |

---

## ◼ Analytics Layers

### 01 — Data Preparation

- Structured raw prospect and marketing data
- Missing-value and data-quality handling
- Feature engineering for commercial analysis
- Reproducible processed datasets

### 02 — Exploratory & Diagnostic Analytics

Analysis across:

- Acquisition channels
- Campaign performance
- Industry
- Region
- Customer segments
- Conversion behavior
- Acquisition cost
- Revenue potential

### 03 — Predictive Analytics

| Model | Purpose | ROC-AUC |
|---|---|---:|
| Logistic Regression | Conversion probability | **72.46%** |
| Decision Tree | Non-linear conversion patterns | 69.62% |
| K-Means | Customer/prospect segmentation | 5 clusters |
| Isolation Forest | Anomaly & gaming-risk detection | Risk screening |

**Logistic Regression metrics:** Accuracy 66.32% · Precision 45.63% · Recall 65.64% · F1 53.84% · ROC-AUC 72.46%

### 04 — Commercial Value

AIM translates model output into business value rather than stopping at model accuracy.

```text
Expected Value
= Conversion Probability × Expected Revenue − Acquisition Cost
```

This enables prospect prioritization based on **expected commercial impact**.

---

## ◼ Decision Engine

AIM converts analytics into operational recommendations:

| Decision | Meaning |
|---|---|
| `PRIORITIZE_HIGH_VALUE_OUTREACH` | High expected-value prospects deserve immediate attention |
| `TARGET_WITH_PERSONALIZED_OFFER` | Use targeted messaging or offers |
| `NURTURE_AND_RETARGET` | Continue lower-intensity engagement |
| `REVIEW_FOR_GAMING` | Investigate anomalous behavior |
| `LOW_PRIORITY` | Deprioritize based on expected value |

### Current Prioritization Output

- **2,664** high-value outreach prospects
- **8,323** personalized-offer prospects
- **114** gaming-risk records for review

---

## ◼ Business Intelligence Outputs

The pipeline produces BI-ready datasets for dashboarding and reporting:

```text
executive_kpis.csv
channel_performance.csv
campaign_performance.csv
industry_performance.csv
region_performance.csv
segment_performance.csv
target_prioritization.csv
gaming_anomalies.csv
recommendations.csv
```

These outputs support executive reporting, marketing optimization, sales prioritization, and campaign decision-making.

---

## ◼ Ask AIM

The platform includes a grounded analytics interface for business questions such as:

```text
Which channel performs best?
Which campaigns have the strongest conversion?
Which segments have the highest expected value?
Which prospects should be prioritized?
Where are anomalies or gaming risks concentrated?
What action should the business take next?
```

Ask AIM is designed to answer from the project's available analytical outputs rather than generating unsupported business claims.

---

## ◼ System Architecture

```text
                 ┌─────────────────────────┐
                 │       RAW DATA          │
                 └────────────┬────────────┘
                              ↓
                 ┌─────────────────────────┐
                 │ Cleaning & Engineering  │
                 │     Python / SQL        │
                 └────────────┬────────────┘
                              ↓
              ┌──────────────────────────────┐
              │      Analytics Layer         │
              │ KPI · EDA · Segmentation     │
              │ Prediction · Anomaly         │
              └──────────────┬───────────────┘
                             ↓
              ┌──────────────────────────────┐
              │      Decision Intelligence   │
              │ Expected Value · Priorities  │
              │ Recommendations · Risk       │
              └──────────────┬───────────────┘
                             ↓
          ┌──────────────────┴──────────────────┐
          ↓                                     ↓
 ┌────────────────────┐              ┌────────────────────┐
 │  FastAPI Backend    │              │ React Dashboard    │
 │  REST Analytics API │              │ BI / Visualization │
 └────────────────────┘              └────────────────────┘
```

---

## ◼ Technology Stack

**Analytics**  
`Python` · `Pandas` · `NumPy` · `SQL` · `PostgreSQL` · `PySpark`

**Business Intelligence**  
`Power BI` · `Recharts`

**Machine Learning**  
`Scikit-learn` · `Logistic Regression` · `Decision Tree` · `K-Means` · `Isolation Forest`

**Application**  
`FastAPI` · `Uvicorn` · `Pydantic` · `React` · `TypeScript` · `Vite`

**Engineering**  
`Git` · `GitHub` · `REST API` · `Render`

---

## ◼ Repository Structure

```text
AIM-Commercial-Intelligence/
│
├── api/                         # FastAPI analytics backend
│   └── main.py
│
├── dashboard/                   # React + TypeScript dashboard
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
│
├── data/                        # Raw & processed datasets
│
├── sql/                         # SQL analytics / transformations
│
├── src/
│   ├── analytics/               # Analytical workflows
│   ├── data/                    # Data preparation
│   └── models/                  # ML models
│
├── requirements.txt
└── README.md
```

---

## ◼ API Surface

The FastAPI service exposes analytical endpoints including:

```text
GET /
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

## ◼ Recruiter View

This project demonstrates practical capability across the complete analytics lifecycle:

**Data Analyst**  
Data cleaning · EDA · KPI design · SQL analysis · segmentation · business insights · dashboard-ready datasets

**Analytics Engineer**  
Reusable pipelines · feature engineering · API-driven analytics · structured outputs

**ML / AI Analyst**  
Classification · clustering · anomaly detection · probability-based prioritization

**Business Intelligence**  
Executive KPIs · performance analysis · commercial metrics · actionable recommendations

**Software Engineering**  
FastAPI · React · TypeScript · REST endpoints · modular project architecture

---

## ◼ Key Takeaway

> **AIM is not just a dashboard and not just a machine-learning model. It is an end-to-end analytics system that connects data → metrics → prediction → commercial value → decisions.**

The strongest outcome is the ability to answer **“what should the business do next?”** using measurable evidence from the data.

---

## ⚠️ Dataset Disclaimer

The dataset and project are intended for **educational, portfolio, and analytical demonstration purposes**. The synthetic data is not affiliated with, endorsed by, or representative of American Express or any financial institution.

---

<div align="center">

### AIM — Data → Intelligence → Action

**Built as a portfolio project for Data Analytics, Business Intelligence, ML Decision Support, and Analytics Engineering.**

</div>