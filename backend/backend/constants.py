from decouple import config
from sqlalchemy.engine import make_url

DEBUG = config("DEBUG", cast=bool, default=False)

_RAW_DATABASE_URL = make_url(config("DATABASE_URL"))

DATABASE_URL = _RAW_DATABASE_URL \
    .set(drivername=f"{_RAW_DATABASE_URL.drivername}+asyncpg") \
    .render_as_string(hide_password=False)

JWT_SECRET = config("JWT_SECRET")

FRONTEND_DOMAIN = config(
    "FRONTEND_DOMAIN",
    default="portfolio-creator.dens.dev" if not DEBUG else "portfolio-creator.local"
)

if DEBUG:
    ALLOW_ORIGIN_PROTOCOL = "http"
    ALLOW_ORIGIN_PARTS = [
        ("127.0.0.1", 3000),
        ("localhost", 3000),
        ("portfolio-creator.local", 3000),
    ]
    ALLOW_ORIGIN_REGEX = None

else:
    ALLOW_ORIGIN_PROTOCOL = "https"
    ALLOW_ORIGIN_PARTS = [
        ("portfolio-creator.dens.dev", None),
        ("portfolio-creator.vercel.app", None),
        ("portfolio-creator-haverford-cc.vercel.app", None),
    ]
    ALLOW_ORIGIN_REGEX = r"portfolio-creator-git-.*-haverford-cc\.vercel\.app"

if (_ENV_ALLOW_ORIGIN_HOST := config("ALLOW_ORIGIN_HOST", default=None)):
    if (_ENV_ALLOW_ORIGIN_PORT := config("ALLOW_ORIGIN_PORT", cast=int, default=None)):
        ALLOW_ORIGIN_PARTS.append((_ENV_ALLOW_ORIGIN_HOST, _ENV_ALLOW_ORIGIN_PORT))
    else:
        ALLOW_ORIGIN_PARTS.append((_ENV_ALLOW_ORIGIN_HOST, None))

ALLOW_ORIGINS = [
    f"{ALLOW_ORIGIN_PROTOCOL}://{host}:{port}"
    if port is not None else f"{ALLOW_ORIGIN_PROTOCOL}://{host}"
    for host, port in ALLOW_ORIGIN_PARTS
]
