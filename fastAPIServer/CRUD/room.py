from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ORM.models.player import GamePlayer
from ORM.models.room import GameRoom
from schemas.protocols.room import PydanticRoom
from schemas.protocols.rooms_list import PydanticListRoom


class ORMRoomAPI:
    @staticmethod
    async def add_new(user_id: int, session: AsyncSession):
        async with session.begin():
            room = GameRoom(players=[
                GamePlayer(user_id=user_id)
            ])
            session.add(room)

        await session.refresh(room)
        return room

    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence[GameRoom]:
        query = select(GameRoom).options(
            selectinload(
                GameRoom.players
            ).selectinload(
                GamePlayer.user
            )
        )
        result = await session.execute(query)
        rooms = result.scalars().all()
        return rooms

    @classmethod
    async def get_all_pydantic(cls, session: AsyncSession):
        orm_rooms = await cls.get_all(session)
        rooms = [PydanticListRoom.from_orm(orm_room) for orm_room in orm_rooms]
        return rooms

    @staticmethod
    async def get(session: AsyncSession, room_id: int) -> GameRoom:
        query = select(GameRoom).filter_by(
            id=room_id
        ).options(
            selectinload(
                GameRoom.players
            ).selectinload(
                GamePlayer.user
            )
        )
        result = await session.execute(query)
        room = result.scalars().one()
        return room

    @classmethod
    async def get_pydantic(cls, session: AsyncSession, room_id: int):
        orm_room = await cls.get(session=session, room_id=room_id)
        return PydanticRoom.from_orm(orm_room)

    @classmethod
    async def add_player(cls, session: AsyncSession, room_id: int, user_id: int):
        room = await cls.get(session=session, room_id=room_id)
        room.players.append(GamePlayer(user_id=user_id))
        await session.commit()

    @staticmethod
    async def delete_player(player: GamePlayer, session: AsyncSession):
        await session.delete(player)
        await session.commit()

    @classmethod
    async def check_empty(cls, room_id: int, session: AsyncSession):
        room = await cls.get(session=session, room_id=room_id)
        if len(room.players) == 0:
            await session.delete(room)
            await session.commit()

    @classmethod
    async def change_name(cls, room_id: int, name: str, session: AsyncSession):
        room = await cls.get(session=session, room_id=room_id)
        room.name = name
        await session.commit()
