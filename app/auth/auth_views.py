from app.auth.auth_forms import RegistrationForm, LoginForm
from app.auth import auth
from flask import render_template, url_for, redirect
from app.models import User, db
from app.main import main

# import password encryption tool
from werkzeug.security import generate_password_hash


@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    # validate the form data before submitting
    if form.validate_on_submit():
        encrypted_password = generate_password_hash(form.password.data, method='pbkdf2:sha1', salt_length=8)

        # add the user data to db
        new_user = User(username=form.username.data, email=form.email.data, password_enc = form.password.data)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('auth/register.html', form=form)
