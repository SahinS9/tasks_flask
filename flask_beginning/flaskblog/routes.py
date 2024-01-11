from flask import render_template,url_for,flash,redirect, request
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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