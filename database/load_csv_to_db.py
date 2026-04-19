import pandas as pd
from database.db_connection import get_engine


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


def validate_dataframe(df):
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_cols:
        raise ValueError(f"[ERROR] Missing columns: {missing_cols}")

    # Basic sanity checks
    if df["revenue"].lt(0).any():
        raise ValueError("[ERROR] Negative revenue found")

    return True


def load_csv_to_db(csv_path):
    engine = get_engine()

    if engine is None:
        print("[ERROR] Could not create DB engine")
        return

    try:
        # Load CSV
        df = pd.read_csv(csv_path)

        print(f"[INFO] Loaded {len(df)} rows from CSV")

        # Convert date
        df["date"] = pd.to_datetime(df["date"])

        # Validate structure
        validate_dataframe(df)

        # Load into DB
        df.to_sql(
            name="financial_data",  # updated table name
            con=engine,
            if_exists="append",
            index=False,
            chunksize=1000,
            method="multi"  # faster inserts (nice touch)
        )

        print("[INFO] Data loaded successfully into 'financial_data'!")

    except Exception as e:
        print(f"[ERROR] Failed to load data: {e}")


if __name__ == "__main__":
    load_csv_to_db("data/raw/financial_data.csv")
