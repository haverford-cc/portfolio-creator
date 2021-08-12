from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.constants import ALLOW_ORIGINS, ALLOW_ORIGIN_REGEX
from backend.routes import routers

app = FastAPI(
    docs_url=None,
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_origin_regex=ALLOW_ORIGIN_REGEX,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

for router in routers:
    app.include_router(router)
