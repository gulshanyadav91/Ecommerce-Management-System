import pandas as pd

def integrate_data(customers, products, orders):
    print("\n=== TASK 2: DATA INTEGRATION ===")
    before = len(orders)

    order_customers = orders.merge(
        customers, on="customer_id", how="left", indicator="_customer_merge"
    )
    missing_customer_info = int((order_customers["_customer_merge"] == "left_only").sum())
    order_customers = order_customers.drop(columns=["_customer_merge"])

    merged = order_customers.merge(
        products, on="product_id", how="left", indicator="_product_merge"
    )
    missing_product_info = int((merged["_product_merge"] == "left_only").sum())
    merged = merged.drop(columns=["_product_merge"])
    merged["gross_amount"] = merged["price"] * merged["quantity"]

    print("Rows in orders before merging:", before)
    print("Rows after merging:", len(merged))
    print("Orders missing customer information:", missing_customer_info)
    print("Orders missing product information:", missing_product_info)
    print("\nMerged dataset preview:\n", merged.head())
    return merged
