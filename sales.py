from database import c, execute

def create_bill(uid):
    try:
        pid = int(input("Product ID: "))
        qty = int(input("Quantity: "))
        date = input("Date: ")

        c.execute(
            "SELECT purchase_price,selling_price,quantity FROM product_details WHERE pro_id=?",
            (pid,)
        )
        row = c.fetchone()

        if not row:
            print("Invalid product")
            return

        p, s, stock = row

        if qty > stock:
            print("Not enough stock")
            return

        total = qty * s
        profit = (s - p) * qty

        execute("""
        INSERT INTO sales(product_id,quantity_sold,total_amount,profit,sale_date,user_id)
        VALUES (?,?,?,?,?,?)
        """, (pid, qty, total, profit, date, uid))

        execute(
            "UPDATE product_details SET quantity=quantity-? WHERE pro_id=?",
            (qty, pid)
        )

        print("Bill created successfully!")

    except Exception as e:
        print("Billing error:", e)

def view_sales(role, uid=None):
    if role == "staff":
        c.execute("""
        SELECT s.sales_id, p.item_name, s.quantity_sold, s.total_amount, s.sale_date
        FROM sales s
        JOIN product_details p ON s.product_id = p.pro_id
        WHERE s.user_id=?
        """, (uid,))
    else:
        c.execute("""
        SELECT s.sales_id, p.item_name, s.quantity_sold,
               s.total_amount, s.profit, s.sale_date, s.user_id
        FROM sales s
        JOIN product_details p ON s.product_id = p.pro_id
        """)

    for row in c.fetchall():
        print(row)

def view_profit():
    c.execute("SELECT SUM(profit) FROM sales")
    print("Total Profit:", c.fetchone()[0] or 0)
