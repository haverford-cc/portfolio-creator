from decouple import config
from sqlalchemy.engine import make_url

DEBUG = config("DEBUG", cast=bool, default=False)

_RAW_DATABASE_URL = make_url(config("DATABASE_URL"))

DATABASE_URL = _RAW_DATABASE_URL \
    .set(drivername=f"{_RAW_DATABASE_URL.drivername}+asyncpg") \
    .render_as_string(hide_password=False)

JWT_SECRET = config("JWT_SECRET")

if DEBUG:
    ALLOW_ORIGINS = [
        "http://127.0.0.1:3000",
        "http://localhost:3000",
        "http://portfolio-creator.local:3000",
    ]
    ALLOW_ORIGIN_REGEX = None

else:
    ALLOW_ORIGINS = [
        "https://portfolio-creator.dens.dev",
        "https://portfolio-creator.vercel.app",
        "https://portfolio-creator-haverford-cc.vercel.app",
    ]
    ALLOW_ORIGIN_REGEX = r"https://portfolio-creator-git-.*-haverford-cc\.vercel\.app"
