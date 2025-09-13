# Credit Card Transactions Analysis

## Overview
This project analyzes **1.3M synthetic credit-card transactions** (merchant, category, customer, geographic, and fraud label data) to explore spending behavior, detect anomalies, and surface cost-savings and risk insights.  
The workflow demonstrates a full analytics pipeline: from data cleaning and feature engineering to exploratory data analysis (EDA) and insight generation.

## Goals
- Clean and standardize raw credit card transaction data.  
- Engineer features relevant to customer demographics, merchant behavior, and fraud signals.  
- Analyze spending trends across categories, merchants, and demographics.  
- Surface recurring spend, outliers, and long-distance anomalies.  
- Generate actionable insights for vendor consolidation, policy controls, and budget optimization.  

## Workflow
### 1. Data Preparation
- **Cleaning:** drop redundant index columns, trim text, standardize state/ZIP, remove duplicates.  
- **Transformation:** parse dates, convert numerics, enforce categorical types.  
- **Feature Engineering:**  
  - Time features: year, month, weekday, hour bands.  
  - Customer features: age, age bands, gender splits.  
  - Distance: customer–merchant kilometers (Haversine).  
  - Recurring spend flag (merchant+amount across ≥3 months).  
  - Outlier detection (95th percentile cutoffs).  
  - Spend grouping: consolidate raw merchant categories into 6 groups.  

### 2. Exploratory Data Analysis (EDA)
- **Trends:** monthly & quarterly spend patterns.  
- **Category Insights:** distribution of spend across groups.  
- **Recurring Spend:** recurring share overall, by group, and over time.  
- **Outliers:** distribution and concentration of high-value transactions; top merchants by outlier spend.  
- **Distance Analysis:** long-distance purchases and anomaly patterns.  
- **Demographics:** spend by age band and gender; trends over time.  

### 3. Insights & Recommendations
- **Vendor consolidation:** *in progress — merchant concentration analysis and savings scenarios will be added.*  
- **Policy controls:** basic thresholds implemented (outlier amounts, long-distance flags).  
  - *Next step: extend to compound policies (amount + distance + time).*  
- **Budget optimization:** identify categories with rising spend trends for potential contract negotiations.  

### 4. Deliverables
- **Jupyter Notebook / Python Script:** data prep + feature engineering + EDA.  
- **Quarto Report (in progress):** narrative report with visuals and methodology.  
- **(Optional) Dashboard:** Tableau/Streamlit for interactive spend exploration.  

## Key Business Questions
This project addresses questions central to fraud operations and spend management analytics:

- ✅ **What are the largest drivers of recurring spend?**  
  Implemented at group level; merchant-level breakdown *in progress*.  

- ❌ **Which merchants dominate within each spend category?**  
  *Planned — top-N merchant coverage to be added.*  

- ✅ **What percentage of transactions are outliers or long-distance anomalies?**  
  Implemented with both fixed (500 km) and data-driven (95th pct) thresholds.  

- ✅ **How does spend vary across demographic groups (age, gender)?**  
  Implemented with age bands, gender splits, and monthly trends.  

- ❌ **Where can vendor consolidation or renegotiation yield savings?**  
  *Planned — savings scenarios under development.*  

- 🟡 **How can controls be set to flag risky or wasteful spending patterns?**  
  Basic thresholds implemented; compound policy rules *in progress*.  

## Next Steps
- Add merchant-level recurring and coverage metrics.  
- Build Quarto report with polished charts and written analysis.  
- Implement vendor consolidation savings scenarios.  
- Extend to **fraud modeling** using `is_fraud` label with leakage-aware validation.  
- Explore spend forecasting and merchant normalization improvements.  

---
This project demonstrates how a structured data pipeline and exploratory analysis can turn raw transactions into actionable **spend and risk insights** for financial operations and fraud prevention.

