from datetime import date

from src.pets_service.database.session import async_session_maker
from sqlalchemy import insert, update, delete

from src.pets_service.database.models import (
    Article
)
from src.pets_service.schemas import (
    Article_schema,
    Update_article_schema
)


class Article_service:
    async def create_article(self, payload: Article_schema):
        payload.date_publish = date.today()

        session = async_session_maker()
        query = (
            insert(Article)
        )
        try:
            await session.execute(query, [payload])
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def update_article(self, payload: Update_article_schema):
        update_values = payload.model_dump(exclude_none=True)

        session = async_session_maker()
        query = (
            update(Article)
            .where(Article.id == payload.id)
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

    async def delete_article(self, article_id: int):
        session = async_session_maker()
        query = (
            delete(Article)
            .where(Article.id == article_id)
        )
        try:
            await session.execute(query)
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()

    async def delete_article_by_card_id(self, card_id: int):
        session = async_session_maker()
        query = (
            delete(Article)
            .where(Article.card_id == card_id)
        )
        try:
            await session.execute(query)
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
        finally:
            await session.close()
