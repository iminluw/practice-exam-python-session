import sqlite3

class DatabaseManager:
    def __init__(self, db_path="task_manager.db"):
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        with self.get_connection() as conn:
            # Таблица пользователей (id, username, email, password, role)
            conn.execute('''CREATE TABLE IF NOT EXISTS users 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, email TEXT, password TEXT, role TEXT)''')
            # Таблица задач
            conn.execute('''CREATE TABLE IF NOT EXISTS tasks 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, 
                 priority TEXT, status TEXT, due_date TEXT, project_id INTEGER, assignee_id INTEGER)''')
            conn.commit()

    def add_user(self, username, password, email="test@test.com", role="user"):
        try:
            with self.get_connection() as conn:
                conn.execute("INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)", 
                             (username, email, password, role))
                conn.commit()
        except sqlite3.IntegrityError:
            pass

    def get_user(self, username, password):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, email, password, role FROM users WHERE username = ? AND password = ?", (username, password))
            return cursor.fetchone()

    def add_task(self, title, description, priority, due_date, assignee_id=None):
        with self.get_connection() as conn:
            conn.execute("""
                INSERT INTO tasks (title, description, priority, status, due_date, assignee_id)
                VALUES (?, ?, ?, 'pending', ?, ?)
            """, (title, description, priority, due_date, assignee_id))
            conn.commit()

    def delete_task(self, task_id):
        with self.get_connection() as conn:
            conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()

    def get_all_tasks(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            return cursor.fetchall()
