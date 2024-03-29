from flask import render_template,url_for,flash,redirect,request,abort
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, AccountForm, PostForm
from flaskblog.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user #it is like request.user of Django

#for managing profile pic upload
import secrets
import os
from PIL import Image #to resize images for save up memory

@app.route('/')
@app.route('/home')
def home():
    # posts = Post.query.order_by(Post.date_posted.desc()).all() #need to change it for pagination
    page = request.args.get('page',default = 1, type = int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page = 4)

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




@app.route('/post/new', methods = ['GET','POST'])
@login_required
def new_post():
    title = "New Post"
    legend = 'New Post'
    form = PostForm()


    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created",'success')
        return redirect(url_for('home'))

    return render_template('create_post.html', title=title, form=form, legend=legend)

@app.route('/post/<int:post_id>')
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id) #if does not exits, return 404 error
    title = post.title
    return render_template('post.html', post = post, title=title)

@app.route('/post/<int:post_id>/update', methods = ['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    title = "Update Post"
    legend = 'Update Post'
    if post.author != current_user:
        abort(403)

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit() #we update the database, that is why we dont use db.session.add()
        flash('Your post has been updated!','success')
        return redirect(url_for('post',post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content


    return render_template('create_post.html', 
     title =title, form = form)

@app.route('/post/<int:post_id>/delete',methods = ['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!','success')
    return redirect(url_for('home'))

@app.route("/user/<string:username>")
def user_posts(username):
    # posts = Post.query.order_by(Post.date_posted.desc()).all() #need to change it for pagination
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page',default = 1, type = int)
    posts = Post.query.filter_by(author = user)\
                .order_by(Post.date_posted.desc())\
                .paginate(page = page, per_page = 4)

    return render_template('user_posts.html', posts = posts, user=user)