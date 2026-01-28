from database import c, execute

def add_product():
    try:
        item = input("Item name: ")
        p = int(input("Purchase price: "))
        s = int(input("Selling price: "))
        q = int(input("Quantity: "))
        d = input("Purchase Date: ")
        w = input("Warranty: ")

        execute("""
        INSERT INTO product_details
        (item_name,purchase_price,selling_price,quantity,purchase_date,warranty)
        VALUES (?,?,?,?,?,?)
        """, (item, p, s, q, d, w))

        print("Product added successfully!")
    except Exception as e:
        print("Error:", e)

def view_products(role):
    if role == "staff":
        print("\nID | Item | Selling | Qty")
        c.execute("SELECT pro_id,item_name,selling_price,quantity FROM product_details")
    else:
        print("\nID | Item | Purchase | Selling | Qty")
        c.execute("SELECT pro_id,item_name,purchase_price,selling_price,quantity FROM product_details")

    for row in c.fetchall():
        print(row)

def delete_product():
    pid = int(input("Product ID: "))
    execute("DELETE FROM product_details WHERE pro_id=?", (pid,))
    print("Product deleted")
