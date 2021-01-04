#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany

class PGMapper:
    GET_URL = """
    SELECT 
        ADDRESS as ADDRESS
    FROM
        LINANY.URL_RECORDER_T
    WHERE
        NAME=%(name)s
        AND ACTIVE='Y'
    """

    GET_ALL_URL = """
    SELECT 
        NAME as NAME,
        ADDRESS as ADDRESS,
        LAST_UPDATE_DATE as LAST_UPDATE_DATE
    FROM
        LINANY.URL_RECORDER_T
    WHERE
        1 = 1
        AND ACTIVE='Y'
    """

    INSERT_URL = """
    INSERT INTO LINANY.URL_RECORDER_T
    (NAME, ADDRESS, ACTIVE, LAST_UPDATE_DATE)
    VALUES
    (%s, %s, 'Y', current_date)
    ON conflict(NAME)
    DO UPDATE
    SET ADDRESS = %s, ACTIVE='Y'
    """

    DELETE_URL = """
    UPDATE LINANY.URL_RECORDER_T
    SET ACTIVE='N'
    WHERE NAME=%s
    """
