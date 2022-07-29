import pyotp
from flask import render_template
from flask_login import current_user
from flask_login.utils import login_required

from web import app
from web.database import Secret


def get_users_secrets(username: str):
    data = []
    selected_data = Secret.select().where(Secret.username == username)
    for secret in selected_data:
        data.append(
            dict(
                name=secret.name,
                password=pyotp.TOTP(secret.secret).now(),
                id=secret.secret_id,
            )
        )
    return data


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard_page():
    secrets = get_users_secrets(current_user.username)
    return render_template("dashboard.html", secrets=secrets)
