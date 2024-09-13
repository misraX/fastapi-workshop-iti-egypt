from pydantic import BaseModel, EmailStr
from typing import Optional
from .user_profile import UserProfile


class User(BaseModel):
    """
    User base model.

    User base model includes a subset of the user defined fields,
    and related objects like UserProfile "user_profile" field.
    """
    user_id: int
    user_name: str
    user_profile: Optional[UserProfile]
    user_email: EmailStr
