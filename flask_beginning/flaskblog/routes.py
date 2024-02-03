from flask import render_template,url_for,flash,redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user #it is like request.user of Django


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
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    context = {
        'title':'About'
    }
    return render_template('about.html', context = context)






@app.route('/register', methods = ['GET','POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()
    title = 'Register'

    if request.method == 'POST':
        print(form.errors)

    if form.validate_on_submit():

        

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)

        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.username.data}. Now you can log in!', 'success')
        return redirect(url_for('login'))




    # context = {
    #     'form': form,
    #     'title' : title
    # }
    return render_template('register.html', form = form, title = title)





@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()
    title = 'Login'

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        password = bcrypt.check_password_hash(user.password, form.password.data)
        if user and password:
            login_user(user, remember = form.remember.data)


            next_page = request.args.get('next') #if user redirected to login, will continue from that page NOT from home
            
            flash(f'Welcome {user.username}!', 'success')
            
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful! Check email or password', 'danger')


    return render_template('login.html', form = form, title = title)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title = 'Account')