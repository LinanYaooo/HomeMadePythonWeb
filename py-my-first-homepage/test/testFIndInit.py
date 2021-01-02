#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany


import os
import pickle
from data_source.conn_instance import Conn


def init_db_files(path):
    """
    根据 static 文件夹有无 init_db 文件确认数据是否进行初始化, 录入;
    - 二进制文件解读确保是 pickle 文件;
    - 二进制文件约定反序列化后得到一个字典文件
    - 约定数据持久化的方法为遍历字典，按照键值将相应数据保存在 dictionary_t 命名集合中
    :param path:
    :return:
    """
    for i in os.listdir(path):
        if i.startswith("init_data"):
            abspath = os.path.join(path, i)
            # 将数据反序列化提取
            with open(abspath, 'rb') as f:
                data = pickle.load(f)
            # 将数据持久化到数据库, 标准实现
            ...


if __name__ == "__main__":
    init_db_files("../static/init")
