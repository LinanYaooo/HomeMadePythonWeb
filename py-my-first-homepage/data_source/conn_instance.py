#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from .redis.RedisCore import RedisCore


class Conn:
    redis = RedisCore()

    @classmethod
    def main_db(cls):
        return cls.redis
