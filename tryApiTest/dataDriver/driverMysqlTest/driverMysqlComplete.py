#!/user/bin/env python
#coding:utf-8
#Author:shenqiang

import pymysql

class MysqlTry:
    '''链接数据库'''
    def connectMysql(self):
        '''尝试链接数据库'''
        try:
            connect =pymysql.connect(
                host = '127.0.0.1',
                user='root',
                password='shen6409175',
                db='students'
            )
        except Exception as e:
            print(e.args)
        return connect

    def selectMysql(self,sql,params):
        '''创建游标'''
        cur = self.connectMysql().cursor()
        '''查重'''
        cur.execute(sql,params)
        '''查询'''
        result = cur.fetchall()
        '''删除游标'''
        cur.close()
        return result

def checkValid(username,age):
    opera = MysqlTry()
    sql = "select * from student where name = %s and age = %s"
    params=(username,age)
    return opera.selectMysql(sql=sql,params=params)

def checkinfo():
    username = input('请输入用户名 \n')
    age = input('请输入用户年龄 \n')
    result = checkValid(username,age)
    if result:
        '''关闭数据库'''
        MysqlTry().connectMysql().close()
        print('该用户在数据库中，测试通过！')
    else:
        print('该用户不在数据库中，存在bug！')

if __name__ == '__main__':
    checkinfo()