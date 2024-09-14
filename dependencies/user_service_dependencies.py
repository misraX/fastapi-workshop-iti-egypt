from fastapi import Depends, Request

from services.user import UserService


def service_state_setter(
        request: Request,
        user_service: UserService = Depends(UserService)
):
    request.state.user_service = user_service
