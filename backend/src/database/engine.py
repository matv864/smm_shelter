import logging

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.settings import settings


engine = create_async_engine(settings.postgres_url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

logging.info("engine is created")
