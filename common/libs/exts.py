# -*- coding: UTF-8 -*-
# @Time     : 2022/6/19 16:27
# @Author   : Runke Zhong
# @Software : PyCharm

from common.models import *
from application import db, app



def create_db():
    with app.app_context():
        db.init_app(app)
        db.create_all()


