from os import environ
from uuid import uuid4
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get("SECRET_KEY", str(uuid4()))
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'

from .routes import add, dashboard, delete, home, login, register