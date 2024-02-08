from tasks_app import app
from flask import render_template, redirect

from tasks_app.models import User, UserTask, TaskTag
from tasks_app.forms import RegistrationForm, LoginForm, TaskForm, TagForm


@app.route('/')
def home():
    title = 'Home Page'
    text = 'NEW PAGE'


    context = {'title':title,
                'text': text}

    return render_template('home.html', **context)


@app.route('/register')
def register():
    title = 'Registration'
    form = RegistrationForm()



    context = {'title':title,
                'form': form}
    return render_template('register.html', **context)

@app.route('/login')
def login():
    title = 'Login'

    context = {'title':title
                ,'form':form}
    return "Login Page"





@app.route('/logout', methods = ['POST'])
def logout():
    title = 'Logout'

    context = {'title':title
                ,'form':form}
    return "Logout Page"





@app.route('/account', methods = ['GET','POST'])
def account():
    title = 'Account'

    context = {'title':title
                ,'form':form}
    return "Account Page"







@app.route('/main', methods = ['GET','POST'])
def main():
    title = 'Main'
    form = TaskForm()
    context = {'title':title
                ,'form':form}
    return render_template('main.html', **context)

