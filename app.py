#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask
from controller import app_register
from common.logger.RedisLogger import logger
from config import Config
import traceback

# 创建Flash核心对象
app = app_register(Flask(__name__))

# 异常处理逻辑
@app.errorhandler(Exception)
def error(e):
    logger.error(str(e) + traceback.format_exc())


# 服务启动
if __name__ == '__main__':
    app.run(host=Config.APP_HOST, port=Config.APP_PORT, debug=Config.DEBUG)
