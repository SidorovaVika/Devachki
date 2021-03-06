from flask_login import UserMixin
from project.models.user import User


class LoginUser(UserMixin):
    def __init__(self, user):
        self.user = user

    def get_id(self):
        return str(self.user.id)


def load_user(user_id):
    user = User.query.filter(User.id == int(user_id)).first()
    return LoginUser(user)
