from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from backend.constants import ALLOW_ORIGINS, ALLOW_ORIGIN_REGEX, DATABASE_URL
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


@app.on_event("startup")
async def startup() -> None:
    """Create database connection on startup."""
    app.state.db_engine = create_async_engine(DATABASE_URL)
    app.state.db_session = sessionmaker(
        app.state.db_engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )


@app.on_event("shutdown")
async def shutdown() -> None:
    """Close database connections on shutdown."""
    await app.state.db_engine.dispose()
