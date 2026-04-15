from sqlalchemy import create_engine
from config.db_config import DB_CONFIG


def get_engine():
    # Create SQLAlchemy engine using config
    try:
        connection_string = (
            f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
            f"{DB_CONFIG['host']}/{DB_CONFIG['database']}"
        )

        engine = create_engine(connection_string)
        return engine

    except Exception as e:
        print(f"[ERROR] Engine creation failed: {e}")
        return None

if __name__ == "__main__":
    engine = get_engine()
    if engine:
        print("Database connection successful")
    else:
        print("Database connection failed")
