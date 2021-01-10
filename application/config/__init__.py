#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
import os

from flask import Flask

from .config import Config

# 部署环境判断
env = os.environ.get("ENV", "DEV")

# 初始化 APP 配置
config = Config()


def init_app(app: Flask):
    """
    根据配置初始化数据库
    :param app:
    :return:
    """
    pass
