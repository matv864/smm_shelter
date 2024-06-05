import uuid

from fastapi import APIRouter, status, Body, UploadFile, File

# from src.security_module import Secret_schema, verify_user

from .service import Images_service


images_router = APIRouter(
    prefix="/images",
    tags=["images"]
)


@images_router.post("/{pets_id}/", status_code=status.HTTP_200_OK)
async def add_images(
    pets_id: uuid.UUID,
    # payload: Secret_schema = Body(...),
    images: list[UploadFile] = File(...)
):
    # await verify_user(payload)
    return await Images_service().add_images(images, pets_id)


@images_router.get("/{pets_id}/list/", status_code=status.HTTP_200_OK)
async def get_all_images_of_pet(pets_id: uuid.UUID):
    return await Images_service().get_all_images_of_pet(pets_id)


@images_router.get("/{images_id}/", status_code=status.HTTP_200_OK)
async def get_image(images_id: uuid.UUID):
    return await Images_service().get_file_image(images_id)


@images_router.delete("/{pets_id}/list", status_code=status.HTTP_200_OK)
async def delete_all_images_of_pet(pets_id: uuid.UUID):
    return await Images_service().delete_all_images(pets_id)


@images_router.delete("/{images_id}/", status_code=status.HTTP_200_OK)
async def delete_image(
    images_id: uuid.UUID,
    # payload: Secret_schema = Body(...)
):
    # await verify_user(payload)
    return await Images_service().delete_image(images_id)
