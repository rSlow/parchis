import asyncio

from fastapi.websockets import WebSocket
from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.user import ORMUserAPI
from CRUD.room import ORMRoomAPI
from schemas.game import PydanticRoomWithUsers, PydanticRoomWithUsersAndPieces
from game.configurator import Configurator


class GameServer:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self._configurator = Configurator()

        self.rooms_info: dict[int, PydanticRoomWithUsersAndPieces] = {}  # {id: room}

        self.main_sockets: list[WebSocket] = []
        self.room_waiting_sockets: dict[int, list[WebSocket]] = {}
        self.room_playing_sockets: dict[int, list[WebSocket]] = {}

    async def register_socket(self, websocket: WebSocket):
        await websocket.accept()
        self.main_sockets.append(websocket)

    async def disconnect_socket(self, websocket: WebSocket):
        try:
            self.main_sockets.remove(websocket)
        except ValueError as ex:
            print(ex)

    async def send_room_to_all_connected(self, session: AsyncSession):
        rooms = await ORMRoomAPI.get_all(session)
        rooms_array = [PydanticRoomWithUsers.from_orm(room).dict() for room in rooms]

        tasks = [websocket.send_json(rooms_array) for websocket in self.main_sockets]
        await asyncio.gather(*tasks)

    async def add_new_room(self, session: AsyncSession, user_id: int):
        user = await ORMUserAPI.get(user_id, session)
        room = await ORMRoomAPI.add_new(session, user)
        await self.send_room_to_all_connected(session=session)
        return room

    async def add_player_in_room(self,
                                 session: AsyncSession,
                                 room_id: int,
                                 user_id: int):
        user = await ORMUserAPI.get(user_id, session)
        await ORMRoomAPI.add_user(session=session, room_id=room_id, user=user)
        await self.send_room_to_all_connected(session=session)
