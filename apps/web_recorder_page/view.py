#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

"""
网站记录器 界面
- 渲染页面
"""
from .controller import Controller
from flask import render_template
from datetime import datetime
import json


class PageView:
    controller = Controller()

    @classmethod
    def index(cls):
        return render_template("index.html", urls=cls.get_urls())

    @classmethod
    def add_url(cls, name, url):
        result = cls.controller.update_urls(name, url)
        return render_template("index.html", urls=cls.get_urls(), result=result)

    @classmethod
    def delete_url(cls, name, url):
        result = cls.controller.delete_url(name, url)
        return render_template("index.html", urls=cls.get_urls(), result=result)

    @classmethod
    def get_urls(cls):
        data = cls.controller.db.connection.hgetall("urls")
        dd = sorted(data)
        result = {k: data.get(k) for k in dd}
        return result
