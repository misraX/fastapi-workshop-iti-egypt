from fastapi import FastAPI

from api.user import user_router_v1, user_router_v2

app = FastAPI()
app.include_router(user_router_v1)
app.include_router(user_router_v2)
