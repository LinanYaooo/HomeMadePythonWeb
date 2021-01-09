#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask
from config import Config


def inject_statics(app: Flask):
    """
    叠加参数到 context processor, 处理静态文件
    :param app:
    :return:
    """

    @app.context_processor
    def inject_web_images():
        """
        注入所有静态文件地址
        :return:
        """
        return dict(web_images=Config().get_web_images())
