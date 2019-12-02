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
        '''SQL语句分离'''
        # sql = 'select * from student where id = %s'
        # params = (1,)
        # '''查重'''
        # cur.execute(sql,params)
        # '''单个语句的查询'''
        # data = cur.fetchone()
        # return datas
        sql = 'select * from student'
        '''查重'''
        cur.execute(sql)
        '''返回多个数据'''
        datas = cur.fetchall()
        '''方法一，遍历'''
        # for data in datas:
        #     print(data)
        '''方法二，列表推倒式'''
        db = [data for data in datas]
        print(db)

    finally:
        # 关闭游标和链接
        cur.close()
        connect.close()

connectMysql()






