# -*- coding: UTF-8 -*-
# @Time     : 2022/6/19 13:49
# @Author   : Runke Zhong
# @Software : PyCharm

import os
import logging
from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config/base_setting.py")

    db.init_app(app)

    return app

from common.models import *

app = create_app()

@app.route("/")
def index():
    return "HelloWorld"



