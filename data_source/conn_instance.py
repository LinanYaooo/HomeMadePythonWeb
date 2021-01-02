#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from .redis.RedisCore import RedisCore


class Conn:
    conn = RedisCore()

    @classmethod
    def main_db(cls):
        return cls.conn
