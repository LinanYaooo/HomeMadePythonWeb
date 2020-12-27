#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

from database.redis.RedisCore import RedisCore

rd = RedisCore()

con = rd.get_conn()

con.set("test",1)

