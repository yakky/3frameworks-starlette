import databases
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".config")

DATABASE_URL = config("DATABASE_URL", cast=databases.DatabaseURL)
DEBUG = config.get("DEBUG", cast=bool, default=False)
SECRET_KEY = config("SECRET_KEY", cast=Secret)
