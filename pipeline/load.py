import os

def save_outputs(df, analysis, anomalies):
    os.makedirs("data/processed", exist_ok=True)

    if df is not None:
        df.to_csv("data/processed/cleaned_data.csv", index=False)

    if analysis:
        analysis["monthly"].to_csv("data/processed/monthly.csv", index=False)
        analysis["category"].to_csv("data/processed/category.csv", index=False)
        analysis["region"].to_csv("data/processed/region.csv", index=False)

    if anomalies is not None:
        anomalies.to_csv("data/processed/anomalies.csv", index=False)

    print("[INFO] Processed data saved")
