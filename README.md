# AIM — Commercial Marketing Intelligence

> **End-to-end Data Analytics project for customer acquisition, marketing performance, segmentation, prospect scoring, and business decision support.**

AIM analyzes **25,000 synthetic commercial prospect records** to answer practical business questions: which channels convert, which campaigns perform best, which segments create the most value, which prospects sales should prioritize, and where risk review is required.

The project follows a recruiter-friendly analytics workflow:

**Raw Data → Cleaning → Feature Engineering → SQL/Python Analysis → KPIs → Segmentation → Predictive Modeling → Business Value → Prioritization → Dashboard → Recommendations**

> **Dataset note:** This project uses synthetically generated data for portfolio and learning purposes. It is not affiliated with, endorsed by, or sponsored by American Express or any financial institution.

---

## 01 — Business Problem

Marketing and sales teams need to allocate limited acquisition effort toward opportunities with the strongest combination of **conversion likelihood, expected revenue, business value, and risk**.

AIM is designed to answer:

- Which acquisition channels perform best?
- Which campaigns generate the strongest conversion rates?
- Which industries and regions show stronger commercial performance?
- Which customer segments are most valuable?
- Which prospects should sales prioritize?
- Where is expected net value highest?
- Which records require gaming/anomaly review?

The goal is to move from **descriptive reporting to data-backed commercial decisions**.

---

## 02 — Executive KPI Snapshot

| KPI | Result |
|---|---:|
| Prospects | **25,000** |
| Conversions | **7,479** |
| Conversion Rate | **29.92%** |
| High-Value Targets | **1,186** |
| Gaming-Risk Records | **114** |
| Expected Revenue | **$1.127B** |
| Acquisition Cost | **$52.93M** |
| Expected Net Value | **$1.074B** |

> All figures above are calculated from the project's synthetic dataset.

---

## 03 — Dataset

The analytical dataset contains **25,000 prospect records** and **26 raw fields** covering:

| Business Dimension | Variables |
|---|---|
| Company | Industry, region, company size, annual revenue, employees, years in business |
| Relationship | Existing customer relationship, previous applications |
| Marketing | Campaign, acquisition channel, sales contacts |
| Digital Engagement | Website visits, email opens, email clicks, engagement |
| Outcome | Conversion |
| Economics | Expected revenue, acquisition cost, business value |
| Risk | Gaming/risk indicators |

Additional analytical features are created during preprocessing.

---

## 04 — Data Preparation & Feature Engineering

The pipeline prepares raw commercial data for reliable analysis through:

- Duplicate prospect removal
- Date parsing and validation
- Numeric validation
- Missing-value handling
- Categorical-value handling
- Data consistency checks

### Derived Features

- `engagement_rate`
- `sales_intensity`
- `revenue_per_employee`
- `is_recent_interaction`
- `is_high_engagement`

These features provide a cleaner analytical layer for SQL, Python, machine learning, and BI reporting.

---

## 05 — Exploratory Data Analysis

### Acquisition Channel Performance

Channels are evaluated using:

- Prospect volume
- Conversion volume
- Conversion rate
- Expected revenue
- Acquisition cost
- Expected net value

**Current dataset finding:** Email records the highest conversion rate at **30.8%**.

### Campaign Performance

Campaigns are compared using:

- Prospect volume
- Conversion volume
- Conversion rate
- Expected revenue
- Expected net value

**Current dataset finding:** `Enterprise_Expansion` has the highest campaign conversion rate at **30.6%**.

### Customer Segmentation

Prospects are evaluated by behavioral and business segments using:

- Segment size
- Average revenue
- Engagement
- Conversion rate
- Average business value

This allows performance to be analyzed at the **segment level**, rather than relying only on overall averages.

---

## 06 — Commercial Value Analysis

AIM separates **conversion likelihood** from **commercial value**.

For each prospect:

```text
Expected Value
    =
Conversion Probability × Expected Revenue
    − Acquisition Cost
```

The resulting value is combined with:

- Conversion propensity
- Engagement
- Gaming risk

to create a **Marketing Priority Score**.

This creates an important distinction:

> **Most likely to convert ≠ Most valuable to prioritize**

That distinction drives the prospect prioritization layer.

---

## 07 — Machine Learning for Decision Support

Machine learning is used as an **analytical decision-support layer**, not as the sole purpose of the project.

### Logistic Regression — Conversion Propensity

Used to estimate prospect conversion probability.

| Metric | Test Result |
|---|---:|
| Accuracy | 66.32% |
| Precision | 45.63% |
| Recall | 65.64% |
| F1 Score | 53.84% |
| ROC-AUC | **72.46%** |

### Decision Tree

Used as an interpretable comparison model.

**ROC-AUC: 69.62%**

### K-Means

Used to identify **5 prospect/customer segments** for behavioral analysis.

### Isolation Forest

Used to identify unusual records and support gaming/risk review.

---

## 08 — Prospect Prioritization

Model outputs are translated into business actions rather than stopping at prediction scores.

| Recommendation | Business Purpose |
|---|---|
| `PRIORITIZE_HIGH_VALUE_OUTREACH` | Focus sales effort on high-value prospects |
| `TARGET_WITH_PERSONALIZED_OFFER` | Tailor offers to stronger opportunities |
| `NURTURE_AND_RETARGET` | Continue engagement with developing prospects |
| `REVIEW_FOR_GAMING` | Review elevated-risk records |
| `LOW_PRIORITY` | Deprioritize lower-value opportunities |

### Current prioritization output

- **2,664** prospects → high-value outreach
- **8,323** prospects → personalized offers
- **114** records → gaming-risk review

---

## 09 — Analytics & Reporting Layer

The project produces structured analytical outputs for executive and operational reporting:

```text
powerbi/
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

The reporting layer supports:

- Executive KPI monitoring
- Acquisition performance
- Campaign analysis
- Industry and regional analysis
- Customer segmentation
- Prospect prioritization
- Risk/anomaly analysis
- Business recommendations

---

## 10 — Ask AIM: Grounded Business Analytics

The application includes a business-question interface for querying the generated analytical results.

Example questions:

```text
Which acquisition channel performs best?

Which campaign has the highest conversion rate?

Which customer segment has the highest business value?

Which prospects should sales prioritize?

Which channel generates the highest expected net value?

Which prospects have elevated gaming risk?
```

The grounded analytics layer uses the project's generated analytical datasets and calculated metrics as its evidence source instead of inventing unsupported business figures.

---

## 11 — End-to-End Architecture

```text
                    ┌─────────────────────┐
                    │  Commercial Dataset │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Data Cleaning       │
                    │ Validation          │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Feature Engineering │
                    └──────────┬──────────┘
                               ↓
              ┌────────────────┴────────────────┐
              ↓                                 ↓
       ┌───────────────┐                 ┌───────────────┐
       │ SQL / Python  │                 │ ML Analytics  │
       │ KPI & EDA     │                 │ Propensity    │
       └───────┬───────┘                 │ Segmentation  │
               │                         │ Anomalies     │
               │                         └───────┬───────┘
               └──────────────┬──────────────────┘
                              ↓
                    ┌─────────────────────┐
                    │ Business Value      │
                    │ & Priority Scoring  │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Reporting / BI      │
                    │ Dashboard           │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Recommendations    │
                    │ Decision Support    │
                    └─────────────────────┘
```

---

## 12 — Technology Stack

### Data Analytics

`Python` · `Pandas` · `NumPy` · `SQL` · `PostgreSQL` · `PySpark`

### Visualization & BI

`Power BI` · `Recharts`

### Machine Learning

`Scikit-learn` · `Logistic Regression` · `Decision Tree` · `K-Means` · `Isolation Forest`

### API & Application

`FastAPI` · `Uvicorn` · `Pydantic` · `React` · `TypeScript`

### Engineering

`Git` · `GitHub` · `Render`

The Python environment is defined in `requirements.txt`, including Pandas, NumPy, scikit-learn, SQLAlchemy, PostgreSQL support, FastAPI, joblib, and PySpark.

---

## 13 — Repository Structure

```text
AIM-Commercial-Intelligence/
│
├── api/
│   └── main.py                 # FastAPI analytics API
│
├── data/
│   ├── raw/                    # Raw prospect data
│   └── processed/              # Cleaned, scored & analytical outputs
│       ├── models/             # Trained ML artifacts & metrics
│       ├── powerbi/            # BI-ready analytical datasets
│       ├── scored_prospects.csv
│       └── automated_insights.json
│
├── dashboard/                  # React + TypeScript dashboard
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
│
├── sql/                        # SQL analytics
│
├── src/
│   ├── analytics/              # Business analytics & grounded insights
│   ├── data/                   # Data preparation
│   └── models/                 # ML training workflows
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 14 — API Analytics Surface

The FastAPI layer exposes business-ready analytical endpoints including:

```text
GET  /health
GET  /api/v1/overview
GET  /api/v1/models
GET  /api/v1/insights
GET  /api/v1/insights/summary
GET  /api/v1/channels
GET  /api/v1/campaigns
GET  /api/v1/segments
GET  /api/v1/targets
GET  /api/v1/prospects/{prospect_id}
GET  /api/v1/anomalies
GET  /api/v1/recommendations
POST /api/v1/genai
```

This keeps the analytical layer reusable for dashboards and downstream applications.

---

## 15 — What This Project Demonstrates

### Data Analysis

- Data cleaning and validation
- Exploratory data analysis
- KPI development
- Funnel analysis
- Channel performance analysis
- Campaign performance analysis
- Industry and regional analysis
- Customer segmentation
- Business-value analysis
- Risk/anomaly analysis

### SQL

- Business aggregations
- Filtering and grouping
- KPI calculations
- Analytical data preparation
- Performance analysis across business dimensions

### Python

- Pandas-based transformation
- Feature engineering
- Statistical analysis
- Automated analytical reporting
- Data preparation for ML and BI

### Machine Learning

- Classification
- Model evaluation
- Probability-based scoring
- Customer segmentation
- Anomaly detection

### Business Decision-Making

- Conversion analysis
- Marketing prioritization
- Expected-value analysis
- Customer targeting
- Risk-aware recommendations

### BI / Reporting

- Executive KPI reporting
- Marketing dashboards
- Segment analysis
- Campaign/channel reporting
- Action-oriented recommendations

---

## 16 — Key Takeaway

AIM demonstrates how a Data Analyst can take a commercial dataset and turn it into a decision-support workflow:

> **Raw data → Clean data → KPIs → EDA → Segmentation → Predictive analytics → Business value → Prioritization → Reporting → Recommendations**

The emphasis is on **answering business questions with data** — not simply training a model or creating a visualization.

---

## Disclaimer

This is an independent portfolio project using **synthetically generated data**. It is not affiliated with, endorsed by, or sponsored by American Express, and it does not use confidential or proprietary company data.
