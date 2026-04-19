import pandas as pd
from pipeline.validate import validate_data


def transform_data(df):
    if df is None or df.empty:
        print("[INFO] No data to transform")
        return None

    print("[INFO] Transforming data...")

    # -------- Validation --------
    df = validate_data(df)

    # -------- Core Financial Features --------

    # Profit (keep for simplicity / compatibility)
    df["profit"] = df["revenue"] - df["expense"]

    # Margins (more meaningful than raw profit)
    df["gross_margin"] = df["gross_profit"] / df["revenue"]
    df["operating_margin"] = df["operating_profit"] / df["revenue"]
    df["net_margin"] = df["net_profit"] / df["revenue"]

    # Expense ratio (important for risk detection)
    df["expense_ratio"] = df["expense"] / df["revenue"]

    # -------- Time Features --------
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    # -------- Growth Metrics --------
    df = df.sort_values(["company", "date"])

    df["revenue_growth"] = df.groupby("company")["revenue"].pct_change()
    df["profit_growth"] = df.groupby("company")["net_profit"].pct_change()

    # -------- Rolling Indicators --------
    df["revenue_ma_30"] = df.groupby("company")["revenue"].transform(
        lambda x: x.rolling(30).mean()
    )

    df["profit_ma_30"] = df.groupby("company")["net_profit"].transform(
        lambda x: x.rolling(30).mean()
    )

    # -------- Risk Flags --------
    df["high_expense_flag"] = df["expense_ratio"] > 1.2
    df["loss_flag"] = df["net_profit"] < 0

    print("[INFO] Transformation complete")

    return df