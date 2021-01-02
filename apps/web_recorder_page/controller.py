#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
"""
网站记录器 控制器
- 请求控制
"""
from data_source.redis.RedisCore import RedisCore
from data_source.conn_instance import Conn
from datetime import datetime


class Controller:

    def __init__(self):
        """ 初始化控制器资源 """
        self.db = Conn.conn

    def update_urls(self, name: str, url: str):
        """ 传入Url并保存到数据库 """
        # 判断是否重复
        if (not name) or (not url):
            return False
        else:
            self.db.connection.hset("urls", name, url)
            return True

    def delete_url(self, name: str):
        """ 从数据库删除url """
        # 先判断是否存在
        if self.db.connection.hget("urls", name):
            self.db.connection.hdel("urls", name)
            return True
        else:
            return False
