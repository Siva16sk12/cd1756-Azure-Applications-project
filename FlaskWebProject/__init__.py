"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Optional logging (safe default)
logging.basicConfig(level=logging.INFO)

# Import routes
import FlaskWebProject.views
