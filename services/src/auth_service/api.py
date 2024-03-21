from fastapi import APIRouter, status

from src.auth_service.service.auth import Auth_service
from src.auth_service.schemas import (
    User_form,
    Its_me,
    Access_token,
    Refresh_token,
    Pair_tokens
)

auth_router = APIRouter(
    prefix="/auth",
)


@auth_router.post("/registration", status_code=status.HTTP_201_CREATED)
async def registration_user(payload: User_form):
    return await Auth_service().create_user(payload)


@auth_router.post("/login", response_model=Pair_tokens)
async def login_user(payload: User_form):
    return await Auth_service().login_user(payload)


@auth_router.post("/refresh", response_model=Access_token)
async def refresh(payload: Refresh_token):
    return await Auth_service().update_token(payload)


@auth_router.post("/me", response_model=Its_me)
async def who_am_i(payload: Access_token):
    return await Auth_service().who_am_i(payload)
