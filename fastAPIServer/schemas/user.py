from pydantic import BaseModel, Field


class PydanticUserBase(BaseModel):
    email: str
    username: str


class PydanticUserCreate(PydanticUserBase):
    password: str

    class Config:
        orm_mode = True


class PydanticUser(PydanticUserBase):
    id: int

    class Config:
        orm_mode = True


class PydanticUserWithPlayer(BaseModel):
    class Player(BaseModel):
        id: int
        room_id: int

        class Config:
            orm_mode = True

    player: Player

    class Config:
        orm_mode = True
