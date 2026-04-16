import pandas as pd

def analyze_data(df, anomalies=None):
    if df is None or df.empty:
        print("[INFO] No data to analyze")
        return None, None

    print("[INFO] Running analysis...")

    # KPIs
    kpis = {
        "total_revenue": df["revenue"].sum(),
        "total_expense": df["expense"].sum(),
        "total_profit": df["profit"].sum(),
        "avg_profit_margin": df["profit_margin"].mean(),
        "max_revenue_day": df.loc[df["revenue"].idxmax(), "date"],
        "min_profit_day": df.loc[df["profit"].idxmin(), "date"]
    }

    # Monthly
    monthly = df.groupby(["year", "month"]).agg({
        "revenue": "sum",
        "expense": "sum",
        "profit": "sum"
    }).reset_index()

    # Category
    category = df.groupby("category").agg({
        "revenue": "sum",
        "expense": "sum",
        "profit": "sum"
    }).reset_index().sort_values(by="expense", ascending=False)

    # Region
    region = df.groupby("region").agg({
        "revenue": "sum",
        "expense": "sum",
        "profit": "sum"
    }).reset_index().sort_values(by="profit", ascending=False)

    print("[INFO] Analysis complete")

    return kpis, {
        "monthly": monthly,
        "category": category,
        "region": region,
    }
