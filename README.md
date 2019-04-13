## flask_web
flask 登录身份验证扩展

简单的模拟登录通过从mysql数据库进行验证

更换pipenv源

url = "https://pypi.tuna.tsinghua.edu.cn/simple"

## 4.12
mysql 配置文件卸载secure配置文件中,没有上传需要自己手动创建

注册验证完成 


##4.13 实现登录 

采用flask第三方登录插件flask_login

限制登录权限

flask 整合Flask-Admin插件


###整合Flask-Migrate

命令：export FLASK_APP=test.py （选定当前运行为test.py）

初始化:flask db init

迁移:flask db migrate

升级:flask db upgrade




###Flask-Admin中整合editor.md Markdown
editor.md:[editor.md](https://github.com/pandao/editor.md)Markdown编辑器

- 最后的回调URL 要注册在web蓝图下面，  @web.route('/image/<name>')
之前是放在@expose admin下面，图片是不会显示。
- 图片存储在本地服务器上,也可选择在存在七牛云上.
参考[https://www.jianshu.com/p/7a2acc3da59e]

参考推荐：[https://blog.csdn.net/kikaylee/article/details/55006262]




