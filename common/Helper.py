# -*- coding: UTF-8 -*-
# @Time     : 2022/6/19 17:44
# @Author   : Runke Zhong
# @Software : PyCharm

from flask import render_template, g
import datetime


'''
统一渲染方法
'''

def ops_render(template, context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template, **context)


def getCurrentDate(format="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(format)