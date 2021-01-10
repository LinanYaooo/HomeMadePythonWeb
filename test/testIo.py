#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

from config import Config

print(Config().get_web_images())

config = Config()
SQLALCHEMY_DATABASE_URI = config.get("pg_sqlalchemy_string").format(
    pg_user=config.get("pg_user"),
    pg_pwd=config.get("pg_pwd"),
    pg_server=config.get("pg_server"),
    pg_port=config.get("pg_port"),
    pg_database=config.get("pg_database"))


print(SQLALCHEMY_DATABASE_URI)
