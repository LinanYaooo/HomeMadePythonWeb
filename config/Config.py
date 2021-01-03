#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
# 从环境变量获取秘钥
import os

conf = os.environ


class Config:
    # redis 配置
    REDIS_SERVER = "192.168.101.18"
    REDIS_PORT = 6379
    # postgres配置
    PG_SERVER = "192.168.101.18"
    PG_PORT = 5432
    PG_USER = "linany"
    PG_DATABASE = PG_USER
    PG_PWD = conf.get("PG_PWD")

    # mysql配置
    MYSQL_SERVER = "192.168.101.18"

    # 部署配置
    APP_HOST = "127.0.0.1"
    APP_PORT = 81
    DEBUG = True
