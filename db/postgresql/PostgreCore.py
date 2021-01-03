#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from db import ConnectingPool
from config import Config
import pandas as pd
import traceback
import psycopg2
import sys


class PGCore(ConnectingPool):
    """
    Postgresql 链接对象
    """

    def __init__(self, *args, **kwargs):
        super().__init__(creator=psycopg2, *args, **kwargs)


# 实例化一个链接对象
try:
    pg_core = PGCore(database=Config.PG_DATABASE, user=Config.PG_USER, password=Config.PG_PWD,
                     host=Config.PG_SERVER, port=Config.PG_PORT, blocking=True, maxconnections=20)
except Exception as e:
    sys.exit("PG链接失败" + traceback.format_exc())
