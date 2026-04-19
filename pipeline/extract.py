import pandas as pd
import json
import os
from sqlalchemy import text
from database.db_connection import get_engine
from utils.logger import setup_logger

# ---------------- CONFIG ----------------
METADATA_PATH = os.path.join("metadata", "pipeline_state.json")
TABLE_NAME = "financial_data"

logger = setup_logger()


# ---------------- METADATA HANDLING ----------------
def get_last_processed_id():
    if not os.path.exists(METADATA_PATH):
        return 0

    try:
        with open(METADATA_PATH, "r") as f:
            return json.load(f).get("last_processed_id", 0)
    except Exception:
        return 0


def update_last_processed_id(last_id):
    os.makedirs(os.path.dirname(METADATA_PATH), exist_ok=True)

    with open(METADATA_PATH, "w") as f:
        json.dump({"last_processed_id": last_id}, f)


# ---------------- EXTRACTION ----------------
def extract_data():
    engine = get_engine()

    if engine is None:
        logger.error("DB connection failed")
        return None

    last_id = get_last_processed_id()

    
    query = text(f"""
        SELECT 
            id,
            company,
            date,
            revenue,
            expense,
            cogs,
            gross_profit,
            operating_profit,
            net_profit,
            category,
            region
        FROM {TABLE_NAME}
        WHERE id > :last_id
        ORDER BY id ASC
    """)

    try:
        
        df = pd.read_sql(query, engine, params={"last_id": last_id})

        if df.empty:
            logger.info("No new data found")
            print("[INFO] No new data found")
            return None

        # Convert date column
        df["date"] = pd.to_datetime(df["date"])

        # Update metadata AFTER successful extraction
        new_last_id = int(df["id"].max())
        update_last_processed_id(new_last_id)

        logger.info(f"Extracted {len(df)} records (ID > {last_id})")
        print(f"[INFO] Extracted {len(df)} records")

        return df

    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        print(f"[ERROR] Extraction failed: {e}")
        return None


# ---------------- MAIN ----------------
if __name__ == "__main__":
    df = extract_data()
    if df is not None:
        print(df.head())