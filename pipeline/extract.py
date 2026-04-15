import pandas as pd
import json
import os
from database.db_connection import get_engine

# Metadata file path
METADATA_PATH = os.path.join("metadata", "pipeline_state.json")


# Get last processed ID from metadata file
def get_last_processed_id():
    if not os.path.exists(METADATA_PATH):
        return 0

    with open(METADATA_PATH, "r") as f:
        return json.load(f).get("last_processed_id", 0)

# Update metadata with latest processed ID
def update_last_processed_id(last_id):
    with open(METADATA_PATH, "w") as f:
        json.dump({"last_processed_id": last_id}, f)

# Extract new data from MySQL (incremental)
def extract_data():
    engine = get_engine()

    if engine is None:
        print("[ERROR] DB connection failed")
        return None

    last_id = get_last_processed_id()

    query = f"""
        SELECT *
        FROM transactions
        WHERE id > {last_id}
        ORDER BY id ASC
    """

    try:
        df = pd.read_sql(query, engine)

        if df.empty:
            print("[INFO] No new data found")
            return None

        # Update metadata
        new_last_id = int(df["id"].max())
        update_last_processed_id(new_last_id)

        print(f"[INFO] Extracted {len(df)} records")

        return df

    except Exception as e:
        print(f"[ERROR] Extraction failed: {e}")
        return None