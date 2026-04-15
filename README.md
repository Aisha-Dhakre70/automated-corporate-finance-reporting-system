# automated-corporate-finance-reporting-system
This end-to-end system automatically collects financial data (sales, expenses, transactions), processes it, and generates structured reports and dashboards for decision-making. In real life, companies use such systems to reduce manual Excel work, ensure accuracy, and enable finance teams and executives to make faster, data-driven decisions.

---

## Dataset

The dataset was generated using `generate dataset/generate_data.py` and saved inside `data/raw/` as a CSV file. Seasonalities and anomalies are added for realism.

Key features included in the dataset are:
- date
- revenue
- expense
- category (Marketing, Operations, HR, IT)
- region (East, West, North, South)
