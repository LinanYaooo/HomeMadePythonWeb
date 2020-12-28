#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

from apps import build_app

# 创建Flash核心对象
app = build_app()

# 服务启动
if __name__ == '__main__':
    app.run(debug=True)
