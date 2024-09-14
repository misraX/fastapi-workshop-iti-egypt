"""
Intro to FastAPI
/user
/user/<id>
"""
from collections.abc import KeysView
from typing import Optional, Iterable

from fastapi import APIRouter, Depends

from core.database import users_db  # noqa
from models.user import User
from schemas.response_schemas.user import UserBulkUpdateResponseSchema
from services.user import UserService

user_router_v1 = APIRouter(tags=["v1"], prefix="/v1/user")
user_router_v2 = APIRouter(tags=["v2"], prefix="/v2/user")



@user_router_v1.get('')
def get_user_list(user_name: Optional[str] = None, user_service: UserService = Depends(UserService)) -> Iterable[User]:
    """
    List all users from the global DB `users_db`

    :return: list[User]
    """
    return user_service.get_user_list(user_name=user_name)


@user_router_v1.get('/{user_id}')
def get_user_by_id(user_id: int, user_service: UserService = Depends(UserService)) -> User:
    """
    Just select an ID from the global users_db

    >>> db = { "111": {"user_name"} }
    >>> user_by_id = db['111']

    :param user_id: int
    :param user_service: UserService
    :return: User
    """

    return user_service.get_user_by_id(user_id)

@user_router_v1.post('')
def create_user(user: User, user_service: UserService = Depends(UserService)) -> User:
    return user_service.create_user(user)


@user_router_v1.post('/bulk-creation')
def bulk_create_user(
        users: list[User],
        user_service: UserService = Depends(UserService)
) -> Iterable[User]:
    """
    Bulk creation of users.

    Takes list of one or many users and creates them into the users_db.

    users_db = []

    - Their items already in the list.
    - The list is empty, and we're appending new items.

    :param users: list[User]
    :param user_service: UserService
    :return: list[User]
    """
    return user_service.bulk_create_user(users)


@user_router_v1.put('/{user_id}')
def update_user(
        user: User,
        user_id: int,
        user_service: UserService = Depends(UserService)
) -> User:
    """
    Update a give user.

    The update process should check if the user does exist on the DB
    if the user exist, update their given values.
    If the user does not exist, throw an error.


    :param user: User
    :param user_id: int
    :param user_service: UserService
    :raise HTTPException: If the user doesn't exist
    :return: User
    """
    return user_service.update_user(user_id, user)


@user_router_v1.put('/bulk-update/')
def bulk_update_user(users: list[User]) -> UserBulkUpdateResponseSchema:
    """
    Bulk updates for existing users.

    The bulk update is so simple:
    - Loop over the list of user
      - if the user exists, update their given values.
      - if the user does not exist, continue

    - The final validation of the API, is the return type
     meaning that if the user exist, the return list will include the user values.

    :param users: list[User] list of Users
    :return: list[User] list of Updated users.
    """
    global users_db

    updated_users: Optional[list[User]] = []
    errors: Optional[list[User]] = []
    for user in users:
        if users_db.get(user.user_id):
            users_db[user.user_id] = user
            updated_users.append(user)
        else:
            errors.append(user)

    user_response = UserBulkUpdateResponseSchema(updated_users=updated_users, errors=errors)

    return user_response


@user_router_v2.put('/bulk-update/')
def bulk_update_user(users: dict[int, User]) -> UserBulkUpdateResponseSchema:
    """
    Bulk updates for existing users.

    Major improvements:
    - Avoid user_id Duplications
      - Duplication caused override on the objects, based on the last id:user
    - Avoid looping over users that do not exist in our DB


    :param users: Dict[UserBulkUpdateRequestSchema] Dict of users
    :return: list[User] list of Updated users.
    """
    errors: Optional[list[User]] = []
    updated_users: Optional[list[User]] = []
    users_ids: KeysView = users.keys()
    for user_id in users_ids:
        if users_db.get(user_id):
            updated_users.append(users[user_id])
        else:
            errors.append(users[user_id])
    return UserBulkUpdateResponseSchema(errors=errors, updated_users=updated_users)
