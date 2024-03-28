from src.pets_service.database.session import async_session_maker
from sqlalchemy import select, insert, delete
from src.pets_service.database.models import (
    Pet_type
)
from src.pets_service.schemas import (
    Pet_type_shema
)


class Pet_type_service:
    async def get_list_pet_types(self):
        session = async_session_maker()

        query = select(Pet_type)

        try:
            result = await session.execute(query)
            result = result.scalars().all()
            return result
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def create_pet_type(self, payload: Pet_type_shema):
        session = async_session_maker()
        query = (
            insert(Pet_type)
        )
        try:
            await session.execute(query, [payload])
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def delete_pet_type(self, id: int):
        session = async_session_maker()
        query = (
            delete(Pet_type)
            .where(Pet_type.id == id)
        )
        try:
            await session.execute(query)
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()
