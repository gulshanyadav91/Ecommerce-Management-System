import pandas as pd

def apply_discount_rules(clean, discount_rules):
    print("\n=== TASK 5: DISCOUNT ELIGIBILITY ===")
    df = clean.copy()

    # JSON is the source of truth; no membership percentages are hardcoded.
    rule_map = {
        str(rule["membership"]).strip().lower(): {
            "minimum_purchase": float(rule["minimum_purchase"]),
            "discount_percent": float(rule["discount_percent"]),
        }
        for rule in discount_rules
    }

    def discount_for_row(row):
        rule = rule_map.get(str(row["membership"]).strip().lower())
        amount = float(row["sales_amount"])
        if rule and amount >= rule["minimum_purchase"] and amount > 0:
            return pd.Series({
                "discount_status": "Eligible",
                "discount_percent": rule["discount_percent"]
            })
        return pd.Series({"discount_status": "Not Eligible", "discount_percent": 0.0})

    result = df.apply(discount_for_row, axis=1)
    df["discount_status"] = result["discount_status"]
    df["discount_percent"] = result["discount_percent"]
    df["discount_amount"] = df["sales_amount"] * df["discount_percent"] / 100
    df["final_amount"] = df["sales_amount"] - df["discount_amount"]
    print(df[["order_id", "membership", "sales_amount", "discount_status",
              "discount_percent", "discount_amount", "final_amount"]].head())
    return df
