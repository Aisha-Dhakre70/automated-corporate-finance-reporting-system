import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ---------------- CONFIG ----------------
NUM_DAYS = 730
START_DATE = datetime(2023, 1, 1)

COMPANIES = ["AlphaCorp", "BetaLtd", "GammaInc"]
CATEGORIES = ["Marketing", "Operations", "HR", "IT"]
REGIONS = ["North", "South", "East", "West"]

# Category impact
CATEGORY_REVENUE_FACTOR = {
    "Marketing": 1.2,
    "Operations": 1.0,
    "HR": 0.8,
    "IT": 1.1
}

CATEGORY_EXPENSE_RANGE = {
    "Marketing": (0.7, 1.2),
    "Operations": (0.6, 1.0),
    "HR": (0.4, 0.8),
    "IT": (0.5, 0.9)
}

# Region impact
REGION_REVENUE_FACTOR = {
    "North": 1.1,
    "South": 0.95,
    "East": 1.0,
    "West": 1.2
}

REGION_COST_FACTOR = {
    "North": 1.05,
    "South": 0.9,
    "East": 1.0,
    "West": 1.15
}

# ---------------- DATA GENERATION ----------------
data = []

for company in COMPANIES:

    # Company-specific growth behavior
    base_growth = random.uniform(1.5, 3.0)

    for i in range(NUM_DAYS):
        date = START_DATE + timedelta(days=i)

        # -------- Base Revenue Model --------
        trend = 1000 + i * base_growth

        seasonality = 1 + 0.2 * np.sin(2 * np.pi * date.month / 12)

        noise = np.random.normal(0, 120)

        revenue = trend * seasonality + noise

        # Occasional downturns (market shocks)
        if random.random() < 0.1:
            revenue *= random.uniform(0.7, 0.9)

        revenue = max(revenue, 200)

        # -------- Assign Business Dimensions --------
        category = random.choice(CATEGORIES)
        region = random.choice(REGIONS)

        # Apply category + region effects on revenue
        revenue *= CATEGORY_REVENUE_FACTOR[category]
        revenue *= REGION_REVENUE_FACTOR[region]

        # -------- Expense Modeling --------
        low, high = CATEGORY_EXPENSE_RANGE[category]
        expense = revenue * random.uniform(low, high)

        # Region affects cost structure
        expense *= REGION_COST_FACTOR[region]

        # Category-specific anomaly (e.g., marketing overspend)
        if category == "Marketing" and random.random() < 0.1:
            expense *= random.uniform(1.5, 2.0)

        # General anomaly (unexpected spike)
        if random.random() < 0.03:
            expense *= random.uniform(1.5, 2.5)

        # -------- Financial Layers --------
        cogs = expense * random.uniform(0.5, 0.7)
        gross_profit = revenue - cogs

        operating_expense = expense * random.uniform(0.2, 0.4)
        operating_profit = gross_profit - operating_expense

        net_profit = operating_profit - random.uniform(50, 150)

        # -------- Region-specific volatility --------
        if region == "West" and random.random() < 0.15:
            net_profit *= random.uniform(0.6, 0.85)

        # -------- Append Row --------
        data.append([
            company,
            date.strftime("%Y-%m-%d"),
            round(revenue, 2),
            round(expense, 2),
            round(cogs, 2),
            round(gross_profit, 2),
            round(operating_profit, 2),
            round(net_profit, 2),
            category,
            region
        ])

# ---------------- DATAFRAME ----------------
df = pd.DataFrame(data, columns=[
    "company",
    "date",
    "revenue",
    "expense",
    "cogs",
    "gross_profit",
    "operating_profit",
    "net_profit",
    "category",
    "region"
])

# ---------------- SAVE ----------------
output_path = "data/raw/financial_data.csv"
df.to_csv(output_path, index=False)

print("Dataset generated successfully!")
print(f"Saved to: {output_path}")
print(df.head())