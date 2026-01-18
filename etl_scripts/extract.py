import pandas as pd
from pathlib import Path


def extract_raw_data(file_path: str) -> pd.DataFrame:
    """
    Extract raw data from CSV file.

    Args:
        file_path (str): Path to raw CSV file

    Returns:
        pd.DataFrame: Raw data as DataFrame
    """
    csv_path = Path(file_path)

    if not csv_path.exists():
        raise FileNotFoundError(f"Raw data file not found at {file_path}")

    df = pd.read_csv(csv_path)

    return df


if __name__ == "__main__":
    # For local testing / debugging
    raw_file_path = "data/raw/online_retail.csv"
    df = extract_raw_data(raw_file_path)
    print(df.head())
