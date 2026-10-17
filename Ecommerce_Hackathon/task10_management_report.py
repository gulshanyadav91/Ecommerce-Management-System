import json
import os
import math

def _json_safe(value):
    if value is None:
        return None
    if hasattr(value, "item"):
        value = value.item()
    if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
        return None
    return value

def create_management_report(data_dir, customers, products, orders, stats, analytics, segments):
    print("\n=== TASK 10: MANAGEMENT REPORT ===")
    highest = analytics["highest_order"]
    report = {
        "total_customers": int(len(customers)),
        "total_products": int(len(products)),
        "total_orders": int(len(orders)),
        "total_sales": _json_safe(stats["total_sales"]),
        "average_order_value": _json_safe(stats["average_order_value"]),
        "top_customer": str(analytics["top_customers"].iloc[0]["name"])
                        if not analytics["top_customers"].empty else "",
        "best_category": str(analytics["best_category"]),
        "highest_value_order": _json_safe(highest["order_id"]) if highest is not None else None,
        "cancelled_order_percentage": _json_safe(analytics["cancelled_order_percentage"]),
        "premium_customers": int((segments["customer_segment"] == "Premium").sum()),
    }
    path = os.path.join(data_dir, "management_report.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, default=str)
    print(json.dumps(report, indent=4))
    print("Saved:", path)
    return report
