from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# from flaskblog import routes #this here still causes circular import, that is why it should be imported after app created

app = Flask(__name__)
app.config['SECRET_KEY'] = '4d25c03a2652dbba3ed90d04b40004bc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'site.db')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


#for creation of db in terminal run: app.app_context().push() after importing app
#then db.create_all() will work


from flaskblog import routes