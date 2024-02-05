from flask import render_template,url_for,flash,redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, AccountForm
from flaskblog.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user #it is like request.user of Django

#for managing profile pic upload
import secrets
import os
from PIL import Image #to resize images for save up memory

@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.all()
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


#utils
def save_picture(form_picture):
    random_hex = secrets.token_hex(8) #create random (distinct) name for pics
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn


@app.route('/account', methods = ['GET','POST'])
@login_required
def account():
    image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
    form = AccountForm()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        
        db.session.commit()
        flash('user info has been updated', 'success')
        return redirect(url_for('account'))

    #this is for autofill of the userinfo on this page
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', 
                            image_file=image_file, form = form)