import uuid

from src.database.models import Pets, Pets_type
from src.database.my_crud import My_crud

from .schemas import (
    Pets_insert_schema,
    Pets_patch_schema
)

from src.pets_service.images.service import Images_service


pets_crud = My_crud(Pets, [Pets.images])


class Pets_service:
    @staticmethod
    async def create_pets_record(payload: Pets_insert_schema):
        payload.date_birth = payload.date_birth.replace(tzinfo=None)
        await My_crud(Pets_type).exist([Pets_type.id == payload.type_id])
        return await pets_crud.create(
            record=payload
        )

    @staticmethod
    async def get_all_pets_records():
        return await pets_crud.get(multi=True)

    @staticmethod
    async def get_pets_record(pets_id: uuid.UUID):
        return await pets_crud.get(
            filters=[Pets.id == pets_id]
        )

    @staticmethod
    async def patch_pets_record(
        payload: Pets_patch_schema,
        pets_id: uuid.UUID
    ):
        payload.date_birth = payload.date_birth.replace(tzinfo=None)
        return await pets_crud.patch(
            filters=[Pets.id == pets_id],
            new_data=payload.model_dump(exclude_none=True)
        )

    @staticmethod
    async def delete_pets_record(pets_id):
        await Images_service().delete_all_images(pets_id)
        return await pets_crud.remove([Pets.id == pets_id])
