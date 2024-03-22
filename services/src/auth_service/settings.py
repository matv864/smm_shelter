from functools import cached_property, lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    POSTGRES_AUTH_NAME_SERVICE: str
    POSTGRES_AUTH_HOST: str
    POSTGRES_AUTH_PORT: str
    POSTGRES_AUTH_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @cached_property
    def postgres_url(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:" + \
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_AUTH_HOST}:" + \
            f"{self.POSTGRES_AUTH_PORT}/{self.POSTGRES_AUTH_DB}"
        # return f"postgresql+asyncpg://{self.POSTGRES_USER}:" + \
        #     f"{self.POSTGRES_PASSWORD}@" + \
        #     f"{self.POSTGRES_AUTH_NAME_SERVICE}/{self.POSTGRES_AUTH_DB}"


@lru_cache
def get_settings():
    return Settings()
