from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ORM.models.game.player import GamePlayer
from ORM.models.game.room import GameRoom


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
                GamePlayer.pieces
            )
        )
        result = await session.execute(query)
        rooms = result.scalars().all()
    return rooms
