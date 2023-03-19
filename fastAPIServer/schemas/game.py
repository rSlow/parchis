from __future__ import annotations
from pydantic import BaseModel


class PydanticRoom(BaseModel):
    id: int
    is_started: bool

    class Config:
        orm_mode = True


class PydanticUser(BaseModel):
    id: int
    current_room_id: int
    username: str

    class Config:
        orm_mode = True


class PydanticRoomWithUsers(PydanticRoom):
    users: list[PydanticUser]


class PydanticUserWithPieces(PydanticUser):
    pieces: list[PydanticGamePiece]


class PydanticRoomWithUsersAndPieces(PydanticRoom):
    users: list[PydanticUserWithPieces]


class PydanticGamePiece(BaseModel):
    id: int
    player_id: int

    x: int
    y: int

    class Config:
        orm_mode = True


PydanticRoom.update_forward_refs()
PydanticUser.update_forward_refs()
PydanticRoomWithUsers.update_forward_refs()

PydanticUserWithPieces.update_forward_refs()
PydanticRoomWithUsersAndPieces.update_forward_refs()

PydanticGamePiece.update_forward_refs()
