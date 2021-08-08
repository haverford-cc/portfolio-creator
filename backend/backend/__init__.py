from fastapi import FastAPI

from backend.routes import api_router

app = FastAPI(
    docs_url=None,
    redoc_url=None,
)
app.include_router(api_router)
