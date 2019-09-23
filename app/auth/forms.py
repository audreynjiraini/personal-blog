from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Required, Length, Email, EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(min=2, max=20)])
    
    email = StringField('Email', validators=[Required(), Email()])
    
    password = PasswordField('Password', validators=[Required()])
    
    confirm_password = PasswordField('Confirm Password', validators=[Required(), EqualTo('password')])
    
    submit = SubmitField('Sign Up')
    
    # def validate_email(self, data_field):
    #     if User.query.filter_by(email = data_field.data).first():
    #         raise ValidationError('An account with that email already exists')
        
        
    # def validate_username(self, data_field):
    #     if User.query.filter_by(username = data_field.data).first():
    #         raise ValidationError('That username is taken')
    
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email()])
    
    password = PasswordField('Password', validators=[Required()])
    
    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Log In')