import os

from fastapi.security import OAuth2PasswordBearer
from jwt import decode as jwt_decode
from jwt import encode as jwt_encode
from jwt import DecodeError as JWTDecodeError
from passlib.hash import bcrypt

from schemas.user import PydanticUser

JWT_SECRET = os.getenv("JWT_SECRET")

auth_schema = OAuth2PasswordBearer(tokenUrl="/api/users/token")


def hash_password(password: str):
    return bcrypt.hash(secret=password)


def create_token(user):
    pydantic_user = PydanticUser.from_orm(user)
    token = jwt_encode(
        payload=pydantic_user.dict(),
        key=JWT_SECRET
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def decode_token(token: str):
    try:
        payload = jwt_decode(
            jwt=token,
            key=JWT_SECRET,
            algorithms=["HS256"]
        )
        return payload
    except JWTDecodeError:
        return
