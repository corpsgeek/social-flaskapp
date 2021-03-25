from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, length


# create user registration form
class RegistrationForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


# create login form
class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
