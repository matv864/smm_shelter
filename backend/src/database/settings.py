from functools import cached_property, lru_cache

from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    POSTGRES_NAME_SERVICE: Optional[str] = None
    POSTGRES_HOST: Optional[str] = None
    POSTGRES_PORT: Optional[str] = None
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @cached_property
    def postgres_url(self):
        if self.POSTGRES_HOST:
            return f"postgresql+asyncpg://{self.POSTGRES_USER}:" + \
                f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:" + \
                f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:" + \
            f"{self.POSTGRES_PASSWORD}@" + \
            f"{self.POSTGRES_NAME_SERVICE}/{self.POSTGRES_DB}"


@lru_cache
def get_settings():
    return Settings()
