import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import get_settings


engine = create_engine(get_settings().postgres_url)
session_maker = sessionmaker(engine, expire_on_commit=False)

logging.info("engine is created")
