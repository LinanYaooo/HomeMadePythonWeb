#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask
from . import context_processors


def init_app(app: Flask):
    """
    上下文处理工厂函数
    :param app:
    :return:
    """
    context_processors.inject_statics(app)
