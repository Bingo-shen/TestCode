#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang
import pymysql

def connectMysqlDelect():
    try:
        '''连接数据库'''
        connectMysqlDelect = pymysql.Connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'shen6409175',
            db = 'students',
        )
    except Exception as  e:
        print(e.args)
    else:
        '''创建游标'''
        cur = connectMysqlDelect.cursor()
        '''执行sql'''
        mysql = 'delete from student order by id desc limit 1'
        cur.execute(mysql)
        '''提交事务'''
        connectMysqlDelect.commit()
        print('success')
    finally:
        '''关闭游标和数据库'''
        cur.close()
        connectMysqlDelect.close()

connectMysqlDelect()





