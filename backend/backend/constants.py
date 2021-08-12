from decouple import config
from sqlalchemy.engine import URL

DEBUG = config("DEBUG", cast=bool, default=False)

DATABASE_URL = URL.create(config("DATABASE_URL")).set(drivername="postgresql+asyncpg")

if DEBUG:
    ALLOW_ORIGINS = [
        "http://127.0.0.1:3000",
        "http://localhost:3000",
    ]
    ALLOW_ORIGIN_REGEX = None

else:
    ALLOW_ORIGINS = [
        "https://portfolio-creator.dens.dev",
        "https://portfolio-creator.vercel.app",
        "https://portfolio-creator-haverford-cc.vercel.app",
    ]
    ALLOW_ORIGIN_REGEX = r"https://portfolio-creator-git-.*-haverford-cc\.vercel\.app"
