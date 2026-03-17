from FlaskWebProject import app, db
from flask import render_template, redirect, url_for, request, flash
from FlaskWebProject.models import Post
from flask_login import login_required, current_user


# Home page
@app.route('/')
def home():
    return "App is working 🎉"


# Create post
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        body = request.form.get('body')

        post = Post(
            title=title,
            author=author,
            body=body,
            user_id=current_user.id
        )

        db.session.add(post)
        db.session.commit()

        flash("Post created successfully!")
        return redirect(url_for('home'))

    return render_template('create.html')


# Delete post
@app.route('/delete/<int:id>')
@login_required
def delete(id):
    post = Post.query.get_or_404(id)

    if post.user_id != current_user.id:
        flash("Not authorized!")
        return redirect(url_for('home'))

    db.session.delete(post)
    db.session.commit()

    flash("Post deleted!")
    return redirect(url_for('home'))

