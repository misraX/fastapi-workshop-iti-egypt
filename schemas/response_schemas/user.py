from typing import Optional

from pydantic import BaseModel, EmailStr

from models.user import User
from schemas.response_schemas.user_profile import UserProfileResponseSchema


class UserResponseSchema(BaseModel):
    user_id: int
    user_name: str
    user_profile: Optional[UserProfileResponseSchema]
    user_email: EmailStr

class UserBulkUpdateResponseSchema(BaseModel):
    updated_users: Optional[list[User]]
    errors: Optional[list[User]]
