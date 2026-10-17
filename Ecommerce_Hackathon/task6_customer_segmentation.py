import pandas as pd
import numpy as np

def segment_customers(discounted_orders, customers):
    print("\n=== TASK 6: CUSTOMER SEGMENTATION ===")
    spending = discounted_orders.groupby("customer_id", as_index=False)["final_amount"].sum()
    spending = spending.rename(columns={"final_amount": "total_spending"})

    # Include customers with no orders so they are classified as Low Value.
    customer_info = customers[["customer_id", "name", "city"]].drop_duplicates("customer_id")
    segments = customer_info.merge(spending, on="customer_id", how="left")
    segments["total_spending"] = segments["total_spending"].fillna(0)

    conditions = [
        segments["total_spending"] >= 100000,
        segments["total_spending"].between(50000, 99999.999999),
        segments["total_spending"].between(20000, 49999.999999),
    ]
    labels = ["Premium", "High Value", "Regular"]
    segments["customer_segment"] = np.select(conditions, labels, default="Low Value")

    print("\nCustomers per segment:\n", segments["customer_segment"].value_counts())
    print("\nAverage spending by segment:\n",
          segments.groupby("customer_segment")["total_spending"].mean().sort_values(ascending=False))
    city_average = segments.groupby("city")["total_spending"].mean()
    if not city_average.empty:
        print("City with highest average customer spending:", city_average.idxmax(),
              "(", round(float(city_average.max()), 2), ")")
    else:
        print("City with highest average customer spending: unavailable")
    return segments
