from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware

from api.v1 import v1_router
from core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME, version=settings.VERSION, debug=settings.DEBUG
    )
    app.include_router(v1_router, prefix="/api", tags=["v1"])
    app.add_middleware(GZipMiddleware, minimum_size=500)

    return app
