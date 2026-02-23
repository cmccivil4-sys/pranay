from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    app_name: str = 'AI Circuit Mentor API'
    jwt_secret: str = 'change-me'
    jwt_algorithm: str = 'HS256'
    redis_url: str = 'redis://redis:6379/0'
    database_url: str = 'postgresql+asyncpg://postgres:postgres@postgres:5432/aicm'
    llm_api_url: str = 'https://api.example-llm.com/v1/chat/completions'
    license_public_key: str = 'offline-public-key-placeholder'


settings = Settings()
