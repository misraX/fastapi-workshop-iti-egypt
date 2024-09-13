from typing import Optional

from pydantic import BaseModel

from models.user import User


class UserBulkUpdateResponseSchema(BaseModel):
    updated_users: Optional[list[User]]
    errors: Optional[list[User]]
