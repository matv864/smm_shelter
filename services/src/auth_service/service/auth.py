from src.auth_service.database.session import async_session_maker
from sqlalchemy import select, insert
# from sqlalchemy.orm import selectinload
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.security_module.jwt import (
    create_pair_tokens,
    create_access_jwt_token,
    verify_jwt_token
)
from src.security_module.passwords import (
    get_hashing_password,
    match_password_with_hash
)


from src.auth_service.database.models import Auth
from src.auth_service.schemas import (
    User_form,
    Auth_record,
    Access_token,
    Refresh_token,
    Pair_tokens
)


class Auth_service:

    async def create_user(self, payload: User_form):
        session = async_session_maker()
        query = (
            select(Auth)
            .where(payload.mail == Auth.mail)
        )
        users = await session.execute(query)
        if users.scalar_one_or_none():
            raise HTTPException(status_code=403, detail="user exists")

        record = Auth_record(
            mail=payload.mail,
            hashed_password=await get_hashing_password(payload.password)
        )

        query = (
            insert(Auth)
        )
        try:
            await session.execute(query, [record])
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def login_user(self, payload: OAuth2PasswordRequestForm):
        session = async_session_maker()
        query = (
            select(Auth)
            .where(Auth.username == payload.username)
        )
        user_data = await session.execute(query)
        user_data = user_data.scalar_one_or_none()

        await session.close()
        if user_data is None or \
            not await match_password_with_hash(
                payload.password,
                user_data.password):

            raise HTTPException(
                status_code=403,
                detail="Wrong login or password"
            )
        pair_tokens: Pair_tokens = await create_pair_tokens(user_data.username)
        return Pair_tokens(**pair_tokens)

    async def update_token(self, payload: Refresh_token):
        data_from_refresh = await verify_jwt_token(payload.refresh_token)
        if data_from_refresh is None:
            raise HTTPException(status_code=403, detail="bad token")
        access_token = Access_token(access_token=await create_access_jwt_token(
                data_from_refresh
            )
        )
        return access_token

    async def who_is_it(self, token: str) -> str | None:
        return await verify_jwt_token(token)
