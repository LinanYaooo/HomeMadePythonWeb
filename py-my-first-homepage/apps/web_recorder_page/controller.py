#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
"""
网站记录器 控制器
"""
from database.redis.RedisCore import RedisCore
from datetime import datetime


class Controller:

    def __init__(self):
        """ 初始化控制器资源 """
        self.redis = RedisCore()

    def hello_world_get(self):
        return self.redis.connection.get("test")

    def hello_world_set(self):
        return self.redis.connection.set("test", datetime.now().strftime("%H:%M:%S"))
