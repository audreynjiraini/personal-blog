from flask import Flask, render_template, redirect, url_for, flash, abort, request
from .forms import BlogForm, CommentForm, UpdateProfile
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from . import main
from ..models import User, Blog, Comment, Subscriber
from flask_login import login_required, current_user
from ..email import mail_message
from ..request import get_quote
from .. import db, photos
import markdown2


# posts = [
#     {
#         'author': 'Audrey Njiraini',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'September 21, 2019'
#     },
#     {
#         'author': 'Kendall Njiraini',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'September 22, 2019'
#     }
# ]



@main.route('/',methods=['GET','POST'])
@main.route('/home',methods=['GET','POST'])
def home():
    
    blogs = Blog.query.all()
        
    title = "Welcome to My Blog"
    
    name  = "Quote"
    
    quote = get_quote()

    return render_template('index.html', blogs = blogs[::-1], name = name,quote = quote)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
    
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))
    
    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/new_blog', methods=['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        new_blog = Blog(title = title,body = body)

        new_blog.save_blog()

    title="Make a blog post"
    return render_template('new_blog.html',title=title,blog_form=form)


@main.route("/blog/<int:id>",methods=['GET','POST'])
def blog(id):
    blog = Blog.query.get_or_404(id)
    comment = Comment.query.all()
    form = CommentForm()

    if request.args.get("like"):
        blog.like = blog.like+1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id = blog.id))

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(id = id,comment = comment,user_id = current_user.id,blog_id = blog.id)

        new_comment.save_comment()

        return redirect("/blog/{blog_id}".format(blog_id = blog.id))

    return render_template('blog.html',blog = blog,comments = comment,comment_form = form)


# @main.route("/blog/<int:id>/update",methods=['GET','POST'])
# @login_required
# def update_blog(id):
#        blog = Blog.query.get_or_404(id)
       
#        form = BlogForm()
#        if form.validate_on_submit():
#            blog.title = form.title.data
#            blog.content = form.body.data
           
#            db.session.commit()
           
#            flash('Blog updated', 'success')
#            return redirect(url_for('main.blog', blog_id=blog.id))
#        elif  request.method == 'GET':
#            form.title.data = blog.title
#            form.body.data = blog.body
#        return render_template('new_blog.html', title='Update Blog', form = form, legend = 'Update Blog')