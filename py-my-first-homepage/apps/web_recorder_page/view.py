#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

"""
网站记录器 界面
"""
from .controller import Controller
from flask import render_template
from datetime import datetime
import json


class PageView:

    controller = Controller()

    @staticmethod
    def index():
        date = datetime.now().strftime("%Y-%m-%D %H:%M:%S")
        pi_info = json.loads(PageView.controller.redis.connection.get("myPi"))
        return render_template("index.html", date=date, pi_info=pi_info)
