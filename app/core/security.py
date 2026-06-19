from datetime import datetime
from datetime import timedelta

from jose import jwt
from jose import JWTError

from passlib.context import CryptContext

from fastapi import HTTPException
from fastapi import status

from app.core.config import settings

# ==========================
# Password Hashing
# ==========================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):

    return pwd_context.hash(password)


def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# ==========================
# JWT Token
# ==========================

def create_access_token(
    data: dict
):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {"exp": expire}
    )

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return encoded_jwt


# ==========================
# Decode Token
# ==========================

def decode_access_token(
    token: str
):

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            return None

        return username

    except JWTError:

        return None


# ==========================
# Authorization Helper
# ==========================

def verify_token(
    token: str
):

    username = decode_access_token(
        token
    )

    if username is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return username