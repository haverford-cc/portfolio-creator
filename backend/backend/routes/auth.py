from fastapi import APIRouter, HTTPException, Request, Response
from starlette.status import HTTP_418_IM_A_TEAPOT

from backend.constants import DEBUG, FRONTEND_HOST
from backend.schemas.auth import NewUser, User
from backend.utils import auth
from backend.utils.hosts import verify_host

router = APIRouter(prefix="/auth")


@router.post("/login")
async def login(request: Request, response: Response, user: User) -> Response:
    """Login the given user."""
    token = await auth.login(request.app.state.db_session, user)

    domain = request.headers.get("x-forwarded-host", FRONTEND_HOST)
    if not verify_host(domain):
        raise HTTPException(status_code=HTTP_418_IM_A_TEAPOT, detail="Nice try.")

    response.set_cookie(
        key="token",
        value=token,
        httponly=True,
        domain=domain,
        samesite="strict",
        secure=not DEBUG,
    )

    return {"success": True}


@router.post("/signup")
async def signup(request: Request, user: NewUser) -> Response:
    """Create a new account for the given user."""
    await auth.signup(request.app.state.db_session, user)
    return {"success": True}
