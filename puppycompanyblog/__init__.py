# puppycompanyblog/__init__.py

# This file is going to hold a lot of our organizational logic, 
# connecting the blueprints, connecting the login manager and
# connecting everything together.
# Handle everything for app.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

#############################################
### DATABASE SETUP ##########################
#############################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

##################
# LOGIN CONFIGS
login_manager = LoginManager()

login_manager.init_app(app)

####################################

from puppycompanyblog.core.views import core
app.register_blueprint(core)
from puppycompanyblog.error_pages.handlers import error_pages
app.register_blueprint(error_pages)


