from app.models.auth import User
from . import web
from app.models.base import db
from flask import render_template
from flask import render_template, request, redirect, url_for, flash
from app.form.auth import RegisterForm,LoginForm

# 登录用
from flask_login import login_user, login_required


@web.route('/register',methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method=='POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        # redirect 需要endpoint
        return redirect(url_for('web.login'))
    return render_template('signup.html',form=form)

@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        # 比对密码
        if user and user.check_password(form.password.data):
            login_user(user,remember=True)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在或密码错误')
        pass
    return  render_template('index.html',form=form)


@web.route('/')
@login_required
def index():
    return 'success'

