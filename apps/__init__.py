#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask
from configs.base import *
from data_source.conn_instance import Conn
import yaml

# 引入蓝图
from apps.web_recorder_page import web_recorder


def init_jobs():
    with open("configs/init_save2_somewhere.yml", encoding="utf-8") as f:
        dict_content = yaml.load(f, Loader=yaml.SafeLoader)
        init_urls = dict_content.get("urls", None)

        # 基于 yaml 配置文件的初始化
        if init_urls:
            for name, url in init_urls.items():
                conn = Conn.redis.connection
                conn.hset("urls", name, url)

        # 基于初始化文件的初始化




def build_app():
    """
    Flask 核心对象构建过程, 包含服务初始化和视图绑定, 静态文件绑定等
    :return:
    """
    # Flask 核心对象
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # 初始化 job
    # 1.将存量Url保存 redis
    init_jobs()

    # 蓝图绑定
    app.register_blueprint(web_recorder)

    return app
