# -*- coding: UTF-8 -*-
# @Time     : 2022/6/19 13:49
# @Author   : Runke Zhong
# @Software : PyCharm

import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
import redis
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()



class Application(Flask):

    def __init__(self, import_name, template_folder=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, static_folder=None)
        self.config.from_pyfile("config/base_setting.py")
        self.config.from_pyfile("config/local_setting.py")
        db.init_app(self)



# 设置日志的记录等级
logging.basicConfig(level=logging.INFO)
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handle = RotatingFileHandler("logs/log", maxBytes=1024*1024*10, backupCount=10)
# 创建日志的记录格式
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录设置日志记录格式
file_log_handle.setFormatter(formatter)
# 为全局的日志工具对象(flask app使用的)添加日志记录器
logging.getLogger().addHandler(file_log_handle)
# 获取根路径
root_path = os.getcwd()
# 数据库
db = SQLAlchemy()
app = Application("__name__", template_folder=root_path + "/web/templates")
# redis链接
redis_store = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])