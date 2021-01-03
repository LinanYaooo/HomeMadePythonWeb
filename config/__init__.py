#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
import os
from .Config import Config

# 部署环境判断
env = os.environ.get("ENV", "DEV")


