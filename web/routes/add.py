import re
from uuid import uuid4

from flask import flash, redirect, render_template, url_for
from flask_login import current_user
from flask_login.utils import login_required

from web import app
from web.database import Secret
from web.routes.forms import SecretForm


@app.route("/add", methods=["GET", "POST"])
@login_required
def add_page():
    form = SecretForm()
    if form.validate_on_submit():
        secret = re.sub("[\s+]", "", form.secret.data)
        Secret.create(
            secret_id=str(uuid4()),
            username=current_user.username,
            name=form.name.data,
            secret=secret,
        )
        flash(f"{form.name.data} added sucessfully !", category="success")
        return redirect(url_for("dashboard_page"))
    if form.errors:
        error = ""
        for key, err in form.errors.items():
            error += key + ": " + str(err[0]) + "<br>"
        flash(error, category="danger")
    return render_template("add.html", form=form)
