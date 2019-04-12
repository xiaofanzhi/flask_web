from app.models.auth import User
from . import web
from app.models.base import db
from flask import render_template
from flask import render_template, request, redirect, url_for, flash
from app.form.auth import RegisterForm


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
    return 'adasdasd'