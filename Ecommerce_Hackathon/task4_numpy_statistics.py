import numpy as np

def calculate_statistics(clean):
    print("\n=== TASK 4: NUMPY STATISTICAL ANALYSIS ===")
    # Order value means delivered sales amount; cancelled orders contribute zero.
    values = clean["sales_amount"].fillna(0).to_numpy(dtype=float)
    quantities = clean["quantity"].to_numpy(dtype=float)
    stats = {
        "total_sales": float(np.sum(values)) if values.size else 0.0,
        "average_order_value": float(np.mean(values)) if values.size else 0.0,
        "median_order_value": float(np.median(values)) if values.size else 0.0,
        "order_value_std_dev": float(np.std(values)) if values.size else 0.0,
        "maximum_order_value": float(np.max(values)) if values.size else 0.0,
        "minimum_order_value": float(np.min(values)) if values.size else 0.0,
        "average_quantity_per_order": float(np.mean(quantities)) if quantities.size else 0.0,
    }
    for key, value in stats.items():
        print(f"{key}: {value:.2f}")
    return stats
