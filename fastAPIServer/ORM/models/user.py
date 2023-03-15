import re
from datetime import datetime

from fastapi import HTTPException
from passlib.hash import bcrypt
from sqlalchemy import func
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column, validates

from ORM.base import Base
from ORM.models.game.player import GamePlayer
from utils.re_patterns import EMAIL_PATTERN


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    hash_password: Mapped[str]
    create_date: Mapped[datetime] = mapped_column(server_default=func.now())

    player: Mapped[GamePlayer] = relationship(back_populates="user", uselist=False)

    @validates("email")
    def validate_email(self, _, address):
        if re.match(
                pattern=EMAIL_PATTERN,
                string=address
        ) is None:
            raise HTTPException(
                status_code=400,
                detail=f"Email <{address}> is incorrect"
            )

        return address

    def is_password_correct(self, password: str):
        return bcrypt.verify(
            secret=password,
            hash=self.hash_password
        )
