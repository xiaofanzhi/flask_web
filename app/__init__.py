
from flask import Flask
from app.models.base import db
from flask_login import LoginManager
from flask_babelex import Babel
from flask_migrate import Migrate, MigrateCommand

login_manager = LoginManager()


def creat_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    register_blueprint(app)
    # 数据库 插件
    db.init_app(app)
    db.create_all(app=app)
    migtate = Migrate(app,db)
    # migtate.add_command('db', MigrateCommand)


    # login 登录插件初始化
    login_manager.init_app(app)
    # 没登录，将其引导到登录页面
    login_manager.login_view = 'web.login'
    login_manager.login_message='请先登录'

    # admin 注册
    from .admin import admin
    admin.init_app(app)
    # 汉化
    babel = Babel(app)
    babel.init_app(app)



    return app




def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)