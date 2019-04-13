from jinja2.filters import do_truncate, do_striptags
from sqlalchemy import Column,Integer,String,Text
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash

from app.models.base import Base
from .base import db
from markdown import markdown
import bleach
import re

pattern_hasmore = re.compile(r'<!--more-->', re.I)
def markitup(text):
    """
    把Markdown转换为HTML
    """

    # 删除与段落相关的标签，只留下格式化字符的标签
    # allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
    #                 'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
    #                 'h1', 'h2', 'h3', 'p', 'img']
    return bleach.linkify(markdown(text,  output_format='html5'))
    # return bleach.linkify(bleach.clean(
    #     # markdown默认不识别三个反引号的code-block，需开启扩展
    #     markdown(text, ['extra'], output_format='html5'),
    #     tags=allowed_tags, strip=True))




class Article(Base):
    """文章"""
    __tablename__ = 'articles'

    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(128),index=True)
    summary = Column(Text)
    content = Column(Text)

    @staticmethod
    def on_change_content(target, value, oldvalue, initiator):
        target.content_html = markitup(value)


        def _format(_html):
            return do_truncate(do_striptags(_html), length=200)

        if target.summary is None or target.summary.strip() == '':
            # 新增文章时，如果 summary 为空，则自动生成
            _match = pattern_hasmore.search(value)
            if _match is not None:
                more_start = _match.start()
                # target.summary = _format(markitup(value[:more_start]))
                target.summary = markitup(value[:more_start])
            else:
                target.summary = target.body_html

db.event.listen(Article.content, 'set', Article.on_change_content)
