#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
"""
网站记录器 控制器
"""
from . import web_recorder
from flask import render_template_string


# 网站主页
@web_recorder("/")
def index():
    return render_template_string("<h1>hello world</h1>")
