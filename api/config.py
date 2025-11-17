import os
from dotenv import load_dotenv


load_dotenv()


HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY", "extra-insecure-secret-key")
    RATELIMIT_STORAGE_URI = os.getenv("RATELIMIT_STORAGE_URI")
    RATELIMIT_ENABLED = True
