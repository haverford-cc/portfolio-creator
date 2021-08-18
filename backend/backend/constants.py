from decouple import config
from sqlalchemy.engine import make_url

DEBUG = config("DEBUG", cast=bool, default=False)

_RAW_DATABASE_URL = make_url(config("DATABASE_URL"))

DATABASE_URL = _RAW_DATABASE_URL \
    .set(drivername=f"{_RAW_DATABASE_URL.drivername}+asyncpg") \
    .render_as_string(hide_password=False)

JWT_SECRET = config("JWT_SECRET")

FRONTEND_HOST = config(
    "FRONTEND_HOST",
    default="portfolio-creator.dens.dev" if not DEBUG else "portfolio-creator.local:3000"
)

PASSWORD_MIN_LENGTH = 8

if DEBUG:
    ALLOW_ORIGIN_PROTOCOL = "https"
    ALLOW_ORIGIN_HOSTS = [
        "127.0.0.1:3000",
        "localhost:3000",
    ]
    ALLOW_ORIGIN_REGEX = None

else:
    ALLOW_ORIGIN_PROTOCOL = "https"
    ALLOW_ORIGIN_HOSTS = [
        "portfolio-creator.vercel.app",
        "portfolio-creator-haverford-cc.vercel.app",
    ]
    ALLOW_ORIGIN_REGEX = r"portfolio-creator-git-.*-haverford-cc\.vercel\.app"

ALLOW_ORIGIN_HOSTS.append(FRONTEND_HOST)

ALLOW_ORIGINS = [
    f"{ALLOW_ORIGIN_PROTOCOL}://{host}"
    for host in ALLOW_ORIGIN_HOSTS
]
