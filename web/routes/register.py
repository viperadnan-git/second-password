from uuid import uuid4

from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user

from web import app, bcrypt
from web.database import User
from web.routes.forms import RegisterForm


@app.route("/register", methods=["GET", "POST"])
def register_page():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard_page"))
    form = RegisterForm()
    if form.validate_on_submit():
        usert_to_create = User.create(
            user_id=str(uuid4()),
            name=form.name.data,
            username=form.username.data,
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password1.data).decode("utf-8"),
        )
        login_user(usert_to_create)
        flash(
            f"Account created successfully! You are now logged in as {usert_to_create.name}",
            category="success",
        )
        return redirect(url_for("dashboard_page"))
    if form.errors:
        error = ""
        for key, err in form.errors.items():
            error += key + ": " + str(err[0]) + "<br>"
        flash(error, category="danger")
    return render_template("register.html", form=form)
