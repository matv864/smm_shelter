import uuid

from fastapi import APIRouter, status

from .service import Pets_type_service

from .schemas import (
    Pets_type_insert_schema,
    Pets_type_patch_schema,
    # Pets_type_output_schema
)


pets_type_router = APIRouter(
    prefix="/type_pets",
    tags=["type_pets"]
)


@pets_type_router.post("/", status_code=status.HTTP_200_OK)
async def create_pets_type(payload: Pets_type_insert_schema):
    return await Pets_type_service().create_pets_type(payload)


@pets_type_router.get("/list/", status_code=status.HTTP_200_OK)
async def get_all_pets_types():
    return await Pets_type_service().get_all_pets_type()


@pets_type_router.patch("/{pets_type_id}/", status_code=status.HTTP_200_OK)
async def patch_pets_type(
    payload: Pets_type_patch_schema,
    pets_type_id: uuid.UUID
):
    return await Pets_type_service().patch_pets_type(payload, pets_type_id)


@pets_type_router.delete("/{pets_type_id}/", status_code=status.HTTP_200_OK)
async def delete_pets_type(pets_type_id: uuid.UUID):
    return await Pets_type_service().delete_pets_type(pets_type_id)
