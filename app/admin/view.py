import os
import random
import flask_admin as admin
from flask_admin import expose
from flask import render_template, request, redirect, url_for, flash, current_app, Response
from wtforms import TextAreaField
from flask_login import current_user, login_user, login_required
from flask_admin.contrib import sqla
from werkzeug.utils import secure_filename
import flask_login as login
from app.form.auth import LoginForm
from app.models.auth import User
import datetime
import json

from app.web import web

bpdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app')

ALLOWED_file_EXTENSIONS = set(['md', 'MD', 'word', 'txt', 'py', 'java', 'c', 'c++', 'xlsx'])
ALLOWED_photo_EXTENSIONS = set(['png', 'jpg', 'xls', 'JPG', 'PNG', 'gif', 'GIF','jpeg'])
imageUpload:True


def random_str(randomlength=5):
    _str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    for i in range(randomlength):
        _str += chars[random.randint(0, length)]
    return _str


def allowed_photo(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_photo_EXTENSIONS


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_file_EXTENSIONS


def format_datetime(self, request, obj, fieldname, *args, **kwargs):
    return getattr(obj, fieldname).strftime("%Y-%m-%d %H:%M")




class MyView(admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=True)
            else:
                flash('账号不存在或密码错误')
        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        # self._template_args['link'] = link
        return super(MyView, self).index()


    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


class UserAdmin(sqla.ModelView):
    column_list = ('nick_name', 'email', 'phone_number')
    form_overrides = dict(about_me=TextAreaField)
    column_searchable_list = ('email', 'nick_name')
    column_labels = dict(
        email=('邮箱'),
        nick_name=('用户名'),
        phone_number=('电话'),
    )
    # 判断后面是否显示
    def is_accessible(self):
        return current_user.is_authenticated

class ArticleAdmin(sqla.ModelView):
    create_template = "admin/model/a_create.html"
    edit_template = "admin/model/a_edit.html"

    #
    column_list = ('title', 'summary', 'create_time','content')

    #
    column_searchable_list = ('title',)
    #
    form_create_rules = (
        'title', 'summary', 'content'
    )

    form_edit_rules = form_create_rules
    form_overrides = dict(
        summary=TextAreaField)
    column_labels = dict(
        title=('标题'),
        content=('正文'),
        summary=('简介'),
        create_time=('创建时间'),
    )
    form_widget_args = {
        'title': {'style': 'width:480px;'},
        'summary': {'style': 'width:680px; height:80px;'},
    }
    @expose('/editor_pic', methods=["POST"])
    def editor_pic(self):
        image_file = request.files.get('editormd-image-file')
        if image_file and allowed_photo(image_file.filename):
            filename = secure_filename(image_file.filename)
            filename = str(datetime.date.today()) + '-' + random_str() + '-' + filename
            image_file.save(os.path.join(current_app.config['SAVEPIC'],filename))
            # image_file.save('app/admin/article/edit/'+filename)
            data = {
                'success': 1,
                'message': '图片上传成功',
                # 所有问题都是在这 url_for image 没有找到
                'url': url_for('web.image',name =filename)
            }
        else:
            data = {
                'success': 0,
                'message': u'没有获得图片或图片类型不支',
                'url': ""
            }
        return json.dumps(data)


    # 如果之后前台显示不了图片 可能是这处理有问题@expose('/image/<name>')
    @web.route('/image/<name>')
    def image(name):
        with open(os.path.join(current_app.config['SAVEPIC'],name), 'rb') as f:
        # with open('app/admin/article/edit/'+name ,'rb') as f:
            resp = Response(f.read(), mimetype="image/jpeg")
        return resp
    def is_accessible(self):
        return current_user.is_authenticated


