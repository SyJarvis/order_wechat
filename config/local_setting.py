# -*- coding: UTF-8 -*-
# @Time     : 2022/6/19 13:52
# @Author   : Runke Zhong
# @Software : PyCharm

DEBUG = True
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = "mysql://root:mysql0220@127.0.0.1:3306/order_wechat?charset=utf8mb4"
SQLALCHEMY_TRACK_MODIFICATIONS = True

REDIS_HOST = '120.25.1.147'
REDIS_PORT = '10010'
REDIS_NO = 1

CAMPUS_SERVICE_APP = {
    'appid': 'wx47b5911f64e0c8b1',
    'appkey': 'a86200ccfbfc64886ab427b812e2e6fb',
    'paykey':'',
    'mch_id':'1443337302',
    'callback_url': '/api/order/callback'
}