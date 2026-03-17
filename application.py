"""
Entry point for running the FlaskWebProject app on Azure.
"""

from FlaskWebProject import app

# Required for Azure / gunicorn
if __name__ == "__main__":
    app.run()
