#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask
from configs.base import *

# 引入蓝图
from apps.web_recorder_page import web_recorder


def build_app():
    # Flask 核心对象
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # 蓝图绑定
    app.register_blueprint(web_recorder)

    return app
