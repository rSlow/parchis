from fastapi import APIRouter, Query, Path
from fastapi import Depends, Body, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from CRUD.user import get_user_by_email, add_user, get_all_users, authenticate_user, get_current_user, \
    get_user_by_username, get_user
from ORM.base import get_session
from schemas.user import PydanticUserCreate, PydanticUser, PydanticUserWithPlayer
from utils.auth import create_token

users_api_router = APIRouter(
    prefix="/users",
    tags=["UserAPI"],
    include_in_schema=True
)


@users_api_router.post("/")
async def create_user(user_schema: PydanticUserCreate = Body(),
                      session: AsyncSession = Depends(get_session)):
    user = await get_user_by_email(
        session=session,
        email=user_schema.email
    )
    if user is None:
        new_user = await add_user(
            session=session,
            user=user_schema
        )
        return create_token(new_user)

    else:
        raise HTTPException(
            status_code=400,
            detail=f"Email <{user_schema.email}> already in use"
        )


@users_api_router.get("/", response_model=list[PydanticUser])
async def get_users(session: AsyncSession = Depends(get_session)):
    users = await get_all_users(session=session)
    return users


@users_api_router.post("/token/")
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends(),
                         session: AsyncSession = Depends(get_session)):
    user = await authenticate_user(
        email=form_data.username,
        password=form_data.password,
        session=session
    )
    if user is not None:
        token = create_token(user=user)
        return token
    else:
        raise HTTPException(
            status_code=401,
            detail="Email or password is not correct."
        )


@users_api_router.get("/me/")
async def get_me(user_schema: PydanticUser = Depends(get_current_user)):
    return user_schema


@users_api_router.get("/check/email/")
async def check_email(email: str = Query(),
                      session: AsyncSession = Depends(get_session)):
    user = await get_user_by_email(
        session=session,
        email=email
    )
    return user is not None


@users_api_router.get("/check/username/")
async def check_username(username: str = Query(),
                         session: AsyncSession = Depends(get_session)):
    user = await get_user_by_username(
        session=session,
        username=username
    )
    return user is not None


@users_api_router.get("/{user_id}/", response_model=PydanticUserWithPlayer)
async def get_user_with_player(user_id: int = Path(),
                               session: AsyncSession = Depends(get_session)):
    user = await get_user(user_id, session)
    return user
