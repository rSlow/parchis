from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from config import BASE_DIR


class Base(DeclarativeBase):
    pass


URL = f"sqlite+aiosqlite:///{BASE_DIR / 'db.sqlite3'}"

Engine = create_async_engine(
    url=URL,
    echo=True,
)
Session = async_sessionmaker(
    bind=Engine,
    expire_on_commit=False,
    autoflush=True
)


async def get_session() -> AsyncSession:
    async with Session() as session:
        yield session


async def create_database() -> None:
    try:
        from ORM.models.user import User
        from ORM.models.game.room import GameRoom
        from ORM.models.game.player import GamePlayer
        from ORM.models.game.piece import GamePiece
        # async with Engine.begin() as conn:
        #     await conn.run_sync(Base.metadata.create_all)

    except ImportError:
        raise


async def stop_database() -> None:
    await Engine.dispose()
