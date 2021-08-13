from fastapi import APIRouter, Cookie, Request, Response

from backend.constants import DEBUG, FRONTEND_DOMAIN
from backend.schemas.auth import NewUser, User
from backend.utils import auth

router = APIRouter(prefix="/auth")


@router.post("/login")
async def login(request: Request, response: Response, user: User) -> Response:
    """Login the given user."""
    token = await auth.login(request.app.state.db_session, user)

    response.set_cookie(
        key="token",
        value=token,
        httponly=True,
        domain=FRONTEND_DOMAIN,
        samesite="strict",
        secure=not DEBUG,
    )

    return {"success": True}


@router.post("/signup")
async def signup(request: Request, user: NewUser) -> Response:
    """Create a new account for the given user."""
    await auth.signup(request.app.state.db_session, user)
    return {"success": True}
