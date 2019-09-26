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
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        body = blog_form.body.data
        
        new_blog = Blog(title = title, body = body, user = current_user)
        new_blog.save_blog()
        
    title="Make a blog post"
    return render_template('new_blog.html',title=title, blog_form = blog_form)
    


@main.route("/blog/<int:id>",methods=['GET','POST'])
def blog(id):
    blog = Blog.get_blog(id)
    posted_date = blog.posted.strftime('%b %d, %Y')
    comment = Comment.query.all()
    
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        name = comment_form.name.data
        comment = comment_form.comment.data
        
        new_comment = Comment(id = id, name = name, comment = comment,user_id = current_user.id,blog_id = blog)

        new_comment.save_comment()

        # return redirect("/blog/{blog_id}".format(blog_id = blog.id))

    return render_template('blog.html',blog = blog,comments = comment,comment_form = comment_form, date = posted_date, blog_id =  blog)


# @main.route('/blog/delete/<int:id>', methods = ['GET', 'POST'])
# @login_required
# def delete_blog(id):
#     blog = Blog.get_blog(id)
#     db.session.delete(blog)
#     db.session.commit()

#     return render_template('blog.html', id = id, blog = blog)


@main.route('/blog/comment/delete/<int:id>', methods = ['GET', 'POST'])
@login_required
def delete_comment(id):
    comment = Comment.query.filter_by(id = id).first()
    blog_id = comment.blog
    Comment.delete_comment(id)

    return redirect(url_for('main.blog',id = blog_id))


@main.route('/user/<uname>/blogs', methods = ['GET','POST'])
def user_blogs(uname):
    user = User.query.filter_by(username = uname).first()
    blogs = Blog.query.filter_by(user_id = user.id).all()

    return render_template('blog.html', user = user, blogs = blogs)


@main.route("/blog/<int:id>/update",methods=['GET','POST'])
@login_required
def update_blog(id):
       blog = Blog.get_blog(id)
       
       blog_form = BlogForm()
       if blog_form.validate_on_submit():
           blog.title = blog_form.title.data
           blog.body = blog_form.body.data
           
           db.session.commit()
           
           flash('Blog updated', 'success')
           return redirect(url_for('main.blog', id=id))
       elif  request.method == 'GET':
           blog_form.title.data = blog.title
           blog_form.body.data = blog.body
       return render_template('new_blog.html', title='Update Blog', blog_form = blog_form, id = id)