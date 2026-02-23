from datetime import datetime, timedelta, timezone
from jose import jwt

from app.core.config import settings


def create_access_token(subject: str, expires_minutes: int = 60) -> str:
    now = datetime.now(timezone.utc)
    payload = {'sub': subject, 'iat': int(now.timestamp()), 'exp': int((now + timedelta(minutes=expires_minutes)).timestamp())}
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
