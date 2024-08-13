from pydantic import BaseModel, PostgresDsn
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


# class DatabaseConfig(BaseModel):
# url: PostgresDsn
# echo: bool = False
# echo_pool: bool = False
# pool_size: int = 50
# max_overflow: int = 10


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    # model_config = SettingsConfigDict(
    #     env_file=(".env.template", ".env"),
    #     case_sensitive=False,
    #     env_nested_delimiter="__",
    #     env_prefix="APP_CONFIG__",
    # )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    # db: DatabaseConfig

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
print(settings.DATABASE_URL)
