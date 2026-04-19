import pandas as pd


def analyze_data(df, anomalies=None):
    if df is None or df.empty:
        print("[INFO] No data to analyze")
        return None, None

    print("[INFO] Running analysis...")

    # -------- KPIs --------
    kpis = {
        "total_revenue": df["revenue"].sum(),
        "total_expense": df["expense"].sum(),
        "total_net_profit": df["net_profit"].sum(),
        "avg_net_margin": df["net_margin"].mean(),
        "max_revenue_day": df.loc[df["revenue"].idxmax(), "date"],
        "min_profit_day": df.loc[df["net_profit"].idxmin(), "date"]
    }

    # -------- Company Performance --------
    company = df.groupby("company").agg({
        "revenue": "sum",
        "net_profit": "sum",
        "net_margin": "mean"
    }).reset_index().sort_values(by="net_profit", ascending=False)

    # -------- Monthly Trends --------
    monthly = df.groupby(["year", "month"]).agg({
        "revenue": "sum",
        "net_profit": "sum"
    }).reset_index()

    # -------- Category Analysis --------
    category = df.groupby("category").agg({
        "revenue": "sum",
        "expense": "sum",
        "net_profit": "sum",
        "expense_ratio": "mean"
    }).reset_index().sort_values(by="expense_ratio", ascending=False)

    # -------- Region Analysis --------
    region = df.groupby("region").agg({
        "revenue": "sum",
        "net_profit": "sum",
        "expense_ratio": "mean"
    }).reset_index().sort_values(by="net_profit", ascending=False)

    # -------- Risk Summary --------
    risk_summary = df.groupby("company").agg({
        "high_expense_flag": "sum",
        "loss_flag": "sum"
    }).reset_index()

    # -------- Insights (🔥 this is the big upgrade) --------
    insights = []

    best_company = company.iloc[0]["company"]
    worst_company = company.iloc[-1]["company"]

    insights.append(f"Best performing company: {best_company}")
    insights.append(f"Lowest performing company: {worst_company}")

    high_risk_company = risk_summary.sort_values(
        by="loss_flag", ascending=False
    ).iloc[0]["company"]

    insights.append(f"Highest risk company (most losses): {high_risk_company}")

    high_cost_category = category.iloc[0]["category"]
    insights.append(f"Most expensive category: {high_cost_category}")

    top_region = region.iloc[0]["region"]
    insights.append(f"Top performing region: {top_region}")

    print("[INFO] Analysis complete")

    return kpis, {
        "company": company,
        "monthly": monthly,
        "category": category,
        "region": region,
        "risk_summary": risk_summary,
        "insights": insights,
        "anomalies": anomalies
    }