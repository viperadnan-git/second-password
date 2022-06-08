from flask import flash, redirect, render_template, url_for
from flask_login import login_user, logout_user, current_user
from web import app, bcrypt, login_manager
from web.database import User
from web.routes.forms import LoginForm


@login_manager.user_loader
def load_user(user_id):
    return User.get_or_none(User.user_id == user_id)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_page'))
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.get_or_none(User.username == form.username.data)
        if attempted_user and bcrypt.check_password_hash(attempted_user.password, form.password.data):
            login_user(attempted_user, remember=(
                True if form.remember.data else False))
            flash(
                f'Success! You are logged in as: {attempted_user.name}', category='success')
            return redirect(url_for('dashboard_page'))
        else:
            flash(f'Username or password is incorrect! Please try again.',
                  category='danger')
    if form.errors:
        error = ""
        for key, err in form.errors.items():
            error += key + ": " + str(err[0]) + "<br>"
        flash(error, category="danger")
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
def logout_page():
    logout_user()
    flash(f'You have been logged out!', category='info')
    return redirect(url_for('home_page'))
