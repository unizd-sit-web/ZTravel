from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

from project.locations.views import locations_blueprint

app.register_blueprint(locations_blueprint, url_prefix='/locations')
