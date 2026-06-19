from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import HTTPBearer

from app.core.security import verify_token

security = HTTPBearer()


def get_current_user(
    credentials=Depends(security)
):

    token = credentials.credentials

    username = verify_token(
        token
    )

    return username