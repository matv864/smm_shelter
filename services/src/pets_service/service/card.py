from fastapi import HTTPException

from src.pets_service.database.session import async_session_maker
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import selectinload


from src.pets_service.database.models import (
    Card,
    Article
)
from src.pets_service.schemas import (
    Card_schema,
    Card_filter_schema,
    Update_card_schema
)

from src.pets_service.service.article import Article_service


class Card_service:
    async def get_list_cards(self, filter: Card_filter_schema):
        filter_parametrs = filter.model_dump(exclude_none=True)

        session = async_session_maker()

        query = (
            select(Card)
            .options(
                selectinload(Card.pet_type)
            )
            .filter_by(**filter_parametrs)
        )

        try:
            result = await session.execute(query)
            result = result.scalars().all()
            return result
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def get_card(self, id: int):
        session = async_session_maker()
        query_get = (
            select(Card)
            .where(Card.id == id)
            .options(
                selectinload(Card.pet_type),
                selectinload(Card.articles).selectinload(Article.images)
            )
        )

        query_view = (
            update(Card)
            .values(counter_views=Card.counter_views+1)
        )

        try:
            result = await session.execute(query_get)
            result = result.scalar_one_or_none()
            if not result:
                raise HTTPException(status_code=400, detail="Event not found")
            await session.execute(query_view)
            await session.commit()
            return result
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def create_card(self, payload: Card_schema):
        session = async_session_maker()
        query = (
            insert(Card)
        )
        try:
            await session.execute(query, [payload])
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def update_card(self, payload: Update_card_schema):
        update_values = payload.model_dump(exclude_none=True)

        session = async_session_maker()
        query = (
            update(Card)
            .where(Card.id == payload.id)
            .values(**update_values)
        )

        try:
            await session.execute(query)
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def delete_card(self, id: int):
        session = async_session_maker()
        query = (
            delete(Card)
            .where(Card.id == id)
        )
        try:
            Article_service().delete_article_by_card_id(id)
            await session.execute(query)
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()
