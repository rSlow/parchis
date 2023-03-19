import os

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

from config import DB_ENV_FILE_PATH


class Base(DeclarativeBase):
    pass


if os.getenv("DATABASE_URL") is None:
    load_dotenv(DB_ENV_FILE_PATH)

URL = os.getenv("DATABASE_URL")

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
        from ORM.models.room import GameRoom
        from ORM.models.piece import GamePiece
        # async with Engine.begin() as conn:
        #     await conn.run_sync(Base.metadata.create_all)

    except ImportError:
        raise


async def stop_database() -> None:
    await Engine.dispose()
