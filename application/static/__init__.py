#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask
from static import injector


def init_app(app: Flask):
    """
    上下文处理工厂函数
    :param app:
    :return:
    """
    injector.injector(app)
