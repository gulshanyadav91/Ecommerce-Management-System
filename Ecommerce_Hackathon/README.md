# E-Commerce Sales & Customer Intelligence System

This project implements the 10 tasks from the supplied Python Data Engineering Mock Hackathon.

## 1. Folder contents

- `solution.py`: runs the complete pipeline from Task 1 through Task 10.
- `task1_load_inspect.py`: loads CSV/JSON files and inspects them.
- `task2_data_integration.py`: merges orders with customers and products.
- `task3_clean_validate.py`: validates records, removes duplicate order IDs, parses dates, and excludes cancelled orders from sales.
- `task4_numpy_statistics.py`: computes statistics with NumPy.
- `task5_discount_eligibility.py`: reads discount rules from `discounts.json` and calculates discounts.
- `task6_customer_segmentation.py`: computes customer spending and segments.
- `task7_business_analytics.py`: generates top customers/products and category/city analyses.
- `task8_sqlite_database.py`: creates SQLite tables and runs the six required SQL queries.
- `task9_visualization.py`: creates the bar and pie charts.
- `task10_management_report.py`: writes `management_report.json`.
- Input files: `customers.csv`, `products.csv`, `orders.csv`, `discounts.json`.

## 2. Install dependencies

```bash
python -m pip install pandas numpy matplotlib
```

SQLite (`sqlite3`) and JSON are included in Python's standard library.

## 3. Run the project

Put the four real hackathon input files in this folder, replacing the example/template files if supplied separately. Do not change the input files during the hackathon.

```bash
python solution.py
```

Run from any current directory; `solution.py` uses its own folder to locate the inputs. It writes a transcript to `output.txt` and creates the database, report, and charts in this folder.

## 4. Important interpretation

- `sales_amount` is `gross_amount` only for Delivered orders; all other statuses contribute zero to sales.
- Discounts are applied per order using that order's `sales_amount` and the membership's JSON rule. A zero-value/cancelled order is not eligible.
- Customer segments use the sum of `final_amount` across a customer's orders. Customers without orders are included with spending zero.
- Order-value statistics use all valid order rows, with cancelled orders represented as zero sales, consistent with the challenge's cancellation rule.
- Category/city averages are averages across order rows, not averages of unique customers.
- SQL queries intentionally avoid window functions.

## 5. Input note

The included CSV and JSON files are small example templates so you can run the project immediately. If your hackathon provides actual inputs, use those files instead. Outputs depend on the input data.
