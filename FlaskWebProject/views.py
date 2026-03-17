"""
Routes for the Flask application.
"""

from FlaskWebProject import app


# Home route
@app.route("/")
def home():
    return "App is working 🎉"


# Test route (optional but useful)
@app.route("/test")
def test():
    return "Test route working ✅"

