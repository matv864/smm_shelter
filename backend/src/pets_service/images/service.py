import uuid

import os
from fastapi import UploadFile
from fastapi.responses import FileResponse
import aiofiles

from src.database.models import Images
from src.database.my_crud import My_crud

from .schemas import Images_record_schema

images_crud = My_crud(Images)

path_to_pets_storage = "/storage/pets_images/"
path_to_pets_image = "/storage/pets_images/{}"


class Images_service:
    async def add_images(
        self,
        images: list[UploadFile],
        pets_id: uuid.UUID
    ):
        result_records = []

        for image in images:
            image_record: Images_record_schema = await images_crud.create(
                record=Images_record_schema(
                    pets_id=pets_id,
                    filename=image.filename
                ),
                Output_model=Images_record_schema
            )

            async with aiofiles.open(
                path_to_pets_image.format(image_record.id), 'wb'
            ) as out_file:
                while content := await image.read(1024):
                    await out_file.write(content)

            result_records.append(image_record.model_dump())
        return result_records

    async def get_all_images_of_pet(self, pets_id: uuid.UUID):
        return await images_crud.get(
            filters=[Images.pets_id == pets_id],
            multi=True
        )

    async def get_file_image(self, images_id: uuid.UUID):
        if not os.path.exists(path_to_pets_storage):
            return "no exists"

        image_record: Images_record_schema = await images_crud.get(
            filters=[Images.id == images_id],
            Output_model=Images_record_schema
        )
        return FileResponse(
            path=path_to_pets_storage,
            filename=image_record.filename,
            media_type='multipart/form-data'
        )

    async def delete_all_images(self, pets_id: uuid.UUID):
        images_records: list[Images_record_schema] = await images_crud.get(
            filters=[Images.pets_id == pets_id],
            multi=True,
            Output_model=Images_record_schema
        )
        for images_record in images_records:
            await self.delete_file(images_record.id)
        return await images_crud.remove([Images.pets_id == pets_id])

    async def delete_image(self, images_id: uuid.UUID):
        await self.delete_file(images_id)
        return await images_crud.remove([Images.id == images_id])

    async def delete_file(self, images_id: uuid.UUID):
        path_to_image = path_to_pets_image.format(images_id)
        if os.path.exists(path_to_image):
            os.remove(path_to_image)
