from decouple import config

DEBUG = config("DEBUG", cast=bool, default=False)

DATABASE_URL = config("DATABASE_URL")
