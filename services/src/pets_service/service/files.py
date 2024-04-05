from fastapi import UploadFile

from src.pets_service.database.session import async_session_maker
from sqlalchemy import insert, delete, select, update

from src.file_module.file_worker import save_file, delete_file, get_file

from src.pets_service.database.models import Card, Image
from src.pets_service.schemas import Image_schema


class File_service:
    async def upload_main_image(self, card_id: int, file: UploadFile):
        session = async_session_maker()

        query_get = (
            select(Card)
            .where(Card.id == card_id)
        )
        result = await session.execute(query_get)
        last_file_path = result.scalar_one().main_image
        if last_file_path:
            await delete_file(id, last_file_path)
        pathfile = await save_file(id, file)
        print(pathfile)
        query = (
            update(Card)
            .where(Card.id == card_id)
            .values(main_image=pathfile)
        )

        try:
            await session.execute(query)
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def upload_article_image(
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

    async def delete_image(self, card_id: int, file_id: int):
        session = async_session_maker()

        query_get = (
            select(Image)
            .where(Image.id == file_id)
        )

        query_delete = (
            delete(Image)
            .where(Image.id == file_id)
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

    async def get_main_image(self, card_id: int):
        session = async_session_maker()

        query_get = (
            select(Card)
            .where(Card.id == card_id)
        )
        try:
            result = await session.execute(query_get)
            filename = result.scalar_one().main_image
            return await get_file(card_id, filename)
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def get_article_image(self, card_id: int, image_id: int):
        session = async_session_maker()

        query_get = (
            select(Image)
            .where(Image.id == image_id)
        )
        try:
            result = await session.execute(query_get)
            filename = result.scalar_one().filename
            return await get_file(card_id, filename)
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()
