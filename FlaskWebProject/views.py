from FlaskWebProject import app

@app.route('/')
def home():
    return "App is working 🎉"
