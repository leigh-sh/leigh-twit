from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

twit = Flask(__name__)
twit.config.from_object('config')
db = SQLAlchemy(twit) 
login_manager = LoginManager()
login_manager.init_app(twit)
login_manager.login_view = 'login'

from twit import views, models

