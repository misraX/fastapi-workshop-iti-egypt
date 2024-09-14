from collections.abc import Iterable
from typing import Optional

from fastapi import HTTPException, Depends

from exceptions.user import UserNotFoundException
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
        :return:
        """
        try:
            user = self._user_repository.get_by_id(user_id)
            # publisher.publish(requested_usr=request.user, requested_user_id= user_id)
            return user
        except UserNotFoundException as exception:
            raise HTTPException(404, detail=f"{exception}")

    def get_user_list(self, user_name: str) -> Optional[Iterable[User]]:
        """
        List users, with filters if any

        Allowed filters are:
         - user_name

        :param user_name: str
        :return: Optional[Iterable[User]]
        """
        return self._user_repository.get_user_list(user_name=user_name)

    def create_user(self, user: User) -> User:
        global users_db
        try:
            user = self._user_repository.get_by_id(user.user_id)
        except UserNotFoundException:
            user_created = self._user_repository.create_user(user=user)
            return user_created
        if user:
            raise HTTPException(400, 'User already exists.')
