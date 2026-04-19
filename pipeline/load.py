import os


def save_outputs(df, analysis, anomalies, insights=None):
    os.makedirs("data/processed", exist_ok=True)

    if df is not None:
        df.to_csv("data/processed/cleaned_data.csv", index=False)

    if analysis:
        analysis["monthly"].to_csv("data/processed/monthly.csv", index=False)
        analysis["category"].to_csv("data/processed/category.csv", index=False)
        analysis["region"].to_csv("data/processed/region.csv", index=False)

        # NEW
        if "company" in analysis:
            analysis["company"].to_csv("data/processed/company.csv", index=False)

        if "risk_summary" in analysis:
            analysis["risk_summary"].to_csv("data/processed/risk_summary.csv", index=False)

    if anomalies is not None:
        anomalies.to_csv("data/processed/anomalies.csv", index=False)

    if insights:
        with open("data/processed/insights.txt", "w") as f:
            for line in insights:
                f.write(line + "\n")

    print("[INFO] Processed data saved")