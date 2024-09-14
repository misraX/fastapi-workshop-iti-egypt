from collections.abc import KeysView
from typing import Optional, ValuesView, Iterable

from core.database import users_db
from models.user import User


class UserRepository(object):
    def __init__(self):
        self._database = users_db

    def get_by_id(self, user_id: int) -> Optional[User]:
        user_ids: KeysView = self._database.keys()
        if user_id not in user_ids:
            return None
        return self._database.get(user_id)

    def get_user_list(self, user_name: Optional[str] = None) -> Optional[Iterable[User]]:
        if user_name:
            users_values: ValuesView = self._database.values()
            user_by_name = filter(
                lambda user: user.user_name == user_name,
                users_values
            )
            return user_by_name
        return self._database.values()

    def create_user(self, user: User) -> User:
        user = user.model_dump()
        user_model = User(**user)
        self._database[user_model.user_id] = user_model
        return user_model

