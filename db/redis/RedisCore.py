#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
import redis
from config import Config


class RedisCore():
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

    def hset(self, name, key, value):
        self.connection.hset(name, key, value)
        return True

    @staticmethod
    def kv_set(self, key: str, value: str) -> bool:
        pass

    @staticmethod
    def kv_get(self, key: str) -> str:
        pass
