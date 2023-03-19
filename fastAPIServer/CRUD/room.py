from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ORM.models.user import User
from ORM.models.room import GameRoom


class ORMRoomAPI:
    @staticmethod
    async def add_new(session: AsyncSession, user: User):
        room = GameRoom(users=[user])
        session.add(room)
        await session.commit()

        await session.refresh(room)
        return room

    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence[GameRoom]:
        query = select(GameRoom).options(
            selectinload(
                GameRoom.users
            )
        )
        result = await session.execute(query)
        rooms = result.scalars().all()
        return rooms

    @staticmethod
    async def get(session: AsyncSession, room_id: int) -> GameRoom:
        query = select(GameRoom).filter_by(
            id=room_id
        ).options(
            selectinload(GameRoom.users)
        )
        result = await session.execute(query)
        room = result.scalars().one()
        return room

    @classmethod
    async def add_user(cls, session: AsyncSession, room_id: int, user: User):
        room = await cls.get(session=session, room_id=room_id)
        room.users.append(user)
        await session.commit()
