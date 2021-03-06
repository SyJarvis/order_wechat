# coding: utf-8
from application import db


class Member(db.Model):
    __tablename__ = 'member'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='???')
    mobile = db.Column(db.String(11, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='??????')
    sex = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?? 1?? 2??')
    avatar = db.Column(db.String(200, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='????')
    salt = db.Column(db.String(32, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='??salt')
    reg_ip = db.Column(db.String(100, 'utf8mb4_general_ci'), nullable=False, server_default=db.FetchedValue(), info='??ip')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?? 1??? 0???')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
