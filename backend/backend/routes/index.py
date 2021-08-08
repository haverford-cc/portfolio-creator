from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/")
async def index() -> Response:
    """The basic index page!"""
    return {"message": "Hello, world!"}
