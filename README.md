# Automated Corporate Finance Reporting System
This end-to-end system automatically collects financial data (sales, expenses, transactions), processes it, and generates structured reports and dashboards for decision-making. In real life, companies use such systems to reduce manual Excel work, ensure accuracy, and enable finance teams and executives to make faster, data-driven decisions.

---

## Dataset

The dataset was generated using `generate dataset/generate_data.py` and saved inside `data/raw/` as a CSV file. Seasonalities and anomalies are added for realism.

Key features included in the dataset are:
- comapny
- date
- revenue
- expense
- cogs
- gross_profit
- operation_profit
- net_profit
- category (Marketing, Operations, HR, IT)
- region (East, West, North, South)

---

## Setup for Automation

### Step 1: Create Batch File
Create the file: `automation/run_pipeline.bat`

### Step 2: Create Scheduled Task
- Open Task Scheduler
- Click Create Basic Task
- Name: Finance Reporting Pipeline
- Trigger:
  - Daily / Weekly (recommended: Daily)

### Step 3: Configure Action
- Action: Start a Program
- Program/script: `C:\path\to\your\project\automation\run_pipeline.bat`

### Step 4: Advanced Settings
After creating the task:
- Right-click → Properties
✅ General Tab\
Enable: Run whether user is logged in or not

✅ Triggers Tab\
Edit trigger → enable:\
Repeat task every (optional)

✅ Conditions Tab\
Enable:
- Wake the computer to run this task

✅ Settings Tab\
Enable:
- Run task as soon as possible after a scheduled start is missed
- If task fails, restart every (e.g., 5 minutes)
