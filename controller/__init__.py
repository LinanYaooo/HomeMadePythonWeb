#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask


def app_register(app: Flask):
    """
    Flask 核心对象构建过程, 包含服务初始化和视图绑定, 静态文件绑定等
    :return:
    """
    # 蓝图绑定
    from controller.urls_recorder import web_recorder
    app.register_blueprint(web_recorder)
    return app
