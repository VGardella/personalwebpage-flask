# Create the app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# App configuration

#app.config.from_object('config.DevelopmentConfig')

# Import views and blueprints

from personalweb.views import base

app.register_blueprint(base)
