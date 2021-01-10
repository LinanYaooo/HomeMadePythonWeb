#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask
import routes
from config import Config
import static

# 实例化配置
config = Config()

# 创建Flash核心对象
app = Flask(__name__)

# 工厂函数初始化核心对象
static.init_app(app)
routes.init_app(app)

# 服务启动
if __name__ == '__main__':
    APP_HOST = config.get("app_host")
    PORT = config.get("app_port")
    DEBUG = config.get("debug")
    app.run(host=APP_HOST, port=PORT, debug=DEBUG)
