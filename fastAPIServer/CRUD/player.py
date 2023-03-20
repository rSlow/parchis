from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ORM.models.player import GamePlayer


class ORMPlayerAPI:
    @staticmethod
    async def get_by_user_id(session: AsyncSession, user_id: int) -> GamePlayer | None:
        query = select(GamePlayer).filter_by(user_id=user_id)
        result = await session.execute(query)
        return result.scalars().one_or_none()
