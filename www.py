# -*- coding: UTF-8 -*-
# @Time     : 2022/6/19 13:50
# @Author   : Runke Zhong
# @Software : PyCharm


from web.controllers.index import route_index
from application import app


app.register_blueprint(route_index, url_prefix="/")

