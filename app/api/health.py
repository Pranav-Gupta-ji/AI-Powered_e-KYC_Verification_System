from fastapi import APIRouter

from app.db.db_health import (
    check_database
)

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():

    return {
        "status": "healthy",
        "database": check_database()
    }

