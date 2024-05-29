import uuid

from fastapi import UploadFile

from src.database.models import Images
from src.database.my_crud import My_crud

images_crud = My_crud(Images)


class Images_service:
    async def add_image(
        self,
        image: UploadFile,
        pets_id: uuid.UUID
    ):
        return await images_crud.create(
            record={
                "path": "good_path",
                "pets_id": pets_id
            },
            Output_model=dict
        )

    async def get_all_images_of_pet(self, pets_id: uuid.UUID):
        return await images_crud.get(
            filters=[Images.pets_id == pets_id],
            multi=True
        )

    async def get_image(self, images_id: uuid.UUID):
        return await images_crud.get(
            filters=[Images.id == images_id]
        )

    async def delete_image(self, images_id: uuid.UUID):
        return await images_crud.remove(
            filters=[Images.id == images_id]
        )
