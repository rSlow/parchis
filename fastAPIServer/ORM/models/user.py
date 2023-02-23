from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from passlib.hash import bcrypt

from ORM.base import Base, Session


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True)
    hash_password: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(server_default=func.now())

    def is_password_correct(self, password: str):
        return bcrypt.verify(
            secret=password,
            hash=self.hash_password
        )

    @classmethod
    async def add(cls, email: str, hash_password: str):
        async with Session() as session:
            async with session.begin():
                ...
