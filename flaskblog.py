from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '6f3d54ebc6ed040fdb08b8254d5c833e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    
    
    def  __repr__(self):
        return f'User("{self.username}", "{self.email}", "{self.image_file}")'
    

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        
        return redirect(url_for('home'))
    
    return render_template('register.html', title = 'Register', form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            
            return redirect(url_for('home'))
        
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    
    return render_template('login.html', title = 'Login', form = form)



if __name__ == "__main__":
    app.run(debug=True)