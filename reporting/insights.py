def generate_insights(kpis, analysis, anomalies):
    insights = []

    # -------- KPIs --------
    insights.append(f"Total Revenue generated is {kpis['total_revenue']:.2f}.")
    insights.append(f"Total Net Profit is {kpis['total_net_profit']:.2f}.")

    # -------- Profitability --------
    if kpis["avg_net_margin"] > 0.2:
        insights.append("The business maintains a strong profit margin.")
    else:
        insights.append("Profit margins are relatively low and need attention.")

    # -------- Company Performance --------
    best_company = analysis["company"].iloc[0]["company"]
    worst_company = analysis["company"].iloc[-1]["company"]

    insights.append(f"Best performing company is {best_company}.")
    insights.append(f"Lowest performing company is {worst_company}.")

    # -------- Region --------
    top_region = analysis["region"].iloc[0]["region"]
    insights.append(f"Top performing region is {top_region}.")

    # -------- Category --------
    high_cost_category = analysis["category"].iloc[0]["category"]
    insights.append(f"Highest expense category is {high_cost_category}.")

    # -------- Risk --------
    risk = analysis.get("risk_summary")

    if risk is not None:
        risky_company = risk.sort_values(by="loss_flag", ascending=False).iloc[0]["company"]
        insights.append(f"Highest risk company is {risky_company} due to frequent losses.")

    # -------- Anomalies --------
    anomaly_count = len(anomalies) if anomalies is not None else 0
    insights.append(f"{anomaly_count} anomalies detected in financial data.")

    if anomaly_count > 0:
        insights.append("Irregular expense spikes and losses detected, requiring monitoring.")

    return insights