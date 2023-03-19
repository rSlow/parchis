from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from sqlalchemy import func
from ORM.base import Base
from ORM.models.user import User


class GameRoom(Base):
    __tablename__ = "game_room"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    is_started: Mapped[bool] = mapped_column(default=False)
    create_date: Mapped[datetime] = mapped_column(server_default=func.now())

    users: Mapped[list[User]] = relationship(
        cascade="all, delete",
        back_populates="current_room"
    )
