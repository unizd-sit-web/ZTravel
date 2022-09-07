from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from project import os, db
from project.models import User
from project.forms import SignInForm, RegistrationForm
from project import bcrypt

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates/users')

# SignIn & Registration VIEWS

@users_blueprint.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    signInForm = SignInForm()

    if signInForm.validate_on_submit():
        email = signInForm.email.data
        password = signInForm.password.data

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            flash(f'Succesfully signed in as {email}', 'success')



            session['email'] = email
            return redirect(url_for('index'))

        flash(f'Invalid email or password!', 'danger')
        return redirect(url_for('users.sign_in'))

    return render_template('sign_in.html', email=session.get('email'), form=signInForm)


@users_blueprint.route('/sign_out')
def sign_out():
    session['email'] = None

    return redirect(request.referrer)


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    registrationForm = RegistrationForm()

    if registrationForm.validate_on_submit():

        email = registrationForm.email.data
        password = registrationForm.password.data
        newUser = User(email=email, password=password)

        if User.query.filter_by(email=email).first():
            flash(f'User with that email already exists!', 'danger')
            return redirect(url_for('users.register'))
        else:
            flash(f'Successfully registered as {email}', 'success')
            session['email'] = email
            db.session.add(newUser)
            db.session.commit()

            return redirect(url_for('index', userMail=email))
            # return redirect(url_for('index'))

    return render_template('register.html', email=session.get('email'), form=registrationForm)
