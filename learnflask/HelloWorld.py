import os
from flask import Flask, render_template, session, redirect, url_for, flash
from datetime import datetime
from flask_script import Manager, Shell, Server
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField, validators
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from threading import Thread

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 邮件发送配置
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = os.environ.get('MAIL_USERNAME')
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)
manager.add_command("runserver", Server(use_debugger=True))


# form表单
class NameForm(Form):
    name = StringField('What is your name?', validators=[validators.data_required()])
    submit = SubmitField('Submit')


# 数据库表Role
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


# 数据库表User
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


# shell添加数据库
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_context))


# 发送邮件
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


# 异步发送邮件
def send_async_email(mailapp, msg):
    with mailapp.app_context():
        mail.send(msg)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


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


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        # 提交
        # 获取输入的用户名
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('form'))
    return render_template('form.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
