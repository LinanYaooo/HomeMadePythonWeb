#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

"""
网站记录器 界面
- 渲染页面
"""
from .controller import Controller
from flask import render_template


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
    def get_urls(cls) -> dict:
        """ 将url按照url名称做排序处理 """
        data = cls.controller.all_urls
        if data:
            dd = sorted(data, key=lambda x: x["name"])
            result = {k.get("name"): k.get("address") for k in dd}
            return result
        else:
            return {}
