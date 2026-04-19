import pandas as pd

REQUIRED_COLUMNS = [
    "company",
    "date",
    "revenue",
    "expense",
    "cogs",
    "gross_profit",
    "operating_profit",
    "net_profit",
    "category",
    "region"
]


def validate_data(df):
    print("[INFO] Running data validation...")

    # -------- Check required columns --------
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"[ERROR] Missing columns: {missing_cols}")

    # -------- Handle missing values --------
    missing = df.isnull().sum()
    if missing.any():
        print("[WARNING] Missing values found:\n", missing)
        df = df.dropna()

    # -------- Remove duplicates --------
    df = df.drop_duplicates()

    # -------- Basic numeric validation --------
    df = df[
        (df["revenue"] >= 0) &
        (df["expense"] >= 0) &
        (df["cogs"] >= 0)
    ]

    # -------- Financial consistency checks --------
    # Gross profit should roughly match revenue - cogs
    df = df[
        abs(df["gross_profit"] - (df["revenue"] - df["cogs"])) < 1e-2
    ]

    # Operating profit should be <= gross profit
    df = df[df["operating_profit"] <= df["gross_profit"]]

    # Net profit should be <= operating profit (usually)
    df = df[df["net_profit"] <= df["operating_profit"]]

    # -------- Convert date --------
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])

    # -------- Optional: flag suspicious rows --------
    high_expense_ratio = df["expense"] / df["revenue"] > 1.5
    if high_expense_ratio.any():
        print(f"[WARNING] {high_expense_ratio.sum()} rows with unusually high expense ratio")

    print(f"[INFO] Validation complete. Final rows: {len(df)}")

    return df