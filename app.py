from flask import Flask, render_template
from markupsafe import escape  #for specific page for each user %filtering%

import sqlalchemy
# from flask import HTTPRequest

app = Flask(__name__)

username = 'Shahin'


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/main')
def main_page():
    context = {'username':username}
    return render_template('main.html', context = context)







if __name__ == '__main__':
    app.run(debug = True)
    