"""
The flask application package.
"""

import logging
from flask import Flask

# Create Flask app
app = Flask(__name__)

# Basic logging (safe for Azure)
logging.basicConfig(level=logging.INFO)

# Import routes (VERY IMPORTANT)
import FlaskWebProject.views
