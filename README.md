# 📊 Automated Corporate Financial Reporting System

An end-to-end automated financial reporting pipeline built using **Python**, **MySQL**, **Machine Learning**, **Streamlit**, and **Excel Automation**.

This project simulates a real-world corporate finance reporting workflow by automating data extraction, validation, transformation, analysis, anomaly detection, forecasting, report generation, and dashboard visualization.

---

## 🚀 Features

- Automated ETL Pipeline
- Incremental Data Extraction
- Data Validation & Quality Checks
- Feature Engineering
- Financial KPI Analysis
- Anomaly Detection
- Automated Excel Report Generation
- Business Insight Generation
- Interactive Streamlit Dashboard
- Windows Task Scheduler Automation
- Logging System
- Metadata Tracking for Incremental Processing

---

## Project Workflow

```

    Raw Dataset
        ↓
   MySQL Database
        ↓
Extract (Incremental)
        ↓
    Validate
        ↓
    Transform
        ↓
   Analyze KPIs
        ↓
 Anomaly Detection
        ↓
 Generate Insights
        ↓
   Excel Report
        ↓
Streamlit Dashboard

```
---

## Project Structure

```
automated-corporate-financial-reporting-system
│
├── automation/
├── config/
├── dashboard/
├── data/
├── database/
├── generate_dataset/
├── logs/
├── metadata/
├── notebooks/
├── pipeline/
├── reporting/
├── reports/
├── utils/
│
├── requirements.txt
└── README.md
```

---

## Technologies Used

| Category         | Tools                  |
|------------------|------------------------|
| Programming      | Python                 |
| Database         | MySQL                  |
| Data Processing  | Pandas, NumPy          |
| Visualization    | Plotly, Streamlit      |
| Reporting        | OpenPyXL               |
| Automation       | Windows Task Scheduler |
| Logging          | Python Logging         |
| Version Control  | Git & GitHub           |

---

## Dataset

The project uses a synthetic financial dataset representing transactions from multiple companies.

#### Features
- Date
- Company
- Revenue
- Expenses
- COGS
- Gross Profit
- Operating Profit
- Net Profit
- Category
- Region

#### Sample categories:
- Marketing
- Operations
- HR
- IT

#### Regions:
- North
- South
- East
- West

---

## ETL Pipeline

#### 1. Extract
- Reads incremental records from MySQL
- Uses metadata tracking
- Prevents duplicate processing

#### 2. Validate
Performs:
- Missing value detection
- Duplicate removal
- Invalid value checks
- Data quality validation

#### 3. Transform
Creates engineered features including:
- Profit
- Gross Profit
- Operating Profit
- Net Profit
- Profit Margin
- Month
- Year

#### 4. Load
Stores processed data inside: `data/processed/`








