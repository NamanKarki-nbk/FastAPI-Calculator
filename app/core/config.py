from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "FastAPI Calculator"

    class Config:
        env_file = ".env"


settings = Settings()
