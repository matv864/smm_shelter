from fastapi import APIRouter

from src.joke_service.api import joke_router
from src.auth_service.api import auth_router

v1_router = APIRouter(
    prefix="/api/v1",
)

v1_router.include_router(joke_router)
v1_router.include_router(auth_router)


@v1_router.get("/healthcheck")
async def healthcheck():
    return "success"
