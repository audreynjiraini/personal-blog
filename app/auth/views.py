from flask import Flask, render_template, redirect, url_for, flash
from .forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from . import auth


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        
        return redirect(url_for('main.home'))
    
    return render_template('auth/register.html', title = 'Register', registration_form = form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            
            return redirect(url_for('main.home'))
        
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    
    return render_template('auth/login.html', title = 'Login', login_form = form)




if __name__ == "__main__":
    app.run(debug=True)