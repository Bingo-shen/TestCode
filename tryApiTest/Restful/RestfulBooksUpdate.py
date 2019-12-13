#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : shenqiang
from flask import Flask,make_response,jsonify,abort,request
from flask_restful import Api,Resource
from flask_httpauth import HTTPBasicAuth

'''实例化Flask、Api、HTTPBasicAuth'''
app = Flask(__name__)
api = Api(app=app)
auth = HTTPBasicAuth()
'''解决jsonify中文显示乱码问题'''
app.config['JSON_AS_ASCII']=False
app.config['DEBUG']=True

'''鉴权和异常验证'''

@auth.get_password
def get_password(name):
    if name == "bingo-shen":
        return 'shenqiang'

@auth.error_handler
def authentication():
    return make_response(jsonify({'msg':'请认证'}),401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'msg':'this is page not found'}))

'''图书管理系统'''
books=[
    {'id':1,'author':'bingo','name':'自动化测试','done':True},
    {'id':2,'author':'bingo','name':'自动化测试','done':True}
]

class Books(Resource):
    '''类方法中使用鉴权'''
    decorators =[auth.login_required]

    def get(self):
        return jsonify({'status':0,'msg':'success','data':books})

    def post(self):
        if not request.json:
            return jsonify({'status':1001,'msg':'您返回的数据类型不是json格式的，请检查，谢谢！'})
        else:
            book = {
                'id': books[-1]['id'] + 1,
                'author': request.json.get('author'),
                'name': request.json.get('name'),
                'done': False
            }
            books.append(book)
            return jsonify({'status':1002,'msg':'书籍信息添加成功','data':books})

class Book(Resource):
    decorators = [auth.login_required]

    def get(self,book_id):
        book = list(filter(lambda t: t['id'] == book_id, books))
        if len(book) == 0:
            return jsonify({'status':1003,'msg':'很抱歉，你查询的书籍的信息不存在！'})
        else:
            return jsonify({'status': 0, 'msg': 'success', 'data': book})

    def put(self,book_id):
        book = list(filter(lambda t: t['id'] == book_id, books))
        if len(book) == 0:
            return jsonify({'status':1002,'msg':'很抱歉，你查询的书籍的信息不存在！'})
        elif not request.json:
            return jsonify({'status':1001,'msg':'您返回的数据类型不是json格式的，请检查，谢谢！'})
        elif 'author' not in request.json:
            return jsonify({'status': 1004, 'msg': '请求参数author不是json格式的'})
        elif 'name' not in request.json:
            return jsonify({'status': 1005, 'msg': '请求参数name不是json格式的'})
        elif 'done' not in request.json:
            return jsonify({'status': 1006, 'msg': '请求参数done不是json格式的'})
        elif type(request.json['done']) is not bool:
            return jsonify({'status': 1007, 'msg': '请求参数done不是bool类型的'})
        else:
            book[0]['author'] = request.json.get('author', book[0]['author'])
            book[0]['name'] = request.json.get('name', book[0]['name'])
            book[0]['done'] = request.json.get('done', book[0]['done'])
            return jsonify({'statues': 1008, 'msg': '更新成功', 'data': book})

    def delete(self,book_id):
        book = list(filter(lambda t: t['id'] == book_id, books))
        if len(book) == 0:
            return jsonify({'status': 1003, 'msg': '很抱歉，你查询的书籍的信息不存在！'})
        else:
            books.remove(book[0])
            return jsonify({'status':1009,'msg':'书籍的信息已经删除'})


api.add_resource(Books,'/v1/api/books')
api.add_resource(Book,'/v1/api/books/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)
