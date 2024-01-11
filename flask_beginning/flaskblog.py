from flask import Flask, render_template, flash, redirect, url_for, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm

import os
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SECRET_KEY'] = '4d25c03a2652dbba3ed90d04b40004bc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref = 'author', lazy=True) #this is not column, this is just relationship! - can use post.author - will show User data!

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"





    



posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



@app.route('/')
@app.route('/home')
def home():
    context = {
        'posts':posts
    }
    return render_template('home.html', context = context)

@app.route('/about')
def about():
    context = {
        'title':'About'
    }
    return render_template('about.html', context = context)






@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    title = 'Register'

    if request.method == 'POST':
        print(form.errors)

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))




    # context = {
    #     'form': form,
    #     'title' : title
    # }
    return render_template('register.html', form = form, title = title)





@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    title = 'Login'

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect( url_for('home'))
        else:
            flash('Check email or password', 'danger')


    return render_template('login.html', form = form, title = title)

@app.route('/logout')
def logout():
    return "HELE qoshmamushuq"
























if __name__ == '__main__':
    app.run(debug = True)
