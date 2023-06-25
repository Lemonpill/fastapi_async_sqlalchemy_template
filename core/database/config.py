from pydantic import BaseSettings


class Config(BaseSettings):
    SQLALCHEMY_URL: str

    class Config:
        env_file = ".env"


settings = Config()
