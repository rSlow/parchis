from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey
from ORM.base import Base
from ORM.models.piece import GamePiece


class GamePlayer(Base):
    __tablename__ = "game_player"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[bool] = mapped_column(ForeignKey("users.id"))
    user = relationship("User")

    current_room_id: Mapped[int] = mapped_column(ForeignKey("game_room.id"))
    current_room = relationship(
        "GameRoom",
        back_populates="players"
    )

    pieces: Mapped[list[GamePiece]] = relationship(
        cascade="all, delete",
        back_populates="player"
    )
