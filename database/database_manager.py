import sqlite3

class DatabaseManager:
    def __init__(self, db_path="task_manager.db"):
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        # Создаем подключение к файлу базы
        return sqlite3.connect(self.db_path)

    def init_db(self):
        # Создаем таблицы, если их еще нет
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Таблица пользователей
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role TEXT NOT NULL
                )
            ''')
            
            # Таблица задач
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    priority TEXT,
                    status TEXT DEFAULT 'pending',
                    due_date TEXT,
                    project_id INTEGER,
                    assignee_id INTEGER,
                    FOREIGN KEY (assignee_id) REFERENCES users (id)
                )
            ''')
            conn.commit()

    # Пример метода для добавления задачи (INSERT)
    def add_task(self, title, description, priority, due_date):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO tasks (title, description, priority, due_date)
                VALUES (?, ?, ?, ?)
            ''', (title, description, priority, due_date))
            conn.commit()

    # Пример метода для получения всех задач (SELECT)
    def get_all_tasks(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM tasks')
            return cursor.fetchall()
