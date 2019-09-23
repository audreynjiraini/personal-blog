from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, SelectField, ValidationError
from wtforms.validators import Required, Email
from ..models import User


class BlogForm(FlaskForm):
    
    title = StringField('Blog title', validators=[Required()])
    body = TextAreaField('Blog post', validators=[Required()])
    submit = SubmitField('Submit')
    
    
    
class CommentForm(FlaskForm):
    
    comment = StringField('Your comment:', validators=[Required()])
    submit = SubmitField('Submit')