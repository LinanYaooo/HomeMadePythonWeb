#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

class UrlRegister:
    """
    URL收藏管理助手
    """

    def __init__(self, backend):
        """
        backend - 存储后端
        """
        self.conn = backend

    def get_url(self, key: str) -> str:
        pass

    def record_url(self, key: str, value: str) -> bool:
        pass

    def delete_url(self, key: str, value: str) -> bool:
        pass

    @property
    def all_urls(self) -> dict:
        pass
