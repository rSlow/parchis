from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ORM.models.game.player import GamePlayer
from ORM.models.game.room import GameRoom
from ORM.models.user import User


async def add_new_room(session: AsyncSession):
    async with session.begin():
        session.add(
            GameRoom()
        )


async def get_rooms_with_players(session: AsyncSession):
    async with session.begin():
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


async def get_orm_room(session: AsyncSession, room_id: int):
    async with session.begin():
        query = select(GameRoom).filter_by(
            id=room_id
        ).options(
            selectinload(GameRoom.players).selectinload(
                GamePlayer.user
            )
        )
        result = await session.execute(query)
        room = result.scalars().one()
    return room


async def add_player_in_room(session: AsyncSession, room_id: str, player: GamePlayer):
    async with session.begin():
        query = select(GameRoom).filter_by(id=room_id)
        result = await session.execute(query)
        room: GameRoom = result.scalars().one()
        room.players.append(player)
