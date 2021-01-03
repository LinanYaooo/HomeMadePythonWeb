#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from .redis.RedisCore import RedisCore
from .postgresql.PostgreCore import pg_core


class Conn:
    __redis_connection = None
    __pg_connection = None

    @classmethod
    def redis(cls):
        if cls.__redis_connection:
            return cls.__redis_connection
        else:
            cls.__redis_connection = RedisCore()
            return cls.__redis_connection

    @classmethod
    def pg(cls):
        if not cls.__pg_connection:
            cls.__pg_connection = pg_core
        return cls.__pg_connection
