import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

app = Flask("app")

from app.config import config

config_name = os.getenv('FLASK_CONFIG', 'development')
app.config.from_object(config[config_name])
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
moment = Moment(app)

from app import views, errors, commands