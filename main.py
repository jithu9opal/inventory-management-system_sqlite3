from database import setup_tables, create_admin, conn
from users import login, signup
from menus import admin_menu, manager_menu, staff_menu

setup_tables()
create_admin()

while True:
    print("\n1.Login")
    print("2.Signup" )
    print("3.Exit")
    try:
        ch = int(input("Choose: "))
    except:
        continue

    if ch == 1:
        result = login()
        if not result:
            print("Invalid login")
            continue

        uid, role = result

        if role == "admin":
            admin_menu()
        elif role == "manager":
            manager_menu(uid)
        elif role == "staff":
            staff_menu(uid)

    elif ch == 2:
        signup()

    elif ch == 3:
        break

conn.close()
print("Good luck!")