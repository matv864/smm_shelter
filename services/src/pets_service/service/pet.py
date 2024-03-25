from src.pets_service.database.session import async_session_maker
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import selectinload
# from sqlalchemy.orm import selectinload
from fastapi import HTTPException
from src.pets_service.database.models import Card, Pet_type, Image, Article
# from src.pets_service.schemas import 


class Pets_service:
    async def get_list_cards(self):
        session = async_session_maker()
        query = (
            select(Card)
            .options(
                selectinload(Card.pet_type),
                selectinload(Card.articles).selectinload(Article.images)
            )
        )
        result = await session.execute(query)
        await session.close()
        result = result.scalars().all()
        return result

    async def get_card(self, id: int):
        session = async_session_maker()
        query = (
            select(Card)
            .where(Card.id == id)
            .options(
                selectinload(Card.pet_type),
                selectinload(Card.articles).selectinload(Article.images)
            )
        )
        result = await session.execute(query)
        await session.close()
        if not result:
            raise HTTPException(status_code=400, detail="Event not found")
        result = result.scalar_one_or_none()
        return result

    # async def create_joke(self, payload: Joke_creating, token: str):
    #     session = async_session_maker()
    #     query = (
    #         insert(Joke)
    #     )
    #     try:
    #         await session.execute(query, [payload])
    #         await session.commit()
    #         return "success"
    #     except Exception as e:
    #         return f"error: {type(e)} |*-*| {str(e)}"

    # async def update_joke(self, payload: Joke_record, token: str):
    #     session = async_session_maker()
    #     query = (
    #         update(Joke)
    #         .where(Joke.id == payload.id)
    #         .values(
    #             title=payload.title,
    #             theme=payload.theme,
    #             text_joke=payload.text_joke,
    #             creating=payload.creating,
    #         )
    #     )

    #     try:
    #         await session.execute(query)
    #         await session.commit()
    #         return "success"
    #     except Exception as e:
    #         return f"error: {type(e)} |*-*| {str(e)}"

    # async def delete_joke(self, id: int, token: str):
    #     session = async_session_maker()
    #     query = (
    #         delete(Joke)
    #         .where(Joke.id == id)
    #     )
    #     try:
    #         await session.execute(query)
    #         await session.commit()
    #         return "success"
    #     except Exception as e:
    #         return f"error: {type(e)} |*-*| {str(e)}"
