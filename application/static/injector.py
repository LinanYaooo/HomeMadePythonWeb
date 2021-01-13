#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask
from config import Config


def injector(app: Flask):
    """
    叠加参数到 static processor, 处理静态文件
    :param app:
    :return:
    """
    @app.context_processor
    def web_images():
        """
        注入所有静态文件地址
        :return:
        """
        return dict(web_images=Config().get_web_images())

    @app.context_processor
    def web_js():
        """
        注入所有 JS 文件地址
        :return:
        """
        return dict(web_js=Config().get_web_js())