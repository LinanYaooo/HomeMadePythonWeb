#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from db.Connector import Conn
from common.system.SystemTools import SystemTools
from datetime import datetime, timezone, timedelta


class RedisLogger:
    """
    基于 Redis 的日志系统
    """
    logger = Conn.redis()
    structure = "[{LEVEL}][{DATE}][node={NODE}][pid={PID}] - {CONTENT}"
    name = "sys.log"

    @classmethod
    def date(cls):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    @classmethod
    def info(cls, content=""):
        text = cls.structure.format(LEVEL="info", DATE=cls.date(), NODE=SystemTools.get_ip(), PID=SystemTools.get_pid(),
                                    CONTENT=content)
        cls.logger.hset(cls.name, cls.date(), text)

    @classmethod
    def error(cls, content=""):
        text = cls.structure.format(LEVEL="error", DATE=cls.date(), NODE=SystemTools.get_ip(),
                                    PID=SystemTools.get_pid(), CONTENT=content)
        cls.logger.hset(cls.name, cls.date(), text)


# 实例化一个出来
logger = RedisLogger()
