from pydantic import BaseModel

from schemas.protocols.rooms_list import Player


class Piece(BaseModel):
    x: int
    y: int

    class Config:
        orm_mode = True


class PlayerWithPieces(Player):
    pieces: list[Piece] = []

    class Config:
        orm_mode = True


class PydanticRoom(BaseModel):
    id: int
    is_started: bool
    name: str
    players: list[Player]

    class Config:
        orm_mode = True
