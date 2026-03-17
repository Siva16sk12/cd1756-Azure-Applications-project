from FlaskWebProject import app
from flask import render_template, redirect, url_for, request
from FlaskWebProject.models import Post
from FlaskWebProject import db

# Home route
@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


# Create new post
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('create.html')


# Delete post
@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('home'))

