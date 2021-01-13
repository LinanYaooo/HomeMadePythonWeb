#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from common.db import ConnectingPool
from common.design_pattern.singleton import singleton
from config import Config
import psycopg2

config = Config()


@singleton
class PGCore(ConnectingPool):
    """
    Postgresql 链接对象
    """

    def __init__(self,
                 database=config.get("pg_database"),
                 user=config.get("pg_user"),
                 password=config.get("pg_pwd"),
                 host=config.get("pg_server"),
                 port=config.get("pg_port"),
                 blocking=True,
                 max_connection=config.get("pg_max_connection")):
        super().__init__(creator=psycopg2,
                         database=database,
                         user=user, password=password,
                         host=host, port=port,
                         blocking=blocking,
                         maxconnections=max_connection,
                         mincached=3)

    def __call__(self, *args, **kwargs):
        return self
