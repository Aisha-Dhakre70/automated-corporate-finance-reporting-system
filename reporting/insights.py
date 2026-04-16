def generate_insights(kpis, analysis, anomalies):
    insights = []

    # KPIs
    insights.append(f"Total Revenue generated is {kpis['total_revenue']:.2f}.")
    insights.append(f"Overall Profit is {kpis['total_profit']:.2f}.")

    # Profitability
    if kpis["avg_profit_margin"] > 20:
        insights.append("The business maintains a healthy profit margin.")
    else:
        insights.append("Profit margins are relatively low and need attention.")

    # Region
    top_region = analysis["region"].iloc[0]["region"]
    insights.append(f"Top performing region is {top_region}.")

    # Category
    top_category = analysis["category"].iloc[0]["category"]
    insights.append(f"Highest expenses are in {top_category} category.")

    # Anomalies
    anomaly_count = len(anomalies)
    insights.append(f"{anomaly_count} anomalies detected in expense data.")

    if anomaly_count > 0:
        insights.append("Irregular expense spikes observed, requiring monitoring.")

    return insights