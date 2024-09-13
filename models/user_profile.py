import phonenumbers
from pydantic import BaseModel, field_validator


class UserProfile(BaseModel):
    """
    User profile model.
    """
    user_phone_number: str

    @field_validator('user_phone_number')
    def validate_user_phone_number(cls, v):
        try:
            phonenumbers.parse(v)
            return v
        except Exception as exc:
            raise exc
