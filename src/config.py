from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_DATABASE: str

    JWT_SECRET: str
    JWT_ALGORITHM: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
