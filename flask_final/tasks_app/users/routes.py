from flask import Blueprint

users = Blueprint('users',__name__)


@users.route('/register')

@users.route('/login')

@users.route('/logout')

@users.route('/account', methods = [])

@users.route('/user/<string:username>')
def user_posts(username):
    pass

@users.route('/reset_password/<token>', methods = [])


