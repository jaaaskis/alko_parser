import os
from dotenv import load_dotenv

load_dotenv()

database_name = os.environ.get("DATABASE_NAME")
database_user = os.environ.get("DATABASE_USER")
