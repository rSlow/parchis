from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.game.player import create_player
from CRUD.game.room import get_rooms_with_players, get_orm_room

from ORM.base import get_session
from schemas.game import PydanticGameRoomWithPlayers
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


@rooms_api_router.put("/{room_id}/")
async def add_player_in_room(room_id: int = Path(),
                             user_id: int = Body(),
                             session: AsyncSession = Depends(get_session)):
    room = await create_player(
        session=session,
        user_id=user_id,
        room_id=room_id
    )

    return room


@rooms_api_router.get("/{room_id}/", response_model=PydanticGameRoomWithPlayers)
async def get_room(room_id: int = Path(),
                   session: AsyncSession = Depends(get_session)):
    rooms = await get_orm_room(
        session=session,
        room_id=room_id
    )
    return rooms
