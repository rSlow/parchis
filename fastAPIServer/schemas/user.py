from pydantic import BaseModel


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


class PydanticUserWithPlayer(PydanticUserBase):
    class Player(BaseModel):
        id: int
        current_room_id: int

        class Config:
            orm_mode = True

    player: Player

    class Config:
        orm_mode = True
