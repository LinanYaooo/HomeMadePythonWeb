#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

# 依赖引入
from flask import Blueprint, request
from common.logger.redis_logger import logger

# 视图函数引入
from .view import PageView

# 创建蓝图
web_recorder = Blueprint("WebRecorder", __name__)


@web_recorder.route("/")
def index():
    logger.info(request.remote_addr + " logging in " + request.full_path)
    return PageView.index()


@web_recorder.route("/update", methods=["GET", "POST"])
def update_url():
    url = request.form.get("urlAddress")
    name = request.form.get("urlName")
    PageView.controller.update_url(name=name, url=url)
    return PageView.index()


@web_recorder.route("/delete", methods=["GET", "POST"])
def delete_url():
    name = request.form.get("urlName")
    PageView.controller.delete_url(name=name)
    return PageView.index()
