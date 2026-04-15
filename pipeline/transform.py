import pandas as pd
from pipeline.validate import validate_data


def transform_data(df):
    if df is None or df.empty:
        print("[INFO] No data to transform")
        return None

    print("[INFO] Transforming data...")

    # Run validation
    df = validate_data(df)

    # Feature Engineering
    df["profit"] = df["revenue"] - df["expense"]

    # Extract time features
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    # Profit margin
    df["profit_margin"] = (df["profit"] / df["revenue"]) * 100

    print("[INFO] Transformation complete")

    return df