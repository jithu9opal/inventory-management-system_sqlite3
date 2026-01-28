import sqlite3

conn = sqlite3.connect("mini_inventory_management_system.db")
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON;")

def execute(query, params=()):
    c.execute(query, params)
    conn.commit()

def setup_tables():
    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('admin','manager','staff'))
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS product_details(
        pro_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT UNIQUE NOT NULL,
        purchase_price INTEGER,
        selling_price INTEGER,
        quantity INTEGER,
        purchase_date TEXT,
        warranty TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS sales(
        sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity_sold INTEGER,
        total_amount INTEGER,
        profit INTEGER,
        sale_date TEXT,
        user_id INTEGER,
        FOREIGN KEY(product_id) REFERENCES product_details(pro_id),
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE SET NULL
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS details_employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        s_m_id INTEGER UNIQUE,
        name TEXT,
        age INTEGER,
        phone TEXT,
        emergency_contact TEXT,
        email TEXT,
        FOREIGN KEY(s_m_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """)

def create_admin():
    c.execute("SELECT 1 FROM users WHERE role='admin'")
    if not c.fetchone():
        execute(
            "INSERT INTO users(username,password,role) VALUES (?,?,?)",
            ('admin', 'admin123', 'admin')
        )
