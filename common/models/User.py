# -*- coding: UTF-8 -*-
# @Time     : 2022/6/19 15:55
# @Author   : Runke Zhong
# @Software : PyCharm

from sqlalchemy import Column, String, Integer
from application import db


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    sex = Column(Integer, nullable=False)
    password = Column(String(80), nullable=False)
    name_cn = Column(String(20), nullable=False)
