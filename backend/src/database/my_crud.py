from fastapi.exceptions import HTTPException

from sqlalchemy import insert, select, exists, update, delete
from sqlalchemy.orm import selectinload

from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.selectable import Select

from src.database.engine import session_maker


def exception_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
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
    def create(
        self,
        record
    ):
        query_insert = insert(self.Main_model)

        query_insert = query_insert.returning(self.Main_model)

        with session_maker() as session:
            output_record = session.execute(query_insert, [record])
            session.commit()

        return output_record.scalar()

    @exception_wrapper
    def exist(
        self,
        filters
    ):
        exists_criteria = exists()

        for filter in filters:
            exists_criteria = exists_criteria.where(filter)

        query = select(self.Main_model).where(exists_criteria)

        with session_maker() as session:
            query_executed = session.execute(query)
            return bool(query_executed.scalar())

    @exception_wrapper
    def get(
        self,
        filters=[],
        join_fields=[],
        where_filters=dict(),
        offset=0,
        limit=100,
        order_by=None,
        multi=False
    ):
        query_search: Select = select(self.Main_model)
        query_search = query_search.options(
            *[
                selectinload(field)
                for field in self.fields_to_join
            ],
        )
        for join_field in join_fields:
            query_search = query_search.join(join_field)

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

        with session_maker() as session:
            query_executed = session.execute(query_search)

            if multi:
                return query_executed.scalars().all()

            return query_executed.scalar_one_or_none()

    @exception_wrapper
    def patch(
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

        with session_maker() as session:
            output_record = session.execute(query_patch)
            session.commit()

        return output_record.scalar()

    @exception_wrapper
    def remove(
        self,
        filters
    ):
        query_delete = delete(self.Main_model)

        for filter in filters:
            query_delete = query_delete.where(filter)

        with session_maker() as session:
            session.execute(query_delete)
            session.commit()
