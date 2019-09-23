from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


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



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)


@app.route('/about')
def about():
    return render_template('about.html', title = 'About')


