import sqlite3
import os

def create_database(data_dir, customers, products, orders, analyzed_orders):
    print("\n=== TASK 8: SQLITE DATABASE ===")
    db_path = os.path.join(data_dir, "ecommerce_intelligence.db")
    conn = sqlite3.connect(db_path)
    try:
        customers.to_sql("customers", conn, if_exists="replace", index=False)
        products.to_sql("products", conn, if_exists="replace", index=False)
        orders.to_sql("orders", conn, if_exists="replace", index=False)
        analyzed_orders.to_sql("order_analysis", conn, if_exists="replace", index=False)

        queries = {
            "SQL 1 - Customer + Order JOIN": """
                SELECT c.name, c.city, o.order_id, o.product_id,
                       COALESCE(a.sales_amount, 0) AS sales_amount
                FROM orders o
                JOIN customers c ON c.customer_id = o.customer_id
                LEFT JOIN order_analysis a ON a.order_id = o.order_id
                LIMIT 10
            """,
            "SQL 2 - Category Sales": """
                SELECT p.category, SUM(COALESCE(a.sales_amount, 0)) AS total_sales
                FROM products p
                JOIN orders o ON o.product_id = p.product_id
                LEFT JOIN order_analysis a ON a.order_id = o.order_id
                GROUP BY p.category
                ORDER BY total_sales DESC
            """,
            "SQL 3 - Customers with sales above 50000": """
                SELECT c.customer_id, c.name, SUM(COALESCE(a.sales_amount, 0)) AS total_sales
                FROM customers c
                JOIN orders o ON o.customer_id = c.customer_id
                LEFT JOIN order_analysis a ON a.order_id = o.order_id
                GROUP BY c.customer_id, c.name
                HAVING SUM(COALESCE(a.sales_amount, 0)) > 50000
                ORDER BY total_sales DESC
            """,
            "SQL 4 - Products never ordered": """
                SELECT product_id, product_name FROM products
                WHERE product_id IN (
                    SELECT product_id FROM products
                    EXCEPT
                    SELECT product_id FROM orders
                )
            """,
            "SQL 5 - Customers without orders": """
                SELECT c.customer_id, c.name
                FROM customers c
                LEFT JOIN orders o ON c.customer_id = o.customer_id
                WHERE o.customer_id IS NULL
            """,
            "SQL 6 - Average order value by city": """
                SELECT c.city, AVG(COALESCE(a.sales_amount, 0)) AS average_order_value
                FROM customers c
                JOIN orders o ON c.customer_id = o.customer_id
                LEFT JOIN order_analysis a ON a.order_id = o.order_id
                GROUP BY c.city
                ORDER BY average_order_value DESC
            """
        }
        for title, query in queries.items():
            print(f"\n{title}:\n")
            try:
                print(__import__("pandas").read_sql_query(query, conn))
            except Exception as exc:
                print("Query error:", exc)
    finally:
        conn.close()
    print("Database created:", db_path)
    return db_path
