import sqlite3
import pandas as pd
from pathlib import Path


def load_to_sqlite(
    df: pd.DataFrame,
    db_path: str,
    table_name: str = "ecommerce_analytics"
) -> None:
    """
    Load transformed data into SQLite database.

    Args:
        df (pd.DataFrame): Transformed DataFrame
        db_path (str): Path to SQLite database file
        table_name (str): Target table name
    """

    # Ensure database directory exists
    db_file = Path(db_path)
    db_file.parent.mkdir(parents=True, exist_ok=True)

    # Connect to SQLite
    conn = sqlite3.connect(db_file)

    try:
        # Overwrite table to ensure idempotency
        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )
    finally:
        conn.close()


if __name__ == "__main__":
    # Local test
    from transform import transform_data

    raw_df = pd.read_csv("data/raw/online_retail.csv")
    transformed_df = transform_data(raw_df)

    load_to_sqlite(
        df=transformed_df,
        db_path="data/analytics.db",
        table_name="ecommerce_analytics"
    )

    print("Data successfully loaded into SQLite database.")
