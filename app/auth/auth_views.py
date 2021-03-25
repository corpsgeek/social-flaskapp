from app.auth.auth_forms import RegistrationForm, LoginForm
from app.auth import auth
from flask import render_template, url_for


@auth.route('/register')
def register():
    form = RegistrationForm()
    return render_template('auth/register.html', form=form)
