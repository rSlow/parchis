from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import BASE_DIR


class Base(DeclarativeBase):
    pass


Engine = create_async_engine(
    url=f"sqlite+aiosqlite:///{BASE_DIR / 'db.sqlite3'}",
    echo=True,
)
Session = async_sessionmaker(
    bind=Engine,
    expire_on_commit=False,
    autoflush=True
)


async def get_session():
    async with Session() as session:
        yield session


async def create_database() -> None:
    try:
        from ORM.models.user import User
        async with Engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    except ImportError:
        raise


async def stop_database() -> None:
    await Engine.dispose()
