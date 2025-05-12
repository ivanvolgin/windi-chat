from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PG_HOST: str = "localhost"
    PG_PORT: int = 5432
    PS_USER: str = "postgres"
    PG_PASSWORD: str = "password"
    PG_DB: str = "my_db"
    DATABASE_URI: str

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')

settings = Settings()