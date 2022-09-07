from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from project import os, db, mail
from project.models import User, Location
from project.forms import SignInForm, RegistrationForm
from flask_mail import Message
from project import bcrypt

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates/users')


@users_blueprint.route('/send/<userMail>/<newsletter>', methods=['GET', 'POST'])
def sendMail(userMail, newsletter):
    content = 'Hello and welcome to ZTravel website. We hope you will enjoy your stay here!'
    if newsletter == 'True':
        content = content + '<br><br><br>' + '<i>You have also successfully subscribed to our newsletter!<i>'

    msg = Message('Welcome to ZTravel!', recipients=[userMail])
    msg.html = content

    try:
        mail.send(msg)
    except Exception as e:
        print(e)
    return redirect(url_for('index'))


@users_blueprint.route('/favorite/<locationId>')
def favorite(locationId):
    user = User.query.filter_by(email=session.get('email')).first()
    location = Location.query.get(int(locationId))
    user.favorites.append(location)
    db.session.commit()

    favorites = []
    for location in user.favorites:
        favorites.append(location.id)

    session['favorites'] = favorites

    return redirect(request.referrer)


@users_blueprint.route('/unfavorite/<locationId>')
def unfavorite(locationId):
    user = User.query.filter_by(email=session.get('email')).first()
    location = Location.query.get(int(locationId))
    user.favorites.remove(location)
    db.session.commit()

    favorites = []
    for location in user.favorites:
        favorites.append(location.id)

    session['favorites'] = favorites

    return redirect(request.referrer)


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

            favorites = []
            for location in user.favorites:
                favorites.append(location.id)

            session['favorites'] = favorites
            session['email'] = email
            return redirect(url_for('index'))

        flash(f'Invalid email or password!', 'danger')
        return redirect(url_for('users.sign_in'))

    return render_template('sign_in.html', email=session.get('email'), form=signInForm)


@users_blueprint.route('/sign_out')
def sign_out():
    session['email'] = None
    session['favorites'] = None

    return redirect(request.referrer)


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    registrationForm = RegistrationForm()

    if registrationForm.validate_on_submit():

        email = registrationForm.email.data
        password = registrationForm.password.data
        newsletter = registrationForm.newsletter.data

        newUser = User(email=email, password=password, newsletter=newsletter)

        if User.query.filter_by(email=email).first():
            flash(f'User with that email already exists!', 'danger')
            return redirect(url_for('users.register'))
        else:
            flash(f'Successfully registered as {email}', 'success')
            session['email'] = email
            session['favorites'] = []
            db.session.add(newUser)
            db.session.commit()

            return redirect(url_for('users.sendMail', userMail=email, newsletter=newsletter))
            # return redirect(url_for('index'))

    return render_template('register.html', email=session.get('email'), form=registrationForm)
