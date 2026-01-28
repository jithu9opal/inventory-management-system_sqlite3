# 🧾 Inventory Management System (Python + SQLite3)

A **role-based Inventory Management System** developed using **Python** and **SQLite3**.
This project is designed as a **college-level mini project** and demonstrates database integration, CRUD operations, and role-based access control through a Command-Line Interface (CLI).

---

## 📌 Project Overview

The Inventory Management System helps manage:

* Products and stock
* Sales and profit tracking
* Purchases and supplier balances
* Users (Admin, Manager, Staff)
* Employee personal details

The system enforces **role-based permissions**, ensuring each user can only access features allowed for their role.

---

## 🛠️ Technologies Used

* **Language:** Python 3
* **Database:** SQLite3
* **Interface:** Command Line Interface (CLI)

---

## 👥 User Roles & Features

### 👑 Admin

The Admin has **full control** over the system.

**Features:**

* Add / View / Delete Products
* Record Sales
* View All Sales
* View Profit Reports
* Manage Users (View / Delete)
* Manage Purchases (Add / View)
* Manage Employee Details (View / Delete)

---

### 👔 Manager

The Manager supervises sales and monitors staff activity.

**Features:**

* View Products & Stock
* Record Sales
* View Profit
* Monitor Staff Sales
* Add / View Own Personal Details (only once)

**Restrictions:**

* Cannot manage users
* Cannot manage purchases
* Cannot add or delete products

---

### 🧑‍🔧 Staff

Staff members handle daily sales operations.

**Features:**

* Make Sales (Generate Bills)
* Automatic Stock Update
* View Products
* Add / View Own Profile (only once)

**Restrictions:**

* Cannot view profit
* Cannot manage users
* Cannot manage purchases
* Cannot edit profile after submission

---

## 🗃️ Database Tables

* `users` – Stores user login credentials and roles
* `product_details` – Stores product and stock information
* `sales` – Stores sales and profit data
* `purchase` – Stores purchase and supplier details
* `bill_table` – Stores billing records
* `details_employess` – Stores staff & manager personal details

---

## 🔐 Default Admin Login

```
Username: admin
Password: admin123
```

---

## ▶️ How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/inventory-management-system.git
   ```

2. Navigate to the project folder:

   ```bash
   cd inventory-management-system
   ```

3. Run the application:

   ```bash
   python main.py
   ```

---

## 📂 Project Structure

```
Inventory-Management-System/
│
├── main.py            # Main application file
├── README.md          # Project documentation
├── inventory.db       # SQLite database (auto-created)
```

---

## 🎓 Academic Relevance

This project is suitable for:

* Python Mini Project
* Database Management Systems (DBMS)
* CRUD Operations Practice
* Role-Based Access Control Demonstration

---

## 🚀 Future Enhancements

* Password hashing for better security
* Date-wise sales reports
* Export reports to CSV/PDF
* GUI version using Tkinter or PyQt
* User activity logs

---

## 🤝 Author

**Developed by:** *Jithu Chittattukara*
**Course:** Python / DBMS Mini Project

---

⭐ If you find this project useful, feel free to star the repository on GitHub!
