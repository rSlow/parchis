from pydantic import BaseModel, Field


class PydanticUserBase(BaseModel):
    email: str


class PydanticUserCreate(PydanticUserBase):
    password: str

    class Config:
        orm_mode = True


class PydanticUser(PydanticUserBase):
    id: int

    class Config:
        orm_mode = True
