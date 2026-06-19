import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import logger


class RequestLoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start_time = time.time()

        response = await call_next(
            request
        )

        duration = round(
            time.time() - start_time,
            3
        )

        logger.info(
            f"{request.method} "
            f"{request.url.path} "
            f"Status={response.status_code} "
            f"Time={duration}s"
        )

        return response