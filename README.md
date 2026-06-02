# Marketing Campaign Analysis

End-to-end analysis of a retail marketing dataset — from raw data ingestion through SQL analysis to an interactive Tableau dashboard.

**[View the Tableau Dashboard](https://public.tableau.com/app/profile/aidan.thomas/viz/MarketingCampaignAnalysis_17804192196840/Dashboard1)**

---

## Project Structure

```
marketing_campaign_analysis/
├── data/
│   ├── marketing_campaign.csv   # Source dataset (2,240 customers, semicolon-delimited)
│   ├── load_data.py             # Loads CSV into SQLite with typed schema
│   └── marketing.db             # SQLite database (gitignored — regenerate via load_data.py)
├── sql/
│   ├── 01_campaign_response_by_segment.sql   # Response rates by education & marital status
│   ├── 02_rolling_engagement_metrics.sql     # 30-day rolling engagement per customer
│   ├── 03_top_customers_by_segment.sql       # Top spenders by segment
│   └── 04_channel_comparison.sql            # Purchase channel breakdown by education
├── tableau/
│   └── data_exports/
│       ├── segment_response.csv     # Campaign response rates by segment
│       ├── rolling_engagement.csv   # Rolling engagement metrics
│       └── channel_comparison.csv   # Channel comparison by education
└── generate_engagement.py   # Generates synthetic daily engagement events (Poisson λ=3, 2× December spike)
```

## Dataset

The source data is the [UCI Marketing Campaign dataset](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis) — 2,240 customers with demographic attributes, spending across 6 product categories, and responses to 6 marketing campaigns.

The `customers` table schema:

| Column | Type | Description |
|---|---|---|
| ID | INTEGER | Customer identifier |
| Year_Birth | INTEGER | Birth year |
| Education | TEXT | Education level |
| Marital_Status | TEXT | Marital status |
| Income | REAL | Annual household income |
| Kidhome / Teenhome | INTEGER | Number of children / teenagers at home |
| Dt_Customer | TEXT | Enrollment date (YYYY-MM-DD) |
| MntWines … MntGoldProds | REAL | Spend by product category (last 2 years) |
| NumWebPurchases … NumStorePurchases | INTEGER | Purchases by channel |
| AcceptedCmp1–5, Response | INTEGER | Campaign acceptance flags |

## Synthetic Engagement Data

`generate_engagement.py` produces a full year (2024) of daily engagement events for all 2,240 customers across 5 event types: `page_view`, `email_open`, `ad_click`, `purchase`, `social_share`.

- Daily event counts drawn from Poisson(λ=3); December uses λ=6 (2× spike)
- Seeded with `numpy.random.default_rng(42)` for reproducibility
- Output: ~3.9M rows, ~110 MB (gitignored — regenerate with `python3 generate_engagement.py`)

## SQL Analyses

| File | Description |
|---|---|
| `01_campaign_response_by_segment.sql` | Acceptance rates across all 6 campaigns, grouped by education and marital status |
| `02_rolling_engagement_metrics.sql` | 30-day rolling event totals per customer using window functions |
| `03_top_customers_by_segment.sql` | Top spenders ranked within each education segment |
| `04_channel_comparison.sql` | Average purchases by channel (web, catalog, store) broken down by education |

## Reproducing the Database

```bash
# 1. Install dependencies
pip install numpy pandas

# 2. Load customer data into SQLite
python3 data/load_data.py

# 3. Generate synthetic engagement log
python3 generate_engagement.py
```

## Dashboard

The Tableau Public dashboard visualises campaign response rates by customer segment, spending patterns across product categories, and engagement trends over time.

**[Open Dashboard](https://public.tableau.com/app/profile/aidan.thomas/viz/MarketingCampaignAnalysis_17804192196840/Dashboard1)**
