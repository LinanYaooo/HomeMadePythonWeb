#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
"""
保存Redis信息到二进制文件
"""
import pickle
from data_source.redis.RedisCore import RedisCore

db = RedisCore()

result = db.connection.hgetall("urls")

files = "init_data.pkl"

with open(files, "wb") as f:
    pickle.dump(result, f)
