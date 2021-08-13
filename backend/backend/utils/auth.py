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
