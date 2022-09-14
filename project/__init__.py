import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

# Sprema path od radnog direktorija
basedir = os.path.abspath(os.path.dirname(__file__))

# Spaja Flask App s Database-om
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SendGrid setup
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'

# TODO Potrebno postaviti svoj SENDGRID_API_KEY u Environment Variables
app.config['MAIL_PASSWORD'] = os.environ.get('SENDGRID_API_KEY')
# TODO Potrebno unijeti vlastiti Sendgrid email account
app.config['MAIL_DEFAULT_SENDER'] = 'ivor.grego@gmail.com'

mail = Mail(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from project.users.views import users_blueprint
from project.locations.views import locations_blueprint

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(locations_blueprint, url_prefix='/locations')
