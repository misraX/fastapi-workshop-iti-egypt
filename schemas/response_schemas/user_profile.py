from pydantic import BaseModel


class UserProfileResponseSchema(BaseModel):
    user_phone_number: str
