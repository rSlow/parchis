from fastapi.websockets import WebSocket
from sqlalchemy.ext.asyncio import AsyncSession

from ORM.CRUD.game.room import add_new_room, get_rooms_with_players
from ORM.schemas.game import PydanticGameRoomWithPlayers, PydanticGameRoomWithPlayersAndPieces
from game.configurator import Configurator


class GameServer:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self._configurator = Configurator()

        self.rooms_info: dict[int, PydanticGameRoomWithPlayersAndPieces] = {}  # {id: room}

        self.main_sockets: list[WebSocket] = []

    async def register_socket(self, websocket: WebSocket):
        await websocket.accept()
        self.main_sockets.append(websocket)

    async def disconnect_socket(self, websocket: WebSocket):
        try:
            self.main_sockets.remove(websocket)
        except ValueError as ex:
            print(ex)

    async def add_new_room(self, session: AsyncSession):
        await add_new_room(session)

        rooms = await get_rooms_with_players(session)
        rooms_array = [dict(PydanticGameRoomWithPlayers.from_orm(room)) for room in rooms]
        for websocket in self.main_sockets:
            await websocket.send_json(rooms_array)
