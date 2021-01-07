#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
import traceback
from flask import Flask, request
from common.logger.redis_logger import logger


def init_app(app: Flask):
    """
    Flask 核心对象构建过程, 包含服务初始化和视图绑定, 静态文件绑定等
    :return:
    """
    # 蓝图绑定
    from routes.recorder.route import web_recorder
    app.register_blueprint(web_recorder)

    @app.errorhandler(Exception)
    def error(e):
        logger.error("[ERROR]--->{}".format(request.full_path) + str(e) + traceback.format_exc())

    return app
