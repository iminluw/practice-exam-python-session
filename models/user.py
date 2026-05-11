from datetime import datetime

class User:
    def __init__(self, username, email, role, id=None, password=None):
        self.id = id
        self.username = username
        self.email = email
        self.role = role
        self.password = password
        self.registration_date = datetime.now()

    @staticmethod
    def from_tuple(data):
        if not data: return None
        # Сопоставляем поля из БД: id, username, email, password, role
        return User(id=data[0], username=data[1], email=data[2], password=data[3], role=data[4])

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        }
