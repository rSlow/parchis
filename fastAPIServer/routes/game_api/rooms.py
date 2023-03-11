from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ORM.CRUD.game.room import get_rooms_with_players

from ORM.base import get_session
from ORM.schemas.game import PydanticGameRoomWithPlayers
from game.game_server import GameServer

rooms_api_router = APIRouter(
    prefix="/rooms",
    tags=["RoomsAPI"]
)

server = GameServer()


@rooms_api_router.get("/", response_model=list[PydanticGameRoomWithPlayers])
async def get_rooms(session: AsyncSession = Depends(get_session)):
    rooms = await get_rooms_with_players(session)
    return rooms


@rooms_api_router.post("/")
async def add_room(session: AsyncSession = Depends(get_session)):
    await server.add_new_room(session)
