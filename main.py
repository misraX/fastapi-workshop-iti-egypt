from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.user import user_router_v1, user_router_v2
from views.user import user_templates_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="statics"), name="static")

app.include_router(user_router_v1)
app.include_router(user_router_v2)
app.include_router(user_templates_router)
