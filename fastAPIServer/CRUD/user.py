from typing import Sequence

from fastapi import Depends, HTTPException
from sqlalchemy import select, Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession

from ORM.base import get_session
from ORM.models.user import User
from schemas.user import PydanticUserCreate, PydanticUser
from utils.auth import hash_password, auth_schema, decode_token


class ORMUserAPI:
    @staticmethod
    async def get_by_id(user_id: int, session: AsyncSession):
        query = select(User).filter_by(id=user_id)
        result = await session.execute(query)
        user = result.scalars().one()
        return user

    @staticmethod
    async def add(
            session: AsyncSession,
            user: PydanticUserCreate):
        user = User(
            email=user.email,
            username=user.username,
            hash_password=hash_password(user.password)
        )
        session.add(user)
        await session.commit()

        await session.refresh(user)
        return user

    @staticmethod
    async def get_by_email(session: AsyncSession,
                           email: str):
        async with session.begin():
            query = select(User).filter_by(email=email)
            result = await session.execute(query)
            user: User | None = result.scalars().one_or_none()
        return user

    @staticmethod
    async def get_by_username(session: AsyncSession,
                              username: str):
        query = select(User).filter_by(username=username)
        result = await session.execute(query)
        user: User | None = result.scalars().one_or_none()
        return user

    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence[Row | RowMapping]:
        query = select(User)
        result = await session.execute(query)
        users = result.scalars().all()
        return users

    @classmethod
    async def authenticate(cls,
                           email: str,
                           password: str,
                           session: AsyncSession):
        user = await cls.get_by_email(
            session=session,
            email=email
        )
        if user is not None and user.is_password_correct(password=password):
            return user
        else:
            return None

    @classmethod
    async def get_current(cls,
                          session: AsyncSession = Depends(get_session),
                          token: str = Depends(auth_schema)):
        payload = decode_token(token=token)

        if payload is not None:
            user = await cls.get_by_id(
                user_id=payload["id"],
                session=session
            )
            return PydanticUser.from_orm(user)

        else:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

    @staticmethod
    async def get(user_id: int, session: AsyncSession):
        query = select(User).filter_by(id=user_id)
        response = await session.execute(query)
        return response.scalars().one_or_none()
