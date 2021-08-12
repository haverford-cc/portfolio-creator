from decouple import config

DEBUG = config("DEBUG", cast=bool, default=False)

DATABASE_URL = config("DATABASE_URL")

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
