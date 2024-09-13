from dotenv import load_dotenv

from functools import cached_property, lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    POSTGRES_HOST: str = None
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    PATH_TO_SAVE_DUMP: str

    @cached_property
    def postgres_url(self):
        return "postgresql+asyncpg://" + \
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@" + \
            f"{self.POSTGRES_HOST}/{self.POSTGRES_DB}" + \
            "?async_fallback=True"

    @cached_property
    def command_pg_dump(self):
        return "pg_dump --column-inserts " + \
            f"-U {self.POSTGRES_USER} " + \
            f"-h {self.POSTGRES_HOST} -p 5432 " + \
            f"{self.POSTGRES_DB} " + \
            f"> {self.PATH_TO_SAVE_DUMP}"


@lru_cache
def get_settings():
    return Settings()
