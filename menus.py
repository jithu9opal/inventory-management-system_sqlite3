from products import add_product, view_products, delete_product
from sales import create_bill, view_sales, view_profit
from users import view_users, delete_user
from employees import add_view_details

def admin_menu():
    while True:
        print("\nADMIN MENU")
        print("1.Add Product \n2.View Products \n3.Delete Product")
        print("4.Create Bill \n5.View Sales \n6.View Profit")
        print("7.View Users \n8.Delete User \n9.Logout")

        try:
            ch = int(input("Choose: "))
        except:
            continue

        if ch == 1:
            add_product()
        elif ch == 2:
            "\n"
            view_products("admin")
        elif ch == 3:
            delete_product()
        elif ch == 4:
            create_bill(1)
        elif ch == 5:
            view_sales("admin")
        elif ch == 6:
            view_profit()
        elif ch == 7:
            view_users()
        elif ch == 8:
            delete_user()
        elif ch == 9:
            break

def manager_menu(uid):
    while True:
        print("\nMANAGER MENU")
        print("1.View Products \n2.Add Product \n3.Create Bill")
        print("4.View Sales \n5.View Profit \n6.My Details 7.Logout")

        try:
            ch = int(input("Choose: "))
        except:
            continue

        if ch == 1:
            view_products("manager")
        elif ch == 2:
            add_product()
        elif ch == 3:
            create_bill(uid)
        elif ch == 4:
            view_sales("manager")
        elif ch == 5:
            view_profit()
        elif ch == 6:
            add_view_details(uid)
        elif ch == 7:
            break

def staff_menu(uid):
    while True:
        print("\nSTAFF MENU")
        print("1.View Products \n2.Create Bill")
        print("3.View My Sales \n4.My Details \n5.Logout")

        try:
            ch = int(input("Choose: "))
        except:
            continue

        if ch == 1:
            view_products("staff")
        elif ch == 2:
            create_bill(uid)
        elif ch == 3:
            view_sales("staff", uid)
        elif ch == 4:
            add_view_details(uid)
        elif ch == 5:
            break