from fastapi import APIRouter, status

from .service import Pets_type_service

pets_type_router = APIRouter(
    prefix="/type_pets",
    tags=["type_pets"]
)


@pets_type_router.get("/list/", status_code=status.HTTP_200_OK)
async def get_all_pet_types():
    return await Pets_type_service().get_all_pets_type()
