from flask import Blueprint


web=Blueprint('web',__name__)

from app.web import auth
from app.web import cookie
from app.admin.view import ArticleAdmin