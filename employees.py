from database import c, execute

def add_view_details(uid):
    c.execute("SELECT * FROM details_employees WHERE s_m_id=?", (uid,))
    row = c.fetchone()

    if row:
        print(f"""
Name: {row[2]}
Age: {row[3]}
Phone: {row[4]}
Emergency: {row[5]}
Email: {row[6]}
""")
    else:
        name = input("Name: ")
        age = input("Age: ")
        phone = input("Phone: ")
        emer = input("Emergency Contact: ")
        email = input("Email: ")

        execute("""
        INSERT INTO details_employees
        (s_m_id,name,age,phone,emergency_contact,email)
        VALUES (?,?,?,?,?,?)
        """, (uid, name, age, phone, emer, email))

        print("Details saved")
