class Task:
    def __init__(self, id, title, description, priority, status, due_date, project_id, assignee_id):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.project_id = project_id
        self.assignee_id = assignee_id

    def __repr__(self):
        return f"Task({self.title}, {self.status})"
