#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang

import pymysql

def content():
    try:
        '''建立连接'''
        mysqllink = pymysql.Connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'shen6409175',
            db = 'students'
                                    )
    except Exception as  e:
        print(e.args)
    else:
        '''创建游标'''
        cur = mysqllink.cursor()
        '''执行sql'''
        sql = 'insert into student values (%s,%s,%s,%s)'
        parames = ('6','shenqiang','29','nanjing')
        cur.execute(sql,parames)
        '''提交事务'''
        mysqllink.commit()
        print('success')
    finally:
        '''关闭游标和数据库链接'''
        cur.close()
        mysqllink.close()

content()





