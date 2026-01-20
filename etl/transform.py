# import pandas as pd


# def transform_data(df: pd.DataFrame) -> pd.DataFrame:
#     """
#     Clean and transform raw e-commerce data.

#     Steps:
#     - Drop duplicate rows
#     - Handle null values
#     - Convert InvoiceDate to datetime
#     - Add total_amount column

#     Args:
#         df (pd.DataFrame): Raw input DataFrame

#     Returns:
#         pd.DataFrame: Transformed DataFrame
#     """

#     # Make a copy to avoid mutating input
#     df = df.copy()

#     # Drop duplicate rows
#     df.drop_duplicates(inplace=True)

#     # Handle null values
#     # Remove rows with missing critical fields
#     critical_columns = ["InvoiceNo", "StockCode", "Quantity", "UnitPrice"]
#     df.dropna(subset=critical_columns, inplace=True)

#     # Convert InvoiceDate to datetime
#     df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

#     # Drop rows where date conversion failed
#     df.dropna(subset=["InvoiceDate"], inplace=True)

#     # Ensure numeric fields are valid
#     df["Quantity"] = df["Quantity"].astype(int)
#     df["UnitPrice"] = df["UnitPrice"].astype(float)

#     # Feature engineering
#     df["total_amount"] = df["Quantity"] * df["UnitPrice"]

#     return df


# if __name__ == "__main__":
#     # Local test
#     sample_df = pd.read_csv("data/raw/online_retail.csv")
#     transformed_df = transform_data(sample_df)
#     print(transformed_df.head())


def transform_data(records):
    """
    Simple transformation:
    quantity * unit_price = total_amount
    """
    transformed = []

    for r in records:
        total = r["quantity"] * r["unit_price"]
        transformed.append({
            "order_id": r["order_id"],
            "total_amount": total
        })

    return transformed

