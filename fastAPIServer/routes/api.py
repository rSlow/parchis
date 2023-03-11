from fastapi import APIRouter

from routes.game_api.rooms import rooms_api_router
from routes.user import users_api_router

api_router = APIRouter(
    prefix="/api",
)

api_router.include_router(users_api_router)
api_router.include_router(rooms_api_router)


@api_router.get("/")
async def test():
    return {"message": "ok"}
