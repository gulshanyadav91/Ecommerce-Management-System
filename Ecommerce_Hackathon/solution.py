import os
import sys
import traceback

from task1_load_inspect import load_and_inspect
from task2_data_integration import integrate_data
from task3_clean_validate import clean_and_validate
from task4_numpy_statistics import calculate_statistics
from task5_discount_eligibility import apply_discount_rules
from task6_customer_segmentation import segment_customers
from task7_business_analytics import run_business_analytics
from task8_sqlite_database import create_database
from task9_visualization import create_charts
from task10_management_report import create_management_report

class Tee:
    """Write output to both the terminal and output.txt."""
    def __init__(self, *streams):
        self.streams = streams
    def write(self, message):
        for stream in self.streams:
            stream.write(message)
            stream.flush()
    def flush(self):
        for stream in self.streams:
            stream.flush()

def main():
    data_dir = os.path.dirname(os.path.abspath(__file__))
    required = ["customers.csv", "products.csv", "orders.csv", "discounts.json"]
    missing = [name for name in required if not os.path.exists(os.path.join(data_dir, name))]
    if missing:
        print("Missing required input file(s):", ", ".join(missing))
        print("Place all four input files in this folder and run solution.py again.")
        sys.exit(1)

    output_path = os.path.join(data_dir, "output.txt")
    with open(output_path, "w", encoding="utf-8") as output_file:
        original_stdout = sys.stdout
        sys.stdout = Tee(original_stdout, output_file)
        try:
            customers, products, orders, discount_rules = load_and_inspect(data_dir)
            merged = integrate_data(customers, products, orders)
            clean = clean_and_validate(merged)
            stats = calculate_statistics(clean)
            discounted = apply_discount_rules(clean, discount_rules)
            segments = segment_customers(discounted, customers)
            analytics = run_business_analytics(discounted, segments, products, orders)
            create_database(data_dir, customers, products, orders, discounted)
            create_charts(analytics, segments, data_dir)
            create_management_report(data_dir, customers, products, orders, stats, analytics, segments)
            print("\nAll tasks completed.")
            print("Generated files: ecommerce_intelligence.db, management_report.json, "
                  "category_sales.png, customer_segments.png, output.txt")
        except Exception:
            traceback.print_exc()
            raise
        finally:
            sys.stdout = original_stdout

if __name__ == "__main__":
    main()
