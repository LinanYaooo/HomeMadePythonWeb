#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from dbutils.pooled_db import PooledDB


class ConnectingPool(PooledDB):
    """
    连接池父类
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

