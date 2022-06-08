from flask import flash, redirect, render_template, url_for
from flask_login import current_user
from flask_login.utils import login_required
from web import app
from web.database import Secret
from web.routes.forms import DeleteForm


def get_secret_data(secret_id, username):
    try:
        data = Secret.get_by_id(secret_id)
        if data.username == username:
            return dict(id=data.secret_id, name=data.name)
        raise ValueError("User doesn't have permission to delete this")
    except Secret.DoesNotExist:
        raise ValueError("Password doesn't exists!")


@app.route('/delete/<secret_id>', methods=["GET", "POST"])
@login_required
def delete_page(secret_id):
    form = DeleteForm()
    if form.validate_on_submit():
        if form.delete.data:
            try:
                Secret.delete_by_id(form.secret_id.data)
                flash(
                    f"Password '{form.name.data}' deleted successfully!", category="success")
            except Secret.DoesNotExist:
                flash(
                    f"Password '{form.name.data}' doesn't exists!", category="warning")
        return redirect(url_for("dashboard_page"))
    if form.errors:
        error = ""
        for key, err in form.errors.items():
            error += key + ": " + str(err[0]) + "<br>"
        flash(error, category="danger")
    try:
        return render_template('delete.html', data=get_secret_data(secret_id, current_user.username),  form=form)
    except ValueError as err:
        flash(str(err), category="danger")
        return redirect(url_for("dashboard_page"))
