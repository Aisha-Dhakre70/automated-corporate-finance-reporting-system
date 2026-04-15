import pandas as pd
from database.db_connection import get_engine


def load_csv_to_db(csv_path):
    engine = get_engine()

    if engine is None:
        print("[ERROR] Could not create DB engine")
        return

    df = pd.read_csv(csv_path)

    df.to_sql(
        name="transactions",
        con=engine,
        if_exists="append",
        index=False,
        chunksize=1000
    )

    print("[INFO] Data loaded successfully!")


if __name__ == "__main__":
    load_csv_to_db("data/raw/financial_data.csv")