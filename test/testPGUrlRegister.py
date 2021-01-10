#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

from models.UrlRegister.UrlRegister import PGUrlRegister

c = PGUrlRegister()

# 查询单挑
print(c.get_url("sascascasc"))

# 查询多条
print(c.all_urls)

# 新增单条
c.record_url("hello", "world")

# 单条删除
c.delete_url("hello")