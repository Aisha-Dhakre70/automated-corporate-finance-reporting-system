import pandas as pd


def validate_data(df):
    print("[INFO] Running data validation...")

    # Check missing values
    missing = df.isnull().sum()
    if missing.any():
        print("[WARNING] Missing values found:\n", missing)

    # Drop missing rows
    df = df.dropna()

    # Remove duplicates
    df = df.drop_duplicates()

    # Validate revenue & expense
    df = df[(df["revenue"] >= 0) & (df["expense"] >= 0)]

    # Ensure correct data types
    df["date"] = pd.to_datetime(df["date"])

    print("[INFO] Validation complete")

    return df