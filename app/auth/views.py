from flask import Flask, render_template, redirect, url_for, flash, request
from .forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from flask_login import LoginManager, login_required, login_user, logout_user
from . import auth
from ..models import User
from .. import db
from ..email import mail_message


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to this blog","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', title = 'Register', registration_form = form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.home'))

        flash('Invalid username or Password')

    title = "Log In"
    return render_template('auth/login.html',login_form = form,title = title)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
