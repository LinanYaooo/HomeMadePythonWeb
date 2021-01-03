#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

from db.Connector import Conn
import pandas as pd

conn = Conn.pg().connection()

print(pd.read_sql(sql="select * from pg_backend_pid()", con=conn))
