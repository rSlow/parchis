from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class Player(BaseModel):
    id: int
    current_room_id: int
    user: User

    class Config:
        orm_mode = True


class PydanticListRoom(BaseModel):
    id: int
    is_started: bool
    name: str
    players: list[Player]

    is_joinable = True
    is_current = False

    class Config:
        orm_mode = True
