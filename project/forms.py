from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class SignInForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired('Please enter your email address.'),
                                              Email('Invalid email format'), Length(min=3, max=100)])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=6, max=60)])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired('Please enter your email address.'),
                                              Email('Invalid email format')])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=6, max=60)])
    confirmPassword = PasswordField('Confirm Password:', validators=[DataRequired(), Length(min=6, max=60),
                                                                     EqualTo('password',
                                                                             message='Passwords must match')])
    newsletter = BooleanField("Subscribe to newsletter")
    submit = SubmitField('Register')
