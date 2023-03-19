from pydantic import BaseModel


class PydanticPlayer(BaseModel):
    id: int
    current_room_id: int

    class Config:
        orm_mode = True
