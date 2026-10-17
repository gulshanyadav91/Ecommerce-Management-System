import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def create_charts(analytics, segments, data_dir="."):
    print("\n=== TASK 9: VISUALIZATION ===")
    category_sales = analytics["category_sales"]
    plt.figure(figsize=(9, 5))
    if not category_sales.empty:
        plt.bar(category_sales["category"].astype(str), category_sales["total_sales"])
    plt.title("Total Sales by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    bar_path = os.path.join(data_dir, "category_sales.png")
    plt.savefig(bar_path, dpi=150)
    plt.close()

    segment_counts = segments["customer_segment"].value_counts().reindex(
        ["Premium", "High Value", "Regular", "Low Value"], fill_value=0
    )
    plt.figure(figsize=(7, 7))
    if segment_counts.sum() > 0:
        plt.pie(segment_counts, labels=segment_counts.index, autopct="%1.1f%%", startangle=90)
    else:
        plt.text(0.5, 0.5, "No customer data", ha="center", va="center")
    plt.title("Customer Segment Distribution")
    plt.tight_layout()
    pie_path = os.path.join(data_dir, "customer_segments.png")
    plt.savefig(pie_path, dpi=150)
    plt.close()
    print("Saved:", bar_path)
    print("Saved:", pie_path)
    return bar_path, pie_path
