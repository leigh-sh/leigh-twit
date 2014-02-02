from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

twit = Flask(__name__)
twit.config.from_object('config')
db = SQLAlchemy(app) 

from twit import views, models

