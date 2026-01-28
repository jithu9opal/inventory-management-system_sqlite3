from database import c, execute

def login():
    u = input("Username: ")
    p = input("Password: ")
    c.execute(
        "SELECT id, role FROM users WHERE username=? AND password=?",
        (u, p)
    )
    return c.fetchone()

def signup():
    u = input("Username: ")
    p = input("Password: ")
    p2 = input("Confirm Password: ")

    if p != p2:
        print("Passwords do not match!")
        return

    print("1.Manager  2.Staff")
    try:
        r = int(input("Choose: "))
    except ValueError:
        print("Invalid choice")
        return

    if r == 1:
        role = "manager"
    elif r == 2:
        role = "staff"
    else:
        print("Invalid role")
        return

    try:
        execute(
            "INSERT INTO users(username,password,role) VALUES (?,?,?)",
            (u, p, role)
        )
        print("Account created successfully!")
    except:
        print("Username already exists")

def view_users():
    print("\nID | Username | Role")
    for row in c.execute("SELECT id,username,role FROM users"):
        print(row)

def delete_user():
    uid = int(input("User ID: "))
    c.execute("SELECT role FROM users WHERE id=?", (uid,))
    row = c.fetchone()

    if not row:
        print("User not found")
        return

    if row[0] == "admin":
        print("You can't delete admin!")
        return

    execute("DELETE FROM users WHERE id=?", (uid,))
    print("User deleted successfully")
