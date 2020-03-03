from flask_wtf import FlaskForm
from wtforms import TextField, Password

class LoginForm(FlaskForm):
    username = TextField('username')
    password = PasswordField('password')