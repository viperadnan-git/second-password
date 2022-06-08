from flask_login import UserMixin
from peewee import *

from . import user_db


class User(Model, UserMixin):
    user_id = TextField(primary_key=True)
    name = TextField()
    username = TextField()
    email = TextField()
    password = TextField()

    def get_id(self):
        return self.user_id

    class Meta():
        database = user_db


class Secret(Model):
    secret_id = TextField(primary_key=True)
    username = TextField()
    name = TextField()
    secret = TextField()

    class Meta():
        database = user_db
