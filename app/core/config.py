import secrets
from typing import List, Optional

from pydantic import AnyHttpUrl, PostgresDsn


class Settings:
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGIN: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "legal_expert_system"

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = "postgresql+psycopg2://prosper:newpass@localhost:5432/expert_system"


settings = Settings()
