import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self, root, task_controller):
        self.root = root
        self.task_controller = task_controller
        self.root.title("Менеджер задач")
        self.root.geometry("600x400")

        tk.Label(root, text="Список ваших задач", font=("Arial", 14)).pack(pady=10)

        self.tree = ttk.Treeview(root, columns=("ID", "Название", "Статус"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Название", text="Название")
        self.tree.heading("Статус", text="Статус")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.load_tasks()

    def load_tasks(self):
        tasks = self.task_controller.get_all_tasks()
        for task in tasks:
            self.tree.insert("", tk.END, values=(task.id, task.title, task.status))
