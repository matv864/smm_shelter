import uuid

from fastapi import APIRouter, status

from .service import Images_service

images_router = APIRouter(
    prefix="/images",
    tags=["images"]
)


@images_router.get("/{pet_id}/list/", status_code=status.HTTP_200_OK)
async def get_all_images_of_pet(pet_id: uuid.UUID):
    return await Images_service().get_all_images_of_pet(pet_id)
