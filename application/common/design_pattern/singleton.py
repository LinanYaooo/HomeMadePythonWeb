#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

def singleton(cls):
    """
    将静态类转为单例
    :param cls:
    :return:
    """
    instance = cls()
    instance.__call__ = lambda: instance
    return instance
