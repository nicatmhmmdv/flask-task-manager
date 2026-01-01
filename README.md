# Flask Task Manager

A dynamic Task Management System built with **Python**, **Flask**, and **MySQL**.
This project demonstrates the "Service Layer" architecture, separating the database logic from the web application routes.

## 🚀 Features
* **View Tasks:** Dynamic list rendering using Jinja2 templates.
* **Add Tasks:** Simple form to insert data into the MySQL database.
* **Status Tracking:** Visual badges for "Pending" vs "Done" tasks.
* **Database Integration:** Real-time data persistence using MySQL.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Database:** MySQL (via `mysql-connector-python`)
* **Templating:** Jinja2, HTML5, CSS3

## ⚙️ Setup & Installation

Follow these steps to run the project locally on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/nicatmhmmdv/flask-task-manager.git](https://github.com/nicatmhmmdv/flask-task-manager.git)
cd flask-task-manager
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

Windows:

```bash

python -m venv venv
.\venv\Scripts\activate
```

Mac/Linux:

```bash

python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Configure the Database
You need a MySQL server running (e.g., via XAMPP, WAMP, or standalone MySQL).

Login to your MySQL server.

Run the following SQL commands to set up the user and table:

SQL

-- 1. Create the database
CREATE DATABASE IF NOT EXISTS task_app_db;

-- 2. Create a secure user
-- (If you change the password here, update it in service.py too)
CREATE USER IF NOT EXISTS 'task_user'@'%' IDENTIFIED BY 'secure_pass';
GRANT ALL PRIVILEGES ON task_app_db.* TO 'task_user'@'%';
FLUSH PRIVILEGES;

-- 3. Create the table
USE task_app_db;
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending'
);
5. Run the Application
```bash
python app.py
```
Open your browser and go to: http://127.0.0.1:5000

📂 Project Structure
Plaintext

flask-task-manager/
├── app.py           # The Controller (Flask Routes)
├── service.py       # The Service Layer (Database Logic)
├── requirements.txt # List of dependencies
├── templates/       # HTML Files (Jinja2)
│   ├── base.html    # Layout Skeleton
│   └── index.html   # Main Dashboard
└── README.md        # Documentation
🔮 Future Improvements
Add functionality to "Delete" tasks.

Add functionality to "Mark as Done".

Add User Login/Authentication.

📝 License
This project is open source.
