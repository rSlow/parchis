from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.player import ORMPlayerAPI
from CRUD.user import ORMUserAPI
from CRUD.room import ORMRoomAPI
from game.configurator import Configurator
from game.socket_managers import MainSocketManager, RoomSocketManager


class GameServer:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self._configurator = Configurator()
        self.main_sockets = MainSocketManager(self)
        self.room_sockets = RoomSocketManager(self)

    async def add_new_room(self, session: AsyncSession, user_id: int):
        room = await ORMRoomAPI.add_new(user_id, session)
        await self.main_sockets.dispatch(session=session)
        return room

    async def add_player_in_room(self,
                                 session: AsyncSession,
                                 room_id: int,
                                 user_id: int):
        user = await ORMUserAPI.get_by_id(user_id, session)
        await ORMRoomAPI.add_player(session=session, room_id=room_id, user_id=user.id)
        await self.main_sockets.dispatch(session=session)

    async def delete_player_from_room(self, user_id: int, room_id: int, session: AsyncSession):
        player = await ORMPlayerAPI.get_by_user_id(user_id=user_id, session=session)
        if player is not None:
            await ORMRoomAPI.delete_player(
                player=player,
                session=session
            )
            await ORMRoomAPI.check_empty(room_id=room_id, session=session)
        await self.main_sockets.dispatch(session=session)

    async def change_room_name(self, room_id: int, name: str, session: AsyncSession):
        await ORMRoomAPI.change_name(room_id=room_id, name=name, session=session)
        await self.main_sockets.dispatch(session=session)
