from os import environ

from peewee import SqliteDatabase


user_db = SqliteDatabase((environ.get("SQLITE_PATH") or "user.db"))
user_db.connect()

from .models import Secret, User
user_db.create_tables([User, Secret])
