from fastapi import APIRouter

from backend.routes import index

api_router = APIRouter(
    prefix="/api"
)
api_router.include_router(index.router)
