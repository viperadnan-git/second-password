import re

import pyotp
from flask_wtf import FlaskForm
from web.database import User
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import (DataRequired, Email, EqualTo, Length,
                                ValidationError)


class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[
                           Length(min=2, max=30), DataRequired()])
    password = PasswordField(label="Password:", validators=[
                             Length(min=5), DataRequired()])
    remember = BooleanField(label="Remember me:")
    submit = SubmitField(label="Sign in")


class RegisterForm(FlaskForm):
    name = StringField(label="Full Name:", validators=[
                       Length(min=3, max=16), DataRequired()])
    username = StringField(label='Username:', validators=[
                           Length(min=4, max=16), DataRequired()])
    email = StringField(label='Email Address:', validators=[
                        Email(), DataRequired()])
    password1 = PasswordField(label="Password:", validators=[
                              Length(min=8), DataRequired()])
    password2 = PasswordField(label="Confirm Password:",  validators=[
                              EqualTo(fieldname='password1'), DataRequired()])
    submit = SubmitField(label="Create Account")

    # validate_<fieldname>
    def validate_username(self, username):
        user = User.get_or_none(User.username == username.data)
        if user:
            raise ValidationError(
                'Username already exist! Please try a different username.')

    def validate_email(self, email):
        email = User.get_or_none(User.email == email.data)
        if email:
            raise ValidationError(
                'Email address already exist! Please try a different email addres.')


class SecretForm(FlaskForm):
    name = StringField(label="Name:", validators=[
                       Length(min=3, max=16), DataRequired()])
    secret = StringField(label="Secret:", validators=[DataRequired()])

    def validate_secret(self, secret: StringField):
        try:
            secret = re.sub('[\s+]', '', secret.data)
            pyotp.TOTP(str(secret)).now()
        except Exception as err:
            raise ValidationError(err)


class DeleteForm(FlaskForm):
    name = StringField(label="Name:", validators=[
                       Length(min=3, max=16), DataRequired()])
    secret_id = StringField(label="Secret:", validators=[
                            Length(min=36, max=36), DataRequired()])
    delete = BooleanField(label="Delete:")
