import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# CONFIGURE 2 YEARS OF DATA
num_days = 730   # 2 years of data
start_date = datetime(2023, 1, 1)

categories = ["Marketing", "Operations", "HR", "IT"]
regions = ["North", "South", "East", "West"]

# GENERATE DATA
data = []

for i in range(num_days):
    date = start_date + timedelta(days=i)

    # Trend (growth over time)
    trend = 1000 + i * 2  

    # Seasonality (monthly pattern)
    month_factor = 1 + 0.2 * np.sin(2 * np.pi * date.month / 12)

    # Random noise
    noise = np.random.normal(0, 100)

    # Revenue
    revenue = trend * month_factor + noise
    revenue = max(revenue, 200)  # avoid negative

    # Expense base
    expense = revenue * random.uniform(0.5, 0.9)

    # Inject anomalies (rare spikes)
    if random.random() < 0.03:  # 3% chance
        expense *= random.uniform(1.5, 2.5)

    category = random.choice(categories)
    region = random.choice(regions)

    data.append([
        date.strftime("%Y-%m-%d"),
        round(revenue, 2),
        round(expense, 2),
        category,
        region
    ])

# CREATE DATAFRAME
df = pd.DataFrame(data, columns=[
    "date", "revenue", "expense", "category", "region"
])

# SAVE DATASET
df.to_csv("data/raw/financial_data.csv", index=False)

print("Dataset generated successfully!")
print(df.head())