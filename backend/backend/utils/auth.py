import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

from fastapi import HTTPException, Request
from fastapi.security import APIKeyCookie
from jose import JWTError, jwt
from passlib.hash import bcrypt
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_409_CONFLICT
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.constants import JWT_SECRET
from backend.models.auth import User
from backend.schemas.auth import User as UserSchema


class JWTBearer(APIKeyCookie):
    """Dependency for HTTP routes to enforce JWT authentication."""

    def __init__(self):
        super().__init__(name="token", auto_error=True)

    async def __call__(self, request: Request) -> str:
        """Check if the given token is valid for this endpoint."""
        token = await super().__call__(request)
        if not token:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Not authenticated.")

        try:
            token_data = jwt.decode(token, JWT_SECRET)
        except JWTError:
            raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid authentication.")

        if time.time() > token_data["exp"]:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Not authenticated.")

        request.state.user_id = token_data["id"]
        return token


async def signup(db_session: AsyncSession, user: UserSchema) -> int:
    """Create an account for a new user."""
    async with db_session() as session:
        async with session.begin():
            db_user = await session.execute(
                select(User).where(User.email == user.email)
            )
            if db_user.first() is not None:
                raise HTTPException(status_code=HTTP_409_CONFLICT, detail="User already exists.")

            loop = asyncio.get_running_loop()
            with ThreadPoolExecutor() as pool:
                password_hash = await loop.run_in_executor(
                    pool,
                    bcrypt.hash,
                    user.password1,
                )

            db_user = User(email=user.email, password_hash=password_hash)
            session.add(db_user)
            await session.flush()

            return db_user.id


async def login(db_session: AsyncSession, user: UserSchema) -> str:
    """Login the given user."""
    async with db_session() as session:
        db_user = (
            await session.execute(
                select(User).where(User.email == user.email)
            )
        ).scalars().first()

        if db_user is None:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )

        loop = asyncio.get_running_loop()
        with ThreadPoolExecutor() as pool:
            if await loop.run_in_executor(
                pool,
                bcrypt.verify,
                user.password,
                db_user.password_hash
            ):
                epoch_time = int(time.time())
                payload = {
                    "id": db_user.id,
                    "iat": epoch_time,
                    "exp": epoch_time + 60 * 60 * 24 * 7,  # 1 week later
                }
                return jwt.encode(payload, JWT_SECRET)

    raise HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Invalid email or password."
    )
