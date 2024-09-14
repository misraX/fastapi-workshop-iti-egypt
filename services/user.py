from collections.abc import Iterable
from typing import Optional

from fastapi import HTTPException, Depends

from models.user import User
from repositories.user import UserRepository


class UserService(object):
    def __init__(self, user_repository: UserRepository = Depends(UserRepository)):
        self._user_repository = user_repository

    def get_user_by_id(self, user_id: int) -> User:
        """
        Get user by id.

        - Consume the repository querying
          - Query user by a give id
            - if the user does not exist, HANDLE EXCEPTION
            - if the user has been found, return the user
        :param user_id:
        :return: User
        """
        user = self._user_repository.get_by_id(user_id)
        if not user:
            raise HTTPException(404, detail="User not found")
        return user

    def get_user_list(self, user_name: Optional[str] = None) -> Optional[Iterable[User]]:
        """
        List users, with filters if any

        Allowed filters are:
         - user_name

        :param user_name: str
        :return: Optional[Iterable[User]]
        """
        return self._user_repository.get_user_list(user_name=user_name)

    def create_user(self, user: User) -> User:
        """
        Create a new user.

        :param user: User
        :return: User
        """
        global users_db
        user = self._user_repository.get_by_id(user.user_id)
        if user:
            raise HTTPException(400, 'User already exists.')
        user_created = self._user_repository.create_user(user=user)
        return user_created

    def bulk_create_user(self, users: list[User]) -> Iterable[User]:
        """
        Bulk create users

        :param users: list[User]
        :return: Iterable[User]
        """
        global users_db
        for user in users:
            if self._user_repository.get_by_id(user.user_id):
                continue
            self._user_repository.create_user(user=user)
        return self._user_repository.get_user_list()

    def update_user(self, user_id: int, user: User) -> User:
        global users_db
        if self._user_repository.get_by_id(user_id):
            return self._user_repository.update_user(user_id=user_id, user=user)

        raise HTTPException(400, 'User Does not exists.')
