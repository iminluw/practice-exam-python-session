import tkinter as tk
from database.database_manager import DatabaseManager
from controllers.user_controller import UserController
from controllers.task_controller import TaskController
from views.user_view import LoginWindow  # Путь изменен на твой файл
from views.main_window import MainWindow

def main():
    root = tk.Tk()
    db_manager = DatabaseManager()
    
    # Создаем админа для теста (логин: admin, пароль: admin)
    db_manager.add_user("admin", "admin", "admin")
    
    user_ctrl = UserController(db_manager)
    task_ctrl = TaskController(db_manager)

    def show_main():
        for widget in root.winfo_children():
            widget.destroy()
        MainWindow(root, task_ctrl)

    LoginWindow(root, user_ctrl, show_main)
    root.mainloop()

if __name__ == "__main__":
    main()
