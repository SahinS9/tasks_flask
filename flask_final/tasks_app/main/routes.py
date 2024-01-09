from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/main')
def main():
    pass

@main.route('/about')
