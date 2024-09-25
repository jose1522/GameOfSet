from fastapi import APIRouter
from api.v1.endpoints.sets import router as set_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(set_router)
