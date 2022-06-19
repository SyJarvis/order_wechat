# -*- coding: UTF-8 -*-
# @Time     : 2022/6/19 17:33
# @Author   : Runke Zhong
# @Software : PyCharm


from flask import Blueprint

route_index = Blueprint("index_page", __name__)


@route_index.route("/")
def index():
    return "helloworld"