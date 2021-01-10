#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config

# 初始化 APP 配置
config = Config()


def init_app(app: Flask):
    """
    初始化应用SqlAlchemy配置
    SQLALCHEMY_DATABASE_URI
    :param app:
    :return:
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = config.get("pg_sqlalchemy_string").format(
        pg_user=config.get("pg_user"),
        pg_pwd=config.get("pg_pwd"),
        pg_server=config.get("pg_server"),
        pg_port=config.get("pg_port"),
        pg_database=config.get("pg_database")
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    return SQLAlchemy(app)
