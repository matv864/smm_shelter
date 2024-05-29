from fastapi import APIRouter, status

from .service import Pets_service


pets_router = APIRouter(
    prefix="/pets",
    tags=["pets"]
)


@pets_router.post("/list/", status_code=status.HTTP_200_OK)
async def get_all_pets():
    return await Pets_service().get_all_pets()
