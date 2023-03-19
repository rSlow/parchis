from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from ORM.base import Base


class GamePiece(Base):
    __tablename__ = "game_piece"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user = relationship(
        "User",
        back_populates="pieces"
    )

    x: Mapped[int]
    y: Mapped[int]
