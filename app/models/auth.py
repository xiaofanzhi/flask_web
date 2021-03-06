
from sqlalchemy import Column,Integer,String,Text
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash

from app.models.base import Base

from flask_login import UserMixin
from app import login_manager

class User(UserMixin,Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    nick_name = Column(String(64),nullable=False)
    email = Column(String(51), unique=True, nullable=False)
    _password = Column('password', String(500))
    content = Column(Text)
    phone_number = Column(String(18), unique=True)

    # admin用
    def is_authenticated(self):
        return True

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)


    def check_password(self,raw):
        return check_password_hash(self._password,raw)


    # # flask_login 要求在用户模型中定义一个函数 是固定的，返回可以表示用户身份字段
    # def get_id(self):
    #     return self.id

# 使用登录限制 需要在这写个函数
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))

