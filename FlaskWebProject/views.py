from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from FlaskWebProject import app, db
from FlaskWebProject.models import User, Post
from FlaskWebProject.forms import LoginForm, PostForm
import requests
import urllib.parse

# ---------------- HOME ----------------

@app.route('/')
@app.route('/home')
@login_required
def home():
posts = Post.query.all()
return render_template("index.html", posts=posts)

# ---------------- LOGIN ----------------

@app.route('/login', methods=['GET', 'POST'])
def login():

```
form = LoginForm()

if form.validate_on_submit():

    user = User.query.filter_by(username=form.username.data).first()

    if user and user.check_password(form.password.data):

        print("SUCCESSFUL LOGIN:", form.username.data)

        login_user(user)

        return redirect(url_for('home'))

    else:

        print("FAILED LOGIN ATTEMPT:", form.username.data)

        flash("Invalid username or password")

return render_template("login.html", form=form)
```

# ---------------- LOGOUT ----------------

@app.route('/logout')
@login_required
def logout():

```
logout_user()

print("USER LOGGED OUT")

return redirect(url_for('login'))
```

# ---------------- CREATE POST ----------------

@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():

```
form = PostForm()

if form.validate_on_submit():

    post = Post()

    post.save_changes(
        form,
        request.files.get("image"),
        1,
        True
    )

    print("POST CREATED")

    return redirect(url_for("home"))

return render_template("post.html", form=form)
```

# ---------------- EDIT POST ----------------

@app.route('/post/<id>', methods=['GET', 'POST'])
@login_required
def post(id):

```
post = Post.query.get(id)

form = PostForm(obj=post)

if form.validate_on_submit():

    post.save_changes(
        form,
        request.files.get("image"),
        1
    )

    print("POST UPDATED:", id)

    return redirect(url_for("home"))

return render_template("post.html", form=form)
```

# ---------------- MICROSOFT LOGIN ----------------

@app.route("/login_microsoft")
def login_microsoft():

```
tenant = app.config["AZURE_TENANT_ID"]
client_id = app.config["AZURE_CLIENT_ID"]
redirect_uri = app.config["AZURE_REDIRECT_URI"]

redirect_uri = urllib.parse.quote(redirect_uri)

auth_url = (
    f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize"
    f"?client_id={client_id}"
    f"&response_type=code"
    f"&redirect_uri={redirect_uri}"
    f"&response_mode=query"
    f"&scope=User.Read"
    f"&state=12345"
)

print("REDIRECTING TO MICROSOFT LOGIN")

return redirect(auth_url)
```

# ---------------- MICROSOFT CALLBACK ----------------

@app.route("/auth")
def auth():

```
code = request.args.get("code")

tenant = app.config["AZURE_TENANT_ID"]

token_url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"

data = {
    "client_id": app.config["AZURE_CLIENT_ID"],
    "client_secret": app.config["AZURE_CLIENT_SECRET"],
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": app.config["AZURE_REDIRECT_URI"],
    "scope": "User.Read"
}

token = requests.post(token_url, data=data).json()

access_token = token["access_token"]

headers = {"Authorization": f"Bearer {access_token}"}

user_data = requests.get(
    "https://graph.microsoft.com/v1.0/me",
    headers=headers
).json()

username = user_data.get("displayName", "MicrosoftUser")

user = User.query.filter_by(username=username).first()

if not user:

    user = User(username=username)
    user.set_password("microsoft_login")

    db.session.add(user)
    db.session.commit()

    print("NEW MICROSOFT USER CREATED:", username)

login_user(user)

print("MICROSOFT LOGIN SUCCESS:", username)

return redirect(url_for("home"))
```

