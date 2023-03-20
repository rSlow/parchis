import asyncio

from fastapi.websockets import WebSocket
from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.room import ORMRoomAPI


class MainSocketManager(list[WebSocket]):
    def __init__(self, server):
        super().__init__()
        # self._server = server

    async def register(self, websocket: WebSocket):
        await websocket.accept()
        self.append(websocket)

    async def disconnect(self, websocket: WebSocket):
        try:
            self.remove(websocket)
        except ValueError as ex:
            print(ex)

    async def dispatch(self, session: AsyncSession):
        rooms = await ORMRoomAPI.get_all_pydantic(session)
        rooms_array = [room.dict() for room in rooms]
        tasks = [websocket.send_json(rooms_array) for websocket in self]
        await asyncio.gather(*tasks)


class RoomSocketManager(dict[int, list[WebSocket]]):
    def __init__(self, server):
        super().__init__()
        # self._server = server

    async def register(self, websocket: WebSocket, room_id: int):
        await websocket.accept()
        self[room_id].append(websocket)

    async def disconnect(self, websocket: WebSocket, room_id: int):
        try:
            self[room_id].remove(websocket)
        except ValueError as ex:
            print(ex)
