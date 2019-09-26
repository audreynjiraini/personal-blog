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
    username = db.Column(db.String(255), index = True, nullable = False)
    email = db.Column(db.String(255), unique = True, nullable = False, index = True)
    password_hash = db.Column(db.String(255), nullable = False)
    profile_pic_path = db.Column(db.String)
    bio = db.Column(db.String(255))
    
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    blogs = db.relationship('Blog', backref = 'user', lazy = 'dynamic')
    
    
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
        return f'User("{self.username}", "{self.email}")'
    
    
 
 
class Blog(db.Model):
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer, primary_key = True)
    # blog_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    body = db.Column(db.String)
    posted = db.Column(db.DateTime,default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    comments = db.relationship('Comment', backref='blog_id', lazy='dynamic')


    def save_blog(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.filter_by(id = id).all()
        return blogs
    
    
    @classmethod
    def get_blog(cls,id):
        blog = Blog.query.filter_by(id = id).first()

        return blog
    
    
    @classmethod    
    def delete_blog(cls, id):
        blog = Blog.query.filter_by(id = id).first()
        db.session.delete(blog)
        db.session.commit()
    
    
    def __repr__(self):
        return f'Blog: {self.title}, {self.body}'



class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)
    # posted = db.Column(db.DateTime, default = datetime.utcnow) 
    name = db.Column(db.String)
    blog = db.Column(db.Integer,db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
        
    @classmethod
    def get_comments(cls,blog):
        comments = Comment.query.filter_by(blog_id = blog).all()
        return comments
        
    
    @classmethod    
    def delete_comment(cls, id):
        comment = Comment.query.filter_by(id = id).first()
        db.session.delete(comment)
        db.session.commit()


    def __repr__(self):
        return f'Comment: {self.comment}'
    
    
    
class Subscriber(db.Model):
    __tablename__='subscribers'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String(255),unique = True)

    # def save_subscriber(self):
    #     db.session.add(self)
    #     db.session.commit()
        
        
        
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'