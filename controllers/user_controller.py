from models.user import User

class UserController:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.current_user = None

    def login(self, username, password):
        user_data = self.db_manager.get_user(username, password)
        if user_data:
            self.current_user = User.from_tuple(user_data)
            return True
        return False

    def logout(self):
        self.current_user = None
