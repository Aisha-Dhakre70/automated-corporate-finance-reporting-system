import pandas as pd
from utils.logger import setup_logger


def detect_anomalies(df):
    if df is None or df.empty:
        print("[INFO] No data for anomaly detection")
        return None

    print("[INFO] Detecting anomalies...")
    logger = setup_logger()

    anomalies_list = []

    # -------- Expense anomaly (per company using IQR) --------
    for company, group in df.groupby("company"):
        Q1 = group["expense"].quantile(0.25)
        Q3 = group["expense"].quantile(0.75)
        IQR = Q3 - Q1

        threshold = Q3 + 1.5 * IQR

        company_anomalies = group[group["expense"] > threshold].copy()
        company_anomalies["anomaly_type"] = "high_expense"

        anomalies_list.append(company_anomalies)

    # -------- Expense ratio anomaly --------
    ratio_anomalies = df[df["expense_ratio"] > 1.5].copy()
    ratio_anomalies["anomaly_type"] = "high_expense_ratio"

    anomalies_list.append(ratio_anomalies)

    # -------- Loss anomalies --------
    loss_anomalies = df[df["net_profit"] < 0].copy()
    loss_anomalies["anomaly_type"] = "loss"

    anomalies_list.append(loss_anomalies)

    # -------- Combine --------
    anomalies = pd.concat(anomalies_list).drop_duplicates()

    logger.info(f"Detected {len(anomalies)} anomalies")
    print(f"[INFO] Found {len(anomalies)} anomalies")

    return anomalies