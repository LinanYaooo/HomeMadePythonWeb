#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

def init_jobs():
    from database.conn_instance import Conn
    import yaml
    with open("../configs/init_save2_somewhere.yml", encoding="utf-8") as f:
        dict_content = yaml.load(f, Loader=yaml.SafeLoader)
        init_urls = dict_content.get("urls", None)
        if init_urls:
            print(init_urls)
            for name, url in init_urls.items():
                conn = Conn.redis.connection
                conn.hset("urls", name, url)
        # 预留日志位置


if __name__ == "__main__":
    init_jobs()
