from fastapi import APIRouter, Depends, Body, Path, Query, Form
from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.room import ORMRoomAPI

from ORM.base import get_session
from game.game_server import GameServer
from schemas.protocols.room import PydanticRoom
from schemas.protocols.rooms_list import PydanticListRoom

rooms_api_router = APIRouter(
    prefix="/rooms",
    tags=["RoomsAPI"]
)

server = GameServer()


@rooms_api_router.get("/", response_model=list[PydanticListRoom])
async def get_rooms(session: AsyncSession = Depends(get_session)):
    rooms = await ORMRoomAPI.get_all(session=session)
    return rooms


@rooms_api_router.post("/")
async def add_room(user_id: int = Body(embed=True),
                   session: AsyncSession = Depends(get_session)):
    room = await server.add_new_room(
        session=session,
        user_id=user_id
    )
    return room


@rooms_api_router.delete("/")
async def delete_player_from_room(room_id: int = Query(),
                                  user_id: int = Query(),
                                  session: AsyncSession = Depends(get_session)):
    await server.delete_player_from_room(room_id=room_id, user_id=user_id, session=session)


@rooms_api_router.put("/{room_id}/")
async def add_player_in_room(room_id: int = Path(),
                             user_id: int = Body(embed=True),
                             session: AsyncSession = Depends(get_session)):
    await server.add_player_in_room(
        session=session,
        user_id=user_id,
        room_id=room_id
    )


@rooms_api_router.get("/{room_id}/", response_model=PydanticRoom)
async def get_room(room_id: int = Path(),
                   session: AsyncSession = Depends(get_session)):
    room = await ORMRoomAPI.get(
        session=session,
        room_id=room_id
    )
    return room


@rooms_api_router.patch("/{room_id}/")
async def change_room_name(room_id: int = Path(),
                           name: str = Body(embed=True),
                           session: AsyncSession = Depends(get_session)):
    await server.change_room_name(room_id=room_id, name=name, session=session)
