"""
Intro to FastAPI
/user
/user/<id>
"""

from typing import Dict, Optional

from fastapi import APIRouter, HTTPException

from models.user import User, UserBulkUpdate

user_router = APIRouter(tags=["user"], prefix="/user")

users_db: Dict[int, User] = {}


@user_router.get('')
def get_user_list() -> list[User]:
    """
    List all users from the global DB `users_db`

    :return: list[User]
    """
    return list(users_db.values())


@user_router.post('')
def create_user(user: User) -> User:
    """
    Create a new user

    :param user: User
    :return: User
    """
    global users_db
    user = user.dict()
    user_model = User(**user)
    if users_db.get(user_model.user_id):
        raise HTTPException(400, 'User already exists.')
    users_db[user_model.user_id] = user_model
    return user_model


@user_router.post('/bulk-creation')
def bulk_create_user(users: list[User]) -> list[User]:
    """
    Bulk creation of users.

    Takes list of one or many users and creates them into the users_db.

    users_db = []

    - Their items already in the list.
    - The list is empty, and we're appending new items.

    :param users: list[User]
    :return: list[User]
    """
    global users_db
    for user in users:
        if users_db.get(user.user_id):
            continue
        users_db[user.user_id] = user

    return list(users_db.values())


@user_router.put('/{user_id}')
def update_user(user: User, user_id: int) -> User:
    """
    Update a give user.

    The update process should check if the user does exist on the DB
    if the user exist, update their given values.
    If the user does not exist, throw an error.


    :param user: User
    :param user_id: int
    :raise HTTPException: If the user doesn't exist
    :return: User
    """
    global users_db
    if users_db.get(user_id):
        users_db[user.user_id] = user
        return user
    raise HTTPException(400, 'User Does not exists.')


@user_router.put('/bulk-update/')
def bulk_update_user(users: list[User]) -> UserBulkUpdate:
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

    user_response = UserBulkUpdate(updated_users=updated_users, errors=errors)

    return user_response
