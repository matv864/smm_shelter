from functools import cached_property, lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    POSTGRES_JOKE_NAME_SERVICE: str
    # POSTGRES_JOKE_HOST: str
    # POSTGRES_JOKE_PORT: str
    POSTGRES_JOKE_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @cached_property
    def postgres_url(self):
        # return f"postgresql+asyncpg://{self.POSTGRES_USER}:" + \
        #     f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_JOKE_HOST}:" + \
        #     f"{self.POSTGRES_JOKE_PORT}/{self.POSTGRES_JOKE_DB}"
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:" + \
            f"{self.POSTGRES_PASSWORD}@" + \
            f"{self.POSTGRES_JOKE_NAME_SERVICE}/{self.POSTGRES_JOKE_DB}"


@lru_cache
def get_settings():
    return Settings()
