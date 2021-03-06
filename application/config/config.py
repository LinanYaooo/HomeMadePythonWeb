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

    def __init__(self, env=conf.get("ENV", "dev")):
        with open(os.path.join(self.__path, "config.yml"), encoding="utf-8") as f:
            self.config_map = yaml.load(f.read(), Loader=yaml.SafeLoader)

        # 获取环境信息 & 数据库密码
        self.env = env.lower()
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
        if isinstance(config_value, dict) and config_value.get("env"):
            config_value = config_value.get(self.env)
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

    def get_web_images(self) -> dict:
        """
        获取静态文件资源
        :return:
        """
        static_root = self.config_map.get("static_root").get(self.env)
        image_path = self.config_map.get("static_images")
        data_map = {name: static_root + sub_path for name, sub_path in image_path.items()}
        return data_map

    def get_web_js(self) -> dict:
        """
        JS文件资源
        :return:
        """
        static_root = self.config_map.get("static_root").get(self.env)
        static_root = ""
        js_path = self.config_map.get("static_js")
        data_map = {name: static_root + sub_path for name, sub_path in js_path.items()}
        return data_map

    def __call__(self, *args, **kwargs):
        return self
