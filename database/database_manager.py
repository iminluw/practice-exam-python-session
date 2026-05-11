import sqlite3

class DatabaseManager:
    def __init__(self, db_path="task_manager.db"):
        self.db_path = db_path
        self.create_user_table()
        self.create_task_table()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    # Методы создания таблиц (важны для тестов)
    def create_user_table(self):
        with self.get_connection() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS users 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, email TEXT, password TEXT, role TEXT)''')

    def create_task_table(self):
        with self.get_connection() as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS tasks 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, 
                 priority TEXT, status TEXT, due_date TEXT, project_id INTEGER, assignee_id INTEGER)''')

    # Методы работы с пользователями
    def add_user(self, username, password, email="test@test.com", role="user"):
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)", 
                             (username, password, email, role))
                conn.commit()
        except sqlite3.IntegrityError:
            pass

    def get_user(self, username, password):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            return cursor.fetchone()

    # Методы работы с задачами
    def add_task(self, title, description, priority, due_date, assignee_id=None):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tasks (title, description, priority, status, due_date, assignee_id)
                VALUES (?, ?, ?, 'pending', ?, ?)
            """, (title, description, priority, due_date, assignee_id))
            conn.commit()

    def get_all_tasks(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            return cursor.fetchall()
