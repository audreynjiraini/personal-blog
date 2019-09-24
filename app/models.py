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
    username = db.Column(db.String(255), unique = True, nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False)
    password_hash = db.Column(db.String(255), nullable = False)
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    # comments = db.relationship('Comment', backref = 'comments', lazy = 'dynamic')
    # blogs = db.relationship('Blog', backref = 'blogs', lazy = 'dynamic')
    
    
    @property
    def password(self):
        raise AttributeError('You do not have permission to view password attribute')
    
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def save_user(self):
        db.session.add(self)
        db.session.commit()


    def  __repr__(self):
        return f'User("{self.username}", "{self.email}", "{self.image_file}")'
    
    
 
 
class Blog(db.Model):
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer, primary_key = True)
    post_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    body = db.Column(db.String)
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    # category = db.Column(db.String)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # comments = db.relationship('Comments', backref='comments1', lazy='dynamic')


    def save_blog(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.filter_by(post_id = id).all()
        return blogs
    
    
    def __repr__(self):
        return f'Blog: {self.body}'



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    posted = db.Column(db.DateTime, default = datetime.utcnow) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
        
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f'Comment: {self.comment}'
    
    
    
class Subscriber(db.Model):
    __tablename__='subscribers'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()