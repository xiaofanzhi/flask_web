
from sqlalchemy import Column, Integer, String, Text, Boolean
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash,check_password_hash

from app.models.base import Base


from app import login_manager

class Role(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    # 只有一个角色的 default 字段要设为 True，其他都设为 False。用户注册时，其角色会被 设为默认角色
    default = Column(Boolean, default=False, index=True)
    permissions = Column(Integer)
    users = relationship('User', backref='role', lazy='dynamic')