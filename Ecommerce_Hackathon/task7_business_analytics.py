import pandas as pd

def run_business_analytics(discounted_orders, segments, products, orders):
    print("\n=== TASK 7: BUSINESS ANALYTICS ===")
    df = discounted_orders.copy()

    # Customer final spending
    top_customers = (df.groupby(["customer_id", "name", "city"], dropna=False)["final_amount"]
                       .sum().reset_index().sort_values("final_amount", ascending=False).head(5))
    print("\nTop 5 customers by final spending:\n", top_customers)

    # Product sales
    top_products = (df.groupby(["product_id", "product_name", "category"], dropna=False)["sales_amount"]
                      .sum().reset_index().sort_values("sales_amount", ascending=False).head(5))
    print("\nTop 5 products by sales:\n", top_products)

    category_sales = df.groupby("category", dropna=False).agg(
        total_sales=("sales_amount", "sum"),
        average_sales=("sales_amount", "mean")
    ).reset_index().sort_values("total_sales", ascending=False)
    print("\nCategory-wise sales:\n", category_sales)

    city_sales = df.groupby("city", dropna=False).agg(
        total_sales=("sales_amount", "sum"),
        average_sales=("sales_amount", "mean")
    ).reset_index().sort_values("total_sales", ascending=False)
    print("\nCity-wise sales:\n", city_sales)

    best_category = category_sales.iloc[0]["category"] if not category_sales.empty else ""
    quantity_sold = df.groupby(["product_id", "product_name"], dropna=False)["quantity"].sum()
    most_ordered_product = quantity_sold.idxmax()[1] if not quantity_sold.empty else ""
    highest_order = df.loc[df["final_amount"].idxmax()] if not df.empty else None

    total_orders = len(df)
    cancelled_pct = (100 * df["order_status"].astype(str).str.strip().str.lower().eq("cancelled").sum()
                     / total_orders) if total_orders else 0.0

    print("\nBest-performing category:", best_category)
    print("Most frequently ordered product:", most_ordered_product)
    print("Highest-value order:\n", highest_order if highest_order is not None else "No orders")
    print(f"Cancelled order percentage: {cancelled_pct:.2f}%")

    return {
        "top_customers": top_customers,
        "top_products": top_products,
        "category_sales": category_sales,
        "city_sales": city_sales,
        "best_category": best_category,
        "most_ordered_product": most_ordered_product,
        "highest_order": highest_order,
        "cancelled_order_percentage": float(cancelled_pct),
    }
