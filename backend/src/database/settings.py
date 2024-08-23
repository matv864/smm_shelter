import logging

from functools import cached_property, lru_cache

from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    POSTGRES_NAME_SERVICE: Optional[str] = None
    POSTGRES_HOST: Optional[str] = None
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    PATH_TO_SAVE_DUMP: str

    @cached_property
    def postgres_url(self):
        if self.POSTGRES_NAME_SERVICE:
            return f"postgresql+asyncpg://{self.POSTGRES_USER}:" + \
                f"{self.POSTGRES_PASSWORD}@" + \
                f"{self.POSTGRES_NAME_SERVICE}/{self.POSTGRES_DB}" + \
                "?async_fallback=True"
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:" + \
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:" + \
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}" + \
            "?async_fallback=True"

    @cached_property
    def command_pg_dump(self):
        if self.POSTGRES_NAME_SERVICE:
            return "pg_dump --column-inserts " + \
                f"-U {self.POSTGRES_USER} " + \
                f"-h {self.POSTGRES_NAME_SERVICE} -p {self.POSTGRES_PORT} " + \
                f"{self.POSTGRES_DB} " + \
                f"> {self.PATH_TO_SAVE_DUMP}"
        return "pg_dump --column-inserts " + \
            f"-U {self.POSTGRES_USER} " + \
            f"-h {self.POSTGRES_HOST} -p {self.POSTGRES_PORT} " + \
            f"{self.POSTGRES_DB} " + \
            f"> {self.PATH_TO_SAVE_DUMP}"


@lru_cache
def get_settings():
    logging.info("settings are created")
    return Settings()
