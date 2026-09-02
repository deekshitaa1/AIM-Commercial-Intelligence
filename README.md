<div align="center">

# AIM
### Commercial Marketing Intelligence

**Data Analytics · Business Intelligence · Predictive Decision Support**

</div>

---

## 🚀 Live Demo

> **The first thing a recruiter should see: the working product.**

| Application | Status |
|---|---|
| **Dashboard** | AIM Commercial Marketing Intelligence |
| **Backend API** | AIM API |
| **API Health** | Health Check |

### Quick Preview

> **Live dashboard:** customer acquisition KPIs, channel and campaign performance, segmentation, prospect prioritization, risk analysis, and grounded business analytics through **Ask AIM**.

<br>

<div align="center">

**CUSTOMER ACQUISITION** &nbsp; → &nbsp; **MARKETING PERFORMANCE** &nbsp; → &nbsp; **SEGMENTATION** &nbsp; → &nbsp; **PREDICTIVE SCORING** &nbsp; → &nbsp; **BUSINESS ACTION**

</div>

---

## 📊 What the Dashboard Delivers

<table>
<tr>
<td width="50%">

### Executive KPIs

Conversion rate, conversions, expected revenue, acquisition cost, expected net value and high-value targets.

</td>
<td width="50%">

### Channel & Campaign Analytics

Compare acquisition performance and identify channels and campaigns generating stronger commercial outcomes.

</td>
</tr>
<tr>
<td width="50%">

### Prospect Intelligence

Rank prospects using conversion probability and expected commercial value.

</td>
<td width="50%">

### Risk & Anomaly Analysis

Identify anomalous and potential gaming-risk records for review.

</td>
</tr>
<tr>
<td width="50%">

### Segmentation

Use behavioral and commercial features to identify distinct prospect groups.

</td>
<td width="50%">

### Ask AIM

Ask business questions and retrieve grounded insights from the project's analytical outputs.

</td>
</tr>
</table>

---

## 🎯 Project in One View

**AIM transforms raw customer-acquisition data into decision-ready commercial intelligence.**

```text
Raw Data
   ↓
Cleaning & Data Quality
   ↓
Feature Engineering
   ↓
SQL + Python Analytics
   ↓
KPI / EDA / Performance Analysis
   ↓
Segmentation + Predictive Modeling
   ↓
Expected Value Calculation
   ↓
Prospect Prioritization
   ↓
Dashboard + API
   ↓
Business Recommendations
```

The focus is not simply predicting conversion. The system connects **analytics → business value → prioritization → action**.

---

## 📈 Executive KPI Snapshot

| KPI | Value |
|:---|---:|
| Prospects Analyzed | **25,000** |
| Conversions | **7,479** |
| Conversion Rate | **29.92%** |
| High-Value Targets | **1,186** |
| Gaming-Risk Records | **114** |
| Expected Revenue | **$1.127B** |
| Acquisition Cost | **$52.93M** |
| Expected Net Value | **$1.074B** |

---

## 🔎 Analytics Workflow

### 01 · Data Preparation

- Structured prospect and marketing data
- Data-quality processing
- Missing-value handling
- Feature engineering
- Reproducible processed datasets

### 02 · Exploratory & Diagnostic Analytics

AIM analyzes:

`Channels` · `Campaigns` · `Industries` · `Regions` · `Segments` · `Conversions` · `Acquisition Cost` · `Revenue`

### 03 · Predictive Analytics

| Technique | Business Use | Result |
|---|---|---:|
| Logistic Regression | Conversion probability | ROC-AUC **72.46%** |
| Decision Tree | Non-linear conversion patterns | ROC-AUC **69.62%** |
| K-Means | Prospect segmentation | **5 clusters** |
| Isolation Forest | Anomaly / gaming-risk detection | Risk screening |

**Logistic Regression:** Accuracy 66.32% · Precision 45.63% · Recall 65.64% · F1 53.84% · ROC-AUC 72.46%

---

## 💰 Commercial Value Engine

AIM turns predictive output into a business metric:

```text
Expected Value
= Conversion Probability × Expected Revenue − Acquisition Cost
```

This creates a practical bridge between **machine-learning probability** and **business prioritization**.

---

## 🧭 Decision Intelligence

The system translates analytical results into recommended actions:

| Recommendation | Action |
|---|---|
| `PRIORITIZE_HIGH_VALUE_OUTREACH` | Immediate attention for high expected-value prospects |
| `TARGET_WITH_PERSONALIZED_OFFER` | Targeted engagement based on prospect value |
| `NURTURE_AND_RETARGET` | Continue lower-intensity engagement |
| `REVIEW_FOR_GAMING` | Investigate anomalous behavior |
| `LOW_PRIORITY` | Deprioritize lower expected-value prospects |

### Current Output

- **2,664** high-value outreach prospects
- **8,323** personalized-offer prospects
- **114** gaming-risk records for review

---

## 🧠 Ask AIM

A grounded business-analytics layer for questions such as:

```text
Which acquisition channel performs best?
Which campaigns have the strongest conversion?
Which segments have the highest expected value?
Which prospects should be prioritized?
Where are anomalies concentrated?
What action should the business take next?
```

Ask AIM is designed to use the project's analytical outputs as its evidence base rather than inventing unsupported business conclusions.

---

## 🏗️ Architecture

```text
                         ┌──────────────────┐
                         │     RAW DATA     │
                         └────────┬─────────┘
                                  ↓
                     ┌────────────────────────┐
                     │ Cleaning + Engineering │
                     │      Python / SQL      │
                     └────────────┬───────────┘
                                  ↓
                     ┌────────────────────────┐
                     │    ANALYTICS ENGINE    │
                     │ KPI · EDA · ML · Risk  │
                     └────────────┬───────────┘
                                  ↓
                     ┌────────────────────────┐
                     │  DECISION INTELLIGENCE │
                     │ Value · Priority ·     │
                     │ Recommendations        │
                     └────────────┬───────────┘
                                  ↓
                  ┌───────────────┴───────────────┐
                  ↓                               ↓
        ┌───────────────────┐           ┌───────────────────┐
        │    AIM API        │           │   AIM Dashboard   │
        │     FastAPI       │           │ React + TypeScript │
        └───────────────────┘           └───────────────────┘
```

---

## 🛠️ Technology Stack

| Layer | Technologies |
|---|---|
| **Data Analytics** | Python, Pandas, NumPy, SQL, PostgreSQL, PySpark |
| **BI / Visualization** | Power BI, Recharts |
| **Machine Learning** | Scikit-learn, Logistic Regression, Decision Tree, K-Means, Isolation Forest |
| **Backend** | FastAPI, Uvicorn, Pydantic |
| **Frontend** | React, TypeScript, Vite |
| **Engineering** | Git, GitHub, REST API, Render |

---

## 📁 Repository Structure

```text
AIM-Commercial-Intelligence/
│
├── api/
│   └── main.py                 # FastAPI analytics API
│
├── dashboard/                 # React + TypeScript application
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
│
├── data/                      # Raw + processed datasets
├── sql/                       # SQL analytics / transformations
│
├── src/
│   ├── analytics/             # Analytical workflows
│   ├── data/                  # Data preparation
│   └── models/                # ML models
│
├── requirements.txt
└── README.md
```

---

## 🔌 AIM API

The backend exposes analytical endpoints for the dashboard and downstream consumers:

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

## 📦 BI-Ready Outputs

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

These outputs can support executive reporting, marketing optimization, sales prioritization and campaign analysis.

---

## 👩‍💻 What This Project Demonstrates

**Data Analytics**  
Data cleaning · EDA · KPI development · SQL · segmentation · business insights

**Business Intelligence**  
Commercial metrics · performance analysis · dashboard design · decision support

**Predictive Analytics**  
Classification · clustering · anomaly detection · probability-based prioritization

**Analytics Engineering**  
Feature engineering · reusable analytical outputs · API-driven analytics

**Application Engineering**  
FastAPI · React · TypeScript · REST architecture

---

## ⭐ Why AIM?

> **Most analytics projects stop at a dashboard. AIM continues from insight to decision.**

It answers three layers of the commercial problem:

```text
WHAT HAPPENED?
       ↓
WHY DID IT HAPPEN?
       ↓
WHAT SHOULD WE DO NEXT?
```

That makes AIM an end-to-end portfolio project across **Data Analytics, Business Intelligence, Predictive Analytics, and Decision Intelligence**.

---

## ⚠️ Dataset Disclaimer

This project is intended for **educational, portfolio, and analytical demonstration purposes**. The dataset is synthetic and is not affiliated with, endorsed by, or representative of American Express or any financial institution.

---

<div align="center">

### AIM
**Data → Insight → Decision**

</div>