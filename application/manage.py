#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask
import routes
from config import Config

config = Config()

# 创建Flash核心对象
app = routes.init_app(Flask(__name__))

# 服务启动
if __name__ == '__main__':
    APP_HOST = config.get("app_host")
    PORT = config.get("app_port")
    DEBUG = config.get("debug")
    app.run(host=APP_HOST, port=PORT, debug=DEBUG)
