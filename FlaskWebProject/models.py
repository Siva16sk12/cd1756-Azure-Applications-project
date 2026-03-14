from FlaskWebProject import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):

```
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(64), unique=True, nullable=False)
password = db.Column(db.String(128), nullable=False)

posts = db.relationship('Post', backref='author', lazy=True)

def set_password(self, password):
    self.password = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password, password)
```

class Post(db.Model):

```
id = db.Column(db.Integer, primary_key=True)

title = db.Column(db.String(150))
author = db.Column(db.String(100))
content = db.Column(db.Text)

image_path = db.Column(db.String(200))

def save_changes(self, form, image, user_id, new=True):

    self.title = form.title.data
    self.author = form.author.data
    self.content = form.content.data

    if image:
        filename = image.filename
        image.save("FlaskWebProject/static/" + filename)
        self.image_path = filename

    if new:
        db.session.add(self)

    db.session.commit()
```

