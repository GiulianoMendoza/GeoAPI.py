import os
import jwt
from datetime import datetime, timedelta, UTC
from typing import Optional

# Usa SECRET_KEY desde entorno si existe; mantiene un fallback para tests/local
SECRET_KEY = os.getenv("SECRET_KEY", "SUPER_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class JwtProvider:
    def create_access_token(self, data: dict, expires_delta: Optional[int] = None):
        to_encode = data.copy()
        expire = datetime.now(UTC) + timedelta(
            minutes=expires_delta or ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token expirado")
        except jwt.InvalidTokenError:
            raise ValueError("Token inválido")

