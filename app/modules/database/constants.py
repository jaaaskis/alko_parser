import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USER = os.environ.get("DATABASE_USER")


DATABASE_CONNECTION = (
    DATABASE_URL if DATABASE_URL else f"dbname={DATABASE_NAME} user={DATABASE_USER}"
)
