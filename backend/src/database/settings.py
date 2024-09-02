from dotenv import load_dotenv

from functools import cached_property, lru_cache

from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    POSTGRES_NAME_SERVICE: Optional[str] = None
    POSTGRES_HOST: Optional[str] = None
    POSTGRES_PORT: Optional[str] = None
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    PATH_TO_SAVE_DUMP: str

    @cached_property
    def postgres_url(self):
        if self.POSTGRES_HOST:
            return f"postgresql+asyncpg://{self.POSTGRES_USER}:" + \
                f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:" + \
                f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}" + \
                "?async_fallback=True"

        return f"postgresql+asyncpg://{self.POSTGRES_USER}:" + \
            f"{self.POSTGRES_PASSWORD}@" + \
            f"{self.POSTGRES_NAME_SERVICE}/{self.POSTGRES_DB}" + \
            "?async_fallback=True"

    @cached_property
    def command_pg_dump(self):
        if self.POSTGRES_HOST:
            return "pg_dump --column-inserts " + \
                f"-U {self.POSTGRES_USER} " + \
                f"-h {self.POSTGRES_HOST} -p {self.POSTGRES_PORT} " + \
                f"{self.POSTGRES_DB} " + \
                f"> {self.PATH_TO_SAVE_DUMP}"
        return "pg_dump --column-inserts " + \
            f"-U {self.POSTGRES_USER} " + \
            f"-h {self.POSTGRES_NAME_SERVICE} -p 5432 " + \
            f"{self.POSTGRES_DB} " + \
            f"> {self.PATH_TO_SAVE_DUMP}"


@lru_cache
def get_settings():
    return Settings()
