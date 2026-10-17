import pandas as pd
import numpy as np

def clean_and_validate(merged):
    print("\n=== TASK 3: DATA CLEANING AND VALIDATION ===")
    df = merged.copy()

    print("\nMissing values by column:\n", df.isna().sum())
    print("Duplicate order IDs:", int(df["order_id"].duplicated().sum()))
    print("Invalid quantity rows:", int((pd.to_numeric(df["quantity"], errors="coerce") <= 0).sum()
                                       + pd.to_numeric(df["quantity"], errors="coerce").isna().sum()))
    prices = pd.to_numeric(df["price"], errors="coerce")
    print("Invalid price rows:", int((prices <= 0).sum() + prices.isna().sum()))
    print("Unique order statuses:", df["order_status"].dropna().unique().tolist())
    print("Unique payment methods:", df["payment_method"].dropna().unique().tolist())

    df = df.drop_duplicates(subset=["order_id"], keep="first").copy()
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["gross_amount"] = df["price"] * df["quantity"]

    valid = (
        df["order_id"].notna()
        & df["customer_id"].notna()
        & df["product_id"].notna()
        & df["quantity"].notna()
        & (df["quantity"] > 0)
        & df["price"].notna()
        & (df["price"] > 0)
        & df["order_date"].notna()
        & df["name"].notna()
        & df["product_name"].notna()
        & df["order_status"].notna()
    )
    clean = df.loc[valid].copy()
    clean["sales_amount"] = np.where(
        clean["order_status"].astype(str).str.strip().str.lower().eq("delivered"),
        clean["gross_amount"],
        0.0
    )
    print("Rows after duplicate removal and validation:", len(clean))
    print("Delivered sales total (cancelled orders contribute zero):", clean["sales_amount"].sum())
    return clean
