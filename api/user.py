"""
Intro to FastAPI
/user
/user/<id>
"""
from fastapi import APIRouter

from models.user import User

user_router = APIRouter(tags=["user"], prefix="/user")

global users

users: list[User] = []


@user_router.get('')
def get_user_list() -> list[User]:
    return users


@user_router.post('')
def create_user(user: User) -> User:
    user = user.dict()
    user_model = User(**user)
    users.append(user_model)
    return user_model
