from flask import Flask 

from tasks_app.main.routes import main
from tasks_app.users.routes import users
from tasks_app.tasks.routes import tasks





app = Flask(__name__)

if __name__ == '__main__':
    app.run()

