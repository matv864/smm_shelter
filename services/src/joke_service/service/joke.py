from src.joke_service.database.session import async_session_maker
from sqlalchemy import select, insert, update, delete
# from sqlalchemy.orm import selectinload
from fastapi import HTTPException
from src.joke_service.database.models import Joke
from src.joke_service.schemas import Joke_record, Joke_creating


class Joke_service:
    async def get_list_jokes(self):
        session = async_session_maker()
        query = (select(Joke))
        result = await session.execute(query)
        await session.close()
        result = result.scalars().all()
        return result

    async def get_joke(self, id: int):
        session = async_session_maker()
        query = (
            select(Joke)
            .where(Joke.id == id)
        )
        result = await session.execute(query)
        await session.close()
        if not result:
            raise HTTPException(status_code=400, detail="Event not found")
        result = result.scalar_one_or_none()
        return result

    async def create_joke(self, payload: Joke_creating):
        session = async_session_maker()
        query = (
            insert(Joke)
        )
        try:
            await session.execute(query, [payload])
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"

    async def update_joke(self, payload: Joke_record):
        session = async_session_maker()
        query = (
            update(Joke)
            .where(Joke.id == payload.id)
            .values(
                title=payload.title,
                theme=payload.theme,
                text_joke=payload.text_joke,
                creating=payload.creating,
            )
        )

        try:
            await session.execute(query)
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"

    async def delete_joke(self, id: int):
        session = async_session_maker()
        query = (
            delete(Joke)
            .where(Joke.id == id)
        )
        try:
            await session.execute(query)
            await session.commit()
            return "success"
        except Exception as e:
            return f"error: {type(e)} |*-*| {str(e)}"
