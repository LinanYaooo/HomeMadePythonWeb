#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from common.logger.RedisLogger import logger
from db.Connector import Conn
import pandas as pd
import traceback


class UrlRegister:
    """
    URL收藏管理助手
    """

    def __init__(self, backend):
        """
        backend - 存储后端
        """
        self.conn = backend

    def get_url(self, key: str) -> str:
        pass

    def record_url(self, key: str, value: str) -> bool:
        pass

    def delete_url(self, key: str, value: str) -> bool:
        pass

    @property
    def all_urls(self) -> dict:
        pass


class PGUrlRegister(UrlRegister):
    """
    基于PG数据库的 url 管理模型
    """

    def __init__(self):
        from model.UrlRegister.Mappers.PGMapper import PGMapper
        super().__init__(backend=Conn.pg())
        self.mapper = PGMapper

    def get_url(self, key) -> str:
        """ url 收藏夹查询, 返回单一字符串 """
        conn = self.conn.connection()
        try:
            data = pd.read_sql(sql=self.mapper.GET_URL, con=conn, params={"name": key})
            if data.shape[0]:
                return data["address"].tolist()[0]
        except Exception as e:
            logger.error(traceback.format_exc())
        finally:
            conn.close()

    def update_url(self, key: str, value: str) -> bool:
        """ url 记录更新或新增 """
        conn = self.conn.connection()
        try:
            params = [key, value, value]
            cursor = conn.cursor()
            cursor.execute(self.mapper.INSERT_URL, params)
            conn.commit()
            return True
        except Exception as e:
            logger.error(traceback.format_exc())
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def delete_url(self, key: str) -> bool:
        conn = self.conn.connection()
        try:
            cursor = conn.cursor()
            cursor.execute(self.mapper.DELETE_URL, [key])
            conn.commit()
            return True
        except Exception as e:
            logger.error(traceback.format_exc())
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    @property
    def all_urls(self) -> list:
        """ url 收藏夹查询, 返回所有地址字典"""
        conn = self.conn.connection()
        try:
            data = pd.read_sql(sql=self.mapper.GET_ALL_URL, con=conn)
            if data.shape[0]:
                return data.to_dict(orient="records")
        except Exception as e:
            logger.error(traceback.format_exc())
        finally:
            conn.close()


# 实例化一个全局的对象爱那个
url_register = PGUrlRegister()
