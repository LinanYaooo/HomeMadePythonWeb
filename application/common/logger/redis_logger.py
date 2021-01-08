#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
import logging
from datetime import datetime
from common.db.redis.redis_core import RedisCore
from common.system.system_tools import SystemTools


class RedisLogger:
    """
    基于 Redis 的日志系统
    """
    logger = RedisCore()
    structure = "[{LEVEL}][{DATE}][node={NODE}][pid={PID}] - {CONTENT}"
    name = "sys.log"
    logger_handler = logging.getLogger("AppLoggerByRedis")
    logger_file = "app.log"

    @classmethod
    def date(cls):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    @classmethod
    def info(cls, content=""):
        text = cls.structure.format(LEVEL="info", DATE=cls.date(), NODE=SystemTools.get_ip(), PID=SystemTools.get_pid(),
                                    CONTENT=content)
        cls.logger.hset(cls.name, cls.date(), text)
        cls.logger_handler.info(text)
        cls.write_log(text)

    @classmethod
    def error(cls, content=""):
        text = cls.structure.format(LEVEL="error", DATE=cls.date(), NODE=SystemTools.get_ip(),
                                    PID=SystemTools.get_pid(), CONTENT=content)
        cls.logger.hset(cls.name, cls.date(), text)
        cls.logger_handler.info(text)
        cls.write_log(text)

    @classmethod
    def write_log(cls, content):
        with open(cls.logger_file, "a+", encoding="utf-8") as f:
            f.write(content)
            f.write("\n")


# 单例
logger = RedisLogger()
