from models.task import Task

class TaskController:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_all_tasks(self):
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks")
            rows = cursor.fetchall()
            return [Task.from_tuple(row) for row in rows]

    def create_task(self, title, description, priority, due_date, assignee_id):
        with self.db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tasks (title, description, priority, status, due_date, assignee_id)
                VALUES (?, ?, ?, 'pending', ?, ?)
            """, (title, description, priority, due_date, assignee_id))
            conn.commit()
