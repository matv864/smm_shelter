import uuid

from src.database.models import Pets_type
from src.database.my_crud import My_crud

from .schemas import (
    Pets_type_insert_schema,
    Pets_type_patch_schema,
    Pets_type_output_schema
)


pets_type_crud = My_crud(Pets_type)


class Pets_type_service:
    async def create_pets_type(self, payload: Pets_type_insert_schema):
        return await pets_type_crud.create(
            record=payload
        )

    async def get_all_pets_type(self):
        return await pets_type_crud.get(
            multi=True
        )

    async def patch_pets_type(
        self,
        payload: Pets_type_patch_schema,
        pets_type_id: uuid.UUID
    ):
        return await pets_type_crud.patch(
            filters=[Pets_type.id == pets_type_id],
            new_data=payload.model_dump(exclude_none=True)
        )

    async def delete_pets_type(self, pets_type_id: uuid.UUID):
        return await pets_type_crud.remove([Pets_type.id == pets_type_id])
