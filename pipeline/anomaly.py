import pandas as pd

# Detect anomalies in expense using IQR method
def detect_anomalies(df):
    if df is None or df.empty:
        print("[INFO] No data for anomaly detection")
        return None

    print("[INFO] Detecting anomalies...")

    Q1 = df["expense"].quantile(0.25)
    Q3 = df["expense"].quantile(0.75)
    IQR = Q3 - Q1

    threshold = Q3 + 1.5 * IQR

    anomalies = df[df["expense"] > threshold]

    print(f"[INFO] Found {len(anomalies)} anomalies")

    return anomalies
