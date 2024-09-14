from typing import Optional

from fastapi import Request, APIRouter, Depends
from fastapi.templating import Jinja2Templates

from dependencies.user_service_dependencies import service_state_setter

user_templates_router = APIRouter(tags=["user_templates"], dependencies=[
    Depends(service_state_setter)
])
templates = Jinja2Templates(directory="templates")


@user_templates_router.get('/user')
def get_user_list_view(request: Request, user_name: Optional[str] = None) -> templates.TemplateResponse:
    """
    List all users from the global DB `users_db`

    :return: list[User]
    """
    users = request.state.user_service.get_user_list(user_name=user_name)
    return templates.TemplateResponse(name='user/user_list.html', context={'request': request, 'users': users})


@user_templates_router.get('/user/{user_id}')
def get_user_by_id_view(request: Request, user_id: int) -> templates.TemplateResponse:
    user = request.state.user_service.get_user_by_id(user_id=user_id)
    return templates.TemplateResponse(name='user/user_details.html', context={'request': request, 'user': user})
