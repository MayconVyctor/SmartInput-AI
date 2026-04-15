from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "SmartInputAI"
    google_api_key: str
    database_url: str = "postgresql://postgres:postgres@localhost:5432/todo_db"

    class Config:
        env_file = ".env"

settings = Settings()