#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
"""
网站记录器 控制器
- 请求控制
"""
from db.Connector import Conn
from model.UrlRegister.UrlRegister import url_register


class Controller:

    def __init__(self):
        """ 初始化控制器资源 """
        self.model = url_register

    def get_url(self, name: str):
        """ 获取地址 """
        return self.model.get_url(name)

    def update_url(self, name: str, url: str):
        """ 传入Url并保存到数据库 """
        # 判断是否重复
        if (not name) or (not url):
            return False
        else:
            self.model.update_url(name, url)
            return True

    def delete_url(self, name: str):
        """ 从数据库删除url """
        # 先判断是否存在
        if self.model.get_url(name):
            return self.model.delete_url(name)

    @property
    def all_urls(self) -> list:
        return self.model.all_urls
