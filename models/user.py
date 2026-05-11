class User:
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    @staticmethod
    def from_tuple(data):
        if not data: return None
        return User(*data)
