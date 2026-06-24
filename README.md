# 📊 Automated Corporate Financial Reporting System

An end-to-end automated financial reporting pipeline built using **Python**, **MySQL**, **Machine Learning**, **Streamlit**, and **Excel Automation**.

This project simulates a real-world corporate finance reporting workflow by automating data extraction, validation, transformation, analysis, anomaly detection, forecasting, report generation, and dashboard visualization.

---

## 🎯 Business Problem

Financial reporting in many organizations involves manual data extraction, spreadsheet manipulation, KPI calculation, and report generation.

This project automates the complete reporting workflow by integrating ETL processes, financial analytics, anomaly detection, automated reporting, and dashboard visualization into a single system.

---

## 🚀 Features

- Automated ETL Pipeline
- Incremental ETL Processing using Metadata Tracking
- Data Validation & Quality Checks
- Feature Engineering
- Financial KPI Analysis
- Anomaly Detection
- Automated Excel Report Generation
- Business Insight Generation
- Interactive Streamlit Dashboard
- Windows Task Scheduler Automation
- Logging System

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
├── app.py
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

---

## 📈 Financial Analysis & Business Intelligence

The system automatically computes and visualizes key financial metrics to support corporate decision-making.

### Executive KPIs

The dashboard provides real-time visibility into:

- Total Revenue
- Total Expenses
- Net Profit
- Gross Profit
- Operating Profit
- Profit Margin (%)

---

### Trend Analysis

Interactive visualizations enable analysis of:

- Revenue trends over time
- Net profit trends over time
- Company-wise performance comparison
- Seasonal financial patterns
- Revenue and profitability growth

---

### Business Breakdown Analysis

The system evaluates performance across multiple dimensions:

#### Category Analysis
- HR
- IT
- Marketing
- Operations

Metrics include:
- Revenue contribution
- Expense distribution
- Profitability comparison

#### Regional Analysis
- North
- South
- East
- West

Metrics include:
- Revenue performance
- Net profit contribution
- Regional efficiency comparison

---

### Company Comparison

The dashboard compares financial performance across multiple organizations:

- AlphaCorp
- BetaLtd
- GammaInc

Comparison metrics include:
- Revenue
- Profitability
- Operating efficiency

---

### Anomaly Detection Dashboard

The system automatically identifies unusual financial transactions and flags:

- High expense events
- Loss-making transactions
- Revenue outliers
- Profit anomalies

Detected anomalies are presented in an interactive investigation table containing:

- Transaction ID
- Company
- Date
- Revenue
- Expense
- Profit Metrics
- Growth Indicators
- Risk Flags

This enables finance teams to quickly identify potentially problematic transactions requiring further review.

---

## Anomaly Detection

The pipeline identifies abnormal financial transactions using statistical techniques to detect:
- Expense spikes
- Revenue outliers
- Unusual profit patterns

---

## Reporting

Automatically generates Excel reports containing:
- KPIs
- Revenue Analysis
- Expense Analysis
- Regional Performance
- Category Analysis
- Business Insights

Generated reports are stored inside: `reports/`

---

## Dashboard

The project includes a multipage Streamlit dashboard.

#### Pages
- Overview
- Insights
- Reports

The dashboard provides:
- KPI Cards
- Revenue Trends
- Expense Analysis
- Profit Trends
- Regional Performance
- Category Analysis

---

## Automation

The entire pipeline can be automated using:
- Windows Task Scheduler
- Batch Script

Files:

`automation/run_pipeline.bat` \
`AUTOMATION_SETUP.txt`

---

## Logging

All pipeline activities are logged. \

Example log information:
- Pipeline started
- Extraction completed
- Anomalies Detected
- Reports generated
- Errors (if any)

Logs are stored inside: `logs/pipeline.log`

---

## How to Run

#### Clone the repository

```
git clone https://github.com/Aisha-Dhakre70/automated-corporate-financial-reporting-system.git

cd automated-corporate-financial-reporting-system
```

#### Install Dependencies

```
pip install -r requirements.txt
```

#### Generate Dataset

```
python generate_dataset/generate_data.py
```

#### Create MySQL Database
Run `database/schema.sql` inside MySQL.

#### Load Dataset

```
python database/load_csv_to_db.py
```

#### Run Pipeline

```
python pipeline/main_pipeline.py
```

#### Launch Dashboard

```
streamlit run app.py
```

---

## Future Improvements
- Docker support
- Cloud database integration
- Airflow orchestration
- Power BI integration
- Email report delivery
- REST API support
- Role-based authentication
- Real-time streaming data
- Revenue/ROI forecasting

---

## Skills Demonstrated

- ETL Pipeline Development
- Data Engineering
- Data Warehousing Concepts
- SQL & Database Management
- Data Validation & Quality Assurance
- Feature Engineering
- Financial Analytics
- Business Intelligence
- KPI Development
- Dashboard Development
- Report Automation
- Streamlit
- Plotly
- Python
- MySQL
- Logging & Monitoring
- Workflow Automation
