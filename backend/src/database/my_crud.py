from fastapi.exceptions import HTTPException

from sqlalchemy import insert, select, exists, update, delete
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import text

from src.database.engine import async_session_maker


def exception_wrapper(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except IntegrityError as e:
            print(str(e))
            raise HTTPException(status_code=400, detail="bad foreign object")
        except Exception as e:
            error_text = f"{type(e)} - {str(e)}"
            raise HTTPException(status_code=400, detail=error_text)
    return wrapper


class My_crud:
    def __init__(
        self,
        Main_model: object,
        fields_to_join: list[list] = []
    ):
        self.Main_model = Main_model
        self.fields_to_join = fields_to_join

    @exception_wrapper
    async def create(
        self,
        record
    ):
        query_insert = insert(self.Main_model)

        query_insert = query_insert.returning(self.Main_model)

        async with async_session_maker() as session:
            output_record = await session.execute(query_insert, [record])
            await session.commit()

        return output_record.scalar()

    @exception_wrapper
    async def exist(
        self,
        filters
    ):
        exists_criteria = exists()

        for filter in filters:
            exists_criteria = exists_criteria.where(filter)

        query = select(self.Main_model).where(exists_criteria)

        async with async_session_maker() as session:
            query_executed = await session.execute(query)
            return bool(query_executed.scalar())

    @exception_wrapper
    async def get(
        self,
        filters=[],
        where_filters=dict(),
        offset=0,
        limit=100,
        order_by=None,
        multi=False
    ):
        query_search = select(self.Main_model).options(
            *[
                selectinload(field)
                for field in self.fields_to_join
            ],
        )

        for filter in filters:
            query_search = query_search.filter(filter)

        for where_filter in where_filters:
            query_search = query_search.where(where_filter)

        if multi:
            if order_by:
                query_search = query_search.order_by(order_by)
            if offset:
                query_search = query_search.offset(offset)
            if limit:
                query_search = query_search.limit(limit)

        async with async_session_maker() as session:
            query_executed = await session.execute(query_search)

            if multi:
                return query_executed.scalars().all()

            return query_executed.scalar_one_or_none()

    @exception_wrapper
    async def patch(
        self,
        filters,
        new_data: dict
    ):
        query_patch = update(self.Main_model)

        for filter in filters:
            query_patch = query_patch.where(filter)

        keys = list(new_data.keys())
        for key in keys:
            if type(key) is str:
                pass
            else:
                new_data.pop(key)
        query_patch = query_patch.values(**new_data)

        query_patch = query_patch.returning(self.Main_model)

        async with async_session_maker() as session:
            output_record = await session.execute(query_patch)
            await session.commit()

        return output_record.scalar()

    @exception_wrapper
    async def remove(
        self,
        filters
    ):
        query_delete = delete(self.Main_model)

        for filter in filters:
            query_delete = query_delete.where(filter)

        async with async_session_maker() as session:
            await session.execute(query_delete)
            await session.commit()
