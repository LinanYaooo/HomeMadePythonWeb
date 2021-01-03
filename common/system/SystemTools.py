#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
import socket
import os


class SystemTools:
    """
    系统层级工具
    """

    @classmethod
    def get_ip(cls):
        return socket.gethostbyname(socket.gethostname())

    @classmethod
    def get_pid(cls):
        return os.getpid()
