from fastapi import FastAPI

from backend.routes import routers

app = FastAPI(
    docs_url=None,
    redoc_url=None,
)

for router in routers:
    app.include_router(router)
