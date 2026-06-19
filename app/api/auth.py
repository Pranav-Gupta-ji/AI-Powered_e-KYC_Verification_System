from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import User

from app.schemas.auth import (
    UserRegister,
    UserLogin,
    TokenResponse
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.core.logger import logger

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

#==========================
# Register Endpoint
#==========================

@router.post("/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing = (
        db.query(User)
        .filter(
            User.username == user.username
        )
        .first()
    )

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    logger.info(
        f"User registered: {user.username}"
    )

    return {
        "message": "User created"
    }

#============================
# Login Endpoint
#============================

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(
            User.username ==
            credentials.username
        )
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        credentials.password,
        user.hashed_password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": user.username
        }
    )

    logger.info(
        f"User login: {user.username}"
    )

    return {
        "access_token": token
    }