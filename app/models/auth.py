
from sqlalchemy import Column,Integer,String
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

from app.models.base import Base


class User(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    nick_name = Column(String(64),nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(500))
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