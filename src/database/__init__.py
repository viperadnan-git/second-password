from os import environ

from peewee import SqliteDatabase, PostgresqlDatabase

db_url = environ.get("DATABASE_URL")

if db_url and db_url.startswith("postgres"):
    user_db = PostgresqlDatabase(
        db_url,
        autorollback=True
    )
else:
    user_db = SqliteDatabase((environ.get("SQLITE_PATH") or "user.db"))

user_db.connect()

from .models import Secret, User

user_db.create_tables([User, Secret])
