import os

from peewee import SqliteDatabase
from playhouse.psycopg3_ext import Psycopg3Database
from playhouse.db_url import parse

db_url = os.getenv("DATABASE_URL")

if db_url and db_url.startswith("postgres"):
    database_params = parse(db_url)
    user_db = Psycopg3Database(
        **database_params,
        autorollback=True
    )
else:
    user_db = SqliteDatabase((os.getenv("SQLITE_PATH") or "user.db"))

user_db.connect()

from .models import Secret, User

user_db.create_tables([User, Secret])
