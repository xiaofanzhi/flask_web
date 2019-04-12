from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer
from datetime import datetime
db=SQLAlchemy()


class Base(db.Model):
    __abstract__=True
    create_time = Column('create_time', Integer)



    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self,arrts_dict):
        for k,v in arrts_dict.items():
            if hasattr(self,k) and k!='id':
                setattr(self,k,v)
