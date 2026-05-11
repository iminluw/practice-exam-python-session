from datetime import datetime

class Task:
    def __init__(self, title, description, priority, due_date, project_id, assignee_id, id=None, status='pending'):
        self.id = id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.project_id = project_id
        self.assignee_id = assignee_id

    def update_status(self, new_status):
        self.status = new_status

    def is_overdue(self):
        return datetime.now() > self.due_date if self.due_date else False

    def to_dict(self):
        return self.__dict__
