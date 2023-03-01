from pydantic import BaseModel


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
