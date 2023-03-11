from __future__ import annotations
from pydantic import BaseModel


class PydanticGameRoom(BaseModel):
    id: int
    is_started: bool

    class Config:
        orm_mode = True


class PydanticGameRoomWithPlayers(PydanticGameRoom):
    players: list[PydanticGamePlayer]

    class Config:
        orm_mode = True


class PydanticGameRoomWithPlayersAndPieces(PydanticGameRoom):
    players: list[PydanticGamePlayerWithPieces]


class PydanticGamePlayer(BaseModel):
    id: int
    user_id: int
    room_id: int

    class Config:
        orm_mode = True


class PydanticGamePlayerWithPieces(PydanticGamePlayer):
    pieces: list[PydanticGamePiece]


class PydanticGamePiece(BaseModel):
    id: int
    player_id: int

    x: int
    y: int

    class Config:
        orm_mode = True


PydanticGameRoom.update_forward_refs()
PydanticGameRoomWithPlayers.update_forward_refs()
PydanticGameRoomWithPlayersAndPieces.update_forward_refs()

PydanticGamePlayer.update_forward_refs()
PydanticGamePlayerWithPieces.update_forward_refs()

PydanticGamePiece.update_forward_refs()
