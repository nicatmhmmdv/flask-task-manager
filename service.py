import mysql.connector

db_config = {
    'host': 'mysql_host',
    'user': 'mysql_user',         
    'password': 'password',          
    'database': 'db_name'
}

def get_db_connection():
    return mysql.connector.connect(use_pure=True, **db_config)

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            status VARCHAR(50) DEFAULT 'Pending'
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def get_all_tasks():
    conn = get_db_connection()
    # dictionary=True lets us use task['title'] instead of task[1]
    cursor = conn.cursor(dictionary=True) 
    
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return rows

def add_task(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    
    conn.commit()
    cursor.close()
    conn.close()
