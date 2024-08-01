import uuid

from fastapi import APIRouter, status

from .service import Pets_service

from .schemas import (
    Pets_insert_schema,
    Pets_patch_schema,
    Pets_output_schema
)


pets_router = APIRouter(
    prefix="/pets",
    tags=["pets"]
)


@pets_router.post(
    "/",
    response_model=Pets_output_schema,
    status_code=status.HTTP_200_OK
)
async def create_pets_record(payload: Pets_insert_schema):
    return await Pets_service().create_pets_record(payload)


@pets_router.get(
    "/list/",
    response_model=list[Pets_output_schema],
    status_code=status.HTTP_200_OK
)
async def get_all_pets_records():
    return await Pets_service().get_all_pets_records()


@pets_router.get(
    "/{pets_id}/",
    response_model=Pets_output_schema,
    status_code=status.HTTP_200_OK)
async def get_pets_record(pets_id: uuid.UUID):
    return await Pets_service().get_pets_record(pets_id)


@pets_router.patch(
    "/{pets_id}/",
    response_model=Pets_output_schema,
    status_code=status.HTTP_200_OK
)
async def patch_pets_record(payload: Pets_patch_schema, pets_id: uuid.UUID):
    return await Pets_service().patch_pets_record(payload, pets_id)


@pets_router.delete("/{pets_id}/", status_code=status.HTTP_200_OK)
async def delete_pets_record(pets_id: uuid.UUID):
    return await Pets_service().delete_pets_record(pets_id)
