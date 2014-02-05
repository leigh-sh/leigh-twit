from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
import os
from config import basedir

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)  ## ORM

## user sessions handler
login_manager = LoginManager() 
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views, models