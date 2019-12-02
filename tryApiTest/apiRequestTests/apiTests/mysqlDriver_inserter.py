#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

import pymysql

def connectMysql():
    try:
        '''链接数据库'''
        connect = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='shen6409175',
            db='students'
        )
    except Exception as  e:
        return e.args
    else:
        '''创建游标'''
        cur = connect.cursor()
        '''导入数据'''
        sql = 'delete from student where id = %s'
        params = (7,)
        cur.execute(sql,params)
        '''执行后必须要commit()'''
        connect.commit()
    finally:
        # 关闭游标和链接
        cur.close()
        connect.close()

connectMysql()






