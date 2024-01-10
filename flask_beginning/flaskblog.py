from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4d25c03a2652dbba3ed90d04b40004bc'

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






@app.route('/register')
def register():
    form = RegistrationForm()
    title = 'Register'


    context = {
        'form': form,
        'title' : title
    }
    return render_template('register.html', context = context)





@app.route('/login')
def login():
    form = LoginForm()
    title = 'Login'


    context = {
        'form': form,
        'title' : title
    }
    return render_template('login.html', context = context)

@app.route('/logout')
def logout():
    return "HELE qoshmamushuq"
























if __name__ == '__main__':
    app.run(debug = True)
