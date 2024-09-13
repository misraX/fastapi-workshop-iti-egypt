"""
Intro to FastAPI
/user
/user/<id>
"""

from typing import Dict

from fastapi import APIRouter, HTTPException

from models.user import User

user_router = APIRouter(tags=["user"], prefix="/user")

users_db: Dict[int, User] = {}


@user_router.get('')
def get_user_list() -> list[User]:
    return list(users_db.values())


@user_router.post('')
def create_user(user: User) -> User:
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
