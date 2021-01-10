#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
# coding: utf-8
from manage import db


class User(db.Model):
    """
    用户信息
    字段:
        - id
        - nickname
        - login_name
        - login_pwd
        - login_salt
        - email
        - status
        - creation_date
        - update_date
    功能:
        - 注册功能
        - 登录功能
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    nickname = db.Column(db.String(50), nullable=False)
    login_name = db.Column(db.String(20), nullable=False, unique=True)
    login_pwd = db.Column(db.String(32), nullable=False)
    login_salt = db.Column(db.String(32))
    status = db.Column(db.String(5), server_default=db.FetchedValue())
    email = db.Column(db.String(200))
    last_update_date = db.Column(db.DateTime)
    creation_date = db.Column(db.DateTime)
