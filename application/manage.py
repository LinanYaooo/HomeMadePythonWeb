#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask
from config import Config
import routes
import static
import models


# 实例化配置
config = Config()

# 创建Flash核心对象
app = Flask(__name__)

# 创建数据库Sqlalchemy实例
db = models.init_app(app)

# 绑定各模块到核心对象
static.init_app(app)
routes.init_app(app)

if __name__ == '__main__':
    APP_HOST = config.get("app_host")
    PORT = config.get("app_port")
    DEBUG = config.get("debug")
    app.run(host=APP_HOST, port=PORT, debug=DEBUG)
