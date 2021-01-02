#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
import os

# 部署环境判断
env = os.environ.get("ENV", "DEV")

from .Config import Config
