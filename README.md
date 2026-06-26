# ☕ Royal Cafe Management System

A feature-rich terminal-based Cafe Management System developed in Python as a second-year B.Tech Computer Science mini project. The project demonstrates object-oriented programming, secure authentication, data management using Pandas, and an interactive command-line interface built with the Rich library.

Unlike a basic billing application, this project includes separate administrative and customer functionalities, secure password storage, persistent data management, and sales tracking.

---

# Features

## Administrator

* Secure administrator authentication using **bcrypt** hashed passwords.
* Add new menu items.
* Remove existing menu items.
* Update item prices.
* Create discount coupons.
* Remove discount coupons.
* View complete menu.
* View customer reviews.
* View sales history.
* View active discount coupons.

## Customer

* Browse the cafe menu.
* Place orders with multiple items.
* Apply discount coupons.
* Automatic bill generation.
* Submit customer reviews.
* Persistent order records.

---

# Technologies Used

* Python
* Pandas
* Rich
* bcrypt
* Pickle
* CSV
* OOP (Object-Oriented Programming)

---

# Data Storage

The project stores application data using CSV files and Pickle.

Files used include:

* menu.csv
* sales.csv
* reviews.csv
* discount.csv
* admin.pkl

---

# Security Features

* Passwords are never stored in plain text.
* Administrator credentials are securely hashed using bcrypt.
* Password strength validation is performed during administrator registration.
* Basic protection against unauthorized reinitialization of administrator credentials.

---

# Project Structure

```text
Cafe Management System
│
├── Main Python Program
├── menu.csv
├── sales.csv
├── reviews.csv
├── discount.csv
└── admin.pkl
```

---

# Libraries Used

```python
pandas
rich
bcrypt
pickle
getpass
datetime
pytz
os
time
```

---

# Learning Outcomes

This project helped me gain practical experience with:

* Object-Oriented Programming
* Data persistence
* File handling
* Password hashing
* Authentication systems
* Working with Pandas DataFrames
* Building terminal-based user interfaces
* Input validation
* Software design for medium-sized applications

---

# Future Improvements

Possible future enhancements include:

* Migration from CSV files to SQLite or MySQL.
* Multi-administrator support.
* Inventory management.
* Sales analytics dashboard.
* PDF invoice generation.
* Role-based permission levels.
* Modular project structure.
* REST API integration.
* GUI or web interface.

---

# Author

**Shaurya Garg**

Second-Year B.Tech Computer Science Student

Interested in Backend Development, Systems Programming, Operating Systems, Compiler Design, and Software Internals.

---

If you find this project helpful or interesting, feel free to star the repository.
