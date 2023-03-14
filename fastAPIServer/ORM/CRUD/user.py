from typing import Sequence

from fastapi import Depends, HTTPException
from sqlalchemy import select, Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession

from ORM.base import get_session
from ORM.models.user import User as ORM_User
from ORM.schemas.user import PydanticUserCreate, PydanticUser
from utils.auth import hash_password, auth_schema, decode_token


async def get_user_by_id(user_id: int, session: AsyncSession):
    query = select(ORM_User).filter_by(id=user_id)
    result = await session.execute(query)
    user = result.scalars().one()
    return user


async def add_user(
        session: AsyncSession,
        user: PydanticUserCreate):
    user = ORM_User(
        email=user.email,
        username=user.username,
        hash_password=hash_password(user.password)
    )
    session.add(user)
    await session.commit()

    await session.refresh(user)
    return user


async def get_user_by_email(session: AsyncSession,
                            email: str):
    query = select(ORM_User).filter_by(email=email)
    result = await session.execute(query)
    user: ORM_User | None = result.scalars().one_or_none()
    return user


async def get_user_by_username(session: AsyncSession,
                               username: str):
    query = select(ORM_User).filter_by(username=username)
    result = await session.execute(query)
    user: ORM_User | None = result.scalars().one_or_none()
    return user


async def get_all_users(session: AsyncSession) -> Sequence[Row | RowMapping]:
    query = select(ORM_User)
    result = await session.execute(query)
    users = result.scalars().all()
    return users


async def authenticate_user(email: str,
                            password: str,
                            session: AsyncSession):
    user = await get_user_by_email(
        session=session,
        email=email
    )
    if user is not None and user.is_password_correct(password=password):
        return user
    else:
        return None


async def get_current_user(session: AsyncSession = Depends(get_session),
                           token: str = Depends(auth_schema)):
    payload = decode_token(token=token)

    if payload is not None:
        user = await get_user_by_id(
            user_id=payload["id"],
            session=session
        )
        return PydanticUser.from_orm(user)

    else:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
