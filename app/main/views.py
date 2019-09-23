from flask import Flask, render_template, redirect, url_for, flash, abort
from .forms import BlogForm, CommentForm
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from . import main
from ..models import User, Blog, Comment, Subscriber
from flask_login import login_required, current_user
from ..email import mail_message


posts = [
    {
        'author': 'Audrey Njiraini',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 21, 2019'
    },
    {
        'author': 'Kendall Njiraini',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 22, 2019'
    }
]



@main.route('/',methods=['GET','POST'])
@main.route('/home',methods=['GET','POST'])
def home():
    
    blogs = Blog.query.all()
        
    title = "Welcome to My Blog"

    return render_template('index.html', posts = blogs)


@main.route('/user/<uname>')
@login_required
def profile():
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user)


@main.route('/new_blog', methods=['GET','POST'])
@login_required
def new_post():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category = form.category.data
        new_post=Post(title=title,content=content,category=category)

        new_post.save_post()

    title="Make a blog post"
    return render_template('new_blog.html',title=title,blog_form=form)


@main.route("/post/<int:id>",methods=['GET','POST'])
def blog(id):
    blog = Blog.query.get_or_404(id)
    comment = Comment.query.all()
    form = CommentForm()

    if request.args.get("like"):
        post.like = post.like+1

        db.session.add(post)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id = blog.id))

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(id=id,comment=comment,user_id=current_user.id,blog_id=blog.id)

        new_comment.save_comment()

        return redirect("/blog/{blog_id}".format(blog_id = blog.id))

    return render_template('post.html',blog = blog,comments = comment,comment_form = form)