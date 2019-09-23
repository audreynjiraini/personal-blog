from flask import Flask, render_template, redirect, url_for, flash
from .forms import BlogForm, CommentForm
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from . import main


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



@main.route('/')
@main.route('/home')
def home():
    return render_template('index.html', posts = posts)


# @main.route('/about')
# def about():
#     return render_template('about.html', title = 'About')


