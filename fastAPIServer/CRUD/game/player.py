from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.game.room import get_orm_room
from ORM.models.game.player import GamePlayer


async def create_player(session: AsyncSession, user_id: int, room_id: int):
    room = await get_orm_room(session=session, room_id=room_id)
    async with session.begin():
        room.players.append(GamePlayer(user_id=user_id))

    await session.refresh(room)
    return room
