from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1 import v1_router
from core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME, version=settings.VERSION, debug=settings.DEBUG
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(v1_router, prefix="/api", tags=["v1"])

    return app
