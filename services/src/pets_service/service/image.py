from fastapi import UploadFile

from src.pets_service.database.session import async_session_maker
from sqlalchemy import insert, delete, select

from src.file_module.file_worker import save_file, delete_file

from src.pets_service.database.models import Image
from src.pets_service.schemas import Image_schema


class Image_service:
    async def upload_image(
        self,
        card_id: int,
        article_id: int,
        file: UploadFile
    ):
        filename = await save_file(card_id, file)
        payload = Image_schema(
            article_id=article_id,
            filename=filename
        )

        session = async_session_maker()
        query = (
            insert(Image)
        )
        try:
            await session.execute(query, [payload])
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def delete_image(self, card_id: int, image_id: int):
        session = async_session_maker()

        query_get = (
            select(Image)
            .where(Image.id == image_id)
        )

        query_delete = (
            delete(Image)
            .where(Image.id == image_id)
        )

        try:
            result = await session.execute(query_get)
            delete_file(card_id, result.scalar_one().filename)

            await session.execute(query_delete)
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()
