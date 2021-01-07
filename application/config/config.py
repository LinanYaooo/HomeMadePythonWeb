#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
# 从环境变量获取秘钥
import os
import yaml

from common.design_pattern.singleton import singleton
from common.logger.app_logger import logger

conf = os.environ


@singleton
class Config:
    __path = os.path.dirname(__file__)

    def __init__(self, env=conf.get("DEPLOY_ENV", "DEV").lower()):
        with open(os.path.join(self.__path, env + ".yml"), encoding="utf-8") as f:
            self.config_map = yaml.load(f.read(), Loader=yaml.SafeLoader)

        # 数据库密码从环境变量获取
        self.init_pwd()

    def get(self, config_name: str) -> str:
        """
        从配置文件获取配置内容
        :param config_name:
        :return:
        """
        config_value = self.config_map.get(config_name.lower(), None)
        if not config_value:
            logger.warn(f"Empty Config={config_name} are Retrieving")
        return config_value

    def set(self, config_name: str, config_value) -> bool:
        """
        设定配置
        :param config_name:
        :param config_value:
        :return:
        """
        self.config_map[config_name.lower()] = config_value
        return True

    def init_pwd(self):
        """
        便利初始化密码
        :return:
        """
        for key in self.config_map:
            if "_pwd" in key:
                self.set(key, conf.get(key.upper()))

    def __call__(self, *args, **kwargs):
        return self
