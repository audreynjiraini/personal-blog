from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, SelectField, ValidationError
from wtforms.validators import Required, Email, EqualTo, Length
from ..models import User, Subscriber


class BlogForm(FlaskForm):
    
    title = StringField('Blog title', validators=[Required()])
    body = TextAreaField('Blog post', validators=[Required()])
    submit = SubmitField('Submit')
    
    
    
class CommentForm(FlaskForm):
    
    name = StringField('Your name', validators = [Required(), Length(min = 3, max = 20)])
    comment = StringField('Your comment:', validators=[Required()])
    submit = SubmitField('Submit')
    
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
    
    
class SubscriberForm(FlaskForm):
    name  = StringField('Your name', validators = [Required()])
    email = StringField('Your email address', validators = [Required(), Email()])
    submit = SubmitField('Subscribe')