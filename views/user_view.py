import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, root, user_controller, on_login_success):
        self.root = root
        self.user_controller = user_controller
        self.on_login_success = on_login_success
        
        self.root.title("Вход в систему")
        self.root.geometry("300x200")

        tk.Label(root, text="Логин:").pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        tk.Label(root, text="Пароль:").pack(pady=5)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Войти", command=self.handle_login).pack(pady=20)

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_controller.login(username, password):
            self.on_login_success()
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")
