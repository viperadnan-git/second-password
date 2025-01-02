from flask_login import UserMixin
from peewee import *
from uuid import uuid4
from . import user_db


class User(Model, UserMixin):
    user_id = UUIDField(primary_key=True, default=uuid4)
    name = TextField()
    username = TextField()
    email = TextField()
    password = TextField()

    def get_id(self):
        return self.user_id

    class Meta:
        database = user_db


class Secret(Model):
    secret_id = UUIDField(primary_key=True, default=uuid4)
    username = TextField()
    name = TextField()
    secret = TextField()

    class Meta:
        database = user_db
