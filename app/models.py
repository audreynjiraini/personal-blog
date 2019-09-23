from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comments', backref = 'comments', lazy = 'dynamic')
    blog = db.relationship('Blog', backref = 'blogs', lazy = 'dynamic')
    
    
    @property
    def password(self):
        raise AttributeError('You do not have permission to view password attribute')
    
    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)


    def save_user(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'User: {self.username}'
    
    
 
 
class Blog(db.Model):
    __tablename__ = 'blog'
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    body = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    category = db.Column(db.String)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    comments = db.relationship('Comments', backref='comments1', lazy='dynamic')


    def save_blog(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_blogs(cls, category):
        blogs = Blog.query.filter_by(category = category).all()
        return blogs
    
    
    def get_blog(cls, id):
        blog = Blog.query.filter_by(id = id).first()
        return blog
    
    
    @classmethod
    def count_blogs(cls, uname):
        user = User.query.filter_by(username = uname). first()
        blogs = Blog.query.filter_by(user_id = user.id).all()
        
        blogs_count = 0
        for blog in blogs:
            blogs_count += 1
            
        return blogs_count
    
    def get_comments(self):
        blog = Blog.query.filter_by(id = self.id).first()
        comments = Comments.query.filter_by(blog = blog.id)
        return comments
    
    
    def __repr__(self):
        return f'Blog: {self.body}'


   
# class Role(db.Model):
#       __tablename__ = 'roles'

#       id = db.Column(db.Integer, primary_key = True)
#       name = db.Column(db.String(255))
#       users = db.relationship('User', backref='role', lazy='dynamic')


#       def __repr__(self):
#         return f'User {self.name}'



class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime, default = datetime.utcnow)  
    blog = db.Column(db.Integer, db.ForeignKey('blog.id'))
    
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_comments(cls, blog):
        comments = Comments.query.filter_by(blog_id = blog).all()
        return comments


    def __repr__(self):
        return f'Comment: {self.comment}'