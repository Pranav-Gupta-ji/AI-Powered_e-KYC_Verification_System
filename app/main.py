from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.kyc import router as kyc_router
from app.api.health import router as health_router

from app.core.exception_handler import (
    global_exception_handler
)

from app.core.request_logger import (
    RequestLoggingMiddleware
)

app = FastAPI(
    title="E-KYC Verification API"
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.add_middleware(
    RequestLoggingMiddleware
)

app.include_router(
    auth_router
)

app.include_router(
    kyc_router
)

app.include_router(
    health_router
)