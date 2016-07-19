from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())


@app.route('/abc')
def abc():
    return '<h1>Bad Request</h1>', 400


@app.route('/user/<name>')
def user(name):
    users = ('a', 'b')
    return render_template('user.html', name=name, comments=users)


@app.route('/buser/<name>')
def buser(name):
    return render_template('user_bootstrap.html', name=name, current_time=datetime.utcnow())


@app.route('/a')
def a():
    return render_template('base.html')


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
