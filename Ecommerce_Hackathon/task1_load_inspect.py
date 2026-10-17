import json
import pandas as pd

def load_and_inspect(data_dir="."):
    customers = pd.read_csv(f"{data_dir}/customers.csv")
    products = pd.read_csv(f"{data_dir}/products.csv")
    orders = pd.read_csv(f"{data_dir}/orders.csv")
    with open(f"{data_dir}/discounts.json", "r", encoding="utf-8") as f:
        discounts = json.load(f)

    print("\n=== TASK 1: LOAD AND INSPECT ===")
    print("Number of customers:", len(customers))
    print("Number of products:", len(products))
    print("Number of orders:", len(orders))
    print("Unique cities:", customers["city"].nunique())
    print("Product categories:", products["category"].nunique())
    print("\nCustomers shape:", customers.shape)
    print("Products shape:", products.shape)
    print("Orders shape:", orders.shape)
    print("\nFirst five customers:\n", customers.head())
    print("\nFirst five orders:\n", orders.head())
    print("\nDiscount rules:\n", json.dumps(discounts, indent=2))
    return customers, products, orders, discounts
