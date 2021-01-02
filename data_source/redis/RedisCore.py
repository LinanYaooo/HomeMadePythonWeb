#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
import redis
from configs import Config


class RedisCore:
    """Redis链接对象"""

    def __init__(self, host=Config.REDIS_SERVER, port=Config.REDIS_PORT):
        self.conn = redis.Redis(host=host, port=port, decode_responses=True)

    @property
    def connection(self) -> redis.connection:
        try:
            self.conn.get("test")
        except Exception as e:
            self.__init__()
        finally:
            return self.conn

    def set(self, key, value):
        self.connection.set(key, value)
        return True