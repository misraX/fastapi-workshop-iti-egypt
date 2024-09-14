from collections.abc import KeysView
from core.database import users_db
from exceptions.user import UserNotFoundException
from models.user import User


class UserRepository(object):
    def __init__(self):
        self._database = users_db

    def get_by_id(self, user_id: int) -> User:
        user_ids: KeysView = self._database.keys()
        if user_id not in user_ids:
            raise UserNotFoundException("User not found")
        return self._database.get(user_id)
