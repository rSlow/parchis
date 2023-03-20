from fastapi import HTTPException
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import mapped_column, Mapped, relationship, validates
from datetime import datetime
from sqlalchemy import func, String
from ORM.base import Base
from ORM.models.player import GamePlayer


class GameRoom(Base):
    __tablename__ = "game_room"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    is_started: Mapped[bool] = mapped_column(default=False)
    create_date: Mapped[datetime] = mapped_column(server_default=func.now())

    players: Mapped[list[GamePlayer]] = relationship(
        cascade="all, delete",
        back_populates="current_room"
    )
    _name = mapped_column("name", String, nullable=True)

    @hybrid_property
    def name(self):
        if self._name is None:
            self._name = f"Комната №{self.id}"
        return self._name

    @name.setter
    def name(self, room_name: str):
        self._name = room_name

    @validates("players")
    def validate_players(self, _, player):
        if len(self.players) == 4:
            raise HTTPException(
                status_code=400,
                detail=f"room #{self.id} yet have 4 players. can't add more."
            )
        return player
